
# Insertion Sort (Ordenação por Inserção)
# Vantagens:
# - Simples e eficiente para pequenos conjuntos.
# - Estável.
# Desvantagens:
# - Ineficiente para listas grandes.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and chave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave
    return arr

lista = [12, 11, 13, 5, 6]
print(insertion_sort(lista))
