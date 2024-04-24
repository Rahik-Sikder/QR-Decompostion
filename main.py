from gram_schmidt import *
from householder import *
from matrix import *
from experiments import *

def main():
    # sample_run()
    average_error_rand(200, 10)
    # find_n_for_error_threshold(.9999, "gram_schmidt")
    # find_n_for_error_threshold(.9999, "gram_schmidt_modified")
    # find_n_for_error_threshold(.9999, "householder")
    # plot_e_perp()
    # plot_e_s()
    pass
    


def sample_run():
    A = Matrix([Vector([1, 1, 1, 1]), Vector([0, 1, 1, 1]), Vector([0, 0, 1, 1])])

    Q, R, error_perp, error_s = gram_schmidt(A)
    print("This is Q from naive Gram-Schmidt\n")
    Q.print_matrix()
    print(f'This is R from naive Gram-Schmidt\n')
    R.print_matrix()
    print("Error perp: ", error_perp)
    print("Error s: ", error_s)
    print("\n")

    Q, R, error_perp, error_s = gram_schmidt_modified(A)
    print("This is Q from modified Gram-Schmidt\n")
    Q.print_matrix()
    print(f'This is R from modified Gram-Schmidt\n')
    R.print_matrix()
    print("Error perp: ", error_perp)
    print("Error s: ", error_s)
    print("\n")


    # TODO: Ask TA about what "truncate Q and R as described in Homework 7, Q3" means
    Q, R, error_perp, error_s = householder(A)
    print(f'This is Q from Householder\n')
    Q.print_matrix()
    print(f'This is R from Householder\n')
    R.print_matrix()
    print("Error perp: ", error_perp)
    print("Error s: ", error_s)
    print("\n")

    print('Matrix Multiplication')
    B = Matrix([Vector([1, 1, 1]), Vector([0, 1, 1]), Vector([0, 0, 1])])
    C = matrix_multiply(A,B)
    C.print_matrix()

if __name__ == '__main__':
    main()