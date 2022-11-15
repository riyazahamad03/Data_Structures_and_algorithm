# Time complexity O(n^2)
# Space complexity O(1)

print("Welcome to Selection Sort Haha")
num = [99,44,36,76,12,34,41,5,5]
def SelectionSort(num):
    length = len(num)
    for i in range(length-1):
        small = i
        for j in range(i+1,length):
            if num[j] < num[small]:
                small = j
        temp = num[i]
        num[i] = num[small]
        num[small] = temp 
        print(num)
    return num

x = SelectionSort(num)
print('Ascending Order Sorting  : ', x)

def SelectionSortLarge(num):
    length = len(num)
    for i in range(length-1):
        large = i
        for j in range(i+1,length):
            if num[j] > num[large]:
                large = j
        temp = num[i]
        num[i] = num[large]
        num[large] = temp 
    return num
y = SelectionSortLarge(num)
print('Descending Order Sorting : ',y)