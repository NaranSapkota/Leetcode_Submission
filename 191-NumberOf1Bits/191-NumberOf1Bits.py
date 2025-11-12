# Last updated: 11/11/2025, 7:47:53 PM
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        count=0
        n='{0:b}'.format(n)
        for i in str(n):
            if i =='1':
                count=count+ 1
                
        return count
        