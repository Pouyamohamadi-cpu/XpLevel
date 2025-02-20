XPL() {
  if [ "$1" == "" ]; then
    echo "Help Center"
    echo "For Source Code Visit http://z7.ct.ws/xplevel/source"
    echo "----------------"
    echo "XPL --v"
    echo "show xpl version installed in system"
    echo "----------------"
    echo "XPL --c"
    echo "compile your xpl program and show result (with py)"
    echo "----------------"
    echo "XPL --c to --bitc"
    echo "compile code to bit code (good for copyright programs)"
    echo "----------------"
    echo "XPL --c for --ios"
    echo "Make your program to swift codes for run in iOS."
  else
    if [ "$1" == "--c" ]; then
      if [ "$2" == "" ]; then
        echo "Error: File Path is inaccessible."
      else
        #!/bin/bash

        filename="xpl-compile-mainer.py"
        
        # استرینگ مورد نظر
        string="filepath = '$2'"
        
        # ایجاد و نوشتن استرینگ در فایل پایتون
        echo $string > $filename
        
        # نمایش پیامی که فایل ایجاد شده است
        echo "File $filename has been created with the filepath: $2"
        python xpl-compile-mainer.py
      fi
    fi
  fi
  if [ "$1" == "--v" ]; then
  echo "XpLevel Proglang Compiler."
  echo "Bash Mode - BM"
  echo "Version XPL-COMPILER-PY : 1.0"
  echo "Version XPL-SERVICE-SH : 1.1"
  echo "Version XPL-MEMORY-PY : 0.1"
  echo "Version XPL-MAINCODE-PYSH : 2.1"
  else
  echo "$1"" Comment not found in XPL Main bash scripts."
  fi
}