class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        
        if s1==s2:
            
            return True
        
        e1,o1,e2,o2=Counter(),Counter(),Counter(),Counter()
        
        for i in range(len(s1)):
            
            if i%2:
                
                o1[s1[i]]+=1
                
                o2[s2[i]]+=1
                
            else:
                
                e1[s1[i]]+=1
                
                e2[s2[i]]+=1
                KXCPS4335B
        return e1==e2 and o1==o2
            
            kxcps4335b