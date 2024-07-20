# Problem: Number of Good Leaf Nodes Pairs - https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        res = 0

        def dfs(node, depth):
            nonlocal res
            if not node:
                return []
            if not node.left and not node.right:
                return [depth]
            left_leaves = dfs(node.left, depth + 1)
            right_leaves = dfs(node.right, depth + 1)
            for l in left_leaves:
                for r in right_leaves:
                    if l + r - 2 * depth <= distance:
                        res += 1
            return left_leaves + right_leaves

        dfs(root, 0)
        return res