from xpl_fikey import *
from xpl_compile_mainer import *
from termcolor import colored

# تعریف کلمات کلیدی ممنوعه
forbidden_keywords = [
    # کلمات کلیدی پایتون
    "False", "None", "True", "and", "as", "assert", "async", "await", "break",
    "class", "continue", "def", "del", "elif", "else", "except", "finally",
    "for", "from", "global", "if", "import", "in", "is", "lambda", "nonlocal",
    "not", "or", "pass", "raise", "return", "try", "while", "with", "yield",

    # نام‌های رزرو شده
    "self", "__init__", "super",

    # توابع داخلی پایتون
    "abs", "all", "any", "bin", "bool", "bytearray", "bytes", "callable",
    "chr", "classmethod", "compile", "complex", "delattr", "dict", "dir",
    "divmod", "enumerate", "eval", "exec", "filter", "float", "format",
    "frozenset", "getattr", "globals", "hasattr", "hash", "help", "hex",
    "id", "input", "int", "isinstance", "issubclass", "iter", "len", "list",
    "locals", "map", "max", "memoryview", "min", "next", "object", "oct",
    "open", "ord", "pow", "print", "property", "range", "repr", "reversed",
    "round", "set", "setattr", "slice", "sorted", "staticmethod", "sum",
    "tuple", "type", "vars", "zip", "__import__",

    # سایر نام‌های رزرو شده
    "BaseException", "Exception", "ArithmeticError", "BufferError",
    "LookupError", "AssertionError", "AttributeError", "EOFError",
    "FloatingPointError", "GeneratorExit", "ImportError", "ModuleNotFoundError",
    "IndexError", "KeyError", "KeyboardInterrupt", "MemoryError", "NameError",
    "NotImplementedError", "OSError", "OverflowError", "RecursionError",
    "ReferenceError", "RuntimeError", "StopIteration", "SyntaxError",
    "IndentationError", "TabError", "SystemError", "SystemExit", "TypeError",
    "UnboundLocalError", "UnicodeError", "UnicodeEncodeError",
    "UnicodeDecodeError", "UnicodeTranslateError", "ValueError",
    "ZeroDivisionError",

    # پرانتزها
    "(", ")"
]

# تابع برای بررسی کدها و نادیده گرفتن کلمات کلیدی درون رشته‌ها
def is_valid_code(code):
    import re
    # الگوی برای شناسایی رشته‌ها
    string_pattern = r'\".*?\"|\'.*?\''

    # یافتن تمام رشته‌ها و جایگزینی آن‌ها با مقدار خالی
    code_without_strings = re.sub(string_pattern, '', code)

    # الگوی جدید برای شناسایی کاراکترهای غیرالفبایی و ترکیب آن‌ها با کلمات کلیدی
    token_pattern = r'(\b\w+\b)|[^a-zA-Z0-9_()]'

    lines = code_without_strings.split('\n')
    for line in lines:
        # تقسیم بر اساس الگوی جدید
        tokens = re.split(token_pattern, line)
        for token in tokens:
            if token in forbidden_keywords:
                return False, token
    return True, None

# تابع برای بررسی و چاپ نتیجه
def check_code(code):
    valid, keyword = is_valid_code(code)
    if valid:
        runit()
    else:
        errortxt = f"Code is invalid: Unknow keyword '{keyword}' found. this keyword is not for XpLevel."
        colored_text = colored("An error occurred:", 'red')
        print(colored_text + "\n" + errortxt)

# خواندن فایل و بررسی کد
with open(filepath, 'r') as filecn:
    filebt = filecn.read()
check_code(filebt)