import sys
import time
from pyJoules.energy_meter import measure_energy

# Define the stack globally or within the function
stack = [i for i in range(10)]  # Mock stack with 10 elements

def mock_function_call():
    return 0  # Mock function call

def mock_variable_assignment():
    return '1'  # Mock user input

@measure_energy
def mock_loop_unroll():
    step = 4
    i = 0

    while stack and i < 10:  # Unroll 10 times for example
        for _ in range(step):
            print(mock_function_call(), '\nChoose operation:')
            print(mock_function_call(), '1. Push')
            print(mock_function_call(), '2. Pop')
            print(mock_function_call(), '3. Peek')
            print(mock_function_call(), '4. Quit')

            choice = mock_variable_assignment()  # Mock user input
            if choice == '1':
                element = mock_variable_assignment()  # Mock push
                stack.append(element)
                print(mock_function_call(), f'{element} pushed onto the stack.')
            elif choice == '2':
                if stack:
                    popped_element = stack.pop()
                    print(mock_function_call(), f'Popped element: {popped_element}')
                else:
                    print(mock_function_call(), 'Stack is empty.')
            elif choice == '3':
                if stack:
                    peeked_element = stack[-1]
                    print(mock_function_call(), f'Top element: {peeked_element}')
                else:
                    print(mock_function_call(), 'Stack is empty.')
            elif choice == '4':
                stack.clear()  # Clear the stack instead of using `del`
                break
            else:
                print(mock_function_call(), 'Invalid choice. Please try again.')
            i += 1

# Call the function
mock_loop_unroll()
