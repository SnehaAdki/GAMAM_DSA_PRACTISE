# https://leetcode.com/problems/find-if-path-exists-in-graph/?envType=problem-list-v2&envId=graph
# Leet Code 1971
# 1971. Find if Path Exists in Graph
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

# You want to determine if there is a valid path that exists from vertex source to vertex destination.

# Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

 

# Example 1:
# Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
# Output: true
# Explanation: There are two paths from vertex 0 to vertex 2:
# - 0 → 1 → 2
# - 0 → 2


# Example 2:
# Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
# Output: false
# Explanation: There is no path from vertex 0 to vertex 5.
 



def find_route(s,d,n,edges):
    hash_map = {}
    if s == d:
        return True
    
    for i in range(0,len(edges)):
        if edges[i][0] in hash_map.keys():
            hash_map[edges[i][0]].append(edges[i][1])
        else:
            hash_map[edges[i][0]] = [edges[i][1]]
        if edges[i][1] in hash_map.keys():
            hash_map[edges[i][1]].append(edges[i][0])
        else:
            hash_map[edges[i][1]] = [edges[i][0]]

    queue = [s]
    i =0 
    visited = [False] * n
    visited[s] = True
    while len(queue) != 0:
        cur = queue.pop()
        if cur == d:
            return True
        for i in hash_map[cur]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)
    
    return False
    
    # while i < len(s) and i<=n:
    #     if s[i] in hash_map.keys():
    #         visited[s[i]] = True
    #         if d in hash_map[s[i]]:
    #             return True
    #         #s.append(list(hash_map.keys())[list(hash_map.keys()).index(hash_map[s[i]])])
    #         if visited[s[i]] == False:
    #             s.extend(hash_map[s[i]])
    #     i+=1
    
    # return False    
    
print(find_route(0,2,3,[[0,1],[1,2],[2,0]]))
# print(find_route(0,5,6,[[0,1],[0,2],[3,5],[5,4],[4,3]]))
# print(find_route(0,0,1,[]))
# print(find_route(7,5,10,[[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]]))

# print(find_route(0,5,6,[[0,1],[2,3],[4,5],[3,4],[1,2]]))
