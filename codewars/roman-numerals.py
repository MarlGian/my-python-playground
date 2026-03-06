class RomanNumerals:
    @staticmethod
    def to_roman(val : int) -> str:
        roman = {1000 : "M", 900 : "CM", 500 : "D", 400 : "CD", 100 : "C",
                 90 : "XC", 50 : "L", 40 : "XL", 10 : "X", 9 : "IX", 5 : "V",
                 4 : "IV", 1 : "I"}
        result = ""
        for key,value in roman.items():
            while key <= val:
                val -= key
                result += value
        return result

    @staticmethod
    def from_roman(roman_num : str) -> int:
        roman = { "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        result = 0
        roman_list = list(roman_num)

        for i in range(len(roman_list) - 1):
            if roman[roman_list[i]] < roman[roman_list[i + 1]]:
                result -= roman[roman_list[i]]
            else:
                result += roman[roman_list[i]]
        result += roman[roman_list[-1]]
        return result



print(RomanNumerals.to_roman(30))
print(RomanNumerals.from_roman("CMXCIX"))
