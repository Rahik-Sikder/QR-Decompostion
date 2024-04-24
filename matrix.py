import math
from typing import List # Types are cool, don't ask why I'm using python

class Vector:

    def __init__(self, nums):
        self.vector = []
        self.length = len(nums)
        for x in nums:
            self.vector.append(x)
    
    def get(self, i):
        return self.vector[i]

    def print_vector(self):
        print("")
        for x in self.vector:
            print("| ", x, "\t|")
        print("")
    
    def dot_product(self, other_vec):
        dot_product = 0
        for i in range(self.length):
            dot_product += self.get(i) * other_vec.get(i)
        return dot_product
    
    def normalize_vector(self):
        vector_length = self.vector_length()
        for i in range(self.length):
            self.vector[i] = self.get(i) / vector_length
        return self
        
    def vector_length(self):
        return math.sqrt(self.dot_product(self))

    def subtract(self, other_vec):
        for i in range(self.length):
            self.vector[i] = self.get(i) - other_vec.get(i)
        return self
        
    def scalar_multiply(self, scalar):
        for i in range(self.length):
            self.vector[i] *= scalar
        return self

    def __sub__(self, other):
        # Subtraction creates new object
        res = Vector(self.vector)
        for i in range(res.length):
            res.vector[i] = res.get(i) - other.get(i)
        return res
    
    def __add__(self, other):
        # Addition creates new object
        res = Vector(self.vector)
        for i in range(res.length):
            res.vector[i] = res.get(i) + other.get(i)
        return res

class Matrix:

    def __init__(self, vector_list: List[Vector]):
        '''
        Vector list should contain a list of Vector objects
        '''
        self.matrix: List[Vector] = []
        self.num_rows = vector_list[0].length
        self.num_cols = len(vector_list)
        for vector in vector_list:
            self.matrix.append(vector)

    def get(self, i):
        # Return a new Vector object
        return Vector(self.matrix[i].vector)
    
    def get_row(self, i):
        return Vector([ self.matrix[col].vector[i] for col in range(self.num_cols) ])
    
    def print_matrix(self):
        for row in range(self.num_rows):
            print("|", end='')
            for col in range(self.num_cols): 
                print("" if col == 0 else "\t\t", '%.5f'%(self.matrix[col].get(row)), end='')
            print(" |", end='\n\n')
        print()
    
    def scalar_multiply(self, scalar):
        for vector in self.matrix:
            vector.scalar_multiply(scalar)
        return self

    def tranpose(self):
        new_vector_list = []
        for i in range(self.num_rows):
            new_vector_list.append(self.get_row(i))
        self.matrix = new_vector_list
        return self
    
    def __sub__(self, other):
        # Subtraction creates new object
        vector_list = []
        for i in range(self.num_cols):
            vector_list.append(self.matrix[i] - other.matrix[i])
        return Matrix(vector_list)
    
    def __add__(self, other):
        # Addition creates new object
        vector_list = []
        for i in range(self.num_cols):
            vector_list.append(self.matrix[i] + other.matrix[i])
        return Matrix(vector_list)
        

# Matrix operations that return a new object

def scalar_multiply(scalar, vector):
    # Scalar multiply creates new object
        res = Vector(vector.vector)
        for i in range(res.length):
            res.vector[i] *= scalar
        return res

def dot_product(vector_a, vector_b):
    dot_product = 0
    for i in range(vector_a.length):
        dot_product += vector_a.get(i) * vector_b.get(i)
    return dot_product

def get_identity(n):
    vectors = []
    for i in range(n):
        list = [0] * n
        list[i] = 1
        vectors.append(Vector(list))
    return Matrix(vectors)
