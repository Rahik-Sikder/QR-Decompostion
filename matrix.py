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
        vector_length = self.calc_vector_length()
        print("Normalizing vector, here is length: ", vector_length)
        for i in range(self.length):
            self.vector[i] = self.get(i) / vector_length
        return self
        
    def calc_vector_length(self):
        print("self dot product is ", self.dot_product(self))
        return math.sqrt(self.dot_product(self))

    def subtract(self, other_vec):
        for i in range(self.length):
            self.vector[i] = self.get(i) - other_vec.get(i)
        
    def scalar_multiply(self, scalar):
        for i in range(self.length):
            self.vector[i] *= scalar
        return self