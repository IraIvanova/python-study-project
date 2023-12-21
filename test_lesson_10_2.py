import pytest
import lesson_10_2


def test_get_distance_with_negative_time():
    time = -2
    speed = 10
    weight = 60
    with pytest.raises(ValueError):
        lesson_10_2.get_distance(time=time, speed=speed, weight=weight)


def test_get_distance_with_negative_speed():
    time = 30
    speed = -2
    weight = 60
    with pytest.raises(ValueError):
        lesson_10_2.get_distance(time=time, speed=speed, weight=weight)


def test_get_distance_with_negative_weight():
    time = 100
    speed = 10
    weight = -2
    with pytest.raises(ValueError):
        lesson_10_2.get_distance(time=time, speed=speed, weight=weight)


def test_get_distance():
    time = 100
    speed = 10
    weight = 30
    distance = speed * time
    expected = f"Транспортний засіб вагою {weight} кг рухався {time} секунд зі швидкістю {speed}м/сек, і подолав відстань {distance} метрів"
    actual_result = lesson_10_2.get_distance(time=time, speed=speed, weight=weight)
    assert expected == actual_result
