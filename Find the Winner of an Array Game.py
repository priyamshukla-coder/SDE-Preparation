class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        if k>=len(arr):

            return max(arr)

        q1=deque(arr[1:])

        val=arr[0]

        cnt=0

        while len(q1)>0:

            # val=arr[0]

            curr=q1.popleft()

            # print(q1)

            if val>curr:

                q1.append(curr)

                cnt=cnt+1

            else:

                q1.append(val)

                val=curr

                cnt=1

            if cnt==k:

                return val