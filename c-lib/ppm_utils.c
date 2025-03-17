#include <stdio.h>
#include <stdlib.h>
#include "ppm_utils.h"

void loadPPM(const char *filename, int *width, int *height, int *maxColor, int ***pixels) {
    FILE *file = fopen(filename, "r");
    if (!file) {
        printf("Error: Cant Open this file.\n");
        return;
    }

    char format[3];
    fscanf(file, "%s", format); // خواندن فرمت (P3)
    if (format[0] != 'P' || format[1] != '3') {
        printf("Error : The File Format is null.\n");
        fclose(file);
        return;
    }

    // خواندن عرض، ارتفاع و مقدار ماکزیمم رنگ
    fscanf(file, "%d %d %d", width, height, maxColor);

    // تخصیص حافظه برای پیکسل‌ها
    *pixels = (int **)malloc(*height * sizeof(int *));
    for (int i = 0; i < *height; i++) {
        (*pixels)[i] = (int *)malloc(*width * 3 * sizeof(int)); // هر پیکسل دارای 3 مقدار (R, G, B) است
    }

    // خواندن داده‌های پیکسل
    for (int y = 0; y < *height; y++) {
        for (int x = 0; x < *width; x++) {
            fscanf(file, "%d %d %d",
                   &((*pixels)[y][x * 3]),     // مقدار R
                   &((*pixels)[y][x * 3 + 1]), // مقدار G
                   &((*pixels)[y][x * 3 + 2])); // مقدار B
        }
    }

    fclose(file);
}

void freePixels(int **pixels, int height) {
    for (int i = 0; i < height; i++) {
        free(pixels[i]);
    }
    free(pixels);
}