from gram_schmidt import *
from householder import *
from matrix import *

def main():
    
    A = Matrix([Vector([1, 1, 1, 1]), Vector([0, 1, 1, 1]), Vector([0, 0, 1, 1])])

    # gram_schmidt(A)
    # print()
    # gram_schmidt_modified(A)

    householder(A)


    

if __name__ == '__main__':
    main()