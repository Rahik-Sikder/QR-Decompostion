# For each of the three methods, find the smallest n such that ε⊥ > 0.9999 
# when applied to the n × n Hilbert matrix. If this is taking too much time, 
# just say you can’t find an n.

from gram_schmidt import gram_schmidt, gram_schmidt_modified
from householder import householder
from rand_matrix import *
from matrix import Matrix, Vector
import matplotlib.pyplot as plt
import math


# Run the three programs on some 200 × 200 matrices whose entries are randomly selected between −1
# and 1. Write down the average of ε⊥. How does this average compare?
def average_error_rand(n, num_times):
    gs_sum = 0
    modified_gs_sum = 0
    householder_qr_sum = 0

    # random matrix
    for i in range(num_times):  
        rand_matrix = random_matrix(200) # random matrix with entries from -1 to 1
        gs_sum += gram_schmidt(rand_matrix)[2]
        modified_gs_sum += gram_schmidt_modified(rand_matrix)[2]
        householder_qr_sum += householder(rand_matrix)[2]
    
    print("Average for Gram Schmidt from Part 1: ", gs_sum/num_times)
    print("Average for Modified Gram Schmidt from Part 2: ", modified_gs_sum/num_times)
    print("Average for Householder QR from Part 3: ", householder_qr_sum/num_times)
    

def average_error_hilbert(n, num_times):
    gs_sum = 0
    modified_gs_sum = 0
    householder_qr_sum = 0

    # random matrix
    for i in range(num_times):  
        rand_matrix = hilbert_matrix(200) # random matrix with entries from -1 to 1
        gs_sum += gram_schmidt(rand_matrix)[2]
        modified_gs_sum += gram_schmidt_modified(rand_matrix)[2]
        householder_qr_sum += householder(rand_matrix)[2]
        print("*", end="")
    
    print("Average for Gram Schmidt from Part 1: ", gs_sum/num_times)
    print("Average for Modified Gram Schmidt from Part 2: ", modified_gs_sum/num_times)
    print("Average for Householder QR from Part 3: ", householder_qr_sum/num_times)


def average_error_regularized_hilbert(n, num_times):
    gs_sum = 0
    modified_gs_sum = 0
    householder_qr_sum = 0

    # random matrix
    for i in range(num_times):  
        reg_hilbert_matrix = regularized_hilbert_matrix(200) # regularized hilbert matrix
        gs_sum += gram_schmidt(H)[2]
        modified_gs_sum += gram_schmidt_modified(H)[2]
        householder_qr_sum = householder(H)[2]
    
    print("Average for Gram Schmidt from Part 1: ", gs_sum/num_times)
    print("Average for Modified Gram Schmidt from Part 2: ", modified_gs_sum/num_times)
    print("Average for Householder QR from Part 3: ", householder_qr_sum/num_times)


def find_n_for_error_threshold(error_threshold, method):
    n = 2
    while True:
        H = hilbert_matrix(n)
        if method == "gram_schmidt":
            Q, R, error_perp, error_s = gram_schmidt(H)
        elif method == "gram_schmidt_modified":
            Q, R, error_perp, error_s = gram_schmidt_modified(H)
        elif method == "householder":
            Q, R, error_perp, error_s = householder(H)
        else:
            raise ValueError("Invalid method name")

        I = Matrix([Vector([1 if i == j else 0 for j in range(n)]) for i in range(n)])
        error = max(abs(Q.tranpose() * Q - I))
        if error > error_threshold:
            break
        n += 1
    print("The smallest n for us to get the desired value based on our threshhold is ", n)


def q8_e_perp():
    x = [i for i in range(2 , 101)]
    y1 = [] # gram_schmidt
    y2 = [] # mod_gram_schmidt
    y3 = [] # householder
    for i in range (2, 101):
        RH = regularized_hilbert_matrix(i)
        y1.append(math.log(gram_schmidt(RH)[2]))
        y2.append(math.log(gram_schmidt_modified(RH)[2]))
        y3.append(math.log(householder(RH)[2]))
    
    plt.plot(x, y1, label="Gram Schmidt")
    # plt.plot(x, y2, label="Modified Gram Schmidt")
    plt.plot(x, y3, label="Householder")
    # naming the x axis
    plt.xlabel('n')
    # naming the y axis
    plt.ylabel('E PERP')
    # giving a title to my graph
    plt.title('E PERP')
 
    # show a legend on the plot
    plt.legend()

    plt.show()

def q8_e_s():
    x = [i for i in range(2 , 101)]
    y1 = [] # gram_schmidt
    y2 = [] # mod_gram_schmidt
    y3 = [] # householder
    for i in range (2, 101):
        RH = regularized_hilbert_matrix(i)
        y1.append(math.log(gram_schmidt(RH)[3]))
        y2.append(math.log(gram_schmidt_modified(RH)[3]))
        y3.append(math.log(householder(RH)[3]))
    plt.plot(x, y1, label="Gram Schmidt")
    plt.plot(x, y2, label="Modified Gram Schmidt")
    plt.plot(x, y3, label="Householder")

    # naming the x axis
    plt.xlabel('n')
    # naming the y axis
    plt.ylabel('E S')
    # giving a title to my graph
    plt.title('E S')
 
    # show a legend on the plot
    plt.legend()
    plt.show()


if __name__ == "__main__":
    error_threshold = 0.9999
    print(f"Smallest n for Gram-Schmidt such that error > {error_threshold}: {find_n_for_error_threshold(error_threshold, 'gram_schmidt')}")
    print(f"Smallest n for Modified Gram-Schmidt such that error > {error_threshold}: {find_n_for_error_threshold(error_threshold, 'gram_schmidt_modified')}")
    print(f"Smallest n for Householder such that error > {error_threshold}: {find_n_for_error_threshold(error_threshold, 'householder')}")
