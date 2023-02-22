# Time Complexity  O(nlogn)
# space complexity O(n)
def mergeSort(lst):
    if len(lst) > 1:
        mid = len(lst)//2
        left = lst[:mid]
        right = lst[mid:]
        mergeSort(left)
        mergeSort(right)
        i,j,k =0,0,0
        while(i < len(left) and j< len(right)):
            if left[i] < right[j]:
                lst[k] = left[i]
                i+=1
            else:
                lst[k]=right[j]
                j+=1
            k+=1
        while(i<len(left)):
            lst[k] = left[i]
            i+=1
            k+=1
        while(j<len(right)):
            lst[k] = right[j]
            j+=1
            k+=1
        print(lst)
        # print("left", left)
        # print("right",right)
    return lst
lst = [99,44,36,76,12,34,41,5,5]
x = mergeSort(lst)
print(x)