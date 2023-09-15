Ok so:

We are given two strings word1 and word2

Task is to merge the strings by adding letters in alternating order, starting with word1.

If one string is longer then the other, the additional letters must be appended to the end of the merged string.

Then return the merged string that has been formed.

### Two ways to do this:

1. Two Pointers Technique:
    - Basically means it's searching for pairs in a sorted array;
    - Take two pointers:
        - One representing the first element;
        - The other representing the last element of the array;
        - Then add the values kept at both the pointers;
    - If their sum is smaller than X, we shift the left pointer to right;
    - If their sum is greater than X, we shift the right pointer to left;
        - In order to get closer to the sum;
    - Keep moving the pointers until we get the sum as X

### Below is an Implementation Example of Two Pointers:

```
from typing import List
 
 
def isPairSum(A: List[int], N: int, X: int) -> bool:
    # represents first pointer
    i = 0
 
    # represents second pointer
    j = N - 1
 
    while i < j:
        # If we find a pair
        if A[i] + A[j] == X:
            return True
 
        # If sum of elements at current
        # pointers is less, we move towards
        # higher values by doing i++
        elif A[i] + A[j] < X:
            i += 1
 
        # If sum of elements at current
        # pointers is more, we move towards
        # lower values by doing j--
        else:
            j -= 1
 
    return False
 
 
# Driver code
if __name__ == "__main__":
    # array declaration
    arr = [2, 3, 5, 8, 9, 10, 11]
 
    # value to search
    val = 17
 
    # size of the array
    arrSize = len(arr)
 
    # array should be sorted before using the two-pointer technique
    arr.sort()
 
    # Function call
    print(isPairSum(arr, arrSize, val))
```
## Output:
### `True`

### Time Complexity: `O(n log n) (As sort function is used)`
### Auxiliary Space: `O(1), since no extra space has been taken.`

# Which leads us to the 1st solution:

## Approach 1: Two Pointers

### Intuition

An intuitive method is to use two pointers to iterate over both strings. Assume we have two pointers, `i` and `j`, with `i` pointing to the first letter of `word1` and `j` pointing to the first letter of `word2`. We also create an empty string `results` to store the outcome.

We append the letter pointed to by pointer `i` i.e., `word1[i]`, and increment `i` by `1` to point to the next letter of `word1`. Because we need to add the letters in alternating order, next we append `word2[j]` to `results`. We also increase `j` by `1`.

We continue iterating over the given strings until both are exhausted. We stop appending letters from `word1` when `i` reaches the end of `word1`, and we stop appending letters from `word2` when `j` reaches the end of `word2`.

# Algorithm

1. Create two variables, m and n, to store the length of word1 and word2.

2. Create an empty string variable result to store the result of merged words.

3. Create two pointers, i and j to point to indices of word1 and word2. We initialize both of them to 0.

4. While i < m || j < n:
    If i < m, it means that we have not completely traversed word1. As a result, we append word1[i] to result. We increment i to point to next index of words.
    If j < n, it means that we have not completely traversed word2. As a result, we append word2[j] to result. We increment j to point to next index of words.

5. Return results.

*NOTE:* It's extremely important how we form the result string;

- Strings are immutable in Python. As a result, we used the list `result` to append letters and later joined the list with an empty string to return it as a string object. The `join` operation takes linear time equal to the length of `results` to merge `results` with empty string.

# Solution Code:

```
class Solution(object):
    def mergeAlternately(self, word1, word2):
        m = len(word1)
        n = len(word2)
        i = 0
        j = 0
        result = []

        while i < m or j < n:
            if i < m:
                result += word1[i]
                i += 1
            if j < n:
                result += word2[j]
                j += 1

        return "".join(result)
```

# Complexity Analysis

    Here, `m` is the length of `word1` and `n` is the length of `word2`.

#   Time complexity: O(m+n)

    We iterate over `word1` and `word2` once and push their letters into `result`. It would take O(m+n) time.

#   Space complexity: O(1)

    Without considering the space consumed by the input strings (word1 and word2) and the output string (result), we do not use more than constant space.


------------------------------------------------------------------------

# Second Solution:

## Approach 2: One Pointer

### Intuition

To merge the given words, we can also use a single pointer.

Let `i` be the pointer that we'll use. We begin with `i = 0` and progress to the size of the longer word between `word1` and `word2`, i.e., till `i = max(word1.length(), word2.length())`.

As we progress to the size of a longer word, we check each time if `i` points to an index that is in bounds of the words or not. If `i < word1.length()`, we append `word1[i]` to `results`.

Similarly if `i < word2.length()`, we append `word2[i]` to results.

However, if `i` exceeds the length of any word, we don't have any letters to add from that word, so we ignore it and continue adding the letter from the longer word.

# Algorithm

1. Create two variables, `m` and `n`, to store the length of `word1` and `word2`.

2. Create an empty string variable `result` to store the result of merged words.

3. Iterate over `word1` and `word2` using a loop running from `i = 0` to `i < max(m, n)` and keep incrementing `i` by `1` after each iteration:
    
    - If `i < m`, it means that we have not completely traversed `word1`. As a result, we append `word1[i]` to `result`.
    - If `i < n`, it means that we have not completely traversed `word2`. As a result, we append `word2[i]` to result.

4. Return `results`.

# Solution Code #2

```
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
```

# Complexity Analysis

    Here, `m` is the length of `word1` and `n` is the length of `word2`.

#   Time complexity: O(m+n)

    We iterate over `word1` and `word2` once pushing their letters into `result`. It would take O(m+n) time.

#   Space Complexity: O(1)
    
    Without considering the space consumed by the input strings (`word1` and `word2`) and the output string (`result`), we do not use more than constant space.