To solve this problem, we'll follow these steps:

1. **Split the Date:** Divide the input string into year, month, and day components using the `split` method.
2. **Convert to Integers:** Convert each component from string to integer.
3. **Convert to Binary:** Use Python's `bin` function to convert each integer to its binary representation. The `bin` function returns a string that starts with `'0b'`, so we'll slice the string from index `2` to remove the `'0b'` prefix.
4. **Concatenate with Dashes:** Combine the binary strings with dashes (`'-'`) separating them to form the final binary date string.

Here's the Python implementation:

```python
class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        # Split the date into year, month, and day
        year, month, day = date.split('-')
        
        # Convert each part to integer and then to binary without '0b' prefix
        year_bin = bin(int(year))[2:]
        month_bin = bin(int(month))[2:]
        day_bin = bin(int(day))[2:]
        
        # Concatenate the binary strings with dashes
        binary_date = f"{year_bin}-{month_bin}-{day_bin}"
        
        return binary_date
```

### **Example Usage:**

```python
# Example 1
solution = Solution()
print(solution.convertDateToBinary("2080-02-29"))  # Output: "100000100000-10-11101"

# Example 2
print(solution.convertDateToBinary("1900-01-01"))  # Output: "11101101100-1-1"
```

### **Explanation:**

- **Splitting the Date:** The `split('-')` function divides the input string into three parts: year, month, and day.
  
- **Converting to Binary:**
  - `int(year)`, `int(month)`, and `int(day)` convert the string parts to integers.
  - `bin(number)[2:]` converts the integer to a binary string and removes the `'0b'` prefix.
  
- **Formatting the Output:** The `f-string` (`f"{year_bin}-{month_bin}-{day_bin}"`) combines the binary strings with dashes in between, as required.

This solution efficiently converts each component of the date to its binary representation and formats the result as specified.