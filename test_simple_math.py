import simple_math
import pytest 

def test_simple_math_simple_add():
    assert simple_math.simple_add(5, 5) == 10

def test_simple_math_simple_sub():
    assert simple_math.simple_sub(5, 5) == 0

def test_simple_math_simple_mult():
    assert simple_math.simple_mult(5, 5) == 25

def test_simple_math_simple_square():
    assert simple_math.simple_square(2, 5) == 32

def test_simple_math_simple_div_float():
    assert simple_math.simple_div_float(1, 3) == 1/3 

def test_simple_math_simple_div_int():
    assert simple_math.simple_div_int(6,6) == 1

def test_simple_math_poly_first():
    assert simple_math.poly_first(2, 1, 1) == 3

def test_simple_math_poly_second():
    assert simple_math.poly_second(2, 6, 5 , 8) == 48 
