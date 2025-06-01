
# Heap Sort
# Vantagens:
# - Complexidade O(n log n) em todos os casos.
# - Não requer memória extra significativa (ordenamento in-place).
# Desvantagens:
# - Não é estável.
# - Na prática, é geralmente mais lento que Quick Sort.

def heapify(arr, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and arr[esquerda] > arr[maior]:
        maior = esquerda

    if direita < n and arr[direita] > arr[maior]:
        maior = direita

    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapify(arr, n, maior)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

lista = [12, 11, 13, 5, 6, 7]
print(heap_sort(lista))
