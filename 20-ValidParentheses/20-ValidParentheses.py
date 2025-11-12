# Last updated: 11/11/2025, 7:48:06 PM
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        hash={ ")" : "(" , "}" : "{","]" : "["}

        for a in s:
            if a in hash:
                if stack and stack[-1] == hash[a]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(a)
        
        return True if not stack else False
        
            
