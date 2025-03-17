#include <zip.h>
#include <stdio.h>

int extract_zip(const char *zip_file, const char *output_dir) {
    struct zip *z = zip_open(zip_file, 0, NULL);
    if (!z) {
        return -1;  // خطا: باز نشدن فایل ZIP
    }

    for (zip_int64_t i = 0; i < zip_get_num_entries(z, 0); i++) {
        const char *filename = zip_get_name(z, i, 0);
        if (!filename) continue;

        char path[1024];
        snprintf(path, sizeof(path), "%s/%s", output_dir, filename);

        struct zip_file *zf = zip_fopen_index(z, i, 0);
        FILE *f = fopen(path, "wb");

        if (zf && f) {
            char buffer[4096];
            zip_int64_t bytes_read;
            while ((bytes_read = zip_fread(zf, buffer, sizeof(buffer))) > 0) {
                fwrite(buffer, 1, bytes_read, f);
            }
        }

        if (zf) zip_fclose(zf);
        if (f) fclose(f);
    }

    zip_close(z);
    return 0;  // عملیات موفقیت‌آمیز
}