#!/bin/bash
echo "Setup the lib for install..."
echo "----------------------------"
echo "install by system info with os name : $(uname -o) in select great package downloaders."
echo "----------------------------"
echo "test for be in windows."
echo "install by system info with os name : Windows (not supported in this version)."
echo "windows doesn't support in the you downloaded version of XpLevel."

conh=$(uname -o)
if [ "$conh" = "Android" ]; then
    echo "Termux Mode selected. Xplevel will install with pkg."
    pkg install python
    pkg install brainfuck
    pkg install nano
    echo "----------------------------"
    echo "Checking Python installation..."
    pyver=$(python3 --version 2>/dev/null)
    if [[ "$pyver" == *"Python 3.12.9"* ]]; then
        echo "Python is installed and verified."
        echo "----------------------------"
        echo "Checking Nano installation..."
        nak=$(nano --version 2>/dev/null)
        if echo "$nak" | grep -q "GNU nano, version 8.3"; then
            echo "Nano with version 8.3 is installed and verified."
            echo "----------------------------"
            echo "Adding Xplevel to .bashrc"
            if [ -f ~/.bashrc ]; then
                echo "Found .bashrc file. Proceeding..."
            else
                echo ".bashrc not found. Creating it..."
                touch ~/.bashrc
            fi
            script_dir=$(dirname "$(readlink -f "$0")")
            echo "XpLevel directory: $script_dir"
            cp -r "$script_dir" ~
            echo "source ~/XpLevel/_xpl_main_bash.sh" >> ~/.bashrc
            echo "Testing Xplevel installation..."
            source ~/XpLevel/_xpl_main_bash.sh
            xple_ver=$(xple --v 2>/dev/null | grep "XpLevel 2.3")
            if [[ "$xple_ver" == *"XpLevel 2.3"* ]]; then
                echo "XpLevel installed successfully with version 2.3."
                exit
            else
                echo "XpLevel installation failed. Please check compatibility."
            fi
        else
            echo "Nano installation failed or version mismatch!"
        fi
    else
        echo "Python installation failed or version mismatch!"
    fi
elif [ "$conh" = "windows" ]; then
    echo "Error: Windows is not supported."
elif [ "$conh" = "GNU/Linux" ]; then
    echo "Linux Bash Mode selected. Xplevel will install with sudo."
    sudo apt update
    sudo apt install python3
    sudo apt install bf
    sudo apt install nano
    echo "----------------------------"
    echo "Checking Python installation..."
    pyver=$(python3 --version 2>/dev/null)
    if [[ "$pyver" == *"Python 3.12.9"* ]]; then
        echo "Python is installed and verified."
        echo "----------------------------"
        echo "Checking Nano installation..."
        nak=$(nano --version 2>/dev/null)
        if echo "$nak" | grep -q "GNU nano, version 8.3"; then
            echo "Nano with version 8.3 is installed and verified."
            echo "----------------------------"
            echo "Adding Xplevel to .bashrc"
            if [ -f ~/.bashrc ]; then
                echo "Found .bashrc file. Proceeding..."
            else
                echo ".bashrc not found. Creating it..."
                touch ~/.bashrc
            fi
            script_dir=$(dirname "$(readlink -f "$0")")
            echo "XpLevel directory: $script_dir"
            cp -r "$script_dir" ~
            echo "source ~/XpLevel/_xpl_main_bash.sh" >> ~/.bashrc
            echo "Testing Xplevel installation..."
            source ~/XpLevel/_xpl_main_bash.sh
            xple_ver=$(xple --v 2>/dev/null | grep "XpLevel 2.3")
            if [[ "$xple_ver" == *"XpLevel 2.3"* ]]; then
                echo "XpLevel installed successfully with version 2.3."
                exit
            else
                echo "XpLevel installation failed. Please check compatibility."
            fi
        else
            echo "Nano installation failed or version mismatch!"
        fi
    else
        echo "Python installation failed or version mismatch!"
    fi
else
    echo "Unknown system! Please check compatibility."
fi