class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:

        time=[]

        for i in range(len(dist)):

            time.append(dist[i]/speed[i])

        time.sort()

        # print(time)

        idx=0

        cnt=0

        while idx+1<=len(time):

            if time[idx]<=idx:

                break

            idx=idx+1

            # print(cnt)

            cnt=cnt+1

        return cnt
        