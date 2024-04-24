import random
from matrix import Matrix, Vector

def random_matrix(n):
    # Create a list of 200 random vectors
    vector_list = []
    for _ in range(n):
        nums = [random.uniform(-1, 1) for _ in range(n)]
        vector_list.append(Vector(nums))

    # Create the matrix from the list of vectors
    return Matrix(vector_list)

def hilbert_matrix(n):
    vectors = []
    for i in range(n):
        nums = []
        for j in range(n):
            nums.append(1 / (i + j - 1))
        vectors.append(Vector(nums))
    return Matrix(vectors)

def get_identity(n):
    vectors = []
    for i in range(n):
        list = [0] * n
        list[i] = 1
        vectors.append(Vector(list))
    return Matrix(vectors)


def regularized_hilbert_matrix(n):
    H = hilbert_matrix(n)
    I = get_identity(n)
    
    # Add epsilon to the diagonal elements
    for i in range(n):
        I.matrix[i].vector[i] += 0.0001
    
    # Compute H_eps = H + eps * I
    H_eps = Matrix([])
    for i in range(n):
        H_eps.matrix.append(H.get(i) + I.get(i))
    
    return H_eps

