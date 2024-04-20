from matrix import *


def householder(A: Matrix):
    '''
    Explaination: 

    '''

    # Initialize two Identity matries. The second will become QT
    I: Matrix = get_identity(A.num_rows)
    B: Matrix = get_identity(A.num_rows)

    # Collection of matricies Rwi, where H = (Rw1)(...)(Rwn)
    H = []

    # Run through each column of A
    for i in range(0, A.num_cols):

        # Find a matrix w to reflect our col_vector across
        # Use the length * std basis vector to find w

        w = Vector(A.matrix[i].vector[i:])
        w.vector[0] -= w.vector_length() 
        wT = w.get_transpose()
        constant_term = 2 / dot_product(w, wT)

        # Instead of finding Rw and computing (Rw)(A), we'll apply wT and w to A individually
        for col in range(i, A.num_cols):
            cur_col_A = Vector(A.matrix[col].vector[i:])
            for row in range(i, A.num_rows):
                cur_row_Rw = scalar_multiply(w.get(row - i), w)
                A.matrix[col].vector[row] -= constant_term * dot_product(cur_col_A, cur_row_Rw)

        print(f'This is RA for reflection {i}\n')
        A.print_matrix()
        print()
