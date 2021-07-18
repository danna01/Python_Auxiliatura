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


def density_dm(xnew,ynew,xold,yold):
    """
    La funcion density_dm va a calcular la  densidad de la masa
    que se acumula en cada una de las barras del histograma y 
    permite compararlas para las galaxias nuevas y viejas.
    
    Parameters
    ----------
    xnew : ndarray
       valores de las posiciones de los radios limite de las 
       barras del histograma (galaxias nuevas).
    ynew : ndarray
       valor de la masa acumulada para 
       cada radio limite (galaxias nuevas).
    xold : ndarray
       valores de las posiciones de los radios limite de las 
       barras del histograma (galaxias viejas).
    yold : ndarray
       el valor de la masa acumulada para 
       cada radio limite (galaxias viejas).
        
    Returns
    -------
    bins_middle_new : ndarray
        retorna los valores de los radios
        promedios de cada barra (galaxias nuevas).
    shell_mass_new : ndarray
        retorna el valor de la masa en cada cascaron para 
        cada radio limite (galaxias nuevas).
    densnew : ndarray
        retorna los valores de la densidad
        de cada cascaron (galaxias nuevas).
    bins_middle_old : ndarray
        retorna los valores de los radios
        promedios de cada barra (galaxias viejas).
    shell_mass_old : ndarray
        retorna el valor de la masa en cada cascaron para 
        cada radio limite (galaxias viejas).
    densold : ndarray
        retorna los valores de la densidad
        de cada cascaron (galaxias viejas).
           
    Notes
    -----
    Recuerde que la funcion de densidad es: \rho = (4/3)*pi*R^3
    
    """
    xnew,ynew, xold, yold =     accumulated_mass(data_nuevo_ruta.dm['pos'],data_nuevo_ruta.dm['mass'],data_viejo_ruta.dm['pos'],data_viejo_ruta.dm['mass'],n=int(limites_materia_oscura[gal][1]*4),limits=limites_materia_oscura[gal])
    x2new = np.roll(xnew,1)
    x2new[0]=0
    
    bins_middle_new = (xnew + x2new )/2
    
    x_cubico_new = xnew**3
    x_cubico_2_new = np.roll(x_cubico_new,1)
    x_cubico_2_new[0]=0
   
    y2new = np.roll(ynew,1)
    y2new[0]=0
  
    shell_mass_new = ynew - y2new
    
    # \rho = (4/3)*pi*R^3
    densnew = 3* shell_mass_new / ((4*np.pi)* (x_cubico_new - x_cubico_2_new) )
    
 
    x2old = np.roll(xold,1)
    x2old[0]=0
    bins_middle_old = (xold + x2old )/2
    
    x_cubico_old = xold**3
    x_cubico_2_old = np.roll(x_cubico_old,1)
    x_cubico_2_old[0]=0
    
    y2old = np.roll(yold,1)
    y2old[0]=0
   
    shell_mass_old = yold - y2old
    
    # \rho = (4/3)*pi*R^3
    densold = 3* shell_mass_old / ((4*np.pi)* (x_cubico_old - x_cubico_2_old) ) 
    
    return bins_middle_new, shell_mass_new, densnew, bins_middle_old, shell_mass_old, densold


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
    

def plot_density(binsnew,densnew,binsold, densold, filename):
    """
    La funcion plot_mass va a permitirle graficar las masas
    acumuladas de cada simulacion vs el radio para poder
    comparar los datos obtenidos.
    
    Parameters
    ----------
    binsnew : ndarray
        valores de los radios
        promedios de cada barra (galaxias nuevas).
    densnew : ndarray
        valores de la densidad
        de cada cascaron (galaxias nuevas).
    binsold : ndarray
        valores de los radios
        promedios de cada barra (galaxias viejas).
    densold : ndarray
        valores de la densidad
        de cada cascaron (galaxias viejas).
    filename : str
        este atributo nos va a permitir 
        el almacenamiento de los plots generados.
    
    """
    fig = plt.figure(figsize=(10, 7))
    
    plt.plot(binsnew, np.log10(densnew), '-k', label= 'New Galaxies '+gal+'/'+snap)
    plt.plot(binsold, np.log10(densold), '-r', label= 'Old Galaxies')
   
    plt.title('Perfil de densidad de materia oscura', fontsize = 18)
    plt.xlabel('Radio [Kpc]', fontsize = 20)
    plt.ylabel(r'$\rho$ [$1x10^{10}$ Msol/$kpc^{2}$]', fontsize = 20)
    plt.legend()
    plt.grid()
    plt.savefig(filename)
    plt.clf()
    plt.close()