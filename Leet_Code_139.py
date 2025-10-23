#https://leetcode.com/problems/word-break/submissions/1809551551/
# Leet Code 139 
# 139. Word Break
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.


# Example 1:
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Example 2:
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.

# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false



class Solution:
    def wordBreak(self, str_val: str, dict_val: List[str]) -> bool:
        s = len(str_val)+1
        dp = [False]*s
        dp[0] = True

        maxLen = 0
        for i in dict_val:
            maxLen = max(len(i),maxLen)


        print(dp)
        print(maxLen)

        for i in range(1,len(dp)):
            j = i-1
            while j >= max(0,i-maxLen):
                if dp[j] and str_val[j:i] in dict_val:
                    dp[i] = True
                    break
                j-=1
        return dp[-1]
