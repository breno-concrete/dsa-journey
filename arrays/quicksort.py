def qsort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]

    less = [i for i in arr[1:] if i < pivot]

    greater = [i for i in arr[1:] if i > pivot]

    return qsort(less) + [pivot] + qsort(greater)

list = [9,12,32,45,656,75,2,2,3,4,5]

print(qsort(list))