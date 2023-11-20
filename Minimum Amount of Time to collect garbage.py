class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:

        prefix=[0]*(len(travel)+1)

        prefix[0]=travel[0]

        for i in range(1,len(travel)):

            prefix[i]=prefix[i-1]+travel[i]

        print(prefix)

        garbage_count={"G":0,"M":0,"P":0}

        last_pos={"G":0,"M":0,"P":0}

        for i in range(len(garbage)):

            for val in garbage[i]:

                last_pos[val]=i

                garbage_count[val]+=1

        print(garbage_count,last_pos)

        res=0

        for i in garbage_count:

            if garbage_count[i]>0:

                res=res+(garbage_count[i]+prefix[last_pos[i]-1])

        return res


        
        