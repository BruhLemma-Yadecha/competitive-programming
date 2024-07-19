# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        level = [root]
        
        while level:
            res.append([node.val for node in level if node])
            level = [child for node in level if node for child in (node.left, node.right)]
            
        for i in range(len(res)):
            if i % 2 == 1:
                res[i] = res[i][::-1]
                
        res.pop()
        return res