#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// تابع برای خواندن تصویر و تولید ماتریس دودویی
int **convertToBinaryMatrix(const char *filename, int threshold, int *width, int *height) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        printf("Error: Could not open file.\n");
        return NULL;
    }

    char format[3];
    fscanf(file, "%s", format);
    if (strcmp(format, "P2") != 0) { // فرمت PGM باید P2 باشد
        printf("Error: Unsupported file format.\n");
        fclose(file);
        return NULL;
    }

    fscanf(file, "%d %d", width, height);
    int maxGray;
    fscanf(file, "%d", &maxGray);

    int **binaryMatrix = (int **)malloc(*height * sizeof(int *));
    for (int i = 0; i < *height; i++) {
        binaryMatrix[i] = (int *)malloc(*width * sizeof(int));
    }

    for (int i = 0; i < *height; i++) {
        for (int j = 0; j < *width; j++) {
            int pixel;
            fscanf(file, "%d", &pixel);
            binaryMatrix[i][j] = (pixel >= threshold) ? 1 : 0;
        }
    }

    fclose(file);
    return binaryMatrix;
}

// تابع آزادسازی حافظه
void freeMatrix(int **matrix, int height) {
    for (int i = 0; i < height; i++) {
        free(matrix[i]);
    }
    free(matrix);
}