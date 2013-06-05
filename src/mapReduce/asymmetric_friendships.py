import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    mr.emit_intermediate(record[0], record[1])
    mr.emit_intermediate(record[1], record[0])
    
def reducer(key, list_of_friends):
    # find the elements with no duplicates in the list 
    s = set([])    
    for friend in list_of_friends:
        if friend in s:
            s.remove(friend)
        else:
            s.add(friend)
    
    # emit asymmetrix friendships (friend1, friend2)
    # (friend2, friend1) will be emitted by the reducer(friend2, list_of friends)
    for friend in s:
        mr.emit((key, friend))

if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
