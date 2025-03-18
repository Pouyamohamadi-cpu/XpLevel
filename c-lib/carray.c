#include "carray.h"

// ایجاد آرایه دوبعدی
MyArray* createArray(int rows, int cols) {
    MyArray* array = (MyArray*)malloc(sizeof(MyArray));
    array->rows = rows;
    array->cols = cols;

    array->data = (double**)malloc(rows * sizeof(double*));
    for (int i = 0; i < rows; i++) {
        array->data[i] = (double*)calloc(cols, sizeof(double)); // مقداردهی به صفر
    }
    return array;
}

// آزادسازی حافظه
void freeArray(MyArray* array) {
    for (int i = 0; i < array->rows; i++) {
        free(array->data[i]);
    }
    free(array->data);
    free(array);
}

// چاپ آرایه
void printArray(const MyArray* array) {
    for (int i = 0; i < array->rows; i++) {
        for (int j = 0; j < array->cols; j++) {
            printf("%.2f ", array->data[i][j]);
        }
        printf("\n");
    }
}

// پر کردن آرایه با مقدار خاص
void fillArray(MyArray* array, double value) {
    for (int i = 0; i < array->rows; i++) {
        for (int j = 0; j < array->cols; j++) {
            array->data[i][j] = value;
        }
    }
}

// ضرب دو آرایه
MyArray* multiplyArrays(const MyArray* A, const MyArray* B) {
    if (A->cols != B->rows) {
        printf("Error: Incompatible matrix dimensions for multiplication.\n");
        return NULL;
    }

    MyArray* result = createArray(A->rows, B->cols);
    for (int i = 0; i < A->rows; i++) {
        for (int j = 0; j < B->cols; j++) {
            result->data[i][j] = 0;
            for (int k = 0; k < A->cols; k++) {
                result->data[i][j] += A->data[i][k] * B->data[k][j];
            }
        }
    }
    return result;
}