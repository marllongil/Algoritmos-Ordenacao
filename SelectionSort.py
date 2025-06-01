
# Selection Sort (Ordenação por Seleção)
# Vantagens:
# - Simples de entender e implementar.
# - Pouca movimentação de dados, útil quando o custo de troca é alto.
# Desvantagens:
# - Ineficiente para grandes conjuntos de dados (O(n²)).
# - Não é estável.

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

lista = [64, 25, 12, 22, 11]
print(selection_sort(lista))
