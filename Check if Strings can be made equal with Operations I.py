class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        
        if s1==s2:
            
            return True
        
        s1,s2=list(s1),list(s2)
        
        for i in range(0,2):
            
            if s1[i]==s2[i+2]:
                
                s1[i],s1[i+2]=s1[i+2],s1[i]
                
        print(s1,s2)
                
        if "".join(s1)=="".join(s2):
            
            return True
        
        else:
            
            return False
        