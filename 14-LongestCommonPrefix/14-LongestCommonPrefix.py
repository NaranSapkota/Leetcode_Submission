# Last updated: 11/11/2025, 7:48:07 PM
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        data = ""
        
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return data
            data += strs[0][i]
            
        return data
