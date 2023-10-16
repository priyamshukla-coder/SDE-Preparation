class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def pascal(rows):

            l1=[]

            for i in range(rows):

                l1.append([])

                for j in range(0,i+1):

                    if j==0 or j==i:

                        l1[i].append(1)

                    else:

                        l1[i].append(l1[i-1][j-1]+l1[i-1][j])

            return l1

        res=pascal(34)

        return res[rowIndex]