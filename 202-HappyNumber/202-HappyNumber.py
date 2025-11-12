# Last updated: 11/11/2025, 7:47:54 PM
class Solution:
    def isHappy(self, n):
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit)**2 for digit in str(n))
        return n == 1



