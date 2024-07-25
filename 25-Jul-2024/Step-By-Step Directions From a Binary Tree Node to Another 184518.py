# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # Convert to regular graph
        nodes = defaultdict(list)
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                nodes[node].append((node.left, 'L'))
                nodes[node.left].append((node, 'U'))
                stack.append(node.left)
            if node.right:
                nodes[node].append((node.right, 'R'))
                nodes[node.right].append((node, 'U'))
                stack.append(node.right)
                
        # Find start and dest nodes
        start, dest = None, None
        for node in nodes.keys():
            if node.val == startValue:
                start = node
            if node.val == destValue:
                dest = node
            if start and dest:
                break
            
        # BFS to find path from start to dest
        def bfs(start, dest):
            queue = [(start, '')]
            visited = set()
            while queue:
                curr, path = queue.pop(0)
                if curr == dest:
                    return path
                visited.add(curr)
                for neighbor, direction in nodes[curr]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + direction))
            return ''
        
        return bfs(start, dest)