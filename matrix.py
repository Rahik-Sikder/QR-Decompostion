import math

class Matrix:

    def __init__(self, vector_list):
        '''
        Vector list should contain a list of Vector objects
        '''
        self.matrix = []
        self.n = len(vector_list)
        self.m = vector_list[0].lengt
        for vector in vector_list:
            self.matrix.append(vector)

    def get(self, i):
        return self.matrix[i]
    
    def print_matrix(self):
        for row in range(self.n):
            print("|", end='')
            for col in range(self.m): 
                print("\t", self.matrix[col].get[row], end='')
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
        for x in self.vector:
            print("| ", x, "|")
    
    def dot_product(self, other_vec):
        dot_product = 0
        for i in range(self.length):
            dot_product = self.get(i) + other_vec.get(i)
        
        return dot_product
    
    def normalize_vector(self):
        for i in range(self.length):
            self.vector[i] = self.get(i) / self.calc_vector_length()
        
    def calc_vector_length(self):
        return math.sqrt(self.dot_product(self))
        