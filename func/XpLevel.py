import sys
from PIL import Image, ImageShow

class InDisplay:
    @staticmethod
    def show(txt):
        print(txt)

    @staticmethod
    def object(txt):
        print(txt)
    def img(lo):
      # باز کردن عکس
      image = Image.open(lo)
      # نمایش عکس
      ImageShow.show(image)

class InImport:
    @staticmethod
    def caller(file):
        __import__(file)

def ma_in(txt):
    eval(txt)
    
def ifit(text1,shart,text2,dosome,elses,dosome2):
  if (shart == "equal"):
    if (text1 == text2):
      exec(dosome)
    else:
      exec(dosome2)

def func_factory(function_name, parameter_name, function_body):
    # قالب بندی کد فانکشن جدید
    function_code = f"def {function_name}({parameter_name}):\n"
    function_code += f"    {function_body}\n"
    
    # ایجاد محیط اجرایی و اجرای کد فانکشن جدید
    exec(function_code, globals())

# استفاده از func_factory برای ایجاد تابع hi
