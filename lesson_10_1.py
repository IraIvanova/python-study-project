def convert_to_string_list(initial_list: list) -> list[str]:
    converted_list = map(lambda i: str(i), initial_list)
    return list(converted_list)


def get_only_numbers(initial_list: list) -> list[int]:
    filtered_list = filter(lambda i: isinstance(i, int), initial_list)
    return list(filtered_list)


random_values_list = [257, 23.69, 'Something', True, 4, ['Fox', 565, 12.22], 'Game of Thrones', 9121, False, None, 78.33, 'Snow', 8, 4987.44]

map_result = convert_to_string_list(random_values_list)
filter_result = get_only_numbers(random_values_list)
