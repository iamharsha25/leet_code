"""
Solution Approach

1.Class was declared for the better calling and utilization of the code...

2.Function was defined with the arguments and a return type--------->nums,target
nums---->Given integer array
target-->The actaul value passed to find the indices which sum up to become equivalent of it...

3.The first(outer) for loop:Tranverses in a range of length_of_array-1,starting from the value-0,which is considered as the first index of the array...

4.The second(inner) loop:Traverses in a range of length_of_aarray_1,starting from the value-i+i,which is used to traverse with the second element of the array at first and later on with the sequential elements...

5.The if condition in the inner loop adds up the two values of the array--->array[i]+array[j] and perfroms comparision operation to verify,
whether the obtanined result is equivalent or not with the target,IF the condition is TRUE,sets up result...

6.Return-->The statement used to return the actual result of the question...
"""
class Solution(object):
    def twoSum(self, nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    result = [i,j]
                    return result