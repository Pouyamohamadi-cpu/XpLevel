import re
from XpLevel import *
from DateManager import *
from ChanceIn import *
from ConnectionManager import *
from ReportsManager import *
from termcolor import colored
from FileManager import *
from StringManager import *
from MathFunction import *
from Casi import *
from PyInXple import *
from StorageManager import *
from SSLComm import *
from VPNLib import *
from E2EE import *
from GPSLib import *
from soso import *
from peep import *
import os

search_text = '      createMain'
funcm = '@'

class Color:
    @staticmethod
    def content(text, yaa, xcx):
        if text == "text":
            coloredtext = colored(yaa, xcx)
            print(coloredtext)

class InUser:
    @staticmethod
    def inputer():
        return input()

def func_factory(function_name, parameter_name, function_body):
    function_code = f"def {function_name}({parameter_name}):\n"
    function_code += f"    {function_body}\n"
    exec(function_code, globals())
    
with open('importlist.txt','r') as nmnk:
  nkn = nmnk.read()
  
def replace_outside_strings(text, old, new):
    string_pattern = r'\".*?\"|\'.*?\''
    parts = re.split(string_pattern, text)
    strings = re.findall(string_pattern, text)

    new_parts = []
    for part in parts:
        new_parts.append(re.sub(r'{}'.format(re.escape(old)), new, part))
    
    result = ''
    for i in range(len(new_parts)):
        result += new_parts[i]
        if i < len(strings):
            result += strings[i]
    
    return result

class ImportManager:
    @staticmethod
    def clean_import_emulator():
        with open("import_emulator.py", "w") as file:
            file.write("")

    @staticmethod
    def xple(filepath):
      
        ImportManager.clean_import_emulator()

        with open(filepath, 'r') as file:
            content = file.read()
        try:
            content = replace_outside_strings(content, 'storio [Instr] ', '')
            
            if search_text in content:
                content = content.replace("\n          ", "").replace("\n      createMain\n", "'")
                
                if "      endMain" in content:
                    content = content.replace("\n      endMain\n", "'")
                    content = replace_outside_strings(content,'storio [recall] ','return ')
                    content = replace_outside_strings(content, 'createFn', 'def')
                    content = replace_outside_strings(content, 'startCreation', ':')
                    content = replace_outside_strings(content,'std [onMain] ','onMainModule')
                    content = replace_outside_strings(content, '[', '(')
                    content = replace_outside_strings(content, ']', ')')
                    content = replace_outside_strings(content, 'ifit', 'if')
                    content = replace_outside_strings(content, 'jump ','else')
                    content = replace_outside_strings(content, 'initLoopFor', 'for')
                    content = replace_outside_strings(content, 'initLoop', 'loop')
                    content = replace_outside_strings(content, 'initWhile', 'while')
                    content = replace_outside_strings(content, 'inside', 'in')
                    content = replace_outside_strings(content, 'initCls', 'class')
                    mkhmb = ["if", "ifit", "initWhile", "initCls", "createFn", "initLoop", "loop", "while", "for", "class", "def"]
                    if any(keyword in content for keyword in mkhmb):
                        if "endCreation" in content:
                            content = replace_outside_strings(content, 'endCreation', '')
                            with open('import_emulator.py', 'w') as mss:
                              mss.write(nkn+content)
                        else:
                            print(colored("An error occurred: in the file, You don't close Your function with <endCreation>", "red"))
                    else:
                        with open('import_emulator.py', 'w') as mss:   mss.write(nkn+content)
            else:
                print(colored("An error occurred:", 'red') + "\n" + "for start xpl Program add ma_in func.")
        except Exception as e:
            if isinstance(e, TypeError):
                print(colored("An error occurred: Type Error in Xpl Program", 'red'))
            else:
                if str(e) == "name 'contents1' is not defined":
                    print(colored("An error occurred:", 'red') + "\n" + "Use An Email Speech in Your code.")
                else:
                    print(colored("An error occurred:", 'red') + "\n" + str(e))