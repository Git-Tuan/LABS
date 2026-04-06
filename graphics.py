import numpy as np
import matplotlib.pyplot as plt

def derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)


def second_derivative(f, x, h=1e-5):
    return (f(x + h) - 2*f(x) + f(x - h)) / (h**2)


def find_extrema(f, x_vals):
    extrema = []

    for i in range(1, len(x_vals) - 1):
        try:
            d1 = derivative(f, x_vals[i-1])
            d2 = derivative(f, x_vals[i])

            if d1 * d2 < 0: 
                extrema.append(x_vals[i])
        except:
            pass

    return extrema


def find_inflection_points(f, x_vals):
    points = []

    for i in range(1, len(x_vals) - 1):
        try:
            d1 = second_derivative(f, x_vals[i-1])
            d2 = second_derivative(f, x_vals[i])

            if d1 * d2 < 0:
                points.append(x_vals[i])
        except:
            pass

    return points


def plot_function(f, a, b, roots):
    x = np.linspace(a, b, 1000)
    y = []

    for xi in x:
        try:
            y.append(f(xi))
        except:
            y.append(np.nan)

    y = np.array(y)

    plt.figure()
    plt.plot(x, y, label="f(x)")

    root_x = []
    root_y = []

    for r in roots:
        if r["root"] is not None:
            root_x.append(r["root"])
            root_y.append(r["fx"])
            
    if root_x:
        plt.scatter(root_x, root_y, label="Root", c="green")

    extrema_x = find_extrema(f, x)
    extrema_y = [f(xi) for xi in extrema_x]
    if extrema_x:
        plt.scatter(extrema_x, extrema_y, label="Extrema", c="red")
    
    inf_x = find_inflection_points(f, x)
    inf_y = [f(xi) for xi in inf_x]

    if inf_x:
        plt.scatter(inf_x, inf_y, label="Inflection", c="purple")
        
    plt.grid()
    plt.legend()
    plt.show()
