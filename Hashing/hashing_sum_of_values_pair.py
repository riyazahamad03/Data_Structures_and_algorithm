def findSumOfPairs(nums,target):
    d={}
    for i,e in enumerate(nums):
        # print (i+1,e)
        if(target - e) in d:
            return(nums[d.get(target-e)] , nums[i])
        d[e] = i
    return("pair not found")

res=findSumOfPairs([1,2,3,4,5] , 9)
print(res)

# d={
#     # "riyaz" : 10,
#     "riyaz1" : 20,
#     "riyaz3" : 30,
#     1:1,
#     2:2
# }
# nums=[1,2,3,4,50,30]
# # print(d.pop("riyaz"))
# print(nums[2])