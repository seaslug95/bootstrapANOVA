import pytest
import numpy as np
from mymodule import fpval, sumSquares, fBootAnova, pvalBootAnova

def test_fpval():
    assert fpval(0.1) == "1.00E-1"
    assert fpval(0.01234) == "1.23E-2"
    assert fpval(0.01239) == "1.24E-2"

def test_sumSquares():
    assert sumSquares([1, 2, 3, 4, 5]) == 10
    s = [1.1, 2, 3]
    s_mean = np.array(s).mean()
    assert round(sumSquares(s), ndigits=10) == round((1.1-s_mean)**2 + (2-s_mean)**2 + (3-s_mean)**2, ndigits=10)

def test_fBootAnova():
    assert fBootAnova([[1, 2, 3], [2, 3, 4]]) > fBootAnova([[1, 2, 3], [1, 2, 3]])
    assert fBootAnova([[1, 2], [3, 4], [5, 6]]) > fBootAnova([[1, 2], [2, 3], [3, 4]])

def test_fBootAnova():
    assert fBootAnova([[1, 2, 3], [2, 3, 4]]) > fBootAnova([[1, 2, 3], [1, 2, 3]])
    assert fBootAnova([[1, 2], [3, 4], [5, 6]]) > fBootAnova([[1, 2], [2, 3], [3, 4]])

def test_pvalBootAnova():
    assert pvalBootAnova([[1, 2, 3], [2, 3, 4]]) < pvalBootAnova([[1, 2, 3], [1, 2, 3]])
    assert pvalBootAnova([[1, 2], [3, 4], [5, 6]]) < pvalBootAnova([[1, 2], [2, 3], [3, 4]])
