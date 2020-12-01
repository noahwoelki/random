

def my_decorator(func):
    def wrapper(a, n):
        print(generator.__doc__)
        func(a, n)
    return wrapper


def generator(a, n):
    """Description of this function:

    This function calculates the different powers of input a:

    a^i with i<= n

    """
    for i in range(n):
        print(a, "^", i, "=")
        print(pow(a, i))


generator = my_decorator(generator)


generator(4, 5)
