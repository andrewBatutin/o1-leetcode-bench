To solve this problem, we need to find the maximum possible total score by the time we reach the last index of the array. The score for a jump from index `i` to index `j` is calculated as `(j - i) * nums[i]`.

We can use a dynamic programming approach to solve this problem efficiently. We'll maintain an array `dp` where `dp[i]` represents the maximum score to reach index `i`.

Here's the step-by-step approach:

1. Initialize a `dp` array with negative infinity values, except for `dp[0]` which should be 0 because we start at index 0.
2. Use a deque to keep track of the indices in a way that helps us efficiently find the maximum score for the next jump.
3. Iterate through the array and update the `dp` values based on the maximum score we can achieve from previous indices.
4. Use the deque to maintain the indices in a way that allows us to quickly find the maximum score for the next jump.

Here's the Python code implementing this approach:

```python
from collections import deque

class Solution(object):
    def findMaximumScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [-float('inf')] * n
        dp[0] = 0
        dq = deque([0])
        
        for i in range(1, n):
            while dq and dq[0] < i - nums[dq[0]]:
                dq.popleft()
            
            dp[i] = dp[dq[0]] + (i - dq[0]) * nums[dq[0]]
            
            while dq and dp[i] >= dp[dq[-1]]:
                dq.pop()
            
            dq.append(i)
        
        return dp[-1]

# Example usage:
solution = Solution()
print(solution.findMaximumScore([1, 3, 1, 5]))  # Output: 7
print(solution.findMaximumScore([4, 3, 1, 3, 2]))  # Output: 16
```

### Explanation:
1. **Initialization**: We initialize the `dp` array with negative infinity values and set `dp[0]` to 0 because we start at index 0.
2. **Deque Usage**: We use a deque to keep track of indices. The deque helps us efficiently find the maximum score for the next jump.
3. **Updating `dp`**: For each index `i`, we update `dp[i]` based on the maximum score we can achieve from previous indices stored in the deque.
4. **Maintaining the Deque**: We maintain the deque by removing indices that are no longer useful (i.e., indices that are too far back to be considered for the current jump) and ensuring that the deque is in a state that allows us to quickly find the maximum score for the next jump.

This approach ensures that we efficiently compute the maximum possible total score by the time we reach the last index.