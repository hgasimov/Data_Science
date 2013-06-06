import MapReduce
import sys

'''
    Multiply 2 matrices A x B 
    A: [5 x 5]
    B: [5 x 5]
'''

N = 5 # number of rows in A
M = 5 # number of columns in B

mr = MapReduce.MapReduce()

def mapper(record):
    table = record[0]
    i, j = record[1], record[2]
    value = record[3] 
    if table == 'a':
        for k in range(M):
            mr.emit_intermediate((i, k), (table, j, value))
    else:
        for k in range(N):
            mr.emit_intermediate((k, j), (table, i, value))
    
def reducer(key, list_of_values):
    A, B = {}, {}
    for cell in list_of_values:
        if cell[0] == 'a': 
            A[cell[1]] = cell[2]
        else:
            B[cell[1]] = cell[2]
    
    msum = 0
    for row in A:
        if row in B:
            msum += A[row] * B[row]
                
    mr.emit((key[0], key[1], msum))
    

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
