import time

class DateManager:
    @staticmethod
    def now_time():
        # دریافت زمان فعلی
        current_time = time.localtime()
        # ساختن یک تاریخ با فرمت "YYYY-MM-DD"
        current_date = f"{current_time.tm_year}-{current_time.tm_mon:02}-{current_time.tm_mday:02}"
        return current_date
