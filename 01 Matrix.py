class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def bfs(mat):
            visited,q1=set(),deque()
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if mat[i][j]==0:
                        q1.append((i,j))
                        visited.add((i,j))
            updated=[[1,0],[-1,0],[0,1],[0,-1]]
            while len(q1)>0:
                a,b=q1.popleft()
                for i in range(len(updated)):
                    x,y=updated[i][0],updated[i][1]
                    x_updated,y_updated=x+a,y+b
                    if x_updated>=0 and x_updated<=len(mat)-1 and y_updated>=0 and y_updated<=len(mat[0])-1:
                        if (x_updated , y_updated) not in visited:
                            visited.add((x_updated,y_updated))
                            mat[x_updated][y_updated]=mat[a][b]+1
                            q1.append((x_updated,y_updated))
            return mat
        return bfs(mat)