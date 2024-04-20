from gram_schmidt import *
from householder import *
from matrix import *

def main():
    
    A = Matrix([Vector([1, 1, 1, 1]), Vector([0, 1, 1, 1]), Vector([0, 0, 1, 1])])

    Q = gram_schmidt(A)
    print("This is Q from naive Gram-Schmidt\n")
    Q.print_matrix()

    Q = gram_schmidt_modified(A)
    print("This is Q from modified Gram-Schmidt\n")
    Q.print_matrix()

    # TODO: Ask TA about what "truncate Q and R as described in Homework 7, Q3" means
    Q, R = householder(A)

    print(f'This is Q from Householder\n')
    Q.print_matrix()

    print(f'This is R from Householder\n')
    R.print_matrix()


    

if __name__ == '__main__':
    main()