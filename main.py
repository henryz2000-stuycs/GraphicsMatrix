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

draw_lines(edges, screen, color)
#draw_lines(Y, screen, color)
#draw_lines( matrix, screen, color )
display(screen)
