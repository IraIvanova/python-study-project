def get_trip_info():
    input_visited_cities = input("Введіть міста, в яких ви були за минулі 10 років (через пробіл): ")
    visited_cities = set(map(lambda s: s.title(), input_visited_cities.split()))

    input_cities_future = input("Введіть міста, куди ви хочете поїхати в наступні 10 років (через пробіл): ")
    cities_future = set(map(lambda s: s.title(), input_cities_future.split()))

    common_cities = visited_cities.intersection(cities_future)

    if common_cities:
        print(f"Схоже, вам дуже сподобалося в цих містах: {', '.join(common_cities)}")
    else:
        print("Виглядає, що ви відкриті до чогось нового.")


get_trip_info()
