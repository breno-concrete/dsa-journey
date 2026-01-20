# quick sort
# escolher um pivô, e criar dois subarrays com numeros menores e maiores que eles, usando recursão pra ordenar eles

def qsort(list):
    if len(list) < 2: #caso base
        return list
    else:
        
        p_index = (len(list))// 2
        pivot = list[p_index]

        left = list[:p_index] + list[p_index+1:]
        lower = [i for i in left if i <= pivot]
        higher = [i for i in left if i > pivot]
        return qsort(lower) + [pivot] + qsort(higher)


bay = [1,4,56,768,89,4,2,13,5,7,8]

print(qsort(bay))

