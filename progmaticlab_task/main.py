from typing import List, Optional

numbers = list(range(9, -1, -1))
possible_operations = ['+', '-', '']


def calculate_expession(operations: List[str]):
    result = 0
    rightValue = numbers[0]
    operation = '+'
    for index in range(len(numbers)): 
        if index != 9 and operations[index] == '':
            rightValue = rightValue * 10 + numbers[index + 1]
        else:
            if operation == '+':
                result += rightValue
            else:
                result -= rightValue
            if index < 9:
                operation = operations[index]
                rightValue = numbers[index + 1]
    return(result)


def find_combination(current_operations: List[str]) -> Optional[List[str]]:
    if len(current_operations) == 9:
        result = calculate_expession(current_operations)
        if result == 200:
           return current_operations
        return None
    for operation in possible_operations:
        current_operations.append(operation)
        result = find_combination(current_operations)
        if result:
            return result
        current_operations.pop()


def get_full_expression(combination: Optional[List[str]]) -> str:
    result = ''
    if combination:
        for number, operation in zip(numbers, combination):
            result += str(number) + operation
        result += str(numbers[-1])
    return result


combination = find_combination([])
expression = get_full_expression(combination)
print(combination)
print(expression)


