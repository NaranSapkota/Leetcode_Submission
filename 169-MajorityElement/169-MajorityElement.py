# Last updated: 11/11/2025, 7:47:56 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res,count=0,0
        for n in nums:
            if count==0:
                res=n
            if n ==res:
                count+=1
            else:
                count-=1
        return res

        