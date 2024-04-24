from matrix import *
import math


def gram_schmidt(A: Matrix):

    # Create list of orthonormal colums
    ON_cols = []

    for i in range(0, A.num_cols):

        # Get column vector of the arbitrary basis matrix
        ortho_col = A.get(i)

        # Find terms to subtract
        terms = []
        for q_vector in ON_cols:
            terms.append(
                scalar_multiply(
                    dot_product(q_vector, A.get(i)), q_vector
                )
            )
        # Subtract terms from basis matrix column
        for term in terms:
            # Creates a new object each time
            ortho_col = ortho_col - term

        # Normalize orthogonal column
        ortho_col.normalize_vector()

        # append to the list
        ON_cols.append(ortho_col)

    Q = Matrix(ON_cols)
    QT = Matrix(ON_cols).tranpose()
    R = matrix_multiply(QT, A)
    QR = matrix_multiply(Q, R)

    I = get_identity(Q.num_cols)
    error_perp = get_abs_max(matrix_multiply(QT, Q) - I)
    error_s = get_abs_max(A - QR)

    return (Q, R, error_perp, error_s)


def gram_schmidt_modified(A):

    # Create list of orthonormal colums
    ON_cols = []

    for i in range(0, A.num_cols):

        # Get column vector of the arbitrary basis matrix
        ortho_col = A.get(i)

        # Subtract project of col onto all q from ON from col
        for q in ON_cols:
            q_vector = Vector(q.vector)
            ortho_col.subtract(q_vector.scalar_multiply(q_vector.dot_product(ortho_col)))

        # Normalize orthogonal column
        ortho_col.normalize_vector()

        # append to the list
        ON_cols.append(ortho_col)

    Q = Matrix(ON_cols)
    QT = Matrix(ON_cols).tranpose()
    R = matrix_multiply(QT, A)
    QR = matrix_multiply(Q, R)

    I = get_identity(Q.num_cols)
    error_perp = get_abs_max(matrix_multiply(QT, Q) - I)
    error_s = get_abs_max(A - QR)

    return (Q, R, error_perp, error_s)
