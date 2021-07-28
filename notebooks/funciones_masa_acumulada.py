import pynbody
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy import optimize
import scipy.stats
from astropy import units as unit
import sys
from matplotlib.animation import FuncAnimation
import funciones_masa_acumulada as facma

def accumulated_mass(pos,mass,n,limits):
    """
    La funcion accumulated_mass va a calcular la 
    masa total acumulada hasta cierto radio para
    las galaxias consideradas.
    
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
        de los radios limite de las barras del histograma.
    histo_acum[0] : ndarray
        retorna el valor de la masa acumulada para 
        cada radio limite.
      
    Notes
    -----
    Esta funcion de masa acumulada sera utilizada cuando
    se esten comparando las diferentes galaxias.
    
    """
    r = np.sqrt((pos[:,:2]**2).sum(axis=1))
 
    histo_acum = scipy.stats.cumfreq(r, n, limits, weights=mass)
   
    positions = histo_acum[1]+ np.arange(1,n+1) * histo_acum[2]
    
    return positions, histo_acum[0]



def plot_mass(filename):
    """
    La funcion plot_mass va a permitirle graficar las masas
    acumuladas de cada simulacion vs el radio para poder
    comparar los datos obtenidos.
    
    Parameters
    ----------
    data1 : pynbody.snapshot
       snapshot leído con pynbody
    data2 : pynbody.snapshot
       snapshot leído con pynbody
    filename : str
        este atributo nos va a permitir 
        el almacenamiento de los plots generados.
    
    """
    fig = plt.figure(figsize=(10, 7))
    
    for snap in np.arange(100,700,200):
        snap = str(snap).zfill(3) 
        try:
            data_viejo_ruta = pynbody.load(data_viejo+'/'+gal+'/snapshot_'+snap+'.hdf5')
            binsold, massold =accumulated_mass(data_viejo_ruta.star['pos'],data_viejo_ruta.star['mass'],
                              n=int(limites_star[gal][1]*5),limits=limites_star[gal])
            plt.plot(binsold,massold,'-r', label= 'Old Galaxies',alpha=0.5)
        except:
            pass
        
    for snap in np.arange(1,600,1): 
        snap = str(snap).zfill(3)
        data_nuevo_ruta = pynbody.load(data_nuevo+'/'+gal+'/snapshot_'+snap+'.hdf5')
        binsnew, massnew = accumulated_mass(data_nuevo_ruta.star['pos'],data_nuevo_ruta.star['mass'],
                                            n=int(limites_star[gal][1]*5),limits=limites_star[gal]) 
        plt.plot(binsnew,massnew,'-k',label= 'New Galaxies',alpha=0.5)
   
    plt.title('Masa acumulada de Estrellas '+gal, fontsize= 20)
    plt.xlabel('Radio [Kpc]',fontsize=18)
    plt.ylabel('Masa Acumulada (10$^{10}$ $M_\odot$)',fontsize=18)
    plt.legend()
    plt.grid()
    plt.savefig(filename)
    plt.clf()
    plt.close()
    

def plot_gas(filename):
    """
    La funcion plot_mass va a permitirle graficar las masas
    acumuladas de cada simulacion vs el radio para poder
    comparar los datos obtenidos.
    
    Parameters
    ----------
    filename : str
        este atributo nos va a permitir 
        el almacenamiento de los plots generados.
    
    """
    fig = plt.figure(figsize=(10, 7))
    for snap in np.arange(100,700,200):
        snap = str(snap).zfill(3)
        try:
            data_viejo_ruta = pynbody.load(data_viejo+'/'+gal+'/snapshot_'+snap+'.hdf5')
            binsold, massold = accumulated_mass(data_viejo_ruta.gas['pos'],data_viejo_ruta.gas['mass'],
                                                n=int(limites_gas[gal][1]*5),limits=limites_gas[gal])
            plt.plot(binsold,massold,'-r', label= 'Old Galaxies',alpha=0.5)
        except:
            pass
        
    for snap in np.arange(1,600,1): 
        snap = str(snap).zfill(3)
        data_nuevo_ruta = pynbody.load(data_nuevo+'/'+gal+'/snapshot_'+snap+'.hdf5')
        binsnew, massnew = accumulated_mass(data_nuevo_ruta.gas['pos'],data_nuevo_ruta.gas['mass'],
                                            n=int(limites_gas[gal][1]*5),limits=limites_gas[gal]) 
        plt.plot(binsnew,massnew,'-k',label= 'New Galaxies',alpha=0.5)
    
    plt.title('Masa acumulada de Gas '+gal, fontsize= 20)
    plt.xlabel('Radio [Kpc]',fontsize=18)
    plt.ylabel('Masa Acumulada (10$^{10}$ $M_\odot$)',fontsize=18)
    plt.legend()
    plt.grid()
    plt.savefig(filename)
    plt.clf()
    plt.close()