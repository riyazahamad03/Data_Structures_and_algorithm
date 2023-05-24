import heapq
class solution:
    def maxScore(self , nums1 : list[int] , nums2 : list[int] , k : int):
        elems = [(n1 , n2) for n1 , n2 in zip(nums1 , nums2)]
        elems = sorted(elems , key=lambda x : x[1] , reverse=True)

        Sum = 0
        res = 0
        heap = []

        for n1 , n2 in elems:
            Sum += n1
            heapq.heappush(heap , n1)

            if len(heap) > k:
                Sum -= heapq.heappop(heap)
            if len(heap) == k:
                res = max(res , Sum * n2)
        return res
x = solution()
print(x.maxScore([4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1))