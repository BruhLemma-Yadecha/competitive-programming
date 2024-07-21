# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        components = 0
        nodes = [[] for _ in range(n)]
        component = [-1] * n
        
        for a, b in edges:
            a -= 1
            b -= 1
            nodes[a].append(b)
            nodes[b].append(a)
            
        visited = [False] * n
        for i in range(n):
            if visited[i]:
                continue
            components += 1
            stack = [i]
            visited[i] = True
            while stack:
                node = stack.pop()
                component[node] = components
                for neighbour in nodes[node]:
                    if not visited[neighbour]:
                        stack.append(neighbour)
                        visited[neighbour] = True
                        
        component_sizes = [0] * (components + 1)
        for comp in component:
            component_sizes[comp] += 1

        res = 0
        for size in component_sizes:
            res += size * (n - size)
        res //= 2

        return res