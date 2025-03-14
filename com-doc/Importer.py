from xpl_fikey import filepath
from ImportFunc import *
from termcolor import colored

# تعریف کلمات کلیدی ممنوعه
forbidden_keywords = [
    "False", "None", "True", "and", "as", "assert", "async", "await", "break",
    "class", "continue", "def", "del", "elif", "else", "except", "finally",
    "for", "from", "global", "if", "import", "in", "is", "lambda", "nonlocal",
    "not", "or", "pass", "raise", "return", "try", "while", "with", "yield",
    "self", "__init__", "super",
    "abs", "all", "any", "bin", "bool", "bytearray", "bytes", "callable",
    "chr", "classmethod", "compile", "complex", "delattr", "dict", "dir",
    "divmod", "enumerate", "eval", "exec", "filter", "float", "format",
    "frozenset", "getattr", "globals", "hasattr", "hash", "help", "hex",
    "id", "input", "int", "isinstance", "issubclass", "iter", "len", "list",
    "locals", "map", "max", "memoryview", "min", "next", "object", "oct",
    "open", "ord", "pow", "print", "property", "range", "repr", "reversed",
    "round", "set", "setattr", "slice", "sorted", "staticmethod", "str", "sum",
    "tuple", "type", "vars", "zip", "__import__",
    "BaseException", "Exception", "ArithmeticError", "BufferError",
    "LookupError", "AssertionError", "AttributeError", "EOFError",
    "FloatingPointError", "GeneratorExit", "ImportError", "ModuleNotFoundError",
    "IndexError", "KeyError", "KeyboardInterrupt", "MemoryError", "NameError",
    "NotImplementedError", "OSError", "OverflowError", "RecursionError",
    "ReferenceError", "RuntimeError", "StopIteration", "SyntaxError",
    "IndentationError", "TabError", "SystemError", "SystemExit", "TypeError",
    "UnboundLocalError", "UnicodeError", "UnicodeEncodeError",
    "UnicodeDecodeError", "UnicodeTranslateError", "ValueError",
    "ZeroDivisionError"
]

# تابع برای بررسی کدها و نادیده گرفتن کلمات کلیدی درون رشته‌ها
def is_valid_code(code):
    import re
    # الگوی برای شناسایی رشته‌ها
    string_pattern = r'\".*?\"|\'.*?\''
    # یافتن تمام رشته‌ها و جایگزینی آن‌ها با مقدار خالی
    code_without_strings = re.sub(string_pattern, '', code)
    lines = code_without_strings.split('\n')
    for line in lines:
        tokens = re.findall(r'\b\w+\b', line)
        for token in tokens:
            if token in forbidden_keywords:
                return False, token
    return True, None

# تابع برای بررسی و چاپ نتیجه
def xpleImport(filepath):
    with open(filepath, 'r') as fileco:
      filemn = fileco.read()
    valid, keyword = is_valid_code(filemn)
    if valid:
        ImportManager.xple(filepath)
    else:
        errortxt = f"Code is invalid: Unknown keyword '{keyword}' found. This keyword is not for XpLevel."
        colored_text = colored("An error occurred:", 'red')
        print(colored_text + "\n" + errortxt)
        
