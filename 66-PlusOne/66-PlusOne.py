# Last updated: 11/11/2025, 7:48:02 PM
class Solution(object):
    def plusOne(self, digits):
        digits=digits[::-1]
        carryOne,i=1,0
        while carryOne:
            if(i<len(digits)):

                if(digits[i]==9):
                    digits[i]=0
                else: 
                    digits[i]+=1
                    carryOne=0

            else:
                digits.append(1)
                carryOne=0
            i+=1
        return digits[::-1]
            


        