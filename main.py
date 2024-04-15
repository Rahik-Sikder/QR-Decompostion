from gram_schmidt import gram_schmidt
from matrix import Matrix
from matrix import Vector

def main():
    
    A = Matrix([Vector([1, 1, 1, 1]), Vector([0, 1, 1, 1]), Vector([0, 0, 1, 1])])

    gram_schmidt(A)

    

if __name__ == '__main__':
    main()