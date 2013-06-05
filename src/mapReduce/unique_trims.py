import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    nucleotide = record[1]
    mr.emit_intermediate(nucleotide[:-10], 1) # trim last 10 chars
    
def reducer(key, list_of_values):
    mr.emit(key)
    

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
