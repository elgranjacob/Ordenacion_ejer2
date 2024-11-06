"""
def bubble_sort_letras(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print("Lista iterada", arr)
    return arr

# Lista de ejemplo
letras = ['d', 'a', 'c', 'b', 'e']
print("Lista original:", letras)

# Ordenar la lista usando el método Burbuja
letras_ordenadas = bubble_sort_letras(letras)
print("Lista ordenada:", letras_ordenadas)


def insertion_sort_letras(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print("Lista iterada", arr)
    return arr

# Lista de ejemplo
letras = ['d', 'a', 'c', 'b', 'e']
print("Lista original:", letras)

# Ordenar la lista usando el método de Inserción
letras_ordenadas = insertion_sort_letras(letras)
print("Lista ordenada:", letras_ordenadas)

"""
def selection_sort_letras(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print("Lista iterada", arr)
    return arr

# Lista de ejemplo
letras = ['d', 'a', 'c', 'b', 'e']
print("Lista original:", letras)

# Ordenar la lista usando el método de Selección Directa
letras_ordenadas = selection_sort_letras(letras)
print("Lista ordenada:", letras_ordenadas)


