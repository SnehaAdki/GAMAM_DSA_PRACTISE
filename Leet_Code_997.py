# https://leetcode.com/problems/find-the-town-judge/submissions/1827043960/?envType=problem-list-v2&envId=graph

# Leet Code 997
# 997. Find the Town Judge
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

# Example 1:
# Input: n = 2, trust = [[1,2]]
# Output: 2

# Example 2:
# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3

# Example 3:
# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1



def town_judge(trust,n):
    incoming = {}
    outgoing = {}
    ans = -1
    
    for i in range(0,n):
        incoming[i+1] = 0
        outgoing[i+1] = 0


    
    for i in range(0,len(trust)):
        incoming[trust[i][1]]+=1
        outgoing[trust[i][0]]+=1
    
    # print("incoming",incoming)    
    # print("outgoing",outgoing)
    
    for i in range(0,n):
        if incoming[i+1] == n-1 and outgoing[i+1] ==0:
            ans = i+1
    
    print(ans)


trust = [[1,2],[2,3]]
town_judge(trust,3)
