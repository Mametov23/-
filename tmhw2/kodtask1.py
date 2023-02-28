import numpy as np
import sympy as sp
from sympy import Symbol, Ellipse, Point, Line, symbols, Eq, solve

Ra, Rax,Ray, Rbx, Rby, Rcx, Rcy, Rex, Rey, Rd, Rfy = symbols('Ra Rax Ray Rbx Rby Rcx Rcy Rex Rey Rd Rfy',
                                                                  real=True)

Rax = Ra*np.cos(np.pi/4)
Ray = Ra*np.sin(np.pi/4)

P1 = 12
P2 = 18
M1 = 36
q = 1.4

equal = [
       Eq(Rax+ Rbx - Rcx),
       Eq(Ray+ Rby - Rcy - P1 - q * 3),
       Eq(-P1*2 + Rby * 4 + Rcy *7 -q*3*1.5),
       Eq(Rcx - Rex),
       Eq(Rcy - Rey -Rd+q*4.5),
       Eq(Rd*2.5+Rey*4.5-q*4.5*(4.5/2)),
       Eq(Rex - P2*np.cos(np.pi/4)),
       Eq(Rey+P2*np.cos(np.pi/4)+Rfy),
       Eq(M1+2.5*P2*np.cos(np.pi/4)+Rfy*4.5)
          ]
otvet = solve(equal, (Rax, Ray, Rbx, Rby, Rcx, Rcy, Rex, Rey, Rd, Rfy))
print(otvet)