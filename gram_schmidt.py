from matrix import *


def gram_schmidt(basis_matrix: Matrix):

    # Create list of orthonormal colums
    ON_cols = []

    for i in range(0, basis_matrix.num_cols):

        # Get column vector of the arbitrary basis matrix
        ortho_col = basis_matrix.get(i)

        # Find terms to subtract
        terms = []
        for q_vector in ON_cols:
            terms.append(
                scalar_multiply(
                    dot_product(q_vector, basis_matrix.get(i)), q_vector
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

    return Matrix(ON_cols)


def gram_schmidt_modified(basis_matrix):

    # Create list of orthonormal colums
    ON_cols = []

    for i in range(0, basis_matrix.num_cols):

        # Get column vector of the arbitrary basis matrix
        ortho_col = basis_matrix.get(i)

        # Subtract project of col onto all q from ON from col
        for q in ON_cols:
            q_vector = Vector(q.vector)
            ortho_col.subtract(q_vector.scalar_multiply(q_vector.dot_product(basis_matrix.get(i))))

        # Normalize orthogonal column
        ortho_col.normalize_vector()

        # append to the list
        ON_cols.append(ortho_col)

    return Matrix(ON_cols)
