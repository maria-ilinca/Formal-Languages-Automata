# nfa parser

import re

sigma = set()  # alfabetul
Q = {}  # multimea starilor
q0 = {}  # starea initiala
d = []  # functia de tranzitie
F = {}  # starile finale
ls_d = []  # lista cu elementele liste de trei elemente pentru functia de tranzitie

fin = open("nfa_config_file")
f = fin.readlines()  # continutul fisierului
ends = 0
valid = True
index = 0
while index < len(f) and ends < 3 and valid is True:
    lin = f[index]
    lin_aux = ""  # linie auxiliara pentru a lua randul pana la primul '#'
    for element in lin.strip():
        if element == '#':
            break
        lin_aux += element
    lin = lin_aux
    index += 1

    # Skip la comentarii
    if len(lin.strip()) > 0 and lin.strip()[0] == "#":
        "skip"

    """
    Sigma
    """

    if lin.strip() == 'Sigma:':
        while index < len(f) and lin.strip() not in {"End", "end"} and valid is True:
            lin = f[index]
            index += 1
            if len(lin.strip()) > 0 and lin.strip()[0] == "#":
                "skip"
            elif lin.strip() not in {"End", "end", ""}:
                lin_aux = ""  # linie auxiliara pentru a lua randul pana la primul '#'
                for element in lin.strip():
                    if element == '#':
                        break
                    lin_aux += element
                if lin_aux.strip() in sigma:  # daca a mai aparut nu e valid - nu puteam avea aceeasi litera de doua ori in alfabet
                    valid = False
                for element in lin_aux.split():
                    sigma.add(element)

        else:
            ends += 1

    """
    States
    """
    if lin.strip() == "States:":
        i = 0
        while index < len(f) and lin.strip() not in {"End", "end", ""} and valid is True:
            lin = f[index]
            index += 1
            ls_aux = []  # lista auxiliara pentru elementele de pe un rand
            if len(lin.strip()) > 0 and lin.strip()[0] == "#":
                "skip"
            elif lin.strip() not in {"End", "end", ""}:
                lin_aux = ""  # linie auxiliara pentru a lua randul pana la primul '#'
                for element in lin.strip():
                    if element == '#':
                        break
                    lin_aux += element
                stari = re.split(" |,",
                                 lin_aux.strip())  # lista care contine starea si, daca e cazul, daca e finala sau de inceput

                if stari[0] in Q:  # nu putem avea aceeasi stare de doua ori in multimea de stari
                    valid = False

                for stare in stari:
                    if stare != "F" and stare != "S" and "#" not in stare:
                        Q[stari[0]] = i
                    if "F" == stare.strip():
                        F[stari[0]] = i
                    if "S" == stare.strip():
                        q0[stari[0]] = i
                i += 1
        else:
            ends += 1

    if lin.strip() == "Transitions:":
        i = 0
        while index < len(f) and lin.strip() not in {"End", "end", ""} and valid is True:
            lin = f[index]
            index += 1
            if len(lin.strip()) > 0 and lin.strip()[0] == "#":
                "skip"
            elif lin.strip() not in {"End", "end", ""}:
                lin_aux = ""  # linie auxiliara pentru a lua randul pana la primul '#'
                for element in lin.strip():
                    if element == '#':
                        break
                    lin_aux += element
                ls = re.split(" |, ", lin_aux.strip())  # lista pentru fiecare element de pe rand

                if len(ls) == 3:
                    ls_d.append(ls)
                i += 1
        else:
            ends += 1

fin.close()

d = [[-1 for i in range(len(Q))] for j in range(len(Q))]

print(ls_d)

for tp in ls_d:
    # In caz ca e posibil ca litera de tranzitie sa nu fie in alfabet
    if tp[1] not in sigma:
        valid = False
        break
    # Q[tp[0]] - din dictionarul Q, identifica linia asociata starii "stateX" si coloana
    # asociata starii "stateY" si pune in matrice litera prin care se realizeaza tranzitia
    # daca e posibil sa se defineasca o functie pe o stare care nu se afla in multimea de stari atunci apare keyerror
    # pentru care avem try-except
    try:
        if d[Q[tp[0]]][Q[tp[2]]] != -1:
            d[Q[tp[0]]][Q[tp[2]]].append(tp[1])
        else:
            d[Q[tp[0]]][Q[tp[2]]] = [tp[1]]

    except:
        valid = False
        break

# daca avem mai multe stari de inceput nu e valid - nu e determinist
if len(q0) != 1:
    valid = False

# daca nu avem vreuna dintre multimi

if len(sigma) <= 0 or len(Q) <= 0 or len(d) <= 0 or len(F) <= 0:
    valid = False

print(f"sigma: {sigma}")
print(f"Q: {Q}")
print(f"q0 {q0}")
print(f"d: {d}")
print(f"F: {F}")

if valid is False:
    print("Automatul nu e valid")
else:
    print("Automatul e valid\n")

cuvant = input("cuvant = ")


ok = 1


# aux - starea initiala
aux = q0[list(q0.keys())[0]]
lista_stari = []  # starile in care ne aflam la un moment dat
# nou_lista_stari se actualizeaza in functie de starile in care ne duce functia de tranzitie pentru fiecare litera# din cuvant
nou_lista_stari = [aux]
for lit in cuvant:
    # daca vreo litera din cuvantul primit nu e in alfabet
    if lit not in sigma:
        ok = 0
    # lista_litere e o lista din matricea asociata functiei de tranzitie care are litere pentru care starea respectiva are tranzitii
    # daca am ajuns in cel putin o stare de la pasul anterior putem continua si copiem lista noua in lista actuala(lista_stari)
    # altfel inseamna ca nu se accepta cuvantul
    if (len(nou_lista_stari) != 0):
        lista_stari = nou_lista_stari.copy()
    else:
        ok = 0
    # pentru fiecare stare in care ne aflam vedem in ce stari ne poate duce
    for stare in lista_stari:
        nou_lista_stari = []
        for index in range(len(d[stare])):
            if d[stare][index] != -1:
                for litera_tranzitie in d[stare][index]:
                    if litera_tranzitie == lit:
                        nou_lista_stari.append(index)
# cand se termina literele din cuvant o sa avem in nou_lista_stari starile in care am ajuns si verificam daca
# cel putin una dintre ele este finala
ok_stare_finala = 0  # pentru a verifica daca avem vreo stare finala

for stare_finala in F:
    try:
        nou_lista_stari.index(F[stare_finala])
        ok_stare_finala = 1
    except:
        "skip"
if ok_stare_finala == 0:
    ok = 0

if ok == 1:
    print("OK")
else:
    print("NOT OK")
