from collections import deque
from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        # Process the first tree
        n = len(edges1) + 1
        tree1 = [[] for _ in range(n)]
        for u, v in edges1:
            tree1[u].append(v)
            tree1[v].append(u)
        
        color1 = [0] * n
        q = deque([0])
        color1[0] = 0
        visited = [False] * n
        visited[0] = True
        while q:
            u = q.popleft()
            for v in tree1[u]:
                if not visited[v]:
                    color1[v] = color1[u] ^ 1
                    visited[v] = True
                    q.append(v)
        count_color0_tree1 = color1.count(0)
        count_color1_tree1 = n - count_color0_tree1
        
        # Process the second tree
        m = len(edges2) + 1
        tree2 = [[] for _ in range(m)]
        for u, v in edges2:
            tree2[u].append(v)
            tree2[v].append(u)
        
        color2 = [0] * m
        q = deque([0])
        color2[0] = 0
        visited = [False] * m
        visited[0] = True
        while q:
            u = q.popleft()
            for v in tree2[u]:
                if not visited[v]:
                    color2[v] = color2[u] ^ 1
                    visited[v] = True
                    q.append(v)
        count_color0_tree2 = color2.count(0)
        count_color1_tree2 = m - count_color0_tree2
        max_tree2 = max(count_color0_tree2, count_color1_tree2)
        
        # Compute answer for each node in tree1
        answer = []
        for i in range(n):
            if color1[i] == 0:
                same_color_tree1 = count_color0_tree1
            else:
                same_color_tree1 = count_color1_tree1
            total = same_color_tree1 + max_tree2
            answer.append(total)
        
        return answer
