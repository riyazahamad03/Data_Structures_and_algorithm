'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Input: [[7,10],[2,4]]
Output: 1
'''

class solution:
    def meetingRooms2(self,arr:list[list[int]]):
        start = sorted([x[0] for x in arr])
        end = sorted([x[1] for x in arr])
        s,e = 0,0
        r,c = 0,0
        while s < len(start):
            if start[s] < end[e]:
                c+=1
                s+=1
            else:
                c-=1
                e+=1

            r = max(r,c)
        return r


x = solution()
print(x.meetingRooms2([[7,10],[2,4]]))