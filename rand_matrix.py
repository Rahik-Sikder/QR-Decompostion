import random
from matrix import Matrix, Vector

def random_matrix(n):
    # Create a list of 200 random vectors
    vector_list = []
    for _ in range(n):
        nums = [random.uniform(-1, 1) for _ in range(n)]
        vector_list.append(Vector(nums))

    # Create the matrix from the list of vectors
    random_matrix = Matrix(vector_list)

    # Print the matrix
    return random_matrix


def hilbert_matrix(n):
    vectors = []
    for i in range(n):
        nums = []
        for j in range(n):
            nums.append(1 / (i + j - 1))
        vectors.append(Vector(nums))
    return Matrix(vectors)

    # # Example usage
    # n = 5
    # H = hilbert_matrix(n)
    # print("Hilbert Matrix of size {}x{}:".format(n, n))
    # H.print_matrix()

def regularized_hilbert_matrix(n, eps):
    H = hilbert_matrix(n)
    I = get_identity(n)
    
    # Add epsilon to the diagonal elements
    for i in range(n):
        I.matrix[i].vector[i] += eps
    
    # Compute H_eps = H + eps * I
    H_eps = Matrix([])
    for i in range(n):
        H_eps.matrix.append(H.get(i) + I.get(i))
    
    return H_eps

