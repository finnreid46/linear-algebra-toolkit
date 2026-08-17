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
        raise ZeroDivisionError
    y = scalar_multiply(1/vector_magnitude(a),a)
    return y


def angle_between(a: list, b: list)-> tuple:
    if vector_magnitude(a) or vector_magnitude(b) == 0:
        raise ValueError

    y = (dot_product(a,b))/(vector_magnitude(a)*vector_magnitude(b))
    rads = math.acos(y)
    degrees = math.degrees(rads)
    return rads, degrees


#print(add_vectors(a,c))
print(scalar_multiply(3,a))
print(add_vectors(scalar_multiply(3,u),scalar_multiply(2,v)))
print(dot_product(u,u_perp))
print(vector_magnitude(zero_vector))
#add_vec(a,b)

#print(normalise(zero_vector))
print(angle_between(u,u_perp))