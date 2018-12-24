"""
Questo script testa il tempo di risoluzione del problema al variare di n e k.
I risultati vengono salvati nel file Excel "Dati.xlsx" che verrà SOVRASCRITTO ad ogni esecuzione.
Il test si interrompe a n = 18 perchè già con n = 19 il tempo di risoluzione è > 30 min.
"""

from _kCavalli import *
import xlsxwriter as xw

file = xw.Workbook("Dati.xlsx")  # Creazione file Excel

for n in range(2, 18):
    print(n)

    # Aggiunta foglio e intestazione
    foglio = file.add_worksheet(str(n))
    foglio.write_row(0, 0, ["K", "Tempo (s)", "Soddisfacibilità"])

    i = 1  # Usato per scrivere i risultati in riga
    for k in range(1, (n ** 2) + 1, n - 1):
        risultato = disposizione_kCavalli(n, k)
        foglio.write_row(i, 0, [k] + risultato)
        i += 1
