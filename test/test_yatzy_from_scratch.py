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
