# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):

            if not root:

                return 0

            root.val += dfs(root.left) + dfs(root.right)

            return root.val

        def bfs(root):

            tree_sum = dfs(root)

            print(tree_sum)

            mx_prod = 0

            q1 = deque([root])

            while len(q1) > 0:

                node = q1.popleft()

                if not root:

                    continue

                prod = (tree_sum - node.val) * node.val

                mx_prod = max(mx_prod , prod)

                if node.left is not None:

                    q1.append(node.left)

                if node.right is not None:

                    q1.append(node.right)

            return mx_prod % int(1e9+7)

        return bfs(root)
