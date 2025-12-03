from pathlib import Path


def read_str(string: str) -> list[str]:
    return string.split(",")


def parse_ranges(parts: list[str]) -> list[list[int]]:
    ranges: list[list[int]] = []
    for element in parts:
        start_str, end_str = element.split("-")
        start, end = int(start_str), int(end_str)
        ranges.append(list(range(start, end + 1)))
    return ranges


def invalid_id(n: int) -> bool:
    s = str(n)
    length = len(s)
    for block_size in range(1, length // 2 + 1):
        if length % block_size != 0:
            continue
        block = s[:block_size]
        if block * (length // block_size) == s:
            return True
    return False


def main(input_str: str) -> list[int]:
    parts = read_str(input_str)
    expanded = parse_ranges(parts)
    invalid_ids: list[int] = []
    for element in expanded:
        for value in element:
            if invalid_id(value):
                invalid_ids.append(value)
    return invalid_ids


if __name__ == "__main__":

    def resource(filename: str) -> Path:
        # Location of THIS PYTHON FILE
        current_dir = Path(__file__).resolve().parent
        # Resources are in ../resources/
        return current_dir.parent / "resources" / filename

    RESOURCE_PATH = resource("input_day_2.txt")

    with open(RESOURCE_PATH) as file:
        input_str = file.read()

    invalids = main(input_str)
    # print("Invalid IDs:", invalids)
    print("Number of invalid IDs:", len(invalids))

    total = sum(invalids)
    print(total)
