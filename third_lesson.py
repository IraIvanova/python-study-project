initial_string = "6..58київ\nоДеса     Львів\tжитоМИР      уЖгОрОд ХарКІВ       слАвУтИч74$:?$"

cities_array = initial_string.split('     ')
formatted_cities = []

for city in cities_array:
    formatted_cities += city.split()

for city in formatted_cities:
    print(f"Я \U00002764 {city.strip('6..58 74$:?$').title()}")
