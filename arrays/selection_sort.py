def smaller(arr):
    small = arr[0]
    small_index = 0
    for i in range(1, len(arr)):
        if arr[i] < small:
            small = arr[i]
            small_index = i
        
    return small_index

def selection_sort(arr):
    newArray = []
    for i in range(len(arr)):
        smalest = smaller(arr)
        newArray.append(arr.pop(smalest))
    return newArray


mylist = [9, 8 , 4, 3,2,2, 2, 3 ,4, 100, 19]
print(selection_sort(mylist))
