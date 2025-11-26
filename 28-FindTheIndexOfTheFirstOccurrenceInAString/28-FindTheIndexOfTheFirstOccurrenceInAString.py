# Last updated: 11/25/2025, 8:02:55 PM
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle=="":
            return 0
        for i in range(len(haystack)+1 -len(needle)):
            if haystack[i: i+len(needle)] == needle :
                return i
        return -1

        
        