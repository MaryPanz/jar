from jar import Jar
import pytest

def test_init():
    pass
    jar = Jar()

    assert jar.capacity == 12
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(9)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(1) == 1
    with pytest.raises(ValueError):
        assert jar.deposit(13)

def test_withdraw():
    jar = Jar()

    jar.deposit(5)
    assert jar.withdraw(2) == 3

    with pytest.raises(ValueError):
        assert jar.withdraw(14)
