import math
class Matrix:

    def __init__(self, vector_list):
        '''
        Vector list should contain a list of Vector objects
        '''
        self.matrix = []
        self.num_rows = vector_list[0].length
        self.num_cols = len(vector_list)
        for vector in vector_list:
            self.matrix.append(vector)

    def get(self, i):
        # Return a new Vector object
        return Vector(self.matrix[i].vector)
    
    def print_matrix(self):
        for row in range(self.num_rows):
            print("|", end='')
            for col in range(self.num_cols): 
                print("\t", self.matrix[col].get(row), end='')
            print("|", end='\n')
    
    def scalar_multiply(self, scalar):
        for vector in self.matrix:
            vector.scalar_multiply(scalar)
        return self

            


class Vector:

    def __init__(self, nums, isTranspose=False):
        self.vector = []
        self.length = len(nums)
        self.isTranspose = isTranspose
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
        # Subtraction modifies object
        for i in range(self.length):
            self.vector[i] = self.get(i) - other_vec.get(i)
        
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
  
def vector_multiply(vector_a, vector_b):
    if (vector_a.isTranspose and not vector_b.isTranspose) or (not vector_a.isTranspose and vector_b.isTranspose):
        raise Exception("Matrix Multiply Error")

    if(vector_a.isTranspose): return dot_product(vector_a, vector_b)
    
    vector_list = []
    #vvT
    for val_b in vector_b.vector:
        nums = []
        for val_a in vector_a.vector:
            nums.append(val_a * val_b)
        vector_list.append(Vector(nums))
    
    return Matrix(vector_list)
