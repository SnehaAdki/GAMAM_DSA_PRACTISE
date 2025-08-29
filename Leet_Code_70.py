# DP 
# Leet Code 70 
# https://leetcode.com/problems/climbing-stairs/submissions/1752536692/
# 70. Climbing Stairs
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step -->


def climbing(n):
    clims=[]
    for i in range(0,n):
        if i ==0:
            clims.append(1)
        elif i ==1:
            clims.append(2)
        else:
            clims.append(clims[i-1]+clims[i-2])
    return clims[-1]

print(climbing(4))
