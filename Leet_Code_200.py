# DP
# https://leetcode.com/problems/number-of-islands/description/
# Leet code 200
# 200. Number of Islands
# Medium
# Topics
# premium lock icon
# Companies
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

def get_island_dfs(grid,i,j):

    if ( i < 0 or i>=len(grid) or
        j < 0 or j>=len(grid[0])
        or (grid[i][j] == '0')):
        return
    grid[i][j] = '0'
    get_island_dfs(grid,i+1,j)
    get_island_dfs(grid,i-1,j)
    get_island_dfs(grid,i,j+1)
    get_island_dfs(grid,i,j-1)



def numIslands(grid):
    num_islands = 0
    row = len(grid)
    col = len(grid[0])
    if grid == None or len(grid) == 0 or len(grid[0]) == 0:
        return 0
    for i in range(0,row):
        for j in range(0,col):
            if grid[i][j] in ('1'):
                get_island_dfs(grid,i,j)
                num_islands+=1
    return num_islands
    

grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
print(numIslands(grid))
