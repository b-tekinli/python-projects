import random
anaDizi = []
A = []
diziElemanSayisi = int (random.uniform(1, 50))
for i in range(0, diziElemanSayisi, 1):
    anaDizi.append(int(random.uniform(1, 250)))

A = anaDizi.copy()

def AnaDizi2():
    print("\n Ana Dizi = ", end = "")
    for i in range(len(anaDizi)):
        if i+1 ==len(anaDizi):
            print(anaDizi[i], end = "\n")
        else:
            print(anaDizi[i], end = ",")

def SelectionSort(A):
    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            if A[j] < A[i]:
                tmp = A[i]
                A[i] = A[j]
                A[j] = tmp

def BubbleSort(A):
    for i in range(len(A)):
        for j in range(len(A)-1):
            if A[j+1] < A[j]:
                 tmp = A[j]
                 A[j] = A[j+1]
                 A[j+1] = tmp

def CombSort(A):
    def getNextGap(gap):
        # Küçültme yapılıyor. Küçülte faktörü kullanılarak
        gap = (gap * 10) / 13
        if gap < 1:
            return 1
        return gap

    n = int(len(A))
    gap = n
    degistiMi = True
    while gap != 1 or degistiMi == True:
        gap = int(getNextGap(gap))
        degistiMi = False
        for i in range(0, n-gap):
            if A[i] > A[i + gap]:
                A[i], A[i + gap]=A[i + gap], A[i]
                #tmp = A[i]
                #A[i] = A[i + gap]
                #A[i + gap] = tmp
                degistiMi = True

def InsertionSort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i-1
        while j >=0 and key < A[j] :
            A[j+1] = A[j]
            j -= 1
            A[j+1] = key

def ShellSort(A):
    n = int(len(A))
    gap = int(round((n+1)//2))
    while gap > 0:
        for i in range(gap,n):
            temp = A[i]
            j = i
            while  j >= gap and A[j-gap] >temp:
                A[j] = A[j-gap]
                j -= gap
            A[j] = temp
        gap //= 2

def MergeSort(A):
    if len(A)>1:
        orta = len(A)//2
        sag = A[orta:]
        sol = A[:orta]
        MergeSort(sag)
        MergeSort(sol)
        i=0
        j=0
        k=0
        while i<len(sol) and j<len(sag):
            if sol[i]<sag[j]:
                A[k]=sol[i]
                i = i +1
            else:
                A[k] = sag[j]
                j = j + 1
            k = k + 1
        while i<len(sol):
            A[k]=sol[i]
            i = i+1
            k = k+1
        while j<len(sag):
            A[k]=sag[j]
            j = j+1
            k = k+1

def QuickSort(A,sol=0,sag=(len(A)-1)):

    def partition(A,sol,sag):
        i = ( sol-1 )
        pivot = A[sag]
        for j in range(sol , sag):
            if A[j] <= pivot:
                i = i+1
                A[i],A[j] = A[j],A[i]
        A[i+1],A[sag] = A[sag],A[i+1]
        return ( i+1 )

    if sol < sag:
        pF = partition(A,sol,sag)
        QuickSort(A, sol, pF-1)
        QuickSort(A, pF+1, sag)

def HeapSort(A):
    def heapify(A, n, i):
        enBuyuk = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and A[i] < A[l]:
            enBuyuk = l
        if r < n and A[enBuyuk] < A[r]:
            enBuyuk = r
        if enBuyuk != i:
            A[i],A[enBuyuk] = A[enBuyuk],A[i]
            heapify(A, n, enBuyuk)

    n = len(A)
    for i in range(n, -1, -1):
        heapify(A, n, i)
    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0)

def PigeonholeSort(A):
    my_min = min(A)
    my_max = max(A)
    size = my_max - my_min + 1
    holes = [0] * size
    for t in A:
        assert type(t) is int, "integers only please"
        holes[t - my_min] += 1
    i = 0
    for t in range(size):
        while holes[t] > 0:
            holes[t] -= 1
            A[i] = count + my_min
            i += 1

def Chooser():
    print("Dizinizi hangi sıralama türüyle sıralamak istersiniz.\n1. Selection Sort (Seçme Sıralama)\n2. Bubble Sort (Kabarcık Sıralama)\n3. Comb Sort (Tarak Sıralama)\n4. Insertion Sort (Araya Eklemeli Sıralama)\n5. Shell Sort (Kabuk Sıralama)\n6. Merge Sort (Birleştirme Sıralama)\n7. Quick Sort (Hızlı Sıralama)\n8. Heap Sort (Yığın Sıralama)\n9. Pigeonhole Sort (Güvercin Yuvası Sıralama)")
    cevap = int(input())
    if cevap == 1:
        AnaDizi2()
        SelectionSort(A)
    elif cevap == 2:
        AnaDizi2()
        BubbleSort(A)
    elif cevap == 3:
        AnaDizi2()
        CombSort(A)
    elif cevap == 4:
        AnaDizi2()
        InsertionSort(A)
    elif cevap == 5:
        AnaDizi2()
        ShellSort(A)
    elif cevap == 6:
        AnaDizi2()
        MergeSort(A)
    elif cevap == 7:
        AnaDizi2()
        QuickSort(A)
    elif cevap == 8:
        AnaDizi2()
        HeapSort(A)
    elif cevap == 9:
        AnaDizi2()
        PigeonholeSort(A)
    else:
        print("Seçiminizi yeniden yapınız. Yaptığınız seçimi gerçekleştiremiyorum\n")
        Chooser()


Chooser()

print("\n Sıralanmış dizi = ",end = "")
for i in range(len(A)):
    if i+1 ==len(A):
        print(A[i],end = "")
    else:
        print(A[i],end = ",")
