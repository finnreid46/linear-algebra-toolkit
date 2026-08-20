import math
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from la_toolkit.vectors import (add_vectors, normalise, scalar_multiply,angle_between, vector_magnitude)


f = [4,-8]
g = [-5,7]
g_perp = [-7,-5]
u = [1, 2]
u_perp = [-2, 1]

plt.figure(figsize=(6, 6))

# Axes
plt.axhline(0)
plt.axvline(0)

# Vectors
def plot_vectors(u):

    return plt.quiver(0, 0, u[0], u[1], angles="xy", scale_units="xy", scale=1, label="u = (u[0], u[1])")

def plot_vector(x0: float,y0: float,x1: float,y1: float)-> list:
    plt.quiver(x0, y0, x1, y1, angles="xy", scale_units="xy", scale=1, label=f"u = ({x1}, {y1})")
    return 

def plot_add_vectors(u: list,v: list)-> list:
    w = add_vectors(u,v)
    
    plt.quiver(0, 0, u[0], u[1], angles="xy", scale_units="xy", scale=1, label=f"{u} = ({u[0]}, {u[1]})")
    plt.quiver(u[0], u[1], v[0], v[1], angles="xy", scale_units="xy", scale=1, label=f"u+v = ({w[0]}, {w[1]})")
    plt.quiver(0, 0, w[0], w[1], angles="xy", scale_units="xy", scale=1, label=f"u+v = ({w[0]}, {w[1]})")
    return 

def plot_resulting_vector(u: list,v: list)-> list:
    # add_vectors without support vectors
    return plt.quiver(0, 0, add_vectors(u,v)[0], add_vectors(u,v)[1], angles="xy", scale_units="xy", scale=1, label=f"u+v = ({add_vectors(u,v)[0]}, {add_vectors(u,v)[1]})")

def plot_normalise_vector(u: list)-> list:
    v = [u[0]/vector_magnitude(u),u[1]/vector_magnitude(u)]
    #v = normalise(u)
    return plt.quiver(0, 0, v[0], v[1], angles="xy", scale_units="xy", scale=1, label=f"v = ({v[0]}, {v[1]})")
    
def plot_scalar_multiply(x: int, u: list)-> list:
    v = scalar_multiply(x,u)
    plt.quiver(0, 0, x*u[0], x*u[1], angles="xy", scale_units="xy", scale=1, label=f"{v} = ({x*u[0]}, {x*u[1]})")

def plot_angle_between(u: list,v: list)-> tuple:
    ax = plt.gca()
    angle_u = math.degrees(math.atan2(u[1], u[0]))
    angle_v = math.degrees(math.atan2(v[1], v[0]))
    arc = Arc(
        (0, 0),
        width=2,
        height=2,
        angle=0,
        theta1=angle_u,
        theta2=angle_v
    )
    ax.add_patch(arc)
    #plt.text((u[0]+v[0])/2, (u[1]+v[1])/2, f"the angle between u,u_perp is {angle_between(u,v)}")
    return 

# function test calls
plot_add_vectors(f,g)
plot_angle_between(f,g)
plot_normalise_vector(g_perp)
plot_scalar_multiply(2,u)
plot_resulting_vector(u,u_perp)

# Limits
plt.xlim(-9, 9)
plt.ylim(-9, 9)

# Formatting
plt.gca().set_aspect("equal", adjustable="box")
plt.grid(True)
plt.legend()
plt.title("Perpendicular vectors in 2D")
plt.xlabel("x")
plt.ylabel("y")

plt.show()





#plt.quiver(0, 0, u_perp[0], u_perp[1], angles="xy", scale_units="xy", scale=1, label="u_perp = (-2, 1)")

#plt.quiver(u_perp[0], u_perp[1], u[0], u[1], angles="xy", scale_units="xy", scale=1, label="u = (1, 2)")




#plt.quiver(u[0], u[1], u_perp[0], u_perp[1], angles="xy", scale_units="xy", scale=1, label="u_perp = (-2, 1)")

#plt.quiver(0, 0, scalar_multiply(0.5,g)[0], scalar_multiply(0.5,g)[1], angles="xy", scale_units="xy", scale=1, label="u_perp = (-2, 1)")
#plt.quiver(0, 0, normalise(f)[0], normalise(f)[1], angles="xy", scale_units="xy", scale=1, label="u_perp = (-2, 1)")


#angle
#plt.text(-3,-4,f"the angle between u,u_perp is {angle_between(u,u_perp)[1]}")