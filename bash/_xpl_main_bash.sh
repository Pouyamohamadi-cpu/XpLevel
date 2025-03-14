#!/data/data/com.termux/files/usr/bin/bash
#!/bin/bash

xple() {
  if [ "$1" == "" ]; then
    python ~/XpLevel/xple_stdin.py
  else
    if [ "$1" == "--h" ]; then
    echo "--c >>> compile program."
    echo "--u >>> update"
    echo "--v >>> version"
    echo "--h >>> help"
    fi
    if [ "$1" == "--c" ]; then
      if [ "$2" == "" ]; then
        echo "Error: File Path is inaccessible."
      else
        truncate -s 0 lib-main/peep_emulator.xple
        
        filename="xpl_fikey.py"
        
        # پاک کردن از نوشتن استرینگ جدید
        truncate -s 0 "$filename"
        
        # استرینگ مورد نظر
        string="filepath = '$2'"
        
        # ایجاد و نوشتن استرینگ در فایل پایتون
        printf "$string" > "$filename"
        # نمایش پیامی که فایل ایجاد شده است
        YEL="\033[0;33m"
        BLUE='\033[0;34m'
        NC='\033[0m'
        ORG='\033[0;36m'
        echo -e "${ORG}"
        python XAllow.py
        echo -e "${NC}"
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
  fi
  if [ "$1" == "--u" ]; then
    echo "Downloading $3 version of xple-compiler... [START]"
    curl -L -o "XpLevel.zip" -H "User-Agent: Mozilla/5.0" "https://github.com/Pouyamohamadi-cpu/XpLevel/releases/download/XpLevel$3/XpLevel.zip" && echo "Download complete. Unzipping package..." && ./xple_vernew_installer.sh
  fi
}