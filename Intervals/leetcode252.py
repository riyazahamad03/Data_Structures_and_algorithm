'''
252. Meeting Rooms
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Input: [[0,30],[5,10],[15,20]]
Output: false

Input: [[7,10],[2,4]]
Output: true

'''

class solution:
    def canAttendMeeting(self,arr : list[list[int]]):
        arr.sort(key = lambda x : x[0])
        print(arr)
        
        for intervals in range(1,len(arr)):
            inter1 = arr[intervals-1]
            inter2 = arr[intervals]

            if inter1[1] > inter2[0]:
                return False
        return True

x = solution()
print(x.canAttendMeeting([[0,30],[5,10],[15,20]]))
print(x.canAttendMeeting([[7,10],[2,4]]))