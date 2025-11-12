# Last updated: 11/11/2025, 7:47:56 PM
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        result_s=[]
        result_t=[]

        for i in s:
            if i!='#':
                result_s.append(i)
            elif len(result_s)>0:  
                result_s.pop()

        for i in t:
            if i!= '#':
                result_t.append(i) 
            elif len(result_t)>0:
                result_t.pop()
            
        if result_s == result_t:
            return True
        
                
        