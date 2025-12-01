# Advent Of Code - Day 1 Python
# Sam Fakhraee
# 01 12 25


class CombinationDial:
    def __init__(self, min_val: int, max_val: int, starting_pos: int = 50) -> None:
        self.min = min_val
        self.max = max_val
        self.size = max_val - min_val + 1
        self.pos = starting_pos

    def update_pos(self, clicks: int, direction: str) -> int:
        if direction.upper() == "L":
            clicks = -clicks
        elif direction.upper() != "R":
            raise ValueError("Direction must be 'L' or 'R'.")

        self.pos = (self.pos + clicks) % self.size
        return self.pos

    def apply_step(self, step: str) -> int:
        direction = step[0]
        clicks = int(step[1:])
        return self.update_pos(clicks, direction)


if __name__ == "__main__":
    RESOURCE_PATH = "/Users/samfredrik/Desktop/AoC_py/resources/input_day1.txt"

    with open(RESOURCE_PATH) as file:
        steps = [line.strip() for line in file]

    dial = CombinationDial(0, 99)
    zero_hits = 0

    for step in steps:
        if dial.apply_step(step) == 0:
            zero_hits += 1

    print(zero_hits)
