from la_toolkit.vectors import dot_product


# remember to add exceptions for invalid inputs
a = [
    [1,2],
    [3,4]
]

v = [5,6]

b = [
    [5,6]
]

def MV_multiplication(m: list, n: list) -> list: 
    if len(m[0]) != len(n):
        raise ValueError("matrix and vector with invalid dimensions")
    x = []
    for i in m:
        
        x.append(dot_product(i,n))
    return x 

print(MV_multiplication(a,v))

def j_th_column(m: list, x: int)-> list:
    j = []
    for i in m: 
        j.append(i[x])
    return j 

print(j_th_column(a,1))


def is_rectangle(m: list)->bool:
    if not m or not m[0]:
        return False

    width = len(m[0])
    return all(len(row) == width for row in m)

def MM_multiplication(m: list, n: list)-> list:
    if len(m[0]) != len(n):
        raise ValueError("matrices with invalid dimensions")
    
    result = []
    
    for row in m:
        result_row = []

        for j in range(len(n[0])):
            column = j_th_column(n, j)
            result_row.append(dot_product(row, column))

        result.append(result_row)

    return result

print(MM_multiplication(a,a))