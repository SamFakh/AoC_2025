from pathlib import Path


def total_removed(path):
    with open(path) as f:
        grid = [list(line.strip()) for line in f if line.strip()]

    h, w = len(grid), len(grid[0])
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    total = 0

    while True:
        removable = []

        # Find all accessible rolls in current grid
        for y in range(h):
            for x in range(w):
                if grid[y][x] != "@":
                    continue
                neighbors = 0
                for dy, dx in dirs:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] == "@":
                        neighbors += 1
                        if neighbors == 4:  # not removable
                            break
                if neighbors < 4:
                    removable.append((y, x))

        # If nothing more is removable → stop
        if not removable:
            return total

        # Remove all accessible rolls this round
        for y, x in removable:
            grid[y][x] = "."

        total += len(removable)


if __name__ == "__main__":

    def resource(filename: str) -> Path:
        # Location of THIS PYTHON FILE
        current_dir = Path(__file__).resolve().parent
        # Resources are in ../Resources/
        return current_dir.parent / "Resources" / filename

    RESOURCE_PATH = resource("input_day_4.txt")

    print(total_removed(RESOURCE_PATH))
