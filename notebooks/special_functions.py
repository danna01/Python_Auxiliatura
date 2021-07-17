def compile_data(origin,gal,minsnap,maxsnap,stepsnap):
    """
    La funcion compile_data permite almacenar de manera
    eficiente la informacion respecto a la velocidad maxima, 
    masa acumulada de las estrellas y de los gases y la 
    densidad de estrellas y gas.
    
    Parameters
    ----------
    origin : pynbody.snapshot
       snapshot leído con pynbody
    gal : dict
       diccionario de las galaxias a considerar
    minsnap : int
       numero minimo del snap considerado
    maxsnap : int
       numero maximo del snap considerado
    stepsnap : float
       valores de intervalo entre los snaps
        
    Returns
    -------
    dicti : dict
       diccionario con la informacion completa de
       Vmax, densidad y masa acumulada.
       
    """
    dicti = {}
    for snap in np.arange(minsnap,maxsnap,stepsnap): 
        if not snap % 10:
            print("working in snapshots number ",snap)
        
        snap = str(snap).zfill(3)        
        data = pynbody.load(origin+'/'+gal+'/snapshot_'+snap+'.hdf5')
        dicti[snap] = {}
                
        V_max = fn.plot_rot_curve(gal,data,filename='plots_nuevos/'+gal+'/'+gal+'_rotcurve_'+snap+'.jpg')
        dicti[snap]['Vmax'] = V_max
            
        N_star = data.star['mass'].size
        dicti[snap]['Nstar'] = N_star

        histo,bins,dens = fn.density(data.gas['pos'],data.gas['mass'],n=20,limits=limites_densidad[gal])
        m,b = fn.fit_exponential(bins,dens,limits=limites_gas[gal])
        fn.plot_exponential(bins,dens,m,b,filename='plots_nuevos/'+gal+'/'+gal+'_gas_'+snap+'.jpg')
        dicti[snap]['h_gas'] = -1/m*np.log10(np.e)
        
        histo,bins,dens = fn.density(data.star['pos'],data.star['mass'],n=20,limits=limites_densidad[gal])
        m,b = fn.fit_exponential(bins,dens,limits=limites_star[gal])
        fn.plot_exponential(bins,dens,m,b,filename='plots_nuevos/'+gal+'/'+gal+'_star_'+snap+'.jpg')
        dicti[snap]['h_star'] = -1/m*np.log10(np.e)

    return dicti

def extract_qtt(dictionary,quantity):
    """
    La funcion extract_qtt nos permite extraer la informacion
    del diccionario que generamos antes.
    
    Parameters
    ----------
    dictionary : dict
       diccionario en el que se recopilo toda la informacion
       importante de los snapshots.
    quantity : str
       la caracteristica que deseamos extraer, por ejemplo
       la Vmax.
        
    Returns
    -------
    lista : list
       lista con los datos de todos los snapshots de la informacion
       que requerimos.
       
    """
    if quantity == 'snapshots':
        lista = [np.float(key) for key in dictionary.keys()]
    else:
        lista = [dictionary[snap][quantity] for snap in dictionary.keys()]
    return lista

def show_results(dicti, dicti_old, gal):
    """
    La funcion show_results te permite visualizar la informacion
    y generar los histogramas con los datos de las propiedades
    que calculados anteriormente.
    
    Parameters
    ----------
    dicti : dict
       diccionario en el que se recopilo toda la informacion
       importante de los snapshots para las simulaciones nuevas.
    dicti_old : dict
       diccionario en el que se recopilo toda la informacion
       importante de los snpashots para las simulaciones viejas.
    gal : dict
       diccionario en el que se tienen las galaxias que 
       deseamos analizar.   
    """
    snapshots_new = extract_qtt(dicti,'snapshots')
    h0_gas_new = extract_qtt(dicti,'h_gas')
    h0_star_new = extract_qtt(dicti,'h_star')
    N_star_new = extract_qtt(dicti,'Nstar')
    Vmax_new = extract_qtt(dicti,'Vmax')
    
    # Aca hacemos lo mismo para los datos viejos:
    snapshots_old = extract_qtt(dicti_old,'snapshots')
    h0_gas_old = extract_qtt(dicti_old,'h_gas')
    h0_star_old = extract_qtt(dicti_old,'h_star')
    N_star_old = extract_qtt(dicti_old,'Nstar')
    Vmax_old = extract_qtt(dicti_old,'Vmax')
    
    # Definimos el tamaño del plot
    plt.figure(figsize=(12,4))
    
    # Definimos cada una de las posiciones de los plots, los histogramas y las posiciones que les vamos a dar,
    # asi como sus especificaciones para cada una de las variables.
    # Para los valores de Y en el plot hemos asignado valores arbitrarios, con el unico fin de poder visualizar 
    # la informacion.
    
    # Para el histograma del gas
    plt.subplot(131)
    plt.hist(h0_gas_new,bins=5,color='green')
    plt.title(gal + '  h0 GAS')
    #Como solo existen datos viejos para las galaxias G0 y G1 debemos especificar que los plots son solo
    #para esos datos con las siguientes lineas
    if gal in ['G0','G1']:
        x = h0_gas_old
        y = np.array([50,50,50])
        plt.plot(x,y, "ok")
    
    # Para el histograma de las estrellas
    plt.subplot(132)
    #Como solo existen datos viejos para las galaxias G0 y G1 debemos especificar que los plots son solo
    #para esos datos con las siguientes lineas
    if gal in ['G0']:
        plt.hist(h0_star_new,bins=5,range=(0,4),color='orange')
        plt.title(gal + 'h0 STARS')
    if gal in ['G1','G3']:
        plt.hist(h0_star_new,bins=5,color='orange')
        plt.title(gal + '  h0 STARS')
    if gal == 'G2':
        h0_gas_new = extract_qtt(super_dict['G2'],'h_star')
        plt.hist(h0_star_new,bins=20,color='green',range=(1,5))
        plt.title(gal + '  h0 STARS')
    if gal in ['G0','G1']:
        x = h0_star_old
        y = np.array([50,50,50])
        plt.plot(x,y,"ok")
    
    #Para la velocidad maxima
    plt.subplot(133)
    plt.hist(Vmax_new,bins=5,color='red')
    plt.title(gal + '  Max Velocity')
    #Como solo existen datos viejos para las galaxias G0 y G1 debemos especificar que los plots son solo
    #para esos datos con las siguientes lineas
    if gal in ['G0','G1']:
        x = Vmax_old
        y = np.array([50,50,50])
        plt.plot(x,y,"ok")