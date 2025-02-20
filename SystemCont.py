import os

# لیستی برای ذخیره آرگومان‌های خط فرمان
argv = []
class InSystemCont:
  def ReadArgv():
    global argv
    argv = os.sys.argv
  def exit():
    SystemCont.os.sys.exit(1)

class out(Exception):
    def __init__(self, code=0):
        self.code = code

def exitcode(code=0):
    raise exitcode(code)
    
#finshed xpde.