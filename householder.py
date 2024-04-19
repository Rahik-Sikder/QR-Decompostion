from matrix import *


def householder(A: Matrix):
    '''
    Explaination: uhhh

    '''

    # Initialize two Identity matries. The second will become QT
    I: Matrix = get_identity()
    B: Matrix = get_identity()

    # Collection of matricies Rwi, where H = (Rw1)(...)(Rwn)
    H = []

    # Run through each column of A
    for i in range(0, A.num_cols):

        col_vector = A.get(i)
        e = I.get(i)

        # Find a matrix w to reflect our col_vectro across
        # Use the length * std basis vector to find w
        w = col_vector - scalar_multiply(col_vector.length, e)

        # Reflect
        

