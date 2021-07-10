def density(pos,mass,n,limits):
    """
    La funcion densidad nos permite calcular la densidad
    superficial radial para las estrellas y para el gas
    de cada una de las galaxias. 
    
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
    histo : tuple
        retorna los dos valores obtenidos con la funcion
        de histo.
    bins : ndarray
        retorna el radio promedio de los dos radios extremos
        de los rectangulos.
    dens : ndarray
        retorna el valor de la densidad para cada una de las
        zonas consideradas.
           
    Notes
    -----
    El radio para la posicion se calcula solo con las coordenas 
    X,Y asumiendo que el disco coincide con el plano ecuatorial.
    
    """
    r       = np.sqrt((pos[:,:2]**2).sum(axis=1))  
    histo   = np.histogram(r,n,range=limits)
    bins     = (histo[1][:-1]+histo[1][1:])/2
    bn_mass = np.zeros(n)
   
    for i in range(n):
            bn_mass[i]      = mass[(r >= histo[1][i])*(histo[1][i+1] > r)].sum()
    dens    = bn_mass/(np.pi)/((histo[1][1:])**2-(histo[1][:-1])**2)
    return histo,bins,dens

def fit_exponential(x,y,limits):
    """
    La funcion fit_exponential nos permite calcular la recta que mejor
    se ajuste a los datos de densidad calculados a partir de la 
    informacion de los snapshots.
    
    Parameters
    ----------
    x : ndarray
       corresponde a los radios medios calculados con la funcion densidad.
    y : ndarray
       corresponde a la densidad calculada con la funcion densidad.
    limits : tuple
       valores maximos y minimos a considerar en el grafico.
        
    Returns
    -------
    m : float
        retorna los valores mas apropiados para la pendiente de la recta que se
        ajusta a los datos obtenidos.
    b : float
        retorna los valores mas apropiados para el intercepto en el eje y
        que se ajusta a los datos obtenidos.
           
    Notes
    -----
    La funcion utilizada para hallar el minimo error cuadrado posible
    es leastsq.
    
    """
    mask = (x >= limits[0])*(x <= limits[1])
    x = x[mask]
    y = y[mask]
    y = np.log10(y)
    m_0 = (y[-1] - y[0])/(x[-1] - x[0])
    b_0 = y[0] - m_0*x[0]
    errfun  = lambda p: np.ravel(p[0]*x[:]+p[1]-y[:])
    fitparam = optimize.leastsq(errfun,[m_0,b_0],full_output=1)[0]
    m = fitparam[0]
    b = fitparam[1]
    return m,b

def plot_exponential(bins,dens,m,b,filename):
    """
    La funcion plot_exponential nos permite graficar
    los datos hallados para la densidad y compararlo
    con la recta con el mejor ajuste cuadrado.
    
    Parameters
    ----------
    bins : ndarray
           retorna el radio promedio de los dos radios extremos
           de los rectangulos.
    dens : ndarray
           retorna el valor de la densidad para cada una de las
           zonas consideradas.
    m : float
        retorna los valores mas apropiados para la pendiente de la recta que se
        ajusta a los datos obtenidos.
    b : float
        retorna los valores mas apropiados para el intercepto en el eje y
        que se ajusta a los datos obtenidos.
    filename : str
               Es la forma en la cual va a quedar almacenado el plot
               al momento de guardarlo.
    
    """
    R = (-1./m)*np.log10(np.e)
    fig = plt.figure(figsize=(10, 7))
    plt.plot(bins, np.log10(dens), 'r.', label = 'h = {a:3.2f}'.format(a = R))
    plt.plot(bins,m*bins+b,'-k')
    plt.legend(fontsize = 20, loc=0)
    plt.title('Perfil de densidad superficial', fontsize = 18)
    plt.xlabel('Radio [Kpc]', fontsize = 20)
    plt.ylabel(r'$\rho$ [$1x10^{10}$ Msol/$kpc^{2}$]', fontsize = 20)
    plt.grid()
    plt.savefig(filename)
    plt.clf()
    plt.close()

def RGas(data):
    """
    La funcion RGas va a calcular el radio azimutal
    del disco que consideraremos para los calculos.
    
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

def Vcartesian2polar(pos,vel):
    """
    La funcion Vcartesian2polar va a calcular las
    velocidades tangenciales y radiales.
    
    Parameters
    ----------
    pos : pynbody.array.SimArray
       la posicion de las particulas del snapshot
    vel : pynbody.array.SimArray
       la velocidad de las particulas del snapshot
        
    Returns
    -------
    Vtan : ndarray
        velocidad tangencial de la particula
    Vrad : ndarray
        velocidad radial de la particula
    
    """
    Vtan    = np.zeros(pos.shape[0])
    Vrad    = np.zeros(pos.shape[0])
    norm    = np.sqrt(pos[:,0]**2+pos[:,1]**2)
    Vtan    = (vel[:,1]*pos[:,0]-vel[:,0]*pos[:,1])/norm
    Vrad    = (vel[:,0]*pos[:,0]+vel[:,1]*pos[:,1])/norm
    return Vtan,Vrad

def radios(points):
    """
    la funcion radios va a calcular el radio azimutal
    del disco que consideraremos para los calculos.
    
    Parameters
    ----------
    points : ndarray
       valores de los radios extremos de los rectangulos
       que se consideran.
        
    Returns
    -------
    Radii : ndarray
        vector con los puntos medios de los radios extremos
        de cada rectangulo.
        
    Notes
    -----
    Este radio se calcula solo con las coordenas X,Y asumiendo
    que el disco coincide con el plano ecuatorial
    
    """
    radii     = (points[:-1]+points[1:])/2
    return radii 

def RotCurvGas(data,points):
    """
    La funcion RotCurvGas a calcular el radio azimutal
    del disco que consideraremos para los calculos y lo hace
    asumiendo que se presentan bins circulares, tomando en cada bin
    la media de las velocidades tangenciales, pero ponderada por la 
    masa de cada partícula.
    
    Parameters
    ----------
    data : pynbody.snapshot
       snapshot leído con pynbody
    points : ndarray
       valores de los radios maximos y minimos
       de cada rectangulo del histograma.
        
    Returns
    -------
    a[1][0:len(points)-1]: PREGUNTAR
    
    Vel: ndarray
         Velocidad de las particulas.
    
    Notes
    -----
    El valor de cada particula dependera de su masa
    en esta funcion, contrario a lo que ocurre normalmente.
         
        
    """
    a = np.histogram(fn.RGas(data), bins=points, weights= fn.Vcartesian2polar(data.gas["pos"],data.gas["vel"])[0]*data.gas['mass'])
    b = np.histogram(fn.RGas(data), bins=points, weights= data.gas['mass'])
    Vel = (a[0]/b[0])
    return a[1][0:len(points)-1],Vel

def plot_rot_curve(gal,data,filename):
    """
    Con esta funcion vamos a calcular el radio azimutal
    del disco que consideraremos para los calculos.
    
    Parameters
    ----------
    gal : list
       el diccionario con las galaxias a trabajar
    data : pynbody.snapshot
       snapshot leído con pynbody
    filename : str
       ruta en la que va a ser almacenado el documento
       
        
    Returns
    -------
    np.nanmax(Vel) : float
        Velocidad maxima de las particulas
    
    """
    r_bins = np.arange(limites_densidad['G0'][0],limites_densidad['G0'][1],0.5)
    Vel = fn.RotCurvGas(data,r_bins)[1]
    r = radios(r_bins)
    plt.plot(r,Vel)
    
    fig = plt.figure(figsize=(10, 7))
    plt.plot(r,Vel)
    plt.title('Curva de rotación del gas', fontsize = 18)
    plt.xlabel('Radio [Kpc]', fontsize = 20)
    plt.ylabel(r'V_{circular}$ [km / s]', fontsize = 20)
    plt.grid()
    plt.savefig(filename)
    plt.clf()
    plt.close()
    
    return np.nanmax(Vel)



