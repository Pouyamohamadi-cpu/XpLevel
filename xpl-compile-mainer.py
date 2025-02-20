filepath = '/storage/emulated/0/my_program.xpl'
from XpLevel import *
#import all XpLevels functions.
# نام فایل و متنی که باید جستجو شود
search_text = '      *st'
def func_factory(function_name, parameter_name, function_body):
    # قالب بندی کد فانکشن جدید
    function_code = f"def {function_name}({parameter_name}):\n"
    function_code += f"    {function_body}\n"
    
    # ایجاد محیط اجرایی و اجرای کد فانکشن جدید
    exec(function_code, globals())

# استفاده از func_factory برای ایجاد تابع hi
# باز کردن فایل در حالت خواندن
with open(filepath, 'r') as file:
    # خواندن محتوای فایل
    content = file.read()

# بررسی وجود متن در فایل
if search_text in content:
  content21 = content.replace("\n          ","")
  content2 = content21.replace("\n      *st\n","'")
  if "      rt*" in content2:
    content3 = content2.replace("\n      rt*\n","'")
    if "func factory?" in content3:
      content4 = content3.replace("func factory?","func_factory(")
      if ";" in content4:
        content5 = content4.replace(";",")")
        if "ifit ?" in content5:
          if " ?\n" in content5:
            content6 = content5.replace("ifit ?","ifit(")
            content7 = content6.replace(" ?\n","):")
            exec(content7)
          else:
            exec(content5)
        else:
          exec(content5)
      else:
        exec(content4)
    else:
      if "ifit" in content3:
        content4 = content3.replace("ifit ?","if( ")
        content5 = content4.replace(" ?"," ):")
        exec(content5)
      else:
        exec(content3)
  else:
    exec(content2)
else:
  print("E")
    