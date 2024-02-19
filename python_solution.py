class Solution:
    def intToRoman(self, num: int) -> str:
        # Store the translations
        roman = [  "M","CM", "D","CD", "C","XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        values = [1000, 900, 500, 400, 100,  90,  50,  40, 10, 9, 5, 4, 1]
        ret_str = ""

        # Iterate through the values and append the appropriate roman numeral
        i = 0
        while num > 0: 
            while num >= values[i]:
                num -= values[i] # Decrement num based on the value you append to the list
                ret_str += roman[i] 
            i += 1
        return ret_str
