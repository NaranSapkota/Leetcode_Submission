# Last updated: 11/11/2025, 7:47:55 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hashset=set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
            
        
    
            
   
        