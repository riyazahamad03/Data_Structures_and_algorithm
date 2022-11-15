# Time complexity O(n^2)
# Space complexity O(1)
print('Welcome To Bubble Sort Haha')
num = [99,44,36,76,12,34,41,5,5]
def BubbleSort(num):
    length = len(num)
    for i in range(length):
        for j in range(length-1):
            if num[j]  > num[j+1]:
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp
    return num
x = BubbleSort(num)
print('Ascending Order Sorting  : ', x)

def BubbleSortDesc(num):
    length = len(num)
    for i in range(length):
        for j in range(length-1):
            if num[j]  < num[j+1]:
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp
    return num

y = BubbleSortDesc(num)
print('Descending Order Sorting : ',y)