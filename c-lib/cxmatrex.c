#include <stdio.h>
#include <stdlib.h>

// تابع برای ضرب ماتریس‌ها
void multiplyMatrices(int *A, int *B, int *C, int rowA, int colA, int colB) {
    for (int i = 0; i < rowA; i++) {
        for (int j = 0; j < colB; j++) {
            C[i * colB + j] = 0;
            for (int k = 0; k < colA; k++) {
                C[i * colB + j] += A[i * colA + k] * B[k * colB + j];
            }
        }
    }
}

// تابع برای نمایش ماتریس (اختیاری برای تست)
void printMatrix(int *matrix, int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%d ", matrix[i * cols + j]);
        }
        printf("\n");
    }
}