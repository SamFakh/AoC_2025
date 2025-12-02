class CombinationDial:
    def __init__(self, min_val: int, max_val: int, starting_pos: int = 50) -> None:
        self.min = min_val
        self.max = max_val
        self.size = max_val - min_val + 1
        self.pos = starting_pos

    def count_zero_hits(self, clicks: int, direction: str) -> int:
        start = self.pos
        N = self.size

        if direction == "L":
            i = (start - 0) % N
            i = i if i != 0 else N
        else:
            i = (0 - start) % N
            i = i if i != 0 else N

        if i > clicks:
            return 0

        return 1 + (clicks - i) // N

    def update_pos(self, clicks: int, direction: str) -> int:
        if direction == "L":
            clicks = -clicks
        elif direction != "R":
            raise ValueError("Direction must be 'L' or 'R'.")

        self.pos = (self.pos + clicks) % self.size
        return self.pos

    def apply_step(
        self, step: str, include_mid_rotation_zeros=False
    ) -> tuple[int, int]:
        direction = step[0]
        clicks = int(step[1:])

        zero_hits = 0
        if include_mid_rotation_zeros:
            zero_hits = self.count_zero_hits(clicks, direction)

        new_pos = self.update_pos(clicks, direction)
        return new_pos, zero_hits


if __name__ == "__main__":
    RESOURCE_PATH = "/Users/samfredrik/Desktop/AoC_2025/AoC_py/resources/input_day1.txt"

    with open(RESOURCE_PATH) as file:
        steps = [line.strip() for line in file]

    dial = CombinationDial(0, 99)
    total_zero_hits = 0

    for step in steps:
        new_pos, _ = dial.apply_step(step, include_mid_rotation_zeros=False)
        if new_pos == 0:
            total_zero_hits += 1

    print(total_zero_hits)
