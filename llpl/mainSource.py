import time, random, math

# ------print------

def type(text):
    print(text)

# using like:
# type("Hello world!")

# ------input------

def uInput():
    return input()

# using like:
# var("var1", uInput())
# a = get("var1")

# ------variables------

variables = {}

def var(varName, value):
    variables[varName] = value

def get(varName):
    return variables.get(varName)

# using like:
# var("var1", 1)
# var1 = get(var1)

# ------loop------

def loop(repeatTime, code):
    for _ in range(repeatTime):
        code()

# using like:
# loop(4, lambda: type("hello world"))

# ------if------

def ifStm(condition, code):
    if condition:
        code()

# using like: ifStm(a == b, lambda: type("a"))

# ------mathematical functions------

def add(var1, var2):
    return var1 + var2

def subtract(var1, var2):
    return var1 - var2

def multiply(var1, var2):
    return var1 * var2

def divide(var1, var2):
    return var1 / var2

def sqrt(var1):
    return math.sqrt(var1)

def sin(var1):
    return math.sin(var1)

def cos(var1):
    return math.cos(var1)

def tan(var1):
    return math.tan(var1)

def log(var1, base):
    return math.log(var1, base)

def factorial(var1):
    return math.factorial(var1)

# ------time------

def tDelay(time):
    time.sleep(time)

# using like: tDelay(1)

# ------random------

def gRandomNum(min, max):
    return random.randint((min), (max))

# using like:
# var("var1", gRandomNum(1, 10))
# a = get("var1")

# ------Functions------
functions = {}

def func(Name, code):
    exec(f"def {Name}():\n    {code}", globals())
    functions[Name] = eval(Name)

def call(Name):
    func = functions.get(Name)
    if func:
        return func()
    else:
        return None

# using like:
# func("a", 'type("a")')
# call("a")


