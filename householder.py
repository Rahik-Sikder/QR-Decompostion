from matrix import *


def householder(input_A: Matrix):
    '''
    Explaination: 
    
    Typically Householder reflection is done by first computing Rw using ith column (i is also the 
    current iteration) of A and then finding A_i+1 through multiplying Rw with A. Matrix 
    multiplication, however, can cause each step of a naive implementation to take O(n^3) time to 
    process. 

    To get around this, we can exploit the matrix wwT and prematurely multiply it into A. 
    To do this, first notice that any element in (wwT)(A) is a dot product formed by a row of wwT 
    and a column of A -> this is just how matrix multiplcation works. 
    
    From there, we can see that any row of wwT is equivalent to w multiplied by the scalar from wT 
    at the column we are trying to find. When finding the values for any column v of A_i+1, we can
    find the dot product of v and w before iterating through each row of v, allowing the 
    computation of v to be in O(n) as each row is just the found dot product * corresponding row 
    in w. 
    
    There are other constant terms in the Householder reflection such as 2 / wTw, but this can be
    found ahead of time. Additionally since RwA = A - (2 / wTw) (wwT) (A), having now computed
    (2 / wTw) (wwT) (A), we can immediately subtract each element from A and perform the entire
    computation of RwA in place. 

    To find Q, whenever we apply any transformation to A, we can do the same on an I. Eventually,
    that I will become QT, which can be turned into Q.

    '''

    A = Matrix([Vector(input_A.matrix[col].vector) for col in range(input_A.num_cols)])
    

    # Initialize an Identity matrix B to become QT
    B: Matrix = get_identity(A.num_rows)

    # Run through each column of A
    for i in range(0, A.num_cols):

        # Find a matrix w to reflect our col_vector across 
        # Don't need the column and rows that have alr been computed
        w = Vector(A.matrix[i].vector[i:]) 
        w.vector[0] -= w.vector_length() 
        constant_term = 2 / dot_product(w, w) # No need for explicitly defining a transpose

        # Instead of finding Rw and computing (Rw)(A), we'll apply wT and w to A individually
        for col in range(0, A.num_cols):
            # Grab the cur col, without the rows that have alr been computed
            cur_col_A = Vector(A.matrix[col].vector[i:])
            cur_col_B = Vector(B.matrix[col].vector[i:])

            # This saves O(n) computation as the only difference between each row in the new vector
            # scalar, allowing us to "pre-process" the dot product
            unscaled_dot_prod = dot_product(cur_col_A, w)
            unscaled_dot_prod_B = dot_product(cur_col_B, w)

            for row in range(i, A.num_rows):
                # print("adjusting row ", row, " and column ", col)
                A.matrix[col].vector[row] -= constant_term * w.get(row - i) * unscaled_dot_prod
                B.matrix[col].vector[row] -= constant_term * w.get(row - i) * unscaled_dot_prod_B

        # Account for possibility that B has more cols than A
        for col in range(A.num_cols, B.num_cols):

            cur_col_B = Vector(B.matrix[col].vector[i:])
            unscaled_dot_prod_B = dot_product(cur_col_B, w)

            for row in range(i, B.num_rows):
                # print("adjusting row ", row, " and column ", col)
                B.matrix[col].vector[row] -= constant_term * w.get(row - i) * unscaled_dot_prod_B

        # For Debugging purposes
        # print(f'This is RA for reflection {i}\n')
        # A.print_matrix()
        # print()

        # print(f'This is B currently for reflection {i}\n')
        # B.print_matrix()
        # print()

    # Q = BT 
    # Also here Q is just given the reference to B after B modifies itself with transpose()
    Q = Matrix(B.tranpose().matrix[:A.num_cols]) # truncation
    QT = Matrix(Q.matrix).tranpose()
    R = matrix_multiply(QT, A)
    QR = matrix_multiply(Q, R)

    I = get_identity(Q.num_cols)
    error_perp = get_abs_max(matrix_multiply(QT, Q) - I)
    error_a = get_abs_max(A - QR)

    return (Q, R, error_perp, error_a)


    