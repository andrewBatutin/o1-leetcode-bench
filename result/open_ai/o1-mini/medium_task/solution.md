To solve the problem of finding the maximum possible total score by reaching the end of the array, we can utilize dynamic programming combined with an efficient data structure known as the **Li Chao Tree**. This approach allows us to efficiently compute the maximum scores by maintaining a set of lines (representing different jump options) and querying the best possible score at each step.

### Problem Breakdown

1. **Dynamic Programming (DP) Approach:**
   - **State Definition:** Let `dp[i]` represent the maximum score to reach index `i`.
   - **State Transition:** To compute `dp[i]`, consider all possible jumps from previous indices `j < i`. The score for a jump from `j` to `i` is `(i - j) * nums[j]`. Therefore, the transition can be expressed as:
     \[
     dp[i] = \max_{j < i} (dp[j] + (i - j) \times nums[j])
     \]
   
2. **Optimizing with Li Chao Tree:**
   - The above transition resembles the problem of finding the maximum value of a linear function at a given point. Specifically, for each `j`, we can represent the score as a line:
     \[
     y = nums[j] \times x + (dp[j] - nums[j] \times j)
     \]
   - The goal is to find the maximum `y` for a given `x = i`. The Li Chao Tree efficiently manages these lines and queries the maximum value at each `x`.

### Implementation Details

- **Li Chao Tree Structure:**
  - Each node in the tree represents an interval `[l, r]`.
  - Lines are inserted into the tree based on their slopes and intercepts.
  - For each index `i`, we query the tree to find the best previous jump that maximizes the score.

- **Steps:**
  1. Initialize `dp[0] = 0` since we start at index `0` with no score.
  2. Insert the first line corresponding to index `0` into the Li Chao Tree.
  3. Iterate through the array, updating `dp[i]` by querying the tree for the best possible score and then inserting the new line corresponding to the current index.

### Python Solution

Here is the complete Python solution using the Li Chao Tree approach:

```python
class Solution(object):
    def findMaximumScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import math
        class LiChaoNode:
            __slots__ = ['l', 'r', 'left', 'right', 'line']
            def __init__(self, l, r):
                self.l = l
                self.r = r
                self.left = None
                self.right = None
                self.line = None  # (a, b)

        class LiChaoTree:
            def __init__(self, l, r):
                self.root = LiChaoNode(l, r)

            def insert_line(self, node, new_a, new_b):
                l, r = node.l, node.r
                m = (l + r) //2
                if node.line is None:
                    node.line = (new_a, new_b)
                    return
                curr_a, curr_b = node.line
                # Compare at midpoint
                y_new_m = new_a * m + new_b
                y_curr_m = curr_a * m + curr_b
                if y_new_m > y_curr_m:
                    # Swap the lines
                    node.line, (new_a, new_b) = (new_a, new_b), node.line
                    curr_a, curr_b = node.line
                    y_new_m, y_curr_m = y_curr_m, y_new_m
                # Now, compare at left and right
                y_new_l = new_a * l + new_b
                y_curr_l = curr_a * l + curr_b
                if y_new_l > y_curr_l:
                    if node.left is None:
                        node.left = LiChaoNode(l, m)
                    self.insert_line(node.left, new_a, new_b)
                y_new_r = new_a * r + new_b
                y_curr_r = curr_a * r + curr_b
                if y_new_r > y_curr_r:
                    if node.right is None:
                        node.right = LiChaoNode(m +1, r)
                    self.insert_line(node.right, new_a, new_b)

            def query_max(self, node, x):
                if node is None:
                    return -math.inf
                res = node.line[0] *x + node.line[1] if node.line else -math.inf
                m = (node.l + node.r) //2
                if x < m:
                    return max(res, self.query_max(node.left, x))
                elif x > m:
                    return max(res, self.query_max(node.right, x))
                else:
                    return res

        n = len(nums)
        dp = [0] *n
        if n ==1:
            return 0
        # Initialize Li Chao Tree with x in [0, n-1]
        tree = LiChaoTree(0, n -1)
        # Insert the first line from j=0: y=nums[0] *x +0
        tree.insert_line(tree.root, nums[0], 0)
        for i in range(1, n):
            # Query at x=i
            max_val = tree.query_max(tree.root, i)
            dp[i] = max_val
            if i != n -1:
                # Insert the line for j=i: y=nums[i]*x + (dp[i] - nums[i]*i)
                # Only need to insert lines for jumps that are not the last index
                tree.insert_line(tree.root, nums[i], dp[i] - nums[i]*i)
        return dp[-1]
```

### Explanation of the Solution

1. **Initialization:**
   - We start by initializing `dp[0] = 0` because we start at index `0` with no score.
   - We create a `LiChaoTree` that handles x-values in the range `[0, n-1]` where `n` is the length of the `nums` array.
   - We insert the first line corresponding to index `0` into the tree.

2. **Dynamic Programming Iteration:**
   - For each index `i` from `1` to `n-1`, we:
     - Query the `LiChaoTree` to find the maximum possible score to reach index `i`.
     - Update `dp[i]` with this maximum score.
     - Insert a new line into the `LiChaoTree` representing the potential jump from the current index `i` to future indices.

3. **Final Result:**
   - After processing all indices, `dp[n-1]` will contain the maximum possible total score to reach the end of the array.

### Complexity Analysis

- **Time Complexity:** \(O(n \log n)\) where \(n\) is the length of the `nums` array. This is due to each insertion and query operation in the Li Chao Tree taking \(O(\log n)\) time.
- **Space Complexity:** \(O(n)\) for storing the `dp` array and the Li Chao Tree nodes.

This solution efficiently computes the desired maximum score by leveraging the properties of the Li Chao Tree, making it suitable for large input sizes within the given constraints.