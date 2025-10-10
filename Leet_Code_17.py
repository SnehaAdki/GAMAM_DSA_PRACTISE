# https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/1797544516/
# Leet Code : 17. Letter Combinations of a Phone Number
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:
# Input: digits = ""
# Output: []

# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]

def letterCombinations(digits):
    if len(digits) == 0:
        return []
    
    dict_phone_book = {
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz',
    }
    def back_track(combination,digits):
        if len(digits) == 0:
            output.append(combination)
        else:
            for i in dict_phone_book[digits[0]]:
                back_track(combination+i,digits[1:])
    output= []  
    back_track("",digits)
    return output
