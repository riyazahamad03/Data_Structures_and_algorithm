class Solution:
    def middlenode(self,head):
        low=high=head
        while (high and high.next):
            low=low.next
            high=high.next.next
        return low
x=Solution()
x.middlenode([1,2,3,45])
print(x)