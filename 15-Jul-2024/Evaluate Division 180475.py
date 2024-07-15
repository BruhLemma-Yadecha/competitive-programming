# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
        self.weights = []

class Solution:
    def calcEquation(self, equations, values, queries):
        nodes = {}
        # Create a weighted graph
        for (a, b), value in zip(equations, values):
            if a not in nodes:
                nodes[a] = Node(a)
            if b not in nodes:
                nodes[b] = Node(b)
            nodes[a].children.append(nodes[b])
            nodes[a].weights.append(value)
            nodes[b].children.append(nodes[a])
            nodes[b].weights.append(1 / value)

        memo = {}
        
        def evaluate(a, b, visited):
            if (a, b) in memo:
                return memo[(a, b)]
            if a not in nodes or b not in nodes:
                return -1.0
            if a == b:
                return 1.0
            visited.add(a)
            for i, child in enumerate(nodes[a].children):
                if child.val in visited:
                    continue
                visited.add(child.val)
                weight = nodes[a].weights[i]
                res = evaluate(child.val, b, visited)
                visited.remove(child.val)
                if res != -1.0:
                    memo[(a, b)] = weight * res
                    return memo[(a, b)]
            return -1.0
        
        return [evaluate(a, b, set()) for a, b in queries]