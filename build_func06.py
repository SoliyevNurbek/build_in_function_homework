from math import *
def main(a):
    """Float type variable 'a' is given. Round the result to 2 decimal places in README.md file.
    https://github.com/codeschool43/Build_in_function_homework#build_func06

    Args:
        a (float): integer
        
    Returns:
        float: The result to 2 decimal places
    """
    return round(a,2)
a=float(input())
print(main(a))