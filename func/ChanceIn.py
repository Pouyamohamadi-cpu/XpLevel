import time

class ChanceIn:
    @staticmethod
    def random():
        # استفاده از زمان فعلی به عنوان بذر (seed)
        current_time = int(time.time() * 1000)
        # تولید عدد تصادفی
        current_time = (current_time * 9301 + 49297) % 233280
        random_number = current_time / 233280.0
        return random_number
