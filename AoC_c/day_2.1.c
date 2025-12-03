#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct {
    long long start;
    long long end;
} Range;

char *read_file(const char *path) {
    FILE *fp = fopen(path, "rb");
    if (!fp) { perror("open"); return NULL; }

    fseek(fp, 0, SEEK_END);
    long size = ftell(fp);
    rewind(fp);

    char *buf = malloc(size + 1);
    if (!buf) { perror("malloc"); fclose(fp); return NULL; }

    fread(buf, 1, size, fp);
    buf[size] = '\0';
    fclose(fp);
    return buf;
}

char **split(const char *text, const char *delim, size_t *out_count) {
    char *copy = strdup(text);
    size_t cap = 16, count = 0;
    char **parts = malloc(cap * sizeof(char*));

    char *token = strtok(copy, delim);
    while (token) {
        if (count == cap) {
            cap *= 2;
            parts = realloc(parts, cap * sizeof(char*));
        }
        parts[count++] = token;
        token = strtok(NULL, delim);
    }

    *out_count = count;
    return parts; // must free(copy) and parts, but not individual tokens
}

Range *parse_ranges(char **parts, size_t count, size_t *out_count) {
    Range *ranges = malloc(count * sizeof(Range));

    for (size_t i = 0; i < count; i++) {
        char *dash = strchr(parts[i], '-');
        *dash = '\0';
        const char *start = parts[i];
        const char *end   = dash + 1;

        ranges[i].start = atoll(start);
        ranges[i].end   = atoll(end);
    }

    *out_count = count;
    return ranges;
}

// Check if n has even digits and first half == second half
bool invalid_id(long long n) {
    char buf[32];
    sprintf(buf, "%lld", n);
    size_t len = strlen(buf);

    if (len % 2 != 0) return false;

    size_t mid = len / 2;
    return strncmp(buf, buf + mid, mid) == 0;
}

int main(void) {
    const char *RESOURCE_PATH =
        "/Users/samfredrik/Desktop/AoC_2025/resources/input_day_2.txt";

    char *contents = read_file(RESOURCE_PATH);
    if (!contents) return 1;

    size_t parts_count;
    char **parts = split(contents, ",", &parts_count);

    size_t range_count;
    Range *ranges = parse_ranges(parts, parts_count, &range_count);

    // MAIN LOGIC: iterate all values and test invalid_id
    long long invalid_sum = 0;

    for (size_t i = 0; i < range_count; i++) {
        long long start = ranges[i].start;
        long long end   = ranges[i].end;

        for (long long n = start; n <= end; n++) {
            if (invalid_id(n)) {
                invalid_sum += n;
            }
        }
    }

    printf("Sum of invalid IDs: %lld\n", invalid_sum);

    free(ranges);
    free(parts);
    free(contents);

    return 0;
}
