
# Quick Sort (Ordenação Rápida)
# Vantagens:
# - Muito eficiente na prática (O(n log n) em média).
# - Não usa memória extra significativa (ordenamento in-place).
# Desvantagens:
# - No pior caso, complexidade O(n²).
# - Não é estável.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivo = arr[len(arr) // 2]
        menores = [x for x in arr if x < pivo]
        iguais = [x for x in arr if x == pivo]
        maiores = [x for x in arr if x > pivo]
        return quick_sort(menores) + iguais + quick_sort(maiores)

lista = [10, 7, 8, 9, 1, 5]
print(quick_sort(lista))
