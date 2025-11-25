# Last updated: 11/24/2025, 7:59:20 PM
class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.strip()
        if not s:
            return 0
        
        sign = 1
        i = 0
        result = 0
        
        # handle sign
        if s[0] == '-' or s[0] == '+':
            if s[0] == '-':
                sign = -1
            i += 1    # move index after sign
        
        # convert number
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        
        result *= sign
        
        # clamp to 32-bit integer
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        
        return result
