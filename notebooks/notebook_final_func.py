import pynbody
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy import optimize
import scipy.stats
from astropy import units as unit
import sys
from matplotlib.animation import FuncAnimation

def accumulated_mass(posnew,massnew,posold, massold,n,limits):
    """
    La funcion accumulated_mass va a calcular la 
    masa total acumulada hasta cierto radio y va a permitirle
    comparar los datos obtenidos para diferentes simulaciones
    de la misma galaxia.
    
    Parameters
    ----------
    posnew : pynbody.array.SimArray
       posicion de las particulas de cada snapshot (simulaciones nuevas)
    massnew : pynbody.array.SimArray
       masa de cada una de las particulas en el snapshot (simulaciones nuevas)
    posold : pynbody.array.SimArray
       posicion de las particulas de cada snapshot (simulaciones viejas)
    massold : pynbody.array.SimArray
       masa de cada una de las particulas en el snapshot (simulaciones viejas)
    n : int
       numero de rectangulos en el histograma
    limits : tuple
       valores maximos y minimos a considerar en el histograma
        
    Returns
    -------
    positionsnew : ndarray
        retorna los valores de las posiciones
        de los radios limite de las barras del histograma (galaxias nuevas).
    histo_acum_new[0] : ndarray
        retorna el valor de la masa acumulada para 
        cada radio limite (galaxias nuevas).
    positionsold : ndarray
        retorna los valores de las posiciones
        de los radios limite de las barras del histograma (galaxias viejas).
    histo_acum_old[0] : ndarray
        retorna el valor de la masa acumulada para 
        cada radio limite (galaxias viejas).
           
    Notes
    -----
    Esta funcion de masa acumulada sera utilizada cuando
    se esten comparando las diferentes galaxias.
    
    """
    
    rnew = np.sqrt((posnew**2).sum(axis=1))
    
    histo_acum_new = scipy.stats.cumfreq(rnew, n, limits, weights=massnew)
   
    positionsnew = histo_acum_new[1]+ np.arange(1,n+1) * histo_acum_new[2]

    rold = np.sqrt((posold**2).sum(axis=1))
    histo_acum_old = scipy.stats.cumfreq(rold, n, limits, weights=massold)
    positionsold = histo_acum_old[1]+ np.arange(1,n+1) * histo_acum_old[2]
    
    return positionsnew, histo_acum_new[0], positionsold, histo_acum_old[0]

def plot_mass(binsnewg0,massnewg0,binsoldg0,massoldg0,binsnewg1,massnewg1,binsoldg1,massoldg1,filename):
    """
    La funcion plot_mass va a permitirle graficar las masas
    acumuladas de cada simulacion vs el radio para poder
    comparar los datos obtenidos.
    
    Parameters
    ----------
    binsnewg0 : ndarray
        retorna los valores de las posiciones
        de los radios limite de las barras del histograma (galaxias nuevas) para G0.
    massnewg0 : ndarray
        retorna el valor de la masa acumulada para 
        cada radio limite (galaxias nuevas) para G0
    binsoldg0 : ndarray
        retorna los valores de las posiciones
        de los radios limite de las barras del histograma (galaxias viejas) para G0.
    massoldg0 : ndarray
        retorna el valor de la masa acumulada para 
        cada radio limite (galaxias viejas) para G0.
    binsnewg1 : ndarray
        retorna los valores de las posiciones
        de los radios limite de las barras del histograma (galaxias nuevas) para G1.
    massnewg1 : ndarray
        retorna el valor de la masa acumulada para 
        cada radio limite (galaxias nuevas) para G1.
    binsoldg1 : ndarray
        retorna los valores de las posiciones
        de los radios limite de las barras del histograma (galaxias viejas) para G1.
    massoldg1 : ndarray
        retorna el valor de la masa acumulada para 
        cada radio limite (galaxias viejas) para G1.
    filename : str
        este atributo nos va a permitir 
        el almacenamiento de los plots generados.
    
    """
    fig = plt.figure(figsize=(10, 7))
    
    plt.plot(binsnewg0,massnewg0,'-',color='red',label= 'New Galaxies G0/'+snap)
    plt.plot(binsoldg0,massoldg0,'-',color='blue',label= 'Old Galaxies G0/'+snap)
    plt.plot(binsnewg1,massnewg1,'-',color='green',label= 'New Galaxies G1/'+snap)
    plt.plot(binsoldg1,massoldg1,'-', color='black', label= 'Old Galaxies G1/'+snap)
    
    plt.title('Masa acumulada de la Materia Oscura', fontsize= 18)
    plt.xlabel('Radio [Kpc]',fontsize=20)
    plt.ylabel('Masa Acumulada ($1x10^{10}$ $M_\odot$)',fontsize=20)
    plt.text(60, 0, '$h_\star$ G0=1.1', fontsize=15, color='black')
    plt.text(60, 1, '$h_\star$ G1=1.5', fontsize=15, color='black')
    plt.legend()
    plt.grid()
    plt.savefig(filename)
    plt.clf()
    plt.close()