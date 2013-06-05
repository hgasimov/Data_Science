import MapReduce
import sys

"""
Implement a relational join
"""

mr = MapReduce.MapReduce()

def mapper(record):
    orderID = record[1]
    mr.emit_intermediate(orderID, record)

def reducer(key, list_of_values):
    # separate order and line_item rows
    order, line_item = [], []
    for row in list_of_values:
        if row[0] == 'order':
            order.append(row)
        else:
            line_item.append(row)
    
    # do cross product
    for row_order in order:
        for row_line_item in line_item:
            mr.emit(row_order + row_line_item)


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
