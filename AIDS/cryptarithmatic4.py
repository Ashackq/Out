def solve_cryptarithmetic(equation):
    """Solves a cryptarithmetic puzzle.

    Args:
        equation: The cryptarithmetic equation as a string.

    Returns:
        A dictionary mapping letters to digits if a solution is found, otherwise None.
    """

    words = equation.split()
    operand1, operator, operand2, equals, result = words

    letters = set("".join(operand1 + operand2 + result))
    if len(letters) > 10:
        return None  # More letters than digits

    def is_valid(mapping):
        """Checks if the current mapping is valid."""
        values = {letter: str(digit) for letter, digit in mapping.items()}
        num1 = int("".join(values[c] for c in operand1))
        num2 = int("".join(values[c] for c in operand2))
        result_num = int("".join(values[c] for c in result))

        if operator == "+":
            return num1 + num2 == result_num
        elif operator == "-":
            return num1 - num2 == result_num

    def backtrack(mapping):
        """Backtracking search for solutions."""
        if len(mapping) == len(letters):
            if is_valid(mapping):
                return mapping
            return None
        for digit in range(10):
            if digit not in mapping.values():
                # Skip if the digit 0 is assigned to any leading letter
                next_letter = next(iter(letters - set(mapping.keys())))
                if digit == 0 and next_letter in [operand1[0], operand2[0], result[0]]:
                    continue
                new_mapping = mapping.copy()
                new_mapping[next_letter] = digit
                solution = backtrack(new_mapping)
                if solution:
                    return solution
        return None

    return backtrack({})


equation = "gerald + donald = robert"


solution = solve_cryptarithmetic(equation)
if solution:
    print(solution)
else:
    print("No solution found.")
