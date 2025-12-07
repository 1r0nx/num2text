#!/usr/bin/bash

pyinstaller --onefile --name bin2text src/bin2text.py
pyinstaller --onefile --name octal2text src/octal2text.py
pyinstaller --onefile --name ascii2text src/ascii2text.py
pyinstaller --onefile --name hex2text src/hex2text.py

