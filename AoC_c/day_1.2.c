#include <stdio.h>
#include <stdlib.h>

int modp(int x, int n) {
    int r = x % n;
    return r < 0 ? r + n : r;
}

int count_zero_hits(int pos, int clicks, char dir, int size) {
    int start = pos;
    int N = size;
    int i;

    if (dir == 'R') {
        // forward: (start + i) % N == 0
        i = (N - start) % N;
        if (i == 0) i = N;
    } else { // 'L'
        // backward: (start - i) % N == 0
        i = (start == 0) ? N : start;
    }

    if (i > clicks)
        return 0;

    return 1 + (clicks - i) / N;
}

int main(void) {
    const char *RESOURCE_PATH = "/mnt/c/Users/SamFredrikFakhraee/OneDrive - inspirit365 AS/Desktop/AoC_2025/resources/input_day_1.txt";
    FILE *file = fopen(RESOURCE_PATH, "r");

    if (!file) {
        perror("Could not open input file");
        return 1;
    }

    int size = 100;    // 0..99
    int pos  = 50;
    int total_zero_hits = 0;

    char line[64];

    while (fgets(line, sizeof(line), file)) {

        char dir = line[0];
        int clicks = atoi(line + 1);

        // First compute mid-rotation zero hits
        int mid_hits = count_zero_hits(pos, clicks, dir, size);

        total_zero_hits += mid_hits;

        // Now update position
        if (dir == 'L')
            pos = modp(pos - clicks, size);
        else
            pos = modp(pos + clicks, size);

        // If ending on zero AND we didn't hit zero mid-rotation, count it
        if (pos == 0 && mid_hits == 0)
            total_zero_hits++;
    }

    fclose(file);

    printf("%d\n", total_zero_hits);
    return 0;
}
