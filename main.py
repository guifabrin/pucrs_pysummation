# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math


def summation(i, n, formula):
    result = 0
    for i in range(i, n + 1):
        result = eval(formula.format(str(i))) + result
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(summation(0, 3, '5+math.sqrt(4**{0})'))
    print(summation(1, 100, '4+3*{0}'))
    print(summation(1, 200, '({0}-3)**2'))
    print(summation(1, 200, '({0}-3)**2'))
    print(summation(15, 150, '4*{0}+1'))
    print(summation(1, 50, 'math.log({0}+3)-math.log({0}+2)'))
    print(summation(25, 150, '1/(i+4)-1/(i+5)'))
    print(summation(10, 80, '{0}**3+{0}**2'))
    print(summation(1, 20, 'math.sin({0}*math.pi/2)'))
    print(summation(7, 32, 'math.cos({0}*math.pi)'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
