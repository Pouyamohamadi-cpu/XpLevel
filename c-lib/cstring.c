#include <string.h>
#include <stdio.h>

int countwords(const char *text) {
    int count = 0;
    const char *word = strtok((char *)text, " ");
    while (word) {
        count++;
        word = strtok(NULL, " ");
    }
    return count;
}

int stringlength(const char *input) {
    return strlen(input);
}

void copystring(char *dest, const char *src, size_t n) {
    strncpy(dest, src, n);
    dest[n] = '\0'; // اطمینان از اینکه رشته مقصد null-terminated است
}

const char* findsubstring(const char *str, const char *substr) {
    const char *result = strstr(str, substr);
    return result; // اگر پیدا شد، اشاره‌گر به زیررشته را برمی‌گرداند
}

void initializebuffer(char *buffer, size_t size, char value) {
    memset(buffer, value, size);
}