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
interval = literal_eval(input('interval in format [a,b]: ').strip())
a,b = interval
epsilon = float(simplify(input("E: ").replace('^', '**')))

parse_f_expr = parse_expr(f_expr, transformations=transforms_syms)
f = lambdify(x_val_sym, parse_f_expr, "math")

n_iter = 0

if f(a) * f(b) > 0:
    print(f'não existe raiz garantida no intervalo: {interval}')

else:
    while abs(b - a) > epsilon and n_iter < 100:
        midpoint = (a + b) / 2
        print(f"{n_iter:3d} | a = {a: .6f} | b = {b: .6f} | m = {midpoint: .6f} | "
      f"f(a) = {f(a): .6e} | f(b) = {f(b): .6e} | f(m) = {f(midpoint): .6e}")
        if abs(f(midpoint)) < epsilon:
            break
        if f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
        n_iter += 1

print(f'\nA raiz aproximada de f(x) = {f_expr} é {midpoint}')