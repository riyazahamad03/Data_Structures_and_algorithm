arr = [121,160,3,18,80,264,166]
def CountingSort(arr,place):
    Size = len(arr)
    count = [0]*10
    output = [0]*Size

    for i in range(Size):
        index = arr[i]//place
        count[index%10]+=1
    for i in range(1,10):
        count[i] = count[i-1]
    i=Size-1
    while i>=0:
        index=arr[i]//place
        output[count[index%10]-1]=arr[i]
        count[index%10]-=1
        i-=1
    for i in range(Size):
        arr[i]=output[i]
    print(arr)

def RadixSort(arr):
    max_element = max(arr)
    place = 1
    while max_element//place > 0:
        CountingSort(arr,place)
        place = place*10
RadixSort(arr)
print(arr)