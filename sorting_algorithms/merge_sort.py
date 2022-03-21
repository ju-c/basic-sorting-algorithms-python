def merge_sort(alist):
    if len(alist) > 1:
        left = alist[:len(alist) // 2]
        right = alist[len(alist) // 2:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            alist[k] = right[j]
            j += 1
            k += 1


list_to_sort = [147, -16, 18, 91, 44, 1, 8, 54, 31, 18]
merge_sort(list_to_sort)
print(list_to_sort)
