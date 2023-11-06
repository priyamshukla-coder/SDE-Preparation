class SeatManager:

    def __init__(self, n: int):

        self.res=[]

        for i in range(1,n+1):

            self.res.append(i)
        

    def reserve(self) -> int:

        val=heapq.heappop(self.res)

        return val

    def unreserve(self, seatNumber: int) -> None:

        heapq.heappush(self.res,seatNumber)

        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)