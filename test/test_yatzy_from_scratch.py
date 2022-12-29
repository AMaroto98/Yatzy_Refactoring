import pytest
from src.yatzy import Yatzy


def test_chance():
    assert Yatzy.chance(1, 2, 3, 4, 5) == 15 
    assert Yatzy.chance(1, 1, 3, 3, 6) == 14
    assert Yatzy.chance(4, 5, 5, 6, 1) == 21

def test_yatzy():
    assert Yatzy.yatzy(5, 5, 5, 5, 5) == 50
    assert Yatzy.yatzy(5, 5, 5, 5, 4) == 0

def test_ones():
    assert Yatzy.ones(1, 2, 3, 4, 1) == 2
    assert Yatzy.ones(1, 1, 1, 4, 5) == 3
    assert Yatzy.ones(5, 2, 6, 4, 5) == 0

def test_twos():
    assert Yatzy.twos(1, 2, 3, 4, 1) == 2
    assert Yatzy.twos(2, 2, 2, 4, 5) == 6
    assert Yatzy.twos(5, 1, 6, 4, 5) == 0

def test_threes():
    assert Yatzy.threes(1, 2, 3, 4, 1) == 3
    assert Yatzy.threes(2, 2, 2, 4, 5) == 0
    assert Yatzy.threes(3, 3, 6, 3, 5) == 9

def test_fours():
    assert Yatzy.fours(4, 4, 3, 4, 1) == 12
    assert Yatzy.fours(2, 2, 2, 4, 5) == 4
    assert Yatzy.fours(3, 3, 6, 3, 5) == 0

def test_fives():
    assert Yatzy.fives(5, 5, 3, 4, 1) == 10
    assert Yatzy.fives(2, 5, 2, 5, 5) == 15
    assert Yatzy.fives(3, 3, 6, 3, 1) == 0

# @pytest.fixture
# def inyector():
#     # Es el setup de unittest o de JUnit
#     tirada = Yatzy(1, 2, 3, 4, 5)
#     return tirada

# @pytest
# def test_fours(inyector):
#     # Es necesario un objeto ya creado
#     valorEsperado = 4
#     # No puedo testear con fixtures = inyeccion de dependencias
#     # los metodos estaticos como chance()
#     assert valorEsperado == inyector.fours()
