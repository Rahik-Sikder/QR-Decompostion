from matrix import Matrix
from matrix import Vector


def gram_schmidt(basis_matrix):

    # Create list of orthonormal colums
    ON_cols = []

    basis_matrix.print_matrix()

    print("This is the type Vector ", isinstance(basis_matrix.get(0), Vector))

    
    for i in range(0, basis_matrix.num_cols):
        
        # Get column vector of the arbitrary basis matrix
        original_col = basis_matrix.get(i)
        ortho_col = basis_matrix.get(i)

        # Subtract project of col onto all q from ON from col
        for q in ON_cols:
            temp_q = Vector(q.vector)
            
            ortho_col.subtract(temp_q.scalar_multiply(temp_q.dot_product(original_col)))
            print("Modifying col ", i+1, " which is")
            ortho_col.print_vector()
     
        # Normalize orthogonal column 
        ortho_col.normalize_vector()

        # append to the list
        ON_cols.append(ortho_col)

        

        print("Length of ON: ", len(ON_cols))
        for q in ON_cols:
            q.print_vector()
        print()

    print("This is ON_Cols")

    for q in ON_cols:
        q.print_vector()
    
    print("This is Q")
    Q = Matrix(ON_cols)
    Q.print_matrix()

            


     
   


















# # implementation of gram schmidt algorithm

# def gram_schmidt(A):

#     # Extract columns from A
    
    

#     # step 1: normalize the first column
#     # step 2: next column is arbitrary vector - (<arbitrary vector,orthonormal vector before it>/<orth vector before it,orth vector before it>) x arbitrary basis vector
#     # step 3: normalize that column to get the next u


#     '''
#     Write a program to perform Gram–Schmidt on an n × k matrix A, i.e. perform the following procedure
#     for i = 1, · · · , k.
#     vi ← vi − (q1 · vi)q1 − · · · − (qi−1 · vi)qi−1
#     qi ← vi/∥vi∥
#     The matrix Q is [q1 · · · qk]. Compute R using R = QT A. Output the matrices Q and R, as well as the
#     two errors ε⊥, εs.
#     (Make sure you are not accidentally doing the modification described in the following part. This could
#     happen from passing by reference.)
#     '''
#     n, k = len(A), len(A[0])
#     Q = [[0.0 for _ in range(k)] for _ in range(n)]
#     R = [[0.0 for _ in range(k)] for _ in range(k)]

#     for i in range(k):
#         # Compute vi = A[i]
#         vi = [row[i] for row in A]

#         # Compute (q1 · vi)q1 + ... + (qi-1 · vi)qi-1
#         for j in range(i):
#             R[j][i] = sum(q * v for q, v in zip(Q[j], vi))
#             vi = [v - R[j][i] * q for v, q in zip(vi, Q[j])]

#         # Normalize vi to get qi
#         norm_vi = sum(v ** 2 for v in vi) ** 0.5
#         if norm_vi > 1e-10:
#             Q[i] = [v / norm_vi for v in vi]
#             R[i][i] = norm_vi
#         else:
#             Q[i] = [0.0 for _ in range(n)]
#             R[i][i] = 0.0

#     # Compute the errors
#     epsilon_perp = sum((sum((a - sum(q * r for q, r in zip(q, a_row))) ** 2 for a_row, q in zip(A, Q))) ** 0.5) / sum(sum(a ** 2 for a in row) ** 0.5 for row in A)
#     epsilon_s = sum((sum((sum(q * q_ for q, q_ in zip(Q[j], Q[i])) - (i == j))) ** 2 for i in range(k))) ** 0.5 / k ** 0.5

#     return Q, R, epsilon_perp, epsilon_s


