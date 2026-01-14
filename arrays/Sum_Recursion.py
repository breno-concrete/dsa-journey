def sumArr(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + sumArr(arr[1:])

list = [1,2,3,4,1,9]

print(sumArr(list))