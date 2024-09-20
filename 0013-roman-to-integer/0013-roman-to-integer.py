class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        i = 0
        for char in s:
            total += roman_to_int[char]
            if i <= len(s) - 1:
                if roman_to_int[char] > roman_to_int[s[i - 1]] and i != 0:
                    total -= 2 * roman_to_int[s[i - 1]]
            i += 1
        return total