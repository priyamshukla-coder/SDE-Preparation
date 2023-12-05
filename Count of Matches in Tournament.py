class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        # return n-1

        mat = 0

        while n!=1:

            if n%2:

                mat=mat+((n-1)//2)

                n=((n-1)//2)+1

            else:

                mat=mat+n//2

                n=n//2

        return mat