https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0 # Initialize two pointers for word1 and word2
        res = []    # Create an empty list to store merged characters
        # Loop until we reach the end of either word1 or word2
        while i < len(word1) and j < len(word2):
            res.append(word1[i]) # Append character from word1 at index i
            res.append(word2[j]) # Append character from word2 at index j
            i += 1 # Move pointer i to the next character in word1
            j += 1 # Move pointer j to the next character in word2
        # If word1 is longer, add the remaining characters to the result
        res.append(word1[i:]) # word1[i:] means "all characters from index i to end"
        # If word2 is longer, add the remaining characters to the result
        res.append(word2[j:]) # word2[j:] means "all characters from index j to end"
        return "".join(res) # Join list elements into a single string and return
