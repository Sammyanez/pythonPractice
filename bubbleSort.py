def bubbleSort(array):
    swap = True
    length = len(array) - 1
    while swap:
        swap = False
        for i in range(length):
            if array[i] > array[i + 1]:
                var = array[i]
                array[i] = array[i + 1]
                array[i + 1] = var
                i += 1
                swap = True
            else:
                i += 1
    return array


array2 = [8, 5, 2, 9, 5, 6, 3]
bubbleSort(array2)
print("done")
