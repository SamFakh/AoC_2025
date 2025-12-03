#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct {
    long long start;
    long long end;
} Range;

/* Read entire file */
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

/* Split string by delimiter (comma) */
char **split(const char *text, const char *delim, size_t *out_count) {
    char *copy = _strdup(text);
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
    return parts;  // Caller frees parts + copy
}

/* Convert "start-end" into Range structs */
Range *parse_ranges(char **parts, size_t count, size_t *out_count) {
    Range *ranges = malloc(count * sizeof(Range));

    for (size_t i = 0; i < count; i++) {
        char *dash = strchr(parts[i], '-');
        *dash = '\0';

        const char *start_str = parts[i];
        const char *end_str = dash + 1;

        ranges[i].start = atoll(start_str);
        ranges[i].end   = atoll(end_str);
    }

    *out_count = count;
    return ranges;
}

/* Check repeating-block invalid ID logic */
bool invalid_id(long long n) {
    char s[32];
    sprintf(s, "%lld", n);

    size_t len = strlen(s);

    // block_size ranges from 1 up to half the total length
    for (size_t block_size = 1; block_size <= len / 2; block_size++) {
        if (len % block_size != 0)
            continue;

        size_t repeat_count = len / block_size;
        const char *block = s;

        bool match = true;
        for (size_t i = 1; i < repeat_count; i++) {
            if (strncmp(block, s + i * block_size, block_size) != 0) {
                match = false;
                break;
            }
        }

        if (match)
            return true;
    }

    return false;
}

int main(void) {
    const char *RESOURCE_PATH =
        "/Users/samfredrik/Desktop/AoC_2025/resources/input_day_2.txt";

    /* Read file */
    char *contents = read_file(RESOURCE_PATH);
    if (!contents) return 1;

    /* Split by comma */
    size_t parts_count;
    char **parts = split(contents, ",", &parts_count);

    /* Parse into ranges */
    size_t range_count;
    Range *ranges = parse_ranges(parts, parts_count, &range_count);

    /* Main logic: iterate all values & check invalid_id(n) */
    long long invalid_sum = 0;
    long long invalid_count = 0;

    for (size_t i = 0; i < range_count; i++) {
        long long start = ranges[i].start;
        long long end   = ranges[i].end;

        for (long long n = start; n <= end; n++) {
            if (invalid_id(n)) {
                invalid_sum += n;
                invalid_count++;
            }
        }
    }

    printf("Number of invalid IDs: %lld\n", invalid_count);
    printf("Sum of invalid IDs: %lld\n", invalid_sum);

    /* Cleanup */
    free(ranges);
    free(parts);
    free(contents);

    return 0;
}
