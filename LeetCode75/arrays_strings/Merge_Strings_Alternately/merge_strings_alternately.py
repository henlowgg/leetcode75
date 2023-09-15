# 1768. Merge Strings Alternately (ezpz)

# You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

# Starter Code
# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
        # Enter code here

# One Pointer Solution

class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = []
        n = max(len(word1), len(word2))
        for i in range(n):
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]

        return "".join(result)