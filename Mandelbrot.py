import os
import numpy as np
from time import sleep
def color(r, g, b):
     return ('\x1b[48;2;' + str(r) + ';' + str(g) + ';' + str(b) + 'm')

def is_in_mandelbrot(c):
    z = complex(0, 0)
    iter = 0
    while z.imag**2 + z.real**2 < 16:
        z = z**2 + c
        iter += 1
        if iter > 25:
            return '*'
            # return color(255, 255, 255) + ' '
    # return color(0, 0, iter) + ' ' 
    return ' '

def scale(val, s1, e1, s2, e2):
    percentage = val/(e1 - s1)
    new_val = percentage * (e2 - s2) + s2
    return new_val


def drawPoint(x, y):
        x *= 2
        x += 1
        y += 1
        print("\033[" + str(y) + ";" + str(x) + "H ")

x_range = (-2.25, 0.75)
y_range = (-1.5, 1.5)

WIDTH = 169 
HEIGHT = 75

x_scale = np.linspace(x_range[0], x_range[1], int(WIDTH))
y_scale = np.linspace(y_range[0], y_range[1], int(HEIGHT))

matrix = [[complex(x,y) for x in x_scale] for y in y_scale]
mandelbrot_plane = [list(map(is_in_mandelbrot, i)) for i in matrix]

board = ""
for i in mandelbrot_plane:
    for j in i:
        board += j
    board += '\n'
        
text_file = open('mandelbrot_plane_no_color_{0}x{1}.txt'.format(int(WIDTH), int(HEIGHT)), 'w')
text_file.write(board)
# print(board)
# while True:pass


   

