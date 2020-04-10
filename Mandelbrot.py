import os
import numpy as np
from functools import reduce
# Output Image Size
WIDTH = 2.253 * 75 #169
HEIGHT = 1 * 75 #75

def color(r, g, b):
     return '\x1b[48;2;{0};{1};{2}m'.format(r, g, b)

def is_in_mandelbrot(c):
    z = complex(0, 0)
    iter = 0
    while z.imag**2 + z.real**2 < 16:
        z = z**2 + c
        iter += 1
        if iter > 25:
            # return '*' # uncomment this line to print it to text
            return color(255, 255, 255) + ' '
    return color(0, 0, iter) + ' ' 
    
    # return ' ' # uncomment this line to print it to text

def scale(val, s1, e1, s2, e2):
    percentage = val/(e1 - s1)
    new_val = percentage * (e2 - s2) + s2
    return new_val


x_range = (-2.25, 0.75)
y_range = (-1.5, 1.5)

x_scale = np.linspace(x_range[0], x_range[1], int(WIDTH))
y_scale = np.linspace(y_range[0], y_range[1], int(HEIGHT))

mandelbrot_plane = [[is_in_mandelbrot(complex(x,y)) for x in x_scale] for y in y_scale]
stripes = [reduce((lambda x, y: x + y), l) for l in mandelbrot_plane]
board = reduce((lambda x, y: x + y + '\n'), stripes)

# uncomment these line to print it to text
# text_file = open('mandelbrot_plane_no_color_{0}x{1}.txt'.format(int(WIDTH), int(HEIGHT)), 'w')
# text_file.write(board)

print(board)
while True:pass


   

