import os


def find_n_largest_digits(s: str, n: int) -> int:
    digits = [int(c) for c in s if c.isdigit()]
    to_remove = len(digits) - n
    stack = []

    for d in digits:
        while to_remove > 0 and stack and stack[-1] < d:
            stack.pop()
            to_remove -= 1
        stack.append(d)

    result_digits = stack[:n]

    result = int("".join(map(str, result_digits)))
    return result


def jolt(input_1, input_2):
    if input_1 > input_2:
        return f"{input_1}{input_2}"
    else:
        return f"{input_2}{input_1}"


if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    RESOURCE_PATH = os.path.join(BASE_DIR, "..", "resources", "input_day_3.txt")

    total = 0

    with open(RESOURCE_PATH) as file:
        for line in file:
            line = line.strip()
            total += find_n_largest_digits(line, 12)

    print(total)
