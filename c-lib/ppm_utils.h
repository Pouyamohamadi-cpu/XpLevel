#ifndef PPM_UTILS_H
#define PPM_UTILS_H

void loadPPM(const char *filename, int *width, int *height, int *maxColor, int ***pixels);
void freePixels(int **pixels, int height);

#endif // PPM_UTILS_H