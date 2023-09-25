from math import *
def main(x,y):
    """Integer type variables 'x' and 'y' are given. Return the value of the expression in README.md file.
    https://github.com/codeschool43/Build_in_function_homework#build_func07

    Args:
        x (int): integer
        y (int): integer
        
    Returns:
        int: the value of the expression
    """
    return int(pow(x,2)+6*pow(x,3)+3*x*y)
x=int(input())
y=int(input())
print(main(x,y))