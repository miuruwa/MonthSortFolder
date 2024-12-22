@echo off
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed  "./app/main.py"