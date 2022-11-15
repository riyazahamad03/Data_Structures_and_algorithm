# Time complexity O(n^2)
# space complexity O(1)
print("Welcome to insertion Sort haha ")
num = [99,44,36,76,12,34,41,5,5]
def insertionSort(num):
    for i in range(1,len(num)):
        val = num[i]
        j = i-1
        while ((j>=0) and (val < num[j])):
            num[j+1] = num[j]
            j-=1
        num[j+1] = val
    return num
x = insertionSort(num)
print('Ascending Order Sorting  : ', x)

def insertionSortDesc(num):
    for i in range(1,len(num)):
        val = num[i]
        j = i-1
        while ((j>=0) and (val > num[j])):
            num[j+1] = num[j]
            j-=1
        num[j+1] = val
    return num
y = insertionSortDesc(num)
print('Descending Order Sorting : ',y)