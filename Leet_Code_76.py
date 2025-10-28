
#leet Code : 76
# https://leetcode.com/problems/minimum-window-substring/submissions/1814221785/

# 76. Minimum Window Substring
# Solved
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.

# Example 3:
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.




# def minWindow(s, t):
#     if len(s) < len(t):
#         return ""
    
#     # Count characters in t
#     char_count = {}
#     for char in t:
#         char_count[char] = char_count.get(char, 0) + 1
    
#     # Variables for sliding window
#     left = 0
#     min_len = float('inf')
#     min_start = 0
#     required_chars = len(char_count)  # Number of unique chars in t
#     formed_chars = 0  # Number of unique chars in current window with desired frequency
    
#     # Dictionary to keep count of characters in current window
#     window_counts = {}
    
#     for right in range(len(s)):
#         # Add character from the right to the window
#         char = s[right]
#         window_counts[char] = window_counts.get(char, 0) + 1
        
#         # Check if the frequency of current character matches the desired count in t
#         if char in char_count and window_counts[char] == char_count[char]:
#             formed_chars += 1
        
#         # Try to contract the window from left
#         while left <= right and formed_chars == required_chars:
#             char = s[left]
            
#             # Update minimum window if current is smaller
#             if right - left + 1 < min_len:
#                 min_len = right - left + 1
#                 min_start = left
            
#             # Remove character from left of window
#             window_counts[char] -= 1
#             if char in char_count and window_counts[char] < char_count[char]:
#                 formed_chars -= 1
            
#             left += 1
    
#     # Return minimum window or empty string if no window found
#     return "" if min_len == float('inf') else s[min_start:min_start + min_len]


# # Test cases
# test_cases = [
#     # ("ADOBECODEBANC", "ABOO"),  # Expected: "BANC"
#     # ("bdab", "ab"),           # Expected: "ab" 
#     ("aa", "aa"),               # Expected: "a"
#     # ("a", "aa"),              # Expected: ""
#     # ("ab", "b"),              # Expected: "b"
# ]

# print("Testing minWindow function:")
# for s, t in test_cases:
#     result = minWindow(s, t)
#     print(f"s='{s}', t='{t}' -> '{result}'")



def minWindow(s,t):
    if len(s) < len(t):
        return ""
    
    char_count = {}
    for en in t:
        char_count[en] = char_count.get(en,0)+1
        
    minlen = float('inf')
    min_start =0 
    left = 0
    req_count = len(char_count)
    formed_char = 0
    
    window = {}
    
    
    for right in range(len(s)):
        char = s[right]
        window[char] = window.get(char , 0)+1
        
        if char in char_count and window[char] == char_count[char]:
            formed_char+=1
        
        while formed_char == req_count and left<=right:
            char = s[left]
            if right-left+1 < minlen:
                minlen = right-left+1
                min_start = left
            
            window[char]-=1
            
            if char in char_count and window[char]< char_count[char]:
                formed_char-=1
            
            left+=1
            
    return "" if minlen == float('inf') else s[min_start:min_start+minlen]
            
    
test_cases = [
    ("ADOBECODEBANC", "ABOO"),  # Expected: "BANC"
    ("aa", "aa"),  # Expected: "BANC"
    # ("bdab", "ab"),           # Expected: "ab" 
    # ("a", "a"),               # Expected: "a"
    # ("a", "aa"),              # Expected: ""
    # ("ab", "b"),              # Expected: "b"
]

print("Testing minWindow function:")
for s, t in test_cases:
    result = minWindow(s, t)
    print(f"s='{s}', t='{t}' -> '{result}'")
