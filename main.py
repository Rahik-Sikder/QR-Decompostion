from gram_schmidt import *
from householder import *
from matrix import *

def main():
    
    A = Matrix([Vector([1, 1, 1, 1]), Vector([0, 1, 1, 1]), Vector([0, 0, 1, 1])])

    # gram_schmidt(A)
    # print()
    # gram_schmidt_modified(A)

    Q, R = householder(A)
    print(f'This is R\n')
    R.print_matrix()
    print()

    print(f'This is Q\n')
    Q.print_matrix()
    print()


    

if __name__ == '__main__':
    main()