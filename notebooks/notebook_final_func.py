import pynbody
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy import optimize
import scipy.stats
from astropy import units as unit
import sys
from matplotlib.animation import FuncAnimation

data_nuevo = '/media/danna01/Disk/SNAPSHOTS/Galaxias_Nuevas'
data_viejo = '/media/danna01/Disk/SNAPSHOTS/Galaxias_Viejas'

dicti = {}
galaxies = ['G0', 'G1']
limites_materia_oscura = {'G0':(0,55), 'G1':(0,75)} #kpc

def accumulated_mass(pos,mass,n,limits):
    """
    La funcion accumulated_mass va a calcular la 
    masa total acumulada hasta cierto radio.
    
    Parameters
    ----------
    posn : pynbody.array.SimArray
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
           
    """
    
    r = np.sqrt((pos**2).sum(axis=1))
    
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
    filename : str
        este atributo nos va a permitir 
        el almacenamiento de los plots generados.
    
    """ 
    fig = plt.figure(figsize=(10, 7))
    
    data_viejo_ruta_G0 = pynbody.load(data_viejo+'/G0/snapshot_100.hdf5')
    binsold1G0, massold1G0 = accumulated_mass(data_viejo_ruta_G0.dm['pos'],data_viejo_ruta_G0.dm['mass'],
                       n=int(limites_materia_oscura[gal][1]*4),limits=limites_materia_oscura[gal])
    plt.plot(binsold1G0,massold1G0,'-k',label= 'Old Galaxies G0/100')
    
    data_nuevo_ruta_G0 = pynbody.load(data_nuevo+'/G0/snapshot_100.hdf5')
    binsnew2G0, massnew2G0 = accumulated_mass(data_nuevo_ruta_G0.dm['pos'],data_nuevo_ruta_G0.dm['mass'],
                       n=int(limites_materia_oscura[gal][1]*4),limits=limites_materia_oscura[gal])
    plt.plot(binsnew2G0,massnew2G0,'-g',label= 'New Galaxies G0/100')
    
    data_viejo_ruta_G1 = pynbody.load(data_viejo+'/G1/snapshot_100.hdf5')
    binsold1G1, massold1G1 = accumulated_mass(data_viejo_ruta_G1.dm['pos'],data_viejo_ruta_G1.dm['mass'],
                            n=int(limites_materia_oscura[gal][1]*4),limits=limites_materia_oscura[gal])
    plt.plot(binsold1G1,massold1G1,'-r',label= 'Old Galaxies G1/100')
    
    data_nuevo_ruta_G1 = pynbody.load(data_nuevo+'/G1/snapshot_100.hdf5')
    binsnew2G1, massnew2G1 = accumulated_mass(data_nuevo_ruta_G1.dm['pos'],data_nuevo_ruta_G1.dm['mass'],
                            n=int(limites_materia_oscura[gal][1]*4),limits=limites_materia_oscura[gal]) 
    plt.plot(binsnew2G1,massnew2G1,'-b',label= 'New Galaxies G1/100')
    
    plt.title('Masa acumulada de la Materia Oscura', fontsize= 20)
    plt.xlabel('Radio [Kpc]',fontsize=18)
    plt.ylabel('Masa Acumulada (10$^{10}$ $M_\odot$)',fontsize=18)
    plt.text(60, 0, '$h_\star$ G0=1.1', fontsize=15, color='black')
    plt.text(60, 1, '$h_\star$ G1=1.5', fontsize=15, color='black')
    plt.legend()
    plt.grid()
    plt.savefig(filename)
    plt.clf()
    plt.close()
