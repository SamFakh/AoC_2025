from pathlib import Path


def count_accessible(path):
    with open(path) as f:
        grid = [line.strip() for line in f if line.strip()]

    h, w = len(grid), len(grid[0])
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    accessible = 0

    for y in range(h):
        for x in range(w):
            if grid[y][x] != "@":
                continue
            neighbors = 0
            for dy, dx in dirs:
                ny, nx = y + dy, x + dx
                if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] == "@":
                    neighbors += 1
                    if neighbors == 4:  # early exit
                        break
            if neighbors < 4:
                accessible += 1

    return accessible


if __name__ == "__main__":

    def resource(filename: str) -> Path:
        # Location of THIS PYTHON FILE
        current_dir = Path(__file__).resolve().parent
        # Resources are in ../Resources/
        return current_dir.parent / "Resources" / filename

    RESOURCE_PATH = resource("input_day_4.txt")

    print(count_accessible(RESOURCE_PATH))
