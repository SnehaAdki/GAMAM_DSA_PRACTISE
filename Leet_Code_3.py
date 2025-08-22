# 3. Longest Substring Without Repeating Characters
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s, find the length of the longest substring without duplicate characters.

 
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

def lengthOfLongestSubstring(string):
    hash_map = []
    r = l = 0 
    max_len = 0

    while r < len(string):
        if string[r] not in hash_map:
            hash_map.append(string[r])
            r+=1
        elif string[r]  in hash_map:
            if r - l > max_len:
                max_len=r-l
            while l <= r and string[r]  in hash_map:
                hash_map.remove(string[l])
                l+=1
    if r - l > max_len:
        max_len=r-l
    
    print(max_len)


# lengthOfLongestSubstring('bbbb')
lengthOfLongestSubstring('pwwkewxpw')
