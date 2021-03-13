import time
import random

# BUBBLESORT

def bubblesort(lista,nr, nmax):
    if nr >= 10**5:
        return -1
    ok=1
    while ok==1:
        ok=0;
        for i in range(len(lista)-1):
            if lista[i]>lista[i+1]:
                lista[i],lista[i+1]=lista[i+1],lista[i]
                ok=1;
    return lista


# COUNTSORT

def countsort(lista,nr,nmax):
    if nr>=10**8 or nmax>=10**9:
        return -1

    # Se initializeaza vectorul de frecventa
    nrmax = max(lista)
    v = [0] * (nrmax+1)
    for element in lista:
        v[element] += 1

    # Se parcurge vectorul de frecventa
    j=0
    for i in range(len(v)):
        while v[i]!=0:
            lista[j]=i
            v[i] -= 1
            j += 1
    return lista


# MERGESORT

def merge(lista,nr,nmax):
    if nr>=10**7:
        return -1

    # Se apeleaza recursiv functia pana cand lista are lungimea 1
    if len(lista) == 1:
        return lista
    l1 = lista[:len(lista)//2]
    l2 = lista[len(lista)//2:]
    merge(l1,nr,nmax)
    merge(l2,nr,nmax)

    # Se interclaseaza cele 2 liste primite ca parametru
    i = j = k = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            lista[k] = l1[i]
            i += 1
        else:
            lista[k] = l2[j]
            j += 1
        k += 1
    while i < len(l1):
        lista[k] = l1[i]
        i += 1
        k += 1
    while j < len(l2):
        lista[k] = l2[j]
        j += 1
        k += 1


# QUICKSORT CU PIVOTUL PE ULTIMUL ELEMENT

def partitie(lista, st, dr):
    i = st - 1
    pivot = lista[dr]

    # Elementele mai mici decat pivotul trec in stanga listei
    # Elementele mai mari decat pivotul trec in dreapta listei
    for j in range(st,dr):
        if lista[j]<pivot:
            i+=1
            lista[i],lista[j]=lista[j],lista[i]
    lista[i+1],lista[dr]=lista[dr],lista[i+1]

    # Returneaza pozitia pivotului in lista sortata
    return i+1

def quicksort1(lista, st, dr,nr,nmax):
    if nr>=10**4 or nmax>=10**6:
       return -1
    if len(lista)==1:
        return lista
    if st<dr:

        # Obtinem pozitia pivotului in lista sortata
        p = partitie(lista,st,dr)

        # Se apeleaza recursiv functia, impartindu-se lista dupa pivot
        quicksort1(lista,st,p-1,nr,nmax)
        quicksort1(lista,p+1,dr,nr,nmax)
    return lista


# QUICKSORT CU PIVOTUL ALES PRIN ALGORITMUL MEDIANA MEDIANELOR

def mediana_medianelor(lista1):
    n = len(lista1)
    if n <=5:
        lista1.sort()
        return lista1[n//2]
    v = []
    i = 0

    # Cream o lista cu valorile din mijlocul fiecarei secvente
    # sortate de cate 5 elemente din lista primita ca parametru
    while i <= n-5:
        aux = lista1[i:i+5].copy()
        aux.sort()
        v.append(aux[2])
        i += 5

    # Se apeleaza functia pana cand lista are cel mult 5 elemente
    return mediana_medianelor(v)

def partitie1(lista, st, dr):
    i = st - 1
    pivot = lista[dr]

    # Elementele mai mici decat pivotul trec in stanga listei
    # Elementele mai mari decat pivotul trec in dreapta listei
    for j in range(st,dr):
        if lista[j]<pivot:
            i+=1
            lista[i],lista[j]=lista[j],lista[i]
    lista[i+1],lista[dr]=lista[dr],lista[i+1]

    # Returneaza pozitia pivotului in lista sortata
    return i+1

def partitie2(lista,st,dr):
    laux=lista[st:dr+1].copy()

    # Obtinem valoarea pivotului prin algoritmul mediana medianelor
    pivot = mediana_medianelor(laux)

    # Cautam pozitia pivotului in lista primita ca parametru
    i=lista[st:dr+1].index(pivot)

    # Punem pivotul pe ultima pozitie din lista
    if st != 0:
        lista[i+st],lista[dr]=lista[dr],lista[i+st]
    else:
        lista[i],lista[dr]=lista[dr],lista[i]
    return partitie1(lista,st,dr)

def quicksort2(lista, st, dr,nr,nmax):
    if nr>=10**6:
        return -1
    if nr>=10**4 and nmax<100:
        return -1
    if len(lista)==1:
        return lista
    if st<dr:

        # Obtinem pozitia pivotului in lista sortata
        p = partitie2(lista,st,dr)

        # Se apeleaza recursiv functia, impartindu-se lista dupa pivot
        quicksort2(lista,st,p-1,nr,nmax)
        quicksort2(lista,p+1,dr,nr,nmax)
    return lista


# RADIXSORT CU NUMERE IN BAZA 10

def count1(lista, exp):

    # Consider numerele in baza 10 deci imi trebuie
    # un vector de frecventa pentru cifrele de la 0 la 9
    vf = [0] * 10
    aux = [0] * len(lista)

    # Se incrementeaza vectorul de frecventa
    for element in lista:
        cifra = (element/exp)
        vf[int(cifra%10)] += 1

    # La fiecare valoare se adauga valorile anterioare
    # pentru a obtine pozitiile in lista sortata
    for i in range(1,10):
        vf[i] += vf[i-1]

    # Se parcurge vectorul de frecventa
    for i in range(len(lista)-1,-1,-1):
        cifra = (lista[i]/exp)
        aux[vf[int(cifra%10)]-1]=lista[i]
        vf[int(cifra%10)] -= 1
    for i in range(0,len(lista)):
        lista[i]=aux[i]

def radixsort_b10(lista,nr,nmax):
    if nr>= 10**5:
        return -1
    nrmax = max(lista)
    exp = 1

    # Se sorteaza numerele dupa cifrele de pe fiecare pozitie din numar,
    # de la rangul cel mai mic la cel mai mare (de la dreapta la stanga)
    while nrmax/exp > 0:
        count1(lista,exp)
        exp *= 10
    return lista


# RADIXSORT CU NUMERE IN BAZA 2

def baza2(numar):

    # Se scrie numarul in baza 2
    l = []
    while numar>0:
        rest = numar%2
        numar = numar//2
        l.append(rest)
    l.reverse()
    for i in range(len(l)):
        numar = numar*10+l[i]
    return numar

def count2(lista, exp):

    # Consider numerele in baza 2 deci imi trebuie
    # doar 2 pozitii in vectorul de frecventa pentru cifrele 0 si 1
    vf = [0] * 2
    aux = [0] * len(lista)

    # Se incrementeaza vectorul de frecventa
    for element in lista:
        cifra = baza2(element>>exp)
        vf[int(cifra%10)] += 1

    # La fiecare valoare se adauga valorile anterioare
    # pentru a obtine pozitiile in lista sortata
    for i in range(1,2):
        vf[i] += vf[i-1]

    # Se parcurge vectorul de frecventa
    for i in range(len(lista)-1,-1,-1):
        cifra = baza2(lista[i]>>exp)
        aux[vf[int(cifra%10)]-1]=lista[i]
        vf[int(cifra%10)] -= 1
    for i in range(0,len(lista)):
        lista[i]=aux[i]

def radixsort_b2(lista,nr,nmax):
    if nr>=10**6:
        return -1
   # if nr>=10**5 and nmax>=10**6:
       # return -1
    nrmax = max(lista)
    exp = 0

    # Se sorteaza numerele dupa cifrele de pe fiecare pozitie din numar,
    # de la rangul cel mai mic la cel mai mare (de la dreapta la stanga)
    while nrmax>>exp > 0:
        count2(lista,exp)
        exp += 1
    return lista


# TEST SORTARE

def test_sort(lista):
    aux = lista.copy()
    lista.sort()
    if lista == aux:
        return True
    else:
        return False

def ordonare(tuplu):
    return tuplu[1]

# Pun algoritmii de sortare in 2 liste in functie de numarul
# de parametrii pe care trebuie sa il primeasca functia
sorts1 = [bubblesort, merge, radixsort_b10, radixsort_b2, countsort]
sorts2= [quicksort1, quicksort2]

# Citesc din fisier cate teste se vor face
f = open("Teste")
s = f.readline()
nr_teste = int(s.strip())
s = f.readline()

# Incepe rularea pentru fiecare test din fisier
for i in range(1,nr_teste+1):
    numere = [int(x) for x in s.split()]
    s = f.readline()
    print("Testul", i, "are o lista cu", numere[0], "numere cu valoarea maxima de", numere[1])

    # Creez lista de sortat in functie de N si MAX (valorile citite din fisier)
    lista_test = random.choices(range(0,numere[1]), k=numere[0])
    rez = []

    # Se parcurge prima lista de algoritmi de sortare
    for sort in sorts1:
        li = lista_test.copy()

        start = time.perf_counter()
        sort(li,numere[0],numere[1])
        end = time.perf_counter()

        dif = float("{:.7f}".format(end-start))
        nume = sort.__name__

        # In lista 'rez' se adauga perechi de forma (nume algoritm, valoare)
        # Unde valoarea = -1 daca algoritmjul a fost oprit
        # Valoarea = -2 daca lista nu a fost sortata corect
        # Valoarea = timpul de rulare al algoritmului daca este corect
        if sort(li,numere[0],numere[1]) == -1:
            rez.append((nume, -1,))

        # Se verifica daca lista a fost sortata corect
        elif test_sort(li) == True:
            rez.append((nume, dif))
        else:
            rez.append((nume, -2))

    # Se parcurge a doua lista de algoritmi de sortare
    for sort in sorts2:
        li = lista_test.copy()

        start = time.perf_counter()
        sort(li, 0, len(li)-1, numere[0],numere[1])
        end = time.perf_counter()

        dif = float("{:.7f}".format(end-start))
        nume = sort.__name__

        # In lista 'rez' se adauga perechi de forma (nume algoritm, valoare)
        # Unde valoarea = -1 daca algoritmjul a fost oprit
        # Valoarea = -2 daca lista nu a fost sortata corect
        # Valoarea = timpul de rulare al algoritmului daca este corect
        if sort(li, 0, len(li)-1, numere[0],numere[1]) == -1:
            rez.append((nume, -1,))

        # Se verifica daca lista a fost sortata corect
        elif test_sort(li) == True:
            rez.append((nume, dif))
        else:
            rez.append((nume, -2))

    # Obtin durata de rulare pentru algoritmul de sortare predefinit din Python
    # Functia .sort()
    li = lista_test.copy()
    if numere[0]>=10**8:
        rez.append(('Sortarea din python', -1))
    else:
        start = time.perf_counter()
        li.sort()
        end = time.perf_counter()

        dif  = float("{:.7f}".format(end-start))
        rez.append(('Sortarea din python', dif))

    # Ordonez lista 'rez' dupa valoare
    rez.sort(key=ordonare)
    i = 1

    # Algoritmii sunt afisati in ordinea urmatoare:
    # Algoritmii care au sortat gresit
    # Algoritmii care au fost opriti
    # Restul algoritmilor de la cel mai rapid la cel mai lent
    # la care se afiseaza si timpul de rulare
    for element in rez:
        if element[1]==-1:
            print(i,".", element[0], "Algoritmul a fost oprit")
        elif element[1]==-2:
            print(i,".", element[0], "Algoritmul nu a sortat corect")
        else:
            print(i, ".", *element, "secunde")
        i += 1
    print("\n")


f.close()
