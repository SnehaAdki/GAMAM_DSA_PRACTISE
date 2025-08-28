# Leet Code 22 
# DP
# https://leetcode.com/problems/generate-parentheses/submissions/1751644317/
# 22. Generate Parentheses
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]


def solve(open,close,s,res):
    if open == 0 and close == 0:
        res.append(s)
        return
    if open > 0 :
        solve(open-1,close,s+"(",res)
    if close>open and close > 0:
        solve(open,close-1,s+")",res)

res = []
solve(3,3,"",res)
print(res)



# class Solution:
#     def generateParenthesis(self, n: int):
#         def dfs(left, right, s):
#             if len(s) == n * 2:
#                 res.append(s)
#                 return
#             if left < n:
#                 dfs(left + 1, right, s + '(')
#             if right < left:
#                 dfs(left, right + 1, s + ')')
#         res = []
#         dfs(0, 0, '')
#         return res
    
# s1 = Solution()
# s1.generateParenthesis(3)
