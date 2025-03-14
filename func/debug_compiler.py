import re
import time
from termcolor import colored
from xpl_fikey import filepath
from XpLevel import *
from DateManager import *
from ChanceIn import *
from ConnectionManager import *
from ReportsManager import *
from FileManager import *
from StringManager import *
from Importer import *
from import_emulator import *
from MathFunction import *
from Casi import *
from PyInXple import *
from EmPy import *
from StorageManager import *

start_time = time.time()

search_text = '      createMain'
funcm = '@'

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

def runit():
    with open(filepath, 'r') as file:
        content = file.read()
        try:
            content = replace_outside_strings(content, 'storio [Instr] ', '')
            
            if search_text in content:
                content = content.replace("\n          ", "").replace("\n      createMain\n", "'")
                
                if "      endMain" in content:
                    content = content.replace("\n      endMain\n", "'")
                    content = replace_outside_strings(content, 'createFn', 'def')
                    content = replace_outside_strings(content, 'startCreation', ':')
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
                            print(content)
                        else:
                            print(colored("An error occurred: in the file, You don't close Your function with <endCreation>", "red"))
                    else:
                        print(content)
            else:
                print(colored("An error occurred:", 'red') + "\nfor start xple Program add ma_in func.")
        except Exception as e:
            if "TypeError" in str(e):
                print(colored("An error occurred: Type Error in Xple Program", 'red'))
            else:
                ervg = "name 'contents1' is not defined"
                em = str(e)
                if ervg == em:
                    print(colored("An error occurred:", "red") + "\nUse An Email Speech in Your code.")
                else:
                    print(colored("An error occurred:", 'red') + "\n" + str(e))