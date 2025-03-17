#include <stdio.h>
#include <string.h>

// تعریف تابع برای ساخت USSD code
void createUSSDCode(const char *baseCode, const char *param, char *output) {
    // ترکیب baseCode و پارامتر وارد شده
    strcpy(output, baseCode);
    
    if (param != NULL && strlen(param) > 0) {
        strcat(output, "*");
        strcat(output, param);
    }
    
    strcat(output, "#");  // تکمیل USSD Code با #
}