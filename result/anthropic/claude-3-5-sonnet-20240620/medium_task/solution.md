Here's a Python solution to the given LeetCode problem:

```python
class Solution(object):
    def findMaximumScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n
        dp[-1] = 0  # Base case: last index has no score
        
        for i in range(n - 2, -1, -1):
            max_score = 0
            for j in range(i + 1, n):
                score = (j - i) * nums[i] + dp[j]
                max_score = max(max_score, score)
            dp[i] = max_score
        
        return dp[0]
```

This solution uses dynamic programming to solve the problem efficiently. Here's how it works:

1. We create a DP array `dp` of length `n` to store the maximum score that can be achieved starting from each index.

2. We initialize the last element of `dp` to 0 since there's no score to be gained from the last index.

3. We iterate through the array from right to left (excluding the last element):
   - For each index `i`, we consider all possible jumps to indices `j` greater than `i`.
   - We calculate the score for each jump as `(j - i) * nums[i] + dp[j]`, where `dp[j]` represents the maximum score that can be achieved from index `j`.
   - We keep track of the maximum score achievable from index `i` and store it in `dp[i]`.

4. After the iteration, `dp[0]` will contain the maximum possible total score starting from index 0.

5. We return `dp[0]` as the final result.

The time complexity of this solution is O(n^2) in the worst case, where n is the length of the input array. The space complexity is O(n) for the DP array.

This solution efficiently handles the given constraints and provides the maximum possible total score for reaching the last index.