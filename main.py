from gram_schmidt import gram_schmidt

def main():
    A = [[1,1,1], 
         [1,1,1], 
         [1,1,0],
         [1,0,0]]
    for row in A: 
        print(row)
    
    Q, R, ep = gram_schmidt(A)

    print("Q")
    for row in Q: 
        print(row)
    print("R")
    for row in R: 
        print(row)
    

if __name__ == '__main__':
    main()