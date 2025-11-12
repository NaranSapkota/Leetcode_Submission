# Last updated: 11/11/2025, 7:48:04 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arrays=s.split()
        return len(arrays[-1])

        