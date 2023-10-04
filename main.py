from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    ret = [] 
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i]+nums[j]==target):
                ret=[i,j]
                break
    return ret