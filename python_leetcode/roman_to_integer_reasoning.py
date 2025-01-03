class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        last = s[-1]

        for item in reversed():
            if item == "C" and last in ["D", "M"]:
                result -= roman[item]
            elif item == "X" and last in ["L", "C"]:
                result -= roman[item]
            elif item == "I" and last in ["V", "X"]:
                result -= roman[item]
            else:
                result += roman[item]

            last = item
        return result


solution = Solution()
solution.romanToInt("LVIII")
