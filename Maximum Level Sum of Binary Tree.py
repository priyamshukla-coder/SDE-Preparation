# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        mx = float('-inf')

        l = 0

        level = 0

        q1 = deque()

        q1.append(root)

        while len(q1) > 0:

            l += 1

            curr_sum = 0

            for i in range(len(q1)):

                node = q1.popleft()

                curr_sum += node.val

                if node.left != None:

                    q1.append(node.left)

                if node.right != None:

                    q1.append(node.right)

            # mx  = max(mx , curr_sum)

            if mx < curr_sum:

                mx = curr_sum

                level = l

        return level
