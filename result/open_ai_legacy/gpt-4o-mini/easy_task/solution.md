To solve the problem of converting a date in the format "yyyy-mm-dd" to its binary representation, we can follow these steps:

1. Split the input string into its components: year, month, and day.
2. Convert each component from decimal to binary.
3. Format the binary representations into the required output format.

Here's the Python solution implementing the above logic:

```python
class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        # Split the date into year, month, and day
        year, month, day = date.split('-')
        
        # Convert each part to binary without leading zeros
        year_binary = bin(int(year))[2:]  # Convert year to binary and remove '0b'
        month_binary = bin(int(month))[2:]  # Convert month to binary and remove '0b'
        day_binary = bin(int(day))[2:]  # Convert day to binary and remove '0b'
        
        # Format the result as required
        return f"{year_binary}-{month_binary}-{day_binary}"

# Example usage:
solution = Solution()
print(solution.convertDateToBinary("2080-02-29"))  # Output: "100000100000-10-11101"
print(solution.convertDateToBinary("1900-01-01"))  # Output: "11101101100-1-1"
```

### Explanation:
- We use `split('-')` to separate the year, month, and day.
- The `bin()` function converts a number to its binary representation, and we slice off the first two characters (`'0b'`) to get the pure binary string.
- Finally, we format the output using an f-string to concatenate the binary representations with hyphens in between.

This solution is efficient and straightforward, adhering to the constraints provided in the problem statement.