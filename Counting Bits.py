class Solution:
    def countBits(self, n: int) -> List[int]:

        res=[]

        for i in range(0,n+1):

            cnt_bits=0

            while i!=0:

                cnt_bits=cnt_bits+1

                i=i&(i-1)
            
            res.append(cnt_bits)

        return res
        