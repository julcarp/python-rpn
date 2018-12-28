#!/usr/bin/env python3

import operator

def factorial(arg):
    if arg == 0:
        return 1
    else:
        return arg * factorial(arg-1)

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '%': operator.mod,
    '//': operator.floordiv,
     '!': factorial,
}



def calculate(myarg):
    stack = list()
    stack2 = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            try:
                function = operators[token]
                stack2.append(function)
                arg2 = stack.pop()
                try:
                    arg1 = stack.pop()
                    result = function(arg1, arg2)
                    stack.append(result)
                except IndexError:
                    result = factorial(arg2)
                    stack.append(result)
            except KeyError:
                while len(stack) > 1:
                    function = stack2.pop()
                    stack2.append(function)
                    result = function(stack.pop(), stack.pop())
                    stack.append(result)

        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()

