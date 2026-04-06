import math

def parse_function(expr):
    code = compile(expr, "<string>", "eval")

    allowed = {
        "x": 0,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "exp": math.exp,
        "ln": math.log,
        "log": math.log,
        "log2": math.log2,
        "log10": math.log10,
        "sqrt": math.sqrt,
        "pi": math.pi,
        "e": math.e,
        "math": math
    }

    def f(x):
        result = 0
        try:
            allowed["x"] = x
            result = eval(code, {"__builtins__": {}}, allowed)
        except ValueError as ve:
            result = float("nan")
        except NameError as ne:
            result = float("nan")

        return result

    return f

def validate_input(a, b, h, eps, nmax, f):
    info = True, ""
    if a >= b:
        info =  False, "a must be less than b"
    elif h <= 0:
        info = False, "Step h must be > 0"
    elif eps <= 0:
        info =  False, "Precision must be > 0"
    elif nmax <= 0:
        info =  False, "Nmax must be > 0"
    elif f != f:
        info = False, "Invalid function input"

    return info
