class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        c=s.count('1')
        
        res=""
        
        # res[-1]='1'
        
        l=len(s)
        
        res='1'*(c-1)+'0'*(l-c)+'1'
        
        return res
            
            