assinment = [0, 0, 0, 0, 0, 0, 0, 0, 0]


def getset(str1, str2, str3):
    first = []
    second = []
    sumed = []
    for i in str1:
        first.append([i, -1])
    for i in str2:
        second.append([i, -1])
    for i in str3:
        sumed.append([i, -1])
    first.reverse()
    second.reverse()
    sumed.reverse()
    return first, second, sumed


def check(first, second, sumed):
    j = 0
    carry = 0
    if len(first) == len(second):
        for i in range(len(first)):
            j += 1
            if first[i][1] + second[i][1] + carry == sumed[i][1]:
                carry = 0
                continue
            elif first[i][1] + second[i][1] == 10 + sumed[i][1]:
                carry = 1
                continue
            else:
                return False
        return True


def solver(used, first, second, sumed):
    if len(first) != len(sumed) or len(second) != len(sumed):
        sumed[-1][1] = 1
        used[1] = 1
        for i in range(10):
            return 0


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
        num1 = int("".join(c.translate(str.maketrans(values)) for c in operand1))
        num2 = int("".join(c.translate(str.maketrans(values)) for c in operand2))
        result_num = int("".join(c.translate(str.maketrans(values)) for c in result))

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
                new_mapping = mapping.copy()
                new_mapping[next(iter(letters - set(mapping.keys())))] = digit
                result = backtrack(new_mapping)
                if result:
                    return result
        print(mapping)
        return None

    return backtrack({})


equation = "gerald + donald = robert"


solution = solve_cryptarithmetic(equation)
if solution:
    print(solution)
else:
    print("No solution found.")
