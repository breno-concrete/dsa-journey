def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high)//2
        guess = arr[mid]
        
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None

mylist = [2, 2, 2, 3, 3, 4, 4, 8, 9, 19, 100]
print(binary_search(mylist, 100))
