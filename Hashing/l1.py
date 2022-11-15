# def LenghtOfLastWords(x):
#     x=x.strip().split()
#     return (len(x[-1]))
# x=LenghtOfLastWords("Hello World This Is Riyaz")
# print(x)
from calendar import c


# count=0
# sentence="nowwaylome"
# d={}
# s={}
# count=0
# abc="abcdefghijklmnopqrstuvwxyz"
# for i in range(len(abc)):
#     d[abc[i]] = i
# for i in range(len(sentence)):
#     s[sentence[i]] = i
# for i in s:
#     if i in d:
#         count+=1
# if(count == 26):
#     print(True)
# else:
#     print (False)

# s="anagram"
# t="nagaram"
# d1={}
# d2={}
# for i in range(len(s)):
#     d1[i] = s[i]
# for j in range(len(t)):
#     d2[j] = t[j]
# # print(d1.values(),d2.values())
# for i in range(len(s)):
#     if(d1 in d2):
#         print(True)
#     else:
#         print(False)

# s=["h","e","l","l","o"]
# l=[]
# l.append(s[::-1])
# print(*l)
# s="abcd"
# t="abcde"
# d={}
# for i in range(len(s)):
#     d[i] = s[i]
#     # print(d[i])
#     if d[i] not in t:
#         d[t[i]]=i

# print(t)

s="abcd"
t="abcde"
l1=[x for x in s]
l2=[y for y in t]
for i in l1:
    l2.remove(i)
print(*l2)