from collections import deque
q = deque(['Riyaz','Riyaz 1'])
print(q.index('Riyaz'))
print(q.popleft())
print(q.count('Riyaz'))
print(q.append('Riyaz 2'))
print(q)


