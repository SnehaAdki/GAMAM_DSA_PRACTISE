# https://leetcode.com/problems/find-center-of-star-graph/?envType=problem-list-v2&envId=graph 
# https://leetcode.com/problems/find-center-of-star-graph/submissions/1827077482/?envType=problem-list-v2&envId=graph
# solution 1 
# Leet code 1791
# 1791. Find Center of Star Graph
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.


# Example 1:
# Input: edges = [[1,2],[2,3],[4,2]]
# Output: 2
# Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.

# Example 2:
# Input: edges = [[1,2],[5,1],[1,3],[1,4]]
# Output: 1

def findCenter(nodes):
    hash_map = {}
    # center_node = -1
    
    for i in range(0,len(nodes)):
        if nodes[i][0] in hash_map.keys():
            hash_map[nodes[i][0]]+=1
        else:
            hash_map[nodes[i][0]] = 1

        if nodes[i][1] in hash_map.keys():
            hash_map[nodes[i][1]]+=1
        else:
            hash_map[nodes[i][1]] = 1

        
    for k,v in hash_map.items():
        if v == len(nodes):
            return k
    
    return -1
    # print(hash_map)
    # print(center_node)

# edges = [[1,2],[2,3],[4,2]]
# print(findCenter(edges))



def sol2():
    nodes = [[1,2],[2,3],[4,2]]
    node1 = nodes[0] #[1,2]
    node2 = nodes[1] #[2,3]
    if node1[0] == node2[0] or node1[0] == node2[1]:
        return node1[0]
    if node1[1] == node2[1] or node1[1] == node2[0]:
        return node1[1]

print(sol2())
