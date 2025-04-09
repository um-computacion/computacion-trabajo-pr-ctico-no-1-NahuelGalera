# roman_converter.py

def decimal_to_roman(number):
    if number < 1 or number > 3999:
        raise ValueError("El número debe estar en el rango de 1 a 3999")

    roman_numerals = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    result = ""
    for value, numeral in roman_numerals:
        while number >= value:
            result += numeral
            number -= value

    return result