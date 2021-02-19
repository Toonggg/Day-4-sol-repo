"""
An extended library of simple math operations
"""

def simple_add(a,b):
    """The sum of two numbers.

    Parameters
    ----------
    a : int or float
        First number to be added. 
    b : int or float
        Second number to be added. 

    Returns
    -------
    out : int or float
        Sum of a and b. 
    """ 
    return a+b

def simple_sub(a,b):
    """The subtraction of two numbers.

    Parameters
    ----------
    a : int or float
        First number to be subtracted. 
    b : int or float
        Second number to be subtracted. 

    Returns
    -------
    out : int or float 
        Subtraction of a and b. 
    """ 
    return a-b

def simple_square(a,b):
    """The square of two numbers.

    Parameters
    ----------
    a : int or float
        First number to be squared. 
    b : int or float
        Second number to be squared. 

    Returns
    -------
    out : int or float 
        Square of a and b. 
    """ 
    return a**b

def simple_mult(a,b):
    """The multiplication of two numbers.

    Parameters
    ----------
    a : int or float
        First number to be multiplied. 
    b : int or float
        Second number to be multiplied. 

    Returns
    -------
    out : int or float
        Multiplication of a and b. 
    """ 
    return a*b

def simple_div_float(a,b):
    """Floating-point division of two numbers. 

    Input variables a and b are explicitly cast to floats.

    Parameters
    ----------
    a : float
        First float to be divided. 
    b : float
        Second float to be divided.. 

    Returns
    -------
    out : float 
        Division of a and b. 
    """ 
    a = float(a)
    b = float(b)
    return (a/b)

def simple_div_int(a,b):
    """Integer division of two numbers.

    Input variables a and b are explicitly cast to ints.
    Parameters
    ----------
    a : int
        First integer to be divided. 
    b : int
        Second integer to be divided. 

    Returns
    -------
    out : int 
        Division of a and b. 
    """ 
    a = int(a)
    b = int(b)
    return a//b

def poly_first(x, a0, a1):
    """First-order polynomial equation in one-dimension. 

    Parameters
    ----------
    x : int or float
        x-coordinate of polynomial. 
    a0 : int or float 
        y-intercept of polynomial. 
    a1 : int or float
        Slope of polynomial. 

    Returns
    -------
    out : int or float 
        Value at x
    """ 
    return a0 + a1*x 

def poly_second(x, a0, a1, a2):
    """Second-order polynomial equation in one dimension. 

    Parameters
    ----------
    x : int or float
        x-coordinate of polynomial. 
    a0 : int or float
        Constant coefficient of polynomial. 
    a1 : int or float
        Linear coefficient of polynomial. 
    a2 : int or float
        Quadratic coefficient of polynomial. 

    Returns 
    -------
    out : int or float 
        Value at x
    """ 
    return a0 + a1*x + a2*(x**2) 
