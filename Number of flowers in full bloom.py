class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:

        st,end=[],[]

        for i in flowers:

            st.append(i[0])

            end.append(i[1]+1)

        st.sort()

        end.sort()

        res=[]

        for i in people:

            l,r=bisect_right(st,i),bisect_right(end,i)

            res.append(l-r)

        return res        