# problems of univariate minimizer:
# TODO: fix possible occurrence of infinite loop
# TODO: fix presence of more than one root
# improvements of the method:
# TODO: implement multivariate minimizer
# github repo:
# TODO: write the documentation

# Issues:
# If the search interval includes a local max or local min of the function, the method will not approach the root
# If the funciton is not well behaved, then the method can start iterating without convergence

# NOTES:
# Newton-Raphson method can also be used at final steps of root-finding routines to "polish" previously obtained results (once the result is close enough to the real root)
# Newton-Raphson with numerical derivatives is always dominated by Brent’s method

def fprime(f, x0, h=1e-5): # first derivative calculations
    return (f(x0 + h) - f(x0 - h))/(2*h)

def fsecond(f, x0, h=1e-5): # second derivative calculations
    fplus = f(x0 + h)
    fminus = f(x0 - h)
    return (fplus - 2*f(x0) + fminus) / (h**2)


def newton_raphson(x, f):  # closure function
    x0 = x

    def nr_closure():
        nonlocal x0, f
        x0 = x0 - fprime(f, x0) / fsecond(f, x0)
        return x0

    return nr_closure


def nr_minimizer(f, x, epsilon=1e-10):  # main method

    minimizer = newton_raphson(x, f)
    x2 = x
    x1 = minimizer()
    while abs(x2 - x1) > epsilon:
        x1 = x2
        x2 = minimizer()
    return x2

if __name__ == '__main':
    def f(x): # function to be solved
        return x**3 - x - 1
        # return x**2 + np.exp(x) -2

    sol = nr_minimizer(f, 5) # 5 = initial guess
    print(sol)
