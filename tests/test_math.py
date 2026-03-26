import pytest

# ---- Code under test (normally you'd import this) ----
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("division by zero")
    return a / b


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


@pytest.fixture
def sample_numbers():
    return {
        "a": 10,
        "b": 2,
        "zero": 0,
    }


def test_divide_basic(sample_numbers):
    result = divide(sample_numbers["a"], sample_numbers["b"])
    assert result == 5


def test_divide_by_zero(sample_numbers):
    with pytest.raises(ValueError, match="division by zero"):
        divide(sample_numbers["a"], sample_numbers["zero"])


@pytest.mark.parametrize(
    "n,expected",
    [
        (2, True),
        (3, True),
        (4, False),
        (17, True),
        (18, False),
        (1, False),
        (0, False),
        (-5, False),
    ],
)
def test_is_prime(n, expected):
    assert is_prime(n) == expected


def test_divide_precision():
    result = divide(1, 3)
    assert pytest.approx(result, rel=1e-6) == 0.333333



