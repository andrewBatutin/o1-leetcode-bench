To solve the problem of reaching the end of the array with the maximum score, we can use a dynamic programming approach. The idea is to maintain a score array where each entry at index `i` represents the maximum score we can achieve when reaching that index.

Here's a step-by-step breakdown of the approach:

1. **Initialization**: Start by initializing a score array `dp` where `dp[i]` will store the maximum score to reach index `i`. The score to reach the first index (index 0) is simply `0` since we start there.

2. **Dynamic Programming Transition**: For each index `i`, we can jump to any index `j` (where `j > i`). The score for jumping from `i` to `j` is calculated as `(j - i) * nums[i]`. Therefore, the score to reach `j` can be updated as:
   \[
   dp[j] = \max(dp[j], dp[i] + (j - i) * nums[i])
   \]
   This means we take the maximum of the current score at `j` and the score we can achieve by jumping from `i` to `j`.

3. **Final Result**: The answer will be the value in `dp[n-1]`, which represents the maximum score to reach the last index.

Here's the implementation of the above logic in Python:

```python
class Solution(object):
    def findMaximumScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n  # Initialize the dp array with zeros
        dp[0] = 0  # Starting point, score is 0
        
        for i in range(n):
            for j in range(i + 1, n):
                score = (j - i) * nums[i]
                dp[j] = max(dp[j], dp[i] + score)
        
        return dp[n - 1]  # The maximum score to reach the last index

# Example usage:
solution = Solution()
print(solution.findMaximumScore([1, 3, 1, 5]))  # Output: 7
print(solution.findMaximumScore([4, 3, 1, 3, 2]))  # Output: 16
```

### Complexity Analysis:
- **Time Complexity**: The time complexity of this solution is \(O(n^2)\) due to the nested loops iterating through the indices.
- **Space Complexity**: The space complexity is \(O(n)\) for the `dp` array.

### Optimization:
For larger inputs, this approach may not be efficient enough. We can optimize it using a more advanced data structure like a deque or a priority queue to keep track of the maximum scores efficiently, but the above solution is straightforward and works well for smaller inputs.