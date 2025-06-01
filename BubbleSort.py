
# Bubble Sort
# Vantagens:
# - Simples de entender e implementar.
# - Detecta rapidamente se a lista já está ordenada.
# Desvantagens:
# - Muito ineficiente para grandes listas (O(n²)).
# - Grande número de comparações e trocas.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocou = True
        if not trocou:
            break
    return arr

lista = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(lista))
