#include <stdio.h>
#include <stdlib.h>

int mod(int x, int n) {
    int r = x % n;
    return r < 0 ? r + n : r;
}

int main(void) {
    const char *RESOURCE_PATH = "/mnt/c/Users/SamFredrikFakhraee/OneDrive - inspirit365 AS/Desktop/AoC_2025/resources/input_day_1.txt";
    FILE *file = fopen(RESOURCE_PATH, "r");

    if (!file) {
        perror("Could not open input file");
        return 1;
    }

    int pos = 50;          // starting position
    int total_zero_hits = 0;

    char line[64];
    while (fgets(line, sizeof(line), file)) {

        char dir = line[0];      // 'L' or 'R'
        int clicks = atoi(line + 1);

        // Apply rotation
        if (dir == 'L')
            pos = mod(pos - clicks, 100);
        else
            pos = mod(pos + clicks, 100);

        // Count landing on zero
        if (pos == 0)
            total_zero_hits++;
    }

    fclose(file);

    printf("%d\n", total_zero_hits);
    return 0;
}
