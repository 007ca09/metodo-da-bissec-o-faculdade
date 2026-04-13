from sympy.parsing.sympy_parser import (
    parse_expr, 
    standard_transformations, 
    implicit_multiplication_application, 
    convert_xor,
)
from sympy import symbols, lambdify, simplify
from math import log2, ceil

#configurando transformações do símbolo de potência '^' e fator implícito ex: '3x'
transforms_syms = standard_transformations + (
    implicit_multiplication_application, convert_xor
)

x = symbols('x')

#cabeçalho
print( '=' * 30 + '\n   METODO DA BISSECÇÃO v2.0\n' + '=' * 30 + '\n')

#entradas do usuario
f_expr = input('f(x) = ')
a, b = map(float, input('interval in format [a,b]: ').strip('[]').split(','))
epsilon = float(simplify(input("E: ").replace('^', '**')))

expr = parse_expr(f_expr, transformations=transforms_syms)
f = lambdify(x, expr, "math")

#definindo previamente f(a) e f(b) para evitar cálculos desnecessários durante o loop
fa = f(a)
fb = f(b)


if fa * fb > 0:
    print(f'\nNão existe raiz garantida no intervalo [{a}, {b}]')

else:
    #maximo de iterações teoricamente calculados
    n_max = ceil(log2((b - a) / epsilon))
    print('')
    for n_iter in range(n_max):
        midpoint = (a + b) / 2
        fm = f(midpoint)

        print(f"{n_iter:3d} | a = {a: .6f} | b = {b: .6f} | m = {midpoint: .6f} | "
              f"f(a) = {fa: .6e} | f(b) = {fb: .6e} | f(m) = {fm: .6e}")

        if fm == 0:
            break

        if (b - a) / 2 < epsilon:
            break

        if fa * fm < 0:
            b = midpoint
            fb = fm
        else:
            a = midpoint
            fa = fm

    print(f'\nRaiz aproximada: {midpoint}')