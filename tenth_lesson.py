import library.library as lib

inches = lib.convert_centimeters_to_inches(25)
even_numbers = lib.get_even_numbers([2, 6, 4, 28, 3, 1, 20, 1, 8, 9, 45, 878])
is_loan_affordable = lib.can_get_loan(850000, 25, 10500, 35)

print(f"{inches=} {even_numbers=} {is_loan_affordable=}")
