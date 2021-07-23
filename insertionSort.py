def insertionSort(array):
    length = len(array)
    for i in range(length):
        if i != length - 1:
            if array[i] > array[i + 1]:
                var = array[i]
                array[i] = array[i + 1]
                array[i + 1] = var
        for j in reversed(range(i)):
            if j - 1 == -1:
                break
            if array[j] < array[j - 1]:
                var = array[j]
                array[j] = array[j - 1]
                array[j - 1] = var
            else:
                continue
    return array


array2 = [8, 5, 2, 9, 5, 6, 3]
insertionSort(array2)
print("done")
