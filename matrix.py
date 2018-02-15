import math


def print_matrix( matrix ):
    for row in matrix:
        #print row
        for col in row:
            print col,
        print ""
    print ""

def ident( matrix ):
    size = len(matrix)
    #print size
    for i in range(size):
        matrix[i][i] = 1
        #print matrix

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    #print len(m1)
    #print len(m2[0])
    ans = new_matrix(len(m2[0]), len(m1))#new_matrix function swapped?
    for row_m1 in range(len(m1)):
        for col_m2 in range(len(m2[0])):
            for row_m2 in range(len(m2)):
                ans[row_m1][col_m2] += m1[row_m1][row_m2] * m2[row_m2][col_m2]
    #print_matrix(ans)
    #m2 = new_matrix(len(ans[0]), len(ans))
    #print_matrix(m2)
    for row in range(len(ans)):
        for col in range(len(ans[0])):
            #print ans[row][col]
            m2[row][col] = ans[row][col]
            #print m2[row][col]
    #return m2



def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
