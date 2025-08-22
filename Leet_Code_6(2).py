# DP (Solution_2)
# https://leetcode.com/problems/longest-palindromic-substring/description/
# 5. Longest Palindromic Substring
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s, return the longest palindromic substring in s.

 
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

def lon_sub_sring(s):
    val_long=""

    if len(s) <=1:
        return s
    for  i in range(len(s)):
        for j in range(i+1,len(s)):
            n_v = s[i:j]
            if n_v == n_v[::-1] and len(n_v)>len(val_long):
                val_long = n_v

    else:
        if val_long == '':
            return s[0]

    return val_long
