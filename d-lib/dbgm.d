import std.stdio;
import std.file;
import std.conv;

// ساختار هدر BMP
struct BMPHeader {
    ubyte[2] fileType; // Fixed-size array syntax
    uint fileSize;
    ushort reserved1;
    ushort reserved2;
    uint offset;
}

// ساختار هدر DIB
struct DIBHeader {
    uint headerSize;
    int width;
    int height;
    ushort planes;
    ushort bitsPerPixel;
    uint compression;
    uint imageSize;
    int xPixelsPerMeter;
    int yPixelsPerMeter;
    uint colorsUsed;
    uint importantColors;
}

// تابع برای خواندن فایل BMP و نمایش آن
export void displayBMP(const string fileName) {
    // خواندن فایل BMP
    auto data = cast(ubyte[]) read(fileName);

    // خواندن هدر BMP
    BMPHeader bmpHeader = *cast(BMPHeader*) data.ptr;
    std.stdio.writeln("File Size: ", bmpHeader.fileSize, " bytes");
    std.stdio.writeln("Pixel Offset: ", bmpHeader.offset);

    // خواندن هدر DIB
    DIBHeader dibHeader = *cast(DIBHeader*) (data.ptr + BMPHeader.sizeof);
    // بررسی اینکه تصویر رنگی باشد
    if (dibHeader.bitsPerPixel != 24) {
        std.stdio.writeln("This program only supports 24-bit BMP images.");
        return;
    }

    // خواندن داده‌های پیکسل‌ها
    int width = dibHeader.width;
    int height = dibHeader.height;
    int offset = bmpHeader.offset;

    for (int y = height - 1; y >= 0; y--) { // BMP از پایین به بالا ذخیره می‌شود
        for (int x = 0; x < width; x++) {
            // هر پیکسل شامل 3 بایت است (RGB)
            int pixelIndex = offset + (y * width + x) * 3;
            ubyte blue = data[pixelIndex];
            ubyte green = data[pixelIndex + 1];
            ubyte red = data[pixelIndex + 2];

            // کدهای ANSI برای تغییر رنگ متن
            string colorCode = "\x1b[38;2;" ~ to!string(red) ~ ";" ~ to!string(green) ~ ";" ~ to!string(blue) ~ "m";

            // نمایش پیکسل با رنگ مربوطه
            std.stdio.write(colorCode, "█");
        }
        std.stdio.writeln("\x1b[0m"); // بازنشانی رنگ به حالت پیش‌فرض
    }
}