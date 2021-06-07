import numpy as np

# Radial surface density of the disk
def density(pos,mass,n,limits):
    r       = np.sqrt((pos[:,:2]**2).sum(axis=1)) # Azymutal radius 
    histo   = np.histogram(r,n,range=limits)
    #plt.hist(r,n,range=limits)
    bins     = (histo[1][:-1]+histo[1][1:])/2
    bn_mass = np.zeros(n)
    # Aca sacamos la sumatoria de la masa que esta concentrada en cada una de las barras del histograma.
    for i in range(n):
            bn_mass[i]      = mass[(r >= histo[1][i])*(histo[1][i+1] > r)].sum()
    dens    = bn_mass/(np.pi)/((histo[1][1:])**2-(histo[1][:-1])**2)
    return histo,bins,dens


#En esta celda vamos a definir las funciones con las cuales se van a calcular los radios para el alcance de las
#posiciones de las particulas de gas en primer lugar y de las estrellas: Para esto se saca la raiz cuadrada
#de sus posiciones en X y en Y elevadas al cuadrado.
def RGas(data):
    """
    En esta celda vamos a definir las funciones con las
    cuales se van a calcular los radios para el alcance de las
    posiciones de las particulas de gas en primer lugar y de
    las estrellas: Para esto se saca la raiz cuadrada
    de sus posiciones en X y en Y elevadas al cuadrado.
    
    Parameters
    ----------
    data : pynbody.snapshot
       snapshot leído con pynbody
        
    Returns
    -------
    Rg : ndarray
        vector con los radios hasta cada partículo, medidos
        en el plano ecuatorial
        
    Notes
    -----
    Este radio se calcula solo con las coordenas X,Y asumiendo
    que el disco coincide con el plano ecuatorial
    
    """
    Rg = np.sqrt(data.gas['pos'][:,0]**2 + data.gas['pos'][:,1]**2)
    return Rg

def RStar(data):
    Rs = np.sqrt(data.star['pos'][:,0]**2 + data.star['pos'][:,1]**2)
    return Rs

#Aca nuevamente calculamos el radio pero en este caso de la materia oscura, en donde ademas consideraremos
#la coordenada en el eje Z: Por ende determinaremos la raiz cuadrada de la suma de las componentes en X, Y y Z al cuadrado.
def RDm(data):
    Rdm = np.sqrt(data.dm['pos'][:,0]**2 + data.dm['pos'][:,1]**2 + data.dm['pos'][:,2]**2)
    return Rdm