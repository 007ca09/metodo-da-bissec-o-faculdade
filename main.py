from sympy.parsing.sympy_parser import (
    parse_expr, 
    standard_transformations, 
    implicit_multiplication_application, 
    convert_xor,
)
from sympy import symbols, lambdify, simplify
from ast import literal_eval


transforms_syms = standard_transformations + ( implicit_multiplication_application, convert_xor)

x_val_sym = symbols('x')

f_expr = input('f(x) = ')
interval = literal_eval(input('interval in format [a,b]: ').strip().split()[0])
epsilon = float(simplify(input("E: ").replace('^', '*')))

parse_f_expr = parse_expr(f_expr, transformations=transforms_syms)
f = lambdify(x_val_sym, parse_f_expr)

midpoint = (interval[0] + interval[1]) / 2

while abs(f(midpoint)) > 0.01:
    midpoint = (interval[0] + interval[1]) / 2

    if f(interval[0]) * f(midpoint) < 0:
        interval[1] = midpoint
    elif f(interval[0]) * f(midpoint) > 0:
        interval[0] = midpoint

print(midpoint)
