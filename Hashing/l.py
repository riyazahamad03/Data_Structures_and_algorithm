# # s=input().strip()
# # x=int(input())
# # k=0
# # l=[]
# # i=0
# # while(i<len(s)):
# #     l.append(s[i])
# #     k=k+1
# #     i+=1
# #     if(k%x==0):
# #         i=i+x
   
# # print(l)

# def fizzBuzz(n):
#     l=[]
#     for i in range(n):
#         if(i%3==0 and i%5==0):
#             l.append("FizzBuzz")
#         elif(i%3==0):
#             l.append("Fizz")
#         elif(i%5==0):
#             l.append("Buzz")
#         else:
#             l.append(i)
#     return l
# x=fizzBuzz(3)
# print(x)

# N=list(map(int,input().split()))
N=[35,81,78,84,53]
res=[]
s=set()
for i in N:
    if i>9:
        res.append(i%10)
        res.append(i//10)
    else:
        res.append(i)
print(res)
for digit in res:
    if digit in s:
        s.remove(digit)
    else:
        s.add(digit)
print(s)