"""
create actual month folder
compile to exe via command:
pyinstaller --noconfirm --onefile --windowed  "main.py"
"""

from .main import main


if __name__ == "__main__":
    main()
