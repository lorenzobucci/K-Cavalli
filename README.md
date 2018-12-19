# Disposizione cavalli su scacchiera

Il software permette di trovare, su una scacchiera *n x n*, una disposizione di un numero arbitrario *k* di cavalli senza attacchi reciproci.

### Uso:

1.  Dal file *kCavalli.py* chiamare la funzione `disposizione_kCavalli(n: int, k: int)`

    *  Parametri: *n* dimensione della scacchiera, *k* numero di cavalli da disporre.

2.  Per semplicità la funzione stamperà direttamente a video la soluzione finale, se esiste.

    *  La soluzione sarà costituita da una matrice *n x n* su cui saranno presenti i valori 0 e 1.\
    Lo 0 rappresenta la cella vuota, il valore 1 rappresenta la presenza di un cavallo.
 
 ### Requisiti:
 
 * **Bash linux (o WSL su Windows 10)**
    * python3-dev (o python-dev)
    * swig (3.X)
    * libxml2-dev
    * zlib1g-dev
    * libgmp-dev
 * Numberjack: `pip install Numberjack`