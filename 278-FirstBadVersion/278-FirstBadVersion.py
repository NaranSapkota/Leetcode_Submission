# Last updated: 1/6/2026, 12:24:19 PM
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        l=1
        r=n
        
        while l<r:
            m=(l+r)//2
            if isBadVersion(m):
                r=m
            else:
                l=m+1

        return l