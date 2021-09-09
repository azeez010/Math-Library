import pytest
from calclib import __Calclib as Calclib

@pytest.mark.parametrize(["x", "y"], ((3, 4), (323, 4), (5, 60)))
def test_add(x, y):
    add = x + y
    assert Calclib.add(x, y) == add

@pytest.mark.parametrize(["x", "y"], ((3, 4), (323, 4), (5, 60)))
def test_sub(x, y):
    sub = x - y
    assert Calclib.sub(x, y) == sub


@pytest.mark.parametrize(["x", "y"], ((3.0, 4), (323.3, 4), (5, 60)))
def test_sub_float(x, y):
    sub = x - y
    assert Calclib.subFloat(x, y) == sub


@pytest.mark.parametrize(["x", "y"], ((3.0, 4), (323.3, 4), (5, 60)))
def test_add_float(x, y):
    add = x + y
    assert Calclib.addFloat(x, y) == add
