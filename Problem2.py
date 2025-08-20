# Given a string s, find the length of the longest substring without duplicate characters.

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
