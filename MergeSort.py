
# Merge Sort (Ordenação por Intercalação)
# Vantagens:
# - Complexidade O(n log n) em todos os casos.
# - Estável.
# - Funciona bem para grandes volumes de dados.
# Desvantagens:
# - Usa memória extra proporcional ao tamanho da lista.

def merge_sort(arr):
    if len(arr) > 1:
        meio = len(arr) // 2
        L = arr[:meio]
        R = arr[meio:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

lista = [12, 11, 13, 5, 6, 7]
print(merge_sort(lista))
