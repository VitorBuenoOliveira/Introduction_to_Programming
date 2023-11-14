def roman_to_int(str_roman: str) -> int:
    roman_translator = {'I': 1,
                        'V': 5,
                        'X': 10,
                        'L': 50,
                        'C': 100,
                        'D': 500,
                        'M': 1000}
    convert = [roman_translator[s] for s in str_roman][::-1]

    number = 0
    prev_value = 0
    for i in convert:
        if i >= prev_value:
            number += i
        else:
            number -= i
        prev_value = i
    return number

r = roman_to_int('VIII')
print(r)
