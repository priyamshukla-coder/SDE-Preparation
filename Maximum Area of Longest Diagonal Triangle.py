class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        
        d1,d2=0,0
        
        area=0
    
        for i in dimensions:
            
            a,b=i[0],i[1]
            
            d1=a*a+b*b
            
            if d1>d2 or d1==d2 and a*b>area:
                
                d2=d1
                
                area=a*b
                
        return area