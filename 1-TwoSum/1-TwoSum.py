# Last updated: 11/13/2025, 8:11:52 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = [(n, i) for i, n in enumerate(nums)]
        arr.sort() 
        
        l, r = 0, len(arr) - 1
        
        while l < r:
            current = arr[l][0] + arr[r][0]
            
            if current == target:
                return [arr[l][1], arr[r][1]]
            elif current < target:
                l += 1
            else:
                r -= 1
        
        return []
