tab = [7,2,4,5,0,9,15,24,-2,1]


def quick_sort(t, left, right):
    if right <= left:
        return
    i = left
    j = right
    pivot = t[(left+right)//2]
    while True:
        while t[i] < pivot:
            i += 1
        while t[j] > pivot:
            j -= 1
        if i <= j:
            p = t[i]
            t[i] = t[j]
            t[j] = p
            i += 1
            j -= 1
        if i > j:
            break
    if left < j:
        quick_sort(t, left, j)
    if right > i:
        quick_sort(t, i, right)
quick_sort(tab, 0, len(tab)-1)
print(tab)
