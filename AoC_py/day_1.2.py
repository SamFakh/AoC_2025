import os


class CombinationDial:
    def __init__(self, min_val: int, max_val: int, starting_pos: int = 50) -> None:
        self.min = min_val
        self.max = max_val
        self.size = max_val - min_val + 1
        self.pos = starting_pos

    def count_zero_hits(self, clicks: int, direction: str) -> int:
        start = self.pos
        N = self.size

        if direction == "R":
            # forward: how many steps until (start + i) % N == 0 ?
            i = (N - start) % N
            i = i if i != 0 else N
        else:  # LEFT
            # backward: how many steps until (start - i) % N == 0 ?
            i = start if start != 0 else N

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
    if __name__ == "__main__":
        RESOURCE_PATH = os.path.join(
            os.path.dirname("__file__"), "..", "resources", "input_day_1.txt"
        )

        with open(RESOURCE_PATH) as file:
            steps = [line.strip() for line in file]

        dial = CombinationDial(0, 99)
        total_zero_hits = 0

        for step in steps:
            new_pos, mid_hits = dial.apply_step(step, include_mid_rotation_zeros=True)

            total_zero_hits += mid_hits

            # Only count end-at-zero if we did NOT already hit zero mid-rotation
            if new_pos == 0 and mid_hits == 0:
                total_zero_hits += 1

        print(total_zero_hits)
