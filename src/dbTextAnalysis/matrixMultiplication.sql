select SUM(A.value * B.value) from A, B 
where A.row_num = 2 and B.col_num = 3 and A.col_num = B.row_num;