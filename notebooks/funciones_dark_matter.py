import pynbody
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy import optimize
import scipy.stats
from astropy import units as unit
import sys
from matplotlib.animation import FuncAnimation
import funciones_dark_matter as fdm

def accumulated_mass(pos,mass,n,limits):
    """
    La funcion accumulated_mass va a calcular la 
    masa total acumulada hasta cierto radio.
    
    Parameters
    ----------
    pos : pynbody.array.SimArray
       posicion de las particulas de cada snapshot 
    mass : pynbody.array.SimArray
       masa de cada una de las particulas en el snapshot 
    n : int
       numero de rectangulos en el histograma
    limits : tuple
       valores maximos y minimos a considerar en el histograma
        
    Returns
    -------
    positions : ndarray
        retorna los valores de las posiciones
        de los radios limite de las barras del histograma (galaxias nuevas).
    histo_acum[0] : ndarray
        retorna el valor de la masa acumulada para 
        cada radio limite (galaxias nuevas).
    
    """
    
    r = np.sqrt((pos**2).sum(axis=1))
  
    histo_acum = scipy.stats.cumfreq(r, n, limits, weights=mass)
    
    positions = histo_acum[1]+ np.arange(1,n+1) * histo_acum[2]
    
    return positions, histo_acum[0]

def plot_mass(numero,filename):
    """
    La funcion plot_mass va a permitirle graficar las masas
    acumuladas de cada simulacion vs el radio para poder
    comparar los datos obtenidos.
    
    Parameters
    ----------
    numero: int
        este atributo nos permitira realizar dos tipos de graficos
        distintos, si escoge el numero 0, realizara graficos de comparacion
        entre galaxias snapshot por snapshot. Si escoge el numero 1, realizara
        el grafico de comparacion de cada snapshot con los snapshots 100, 300 y 500.
    filename : str
        este atributo nos va a permitir 
        el almacenamiento de los plots generados.
    
    """
    
    fig = plt.figure(figsize=(10, 7))
    try:  
        if numero == 0:
            data_viejo_ruta = pynbody.load(data_viejo+'/'+gal+'/snapshot_'+snap+'.hdf5')
            binsold, massold  = accumulated_mass(data_viejo_ruta.dm['pos'],data_viejo_ruta.dm['mass'],
                             n=int(limites_materia_oscura[gal][1]*4),limits=limites_materia_oscura[gal])
            plt.plot(binsold, massold, color='r', label= 'Old Galaxies '+gal+'/'+snap)
        if numero == 1:
            data_viejo_100 = pynbody.load(data_viejo+'/'+gal+'/snapshot_100.hdf5')
            data_viejo_300 = pynbody.load(data_viejo+'/'+gal+'/snapshot_300.hdf5')
            data_viejo_500 = pynbody.load(data_viejo+'/'+gal+'/snapshot_500.hdf5')
            binsold100,massold100 =accumulated_mass(data_viejo_100.dm['pos'],data_viejo_100.dm['mass'],
                             n=int(limites_materia_oscura[gal][1]*4),limits=limites_materia_oscura[gal])
            binsold300,massold300 = accumulated_mass(data_viejo_300.dm['pos'],data_viejo_300.dm['mass'],
                             n=int(limites_materia_oscura[gal][1]*4),limits=limites_materia_oscura[gal])
            binsold500,massold500 = accumulated_mass(data_viejo_500.dm['pos'],data_viejo_500.dm['mass'],
                             n=int(limites_materia_oscura[gal][1]*4),limits=limites_materia_oscura[gal])
            
            plt.plot(binsold100, massold100, color='r', label= 'Old Galaxies '+gal+'/100',alpha=0.5)
            plt.plot(binsold300, massold300, color='g', label= 'Old Galaxies '+gal+'/300',alpha=0.5)
            plt.plot(binsold500, massold500, color='b', label= 'Old Galaxies '+gal+'/500',alpha=0.5)
    except:
        pass
        
    data_nuevo_ruta = pynbody.load(data_nuevo+'/'+gal+'/snapshot_'+snap+'.hdf5')
    binsnew, massnew = accumulated_mass(data_nuevo_ruta.dm['pos'],data_nuevo_ruta.dm['mass'],
                           n=int(limites_materia_oscura[gal][1]*4),limits=limites_materia_oscura[gal]) 
    
    plt.plot(binsnew,massnew,'-k',label= 'New Galaxies '+gal+'/'+snap)
    plt.title('Masa acumulada de la Materia Oscura', fontsize= 20)
    plt.xlabel('Radio [Kpc]',fontsize=18)
    plt.ylabel('Masa Acumulada (10$^{10}$ $M_\odot$)',fontsize=18)
    plt.legend()
    plt.grid()
    plt.savefig(filename)
    plt.clf()
    plt.close()

def density_dm(data):
    """
    La funcion density_dm va a calcular la  densidad de la masa
    que se acumula en cada una de las barras del histograma y 
    permite compararlas para las galaxias nuevas y viejas.
    
    Parameters
    ----------
    data: pynbody.array
        es la ruta que lo llevara al snapshot a partir del 
        cual se extraera la informacion de la masa acumulada
        para poder calcular la densidad.
        
    Returns
    -------
    bins_middle_new : ndarray
        retorna los valores de los radios
        promedios de cada barra.
    shell_mass_new : ndarray
        retorna el valor de la masa en cada cascaron para 
        cada radio limite.
    densnew : ndarray
        retorna los valores de la densidad
        de cada cascaron.
           
    Notes
    -----
    Recuerde que la funcion de densidad es: \rho = (4/3)*pi*R^3
    
    """
    
    x,y = accumulated_mass(data.dm['pos'],data.dm['mass'],n=int(limites_materia_oscura[gal][1]*4),limits=limites_materia_oscura[gal])
    
    x2 = np.roll(x,1)
    x2[0]=0
    # promedio del radio
    bins_middle = (x + x2 )/2
    
    x_cubico = x**3
    x_cubico_2 = np.roll(x_cubico,1)
    x_cubico_2[0]=0
   
    y2 = np.roll(y,1)
    y2[0]=0
  
    shell_mass = y - y2
    
    # \rho = (4/3)*pi*R^3
    dens = 3* shell_mass / ((4*np.pi)* (x_cubico - x_cubico_2) )
    
    return bins_middle, shell_mass, dens


def plot_density(numero,filename):
    """
    La funcion plot_density le va a permitir graficar
    los datos obtenidos para la densidad radial de las 
    galaxias.
    
    Parameters
    ----------
    numero: int
        este atributo nos permitira realizar dos tipos de graficos
        distintos, si escoge el numero 0, realizara graficos de comparacion
        entre galaxias snapshot por snapshot. Si escoge el numero 1, realizara
        el grafico de comparacion de cada snapshot con los snapshots 100, 300 y 500.
    filename : str
        este atributo nos va a permitir 
        el almacenamiento de los plots generados.
    
    """
    
    fig = plt.figure(figsize=(10, 7))
    try: 
        if numero == 0:
            data_viejo_ruta = pynbody.load(data_viejo+'/'+gal+'/snapshot_'+snap+'.hdf5')
            bins_middle_old, shell_mass_old, dens_old  = density_dm(data_viejo_ruta)
            plt.plot(bins_middle_old, np.log10(dens_old), color='r', label= 'Old Galaxies '+gal+'/'+snap)
        if numero == 1:
            data_viejo_100 = pynbody.load(data_viejo+'/'+gal+'/snapshot_100.hdf5')
            data_viejo_300 = pynbody.load(data_viejo+'/'+gal+'/snapshot_300.hdf5')
            data_viejo_500 = pynbody.load(data_viejo+'/'+gal+'/snapshot_500.hdf5')
            bins_100, shell_100, dens_100  = density_dm(data_viejo_100)
            bins_300, shell_300, dens_300  = density_dm(data_viejo_300)
            bins_500, shell_500, dens_500  = density_dm(data_viejo_500)
            plt.plot(bins_100, np.log10(dens_100), color='r', label= 'Old Galaxies '+gal+'/100')
            plt.plot(bins_300, np.log10(dens_300), color='g', label= 'Old Galaxies '+gal+'/300')
            plt.plot(bins_500, np.log10(dens_500), color='b', label= 'Old Galaxies '+gal+'/500')
    
    except:
        pass
        
    data_nuevo_ruta = pynbody.load(data_nuevo+'/'+gal+'/snapshot_'+snap+'.hdf5')
    bins_middle_new, shell_mass_new, dens_new  = density_dm(data_nuevo_ruta)
    
    plt.plot(bins_middle_new, np.log10(dens_new), '-k', label= 'New Galaxies '+gal+'/'+snap)
    
    plt.title('Perfil de densidad de materia oscura', fontsize = 20)
    plt.xlabel('Radio [Kpc]', fontsize = 18)
    plt.ylabel(r'$\rho$ [$10^{10}$ Msol/$kpc^{2}$]', fontsize = 18)
    plt.legend()
    plt.grid()
    plt.savefig(filename)
    plt.clf()
    plt.close()