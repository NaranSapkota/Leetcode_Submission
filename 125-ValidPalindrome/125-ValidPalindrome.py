# Last updated: 11/23/2025, 7:37:58 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString=""
        
        for  i in s:
            if i.isalnum():
                newString+=i.lower()
        
        return newString == newString[::-1]

        