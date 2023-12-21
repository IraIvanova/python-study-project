def get_distance(*, time: int | float, speed: int | float, weight: int | float) -> str:
    if time < 0 or speed < 0 or weight < 0:
        raise ValueError('All arguments should be more than 0')

    distance = speed * time
    return f"Транспортний засіб вагою {weight} кг рухався {time} секунд зі швидкістю {speed}м/сек, і подолав відстань {distance} метрів"
