To solve the problem of converting a date in the format "yyyy-mm-dd" to its binary representation, we need to follow these steps:

1. Split the input date string into year, month, and day components.
2. Convert each component (year, month, and day) to its binary representation.
3. Concatenate these binary representations with hyphens in between.

Here's the Python solution for the given problem:

```python
class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        # Split the date into year, month, and day
        year, month, day = date.split('-')
        
        # Convert each part to an integer
        year = int(year)
        month = int(month)
        day = int(day)
        
        # Convert each part to its binary representation without leading zeroes
        year_bin = bin(year)[2:]
        month_bin = bin(month)[2:]
        day_bin = bin(day)[2:]
        
        # Concatenate the binary representations with hyphens
        binary_date = f"{year_bin}-{month_bin}-{day_bin}"
        
        return binary_date

# Example usage:
solution = Solution()
print(solution.convertDateToBinary("2080-02-29"))  # Output: "100000100000-10-11101"
print(solution.convertDateToBinary("1900-01-01"))  # Output: "11101101100-1-1"
```

### Explanation:
1. **Splitting the Date**: We use the `split('-')` method to separate the date string into `year`, `month`, and `day`.
2. **Converting to Integers**: We convert these string components to integers using `int()`.
3. **Binary Conversion**: We convert each integer to its binary representation using the `bin()` function and strip the '0b' prefix using slicing `[2:]`.
4. **Concatenation**: We format the binary strings into the required format using an f-string.

This solution ensures that each part of the date is correctly converted to its binary representation and concatenated with hyphens as specified.