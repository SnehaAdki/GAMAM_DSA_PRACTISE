# DP (Solution_1)
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

def lon_sub_sring(string):
    if len(string) <= 1:
        return string
    

    LBS = ""

    for i in range(1,len(string)):

        ## for odd string
        low = high = i
        while string[low] == string[high]:
            low -=1
            high +=1
        
            if low == -1 or high == len(string):
                break

        curr_pal = string[low+1:high]
        if len(curr_pal) > len(LBS):
            LBS = curr_pal


        ## even len

        low = i-1
        high = i

        while string[low] == string[high]:
            low-=1
            high+=1
            
            if low == -1 or high == len(string):
                break

        curr_pal = string[low+1:high]

        if len(curr_pal) > len(LBS):
            LBS = curr_pal

    return LBS


print(lon_sub_sring('abb'))
