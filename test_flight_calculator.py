import pytest

from flight_calculator import calculate_flight_time, flight_time_table


@pytest.mark.parametrize(
    ("weight", "expected"),
    [
        (0, 180),
        (100, 170),
        (500, 130),
        (1800, 0),
        (2000, 0),
    ],
)
def test_calculate_flight_time(weight, expected):
    assert calculate_flight_time(weight) == expected


def test_calculate_flight_time_rejects_negative_weight():
    with pytest.raises(ValueError, match="Weight cannot be negative"):
        calculate_flight_time(-1)


def test_flight_time_table():
    assert flight_time_table(500, 100) == [
        (0, 180),
        (100, 170),
        (200, 160),
        (300, 150),
        (400, 140),
        (500, 130),
    ]


@pytest.mark.parametrize(
    ("max_weight", "step"),
    [
        (-1, 100),
        (500, 0),
        (500, -10),
    ],
)
def test_flight_time_table_rejects_invalid_arguments(max_weight, step):
    with pytest.raises(
        ValueError,
        match="Max weight must be non-negative and step must be positive",
    ):
        flight_time_table(max_weight, step)