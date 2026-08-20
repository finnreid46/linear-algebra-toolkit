import math

zero_vector = [0,0,0]
a = [1,2,3]
b = [4,5,6]
c = [7,8,9,0]

u_perp = [-2,1]
u = [1,2]
v = [-1,3]

def add_vectors(a: list, b: list)-> list:
    y = []
    if len(a) != len(b):
        raise ValueError

    for i in range(len(a)):
        y.append(a[i]+b[i])
    return y 


def add_vec(a: list, b: list)-> list:
    print(list(zip(a,b)))
# was a suggestion to use the zip function

def scalar_multiply(x: int | float , a: list)-> list:
    y = []
    for v in a:
        y.append(x*v)
    return y


def dot_product(a: list, b: list)-> int:
    y = 0
    if len(a) != len(b):
        raise ValueError
    for i in range(len(a)):
        y += a[i]*b[i]
    return y

def vector_magnitude(a: list)-> int | float:
    y = math.sqrt(dot_product(a,a))
    return y



def normalise(a: list)-> list:
    if vector_magnitude(a) == 0:
        raise ValueError("cannot normalise the zero vector")
    y = scalar_multiply(1/vector_magnitude(a),a)
    return y


def angle_between(a: list, b: list)-> tuple:
    if vector_magnitude(a) == 0 or vector_magnitude(b) == 0:
        raise ValueError("angle is undefined for zero vector")
    
    y = (dot_product(a,b))/(vector_magnitude(a)*vector_magnitude(b))
    y = max(-1.0, min(1.0, y))
    rads = math.acos(y)
    degrees = math.degrees(rads)
    return rads, degrees


