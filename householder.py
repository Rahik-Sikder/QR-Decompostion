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
        # Don't need the column and rows that have alr been computed
        w = Vector(A.matrix[i].vector[i:]) 
        w.vector[0] -= w.vector_length() 
        wT = w.get_transpose()
        constant_term = 2 / dot_product(w, wT)

        # Instead of finding Rw and computing (Rw)(A), we'll apply wT and w to A individually
        for col in range(i, A.num_cols):
            # Grab the cur col, without the rows that have alr been computed
            cur_col_A = Vector(A.matrix[col].vector[i:])
            # This saves O(n) computation as the only difference between each row in the new vector
            # scalar, allowing us to "pre-process" the dot product
            unscaled_dot_prod = dot_product(cur_col_A, w)
            for row in range(i, A.num_rows):
                A.matrix[col].vector[row] -= constant_term * w.get(row - i) * unscaled_dot_prod

        print(f'This is RA for reflection {i}\n')
        A.print_matrix()
        print()
