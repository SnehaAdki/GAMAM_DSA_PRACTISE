# https://leetcode.com/problems/course-schedule/submissions/1826129845/

# Leet Code 207
# 207. Course Schedule

# BFS using stack  & hashmap

# Medium
# Topics
# premium lock icon
# Companies
# Hint
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

 

# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.


# Example 2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.


def canFinish(arr_val):
    
    hash_map_pre = {}
    for i in range(0,len(arr_val)):
        if hash_map_pre.get(arr_val[i][-1]):
            hash_map_pre[arr_val[i][-1]]+=1
        else:
            hash_map_pre[arr_val[i][-1]]=1
        
    
    
    queue = []
    for i in range(0,len(arr_val)):
        if arr_val[i][0] not in (hash_map_pre.keys()):
            if arr_val[i][0] not in queue:
                queue.append(arr_val[i][0])
        if arr_val[i][-1] not in (hash_map_pre.keys() ):
            if arr_val[i][-1] not in queue:
                queue.append(arr_val[i][-1])
            
    print(queue)
    print(hash_map_pre)
    
    
    # for i in range(0,len(queue)):
    i = 0
    while i < len(queue):
        for j in range(0,len(arr_val)):
            if queue[i] == arr_val[j][0]:
                hash_map_pre[arr_val[j][1]] -= 1
            if arr_val[j][1] in hash_map_pre.keys() and hash_map_pre[arr_val[j][1]] == 0:
                queue.append(arr_val[j][1])
                del hash_map_pre[arr_val[j][1]]
        i+=1
            
    # print(queue)
    # print(hash_map_pre)
    
    
    
    val= True if len(hash_map_pre)==0 else False
    print(val)
    
# arr_val = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
arr_val =[[1,4],[2,4],[3,1],[3,2]]
canFinish(arr_val)

