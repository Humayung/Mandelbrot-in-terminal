import os
import numpy as np
from functools import reduce
import math
# Output Image Size
WIDTH = 2.253 * 75 #169
HEIGHT = 1 * 75 #75

on_terminal = True

def color(r, g, b):
     return '\x1b[48;2;{0};{1};{2}m'.format(r, g, b)

def is_in_mandelbrot(c):
    z = complex(0, 0)
    iter = 0
    for i in range(256):
        z = z**2 + c
        if abs(z) > 2:
            return color(0, i, i) + ' ' if on_terminal else ' '
    color_ = int((abs(z) * 255)/2)
    return color(0, color_,color_ ) + ' ' if on_terminal else '*'

x_bounds = (-2.25, 0.75)
y_bounds = (-1.5, 1.5)

x_scale = np.linspace(x_bounds[0], x_bounds[1], int(WIDTH))
y_scale = np.linspace(y_bounds[0], y_bounds[1], int(HEIGHT))

board = ""
for y in y_scale:
    for x in x_scale:
        board += is_in_mandelbrot(complex(x,y))
    board += '\n'

if not on_terminal:
    text_file = open('mandelbrot_plane_no_color_{0}x{1}.txt'.format(int(WIDTH), int(HEIGHT)), 'w')
    text_file.write(board)

print(board)
while True:pass

   

