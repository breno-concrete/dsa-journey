#criar o array de prefix sum com as somas

def prefix_sum(arr):
    _sum = []
    total = 0

    for i in arr:
        total += i
        _sum.append(total)

    return _sum

# fatiar o array
def sumRange(right, left):
    if left > 0 or right > 0:
        return _sum[right] - _sum[left-1]
    else:
        return _sum[right or left]
