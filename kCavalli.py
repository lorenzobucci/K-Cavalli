import Numberjack as nj


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

    if solver.solve():
        print("In una scacchiera %dx%d una soluzione che dispone %d cavalli senza attacchi è :" % (n, n, k))
        print(m)
    else:
        print("In una scacchiera %dx%d è impossibile disporre %d cavalli senza attacchi!" % (n, n, k))