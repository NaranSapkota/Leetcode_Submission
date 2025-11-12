# Last updated: 11/11/2025, 7:47:58 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        res=0
        for n in nums:
            res=n^ res
        return res
            
        