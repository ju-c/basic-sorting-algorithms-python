def bubble_sort(alist):

    for i in range(len(alist)-1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j+1]:
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp

    return alist


list_to_sort = [147, -16, 18, 91, 44, 1, 8, 54, 31, 18]
bubble_sort(list_to_sort)
print(list_to_sort)
