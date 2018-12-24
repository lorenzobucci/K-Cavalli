import Numberjack as nj
from timeit import default_timer as timer


def disposizione_kCavalli(n: int, k: int):
    m = nj.Matrix(n, n)  # Matrice di variabili booleane nxn
    kCavalli = nj.Model()

    # Vincoli di interdizione delle celle rispetto alla cella corrente
    for i in range(n):
        for j in range(n):
            if j - 2 >= 0 and i + 1 <= n - 1:
                kCavalli.add((m[i][j] + m[i + 1][j - 2]) != 2)
            if j - 1 >= 0 and i + 2 <= n - 1:
                kCavalli.add((m[i][j] + m[i + 2][j - 1]) != 2)
            if j + 1 <= n - 1 and i + 2 <= n - 1:
                kCavalli.add((m[i][j] + m[i + 2][j + 1]) != 2)
            if j + 2 <= n - 1 and i + 1 <= n - 1:
                kCavalli.add((m[i][j] + m[i + 1][j + 2]) != 2)

    kCavalli.add(sum([m[i][j] for i in range(n) for j in range(n)]) == k)  # Vincolo per il numero di cavalli totali

    solver: nj.NBJ_STD_Solver = kCavalli.load('MiniSat')

    start = timer()
    esito = solver.solve()
    end = timer()

    return [end - start, esito]
