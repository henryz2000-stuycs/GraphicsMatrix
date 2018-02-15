from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

print_matrix(matrix)
ident(matrix)
print_matrix(matrix)

X = [[11,12,13],[14,15,16],[17,18,19]]
Y = [[1,2],[3,4],[5,6]]

matrix_mult(X, Y)
print_matrix(Y)

add_point(Y, 1, 2, 3)
print_matrix(Y)
add_edge(Y, 1, 2, 3, 4, 5, 6)
print_matrix(Y)

edges = new_matrix(4, 4)
add_edge(edges, 50, 450, 0, 100, 450, 0)
add_edge(edges, 50, 450, 0, 50, 400, 0)
add_edge(edges, 100, 450, 0, 100, 400, 0)
add_edge(edges, 100, 400, 0, 50, 400, 0)

add_edge(edges, 200, 450, 0, 250, 450, 0)
add_edge(edges, 200, 450, 0, 200, 400, 0)
add_edge(edges, 250, 450, 0, 250, 400, 0)
add_edge(edges, 250, 400, 0, 200, 400, 0)

add_edge(edges, 150, 400, 0, 130, 360, 0)
add_edge(edges, 150, 400, 0, 170, 360, 0)
add_edge(edges, 130, 360, 0, 170, 360, 0)

add_edge(edges, 100, 340, 0, 200, 340, 0)
add_edge(edges, 100, 320, 0, 200, 320, 0)
add_edge(edges, 100, 340, 0, 100, 320, 0)
add_edge(edges, 200, 340, 0, 200, 320, 0)

'''
green1 = new_matrix(4,4)
for i in range(250):
    add_edge(green1, 0, i, 0, i, i, 0)
draw_lines(green1, screen, color)

green2 = new_matrix(4,4)
color = [0, 220, 0]
for i in range(250):
    add_edge(green2, i, 0, 0, i, i, 0)
draw_lines(green2, screen, color)

green3 = new_matrix(4,4)
color = [0, 185, 0]
for i in range(250):
    add_edge(green3, 0, i+250, 0, i, i+250, 0)
draw_lines(green3, screen, color)

green4 = new_matrix(4,4)
color = [0, 150, 0]
for i in range(250):
    add_edge(green4, i+250, 0, 0, i+250, i, 0)
draw_lines(green4, screen, color)

green5 = new_matrix(4,4)
color = [0, 115, 0]
for i in range(250):
    add_edge(green5, 250, i, 0, i+250, i, 0)
draw_lines(green5, screen, color)

green6 = new_matrix(4,4)
color = [0, 80, 0]
for i in range(250):
    add_edge(green6, i, 250, 0, i, i+250, 0)
draw_lines(green6, screen, color)

green7 = new_matrix(4,4)
color = [0, 45, 0]
for i in range(250):
    add_edge(green7, 250, i+250, 0, i+250, i+250, 0)
draw_lines(green7, screen, color)

green8 = new_matrix(4,4)
color = [0, 10, 0]
for i in range(250):
    add_edge(green8, i+250, 250, 0, i+250, i+250, 0)
draw_lines(green8, screen, color)
'''

#draw_lines(gallery, screen, color)
draw_lines(edges, screen, color)
#draw_lines(Y, screen, color)
#draw_lines( matrix, screen, color )
display(screen)
save_extension(screen, 'img.png')
