Here's a Python solution for the given LeetCode problem:

```python
class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        # Split the date string into year, month, and day
        year, month, day = date.split('-')
        
        # Convert year, month, and day to integers
        year = int(year)
        month = int(month)
        day = int(day)
        
        # Convert year, month, and day to binary strings without leading zeros
        binary_year = bin(year)[2:]  # [2:] removes the '0b' prefix
        binary_month = bin(month)[2:]
        binary_day = bin(day)[2:]
        
        # Combine the binary representations in the required format
        binary_date = f"{binary_year}-{binary_month}-{binary_day}"
        
        return binary_date
```

This solution works as follows:

1. We split the input `date` string into `year`, `month`, and `day` using the `-` separator.

2. We convert each part (year, month, day) to integers.

3. We use the `bin()` function to convert each integer to its binary representation. The `bin()` function returns a string starting with '0b', so we use string slicing `[2:]` to remove this prefix.

4. We combine the binary representations of year, month, and day using f-string formatting, separating them with '-' as required.

5. Finally, we return the resulting binary date string.

This solution correctly handles the conversion of dates to their binary representation as per the problem requirements. It will work for any valid input date within the specified constraints.