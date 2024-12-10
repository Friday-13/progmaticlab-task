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

def find_combinations(current_operations: List[str] = [], founded_operations: List[List[str]] = []) -> Optional[List[List[str]]]:
    if len(current_operations) == 9:
        result = calculate_expession(current_operations)
        if result == 200:
            founded_operations.append([*current_operations])
        return

    for operation in possible_operations:
        current_operations.append(operation)
        result = find_combinations(current_operations, founded_operations)
        current_operations.pop()
    return founded_operations


def get_full_expressions(combinations: Optional[List[List[str]]]) -> str:
    result = ''
    if combinations:
        for combination in combinations:
            for number, operation in zip(numbers, combination):
                result += str(number) + operation
            result += str(numbers[-1])
            result+='\n'
    return result


combinations = find_combinations()
expression = get_full_expressions(combinations)
print(combinations)
print(expression)


