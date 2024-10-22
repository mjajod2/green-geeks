import sys
import time
from pyJoules.energy_meter import measure_energy

# Mocking necessary variables
valid_expression = ['a', '+', 'b', '-', 'c'] * 2000000  # Mock expression (total 10 million elements)
stack = []  # Stack
verbose = False  # Toggle for verbosity

def mock_function_call():
    return 0  # Mock function call

def mock_variable_assignment():
    return '+'  # Mock variable assignment

OPERATORS = {'+': lambda a, b: a + b, '-': lambda a, b: a - b}  # Mock operators

@measure_energy
def mock_loop_unroll():
    step = 4
    i = 0

    while i < len(valid_expression) - step:
        for _ in range(step):
            x = valid_expression[i]
            if x not in OPERATORS:
                stack.append(x)
                if verbose:
                    print(mock_function_call(), f'{x}'.rjust(8), f'push({x})'.ljust(12), stack, sep=' | ')
                continue
            if x in ['-'] and len(stack) < 2:
                b = stack.pop()
                if x == '-':
                    b *= -1
                stack.append(b)
                if verbose:
                    print(mock_function_call(), ''.rjust(8), f'pop({b})'.ljust(12), stack, sep=' | ')
                    print(mock_function_call(), str(x).rjust(8), f'push({x}{b})'.ljust(12), stack, sep=' | ')
                continue
            b = stack.pop()
            if verbose:
                # print(mock_function_call(), ''.rjust(8), f'pop({b})'.ljust(12), stack, sep=' | ')
            a = stack.pop()
            if verbose:
                # print(mock_function_call(), ''.rjust(8), f'pop({a})'.ljust(12), stack, sep=' | ')
            stack.append(OPERATORS[x](a, b))
            if verbose:
                print(mock_function_call(), f'{x}'.rjust(8), f'push({a}{x}{b})'.ljust(12), stack, sep=' | ')
            i += 1

# Call the function
mock_loop_unroll()
