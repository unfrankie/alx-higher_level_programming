def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0
    r_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(roman_string)):
        value_0 = r_n[roman_string[i]]
        value_1 = r_n[roman_string[i + 1]] if i + 1 < len(roman_string) else 0
        if value_0 < value_1:
            result -= value_0
        else:
            result += value_0
    return result
