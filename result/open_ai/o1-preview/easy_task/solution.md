To solve this problem, we'll follow these steps:

1. **Parse the input string**: Extract the year, month, and day from the input string `date`. Since the format is always `yyyy-mm-dd`, we can use string slicing.

2. **Convert to integers**: Convert the extracted year, month, and day strings to integers using the `int()` function. This removes any leading zeros and ensures we're working with numerical values.

3. **Convert to binary strings**: Use Python's built-in `bin()` function to convert each integer to its binary representation. The `bin()` function returns a string in the format `'0b...'`, so we'll slice off the first two characters to remove the `'0b'` prefix.

4. **Assemble the result**: Concatenate the binary strings of the year, month, and day with hyphens in between to match the required format.

Here is the implementation:

```python
class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        year = date[0:4]
        month = date[5:7]
        day = date[8:10]
        year_bin = bin(int(year))[2:]
        month_bin = bin(int(month))[2:]
        day_bin = bin(int(day))[2:]
        return f"{year_bin}-{month_bin}-{day_bin}"
```