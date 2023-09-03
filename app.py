"""
create actual month folder
compile to exe via command:
pyinstaller --noconfirm --onefile --windowed  "main.py"
"""

from datetime import datetime
from enum import Enum
import os
from pathlib import Path
import sys
import shutil

class Month(Enum):
    """
    Month by it's number
    """

    DECEMBER = 12
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11

def check_folder(path):
    """
    check folder if it exists and create it
    """

    if not os.path.exists(path):
        os.mkdir(path)


CURRENT_YEAR = str(datetime.now().year)
CURRENT_MONTH_NUM = datetime.now().month
CURRENT_MONTH = Month(CURRENT_MONTH_NUM).name.capitalize()

SEPARATOR = os.path.sep
YEAR_PATH = SEPARATOR.join(["O:\\Miuruwa", CURRENT_YEAR])
MONTH_PATH = SEPARATOR.join(["O:\\Miuruwa", CURRENT_YEAR, CURRENT_MONTH])

check_folder(YEAR_PATH)
check_folder(MONTH_PATH)

OPEN_ACTUAL_FOLDER = len(sys.argv) == 1
MOVE_FILE_OR_DIR = len(sys.argv) == 2 and os.path.exists(sys.argv[1])


if OPEN_ACTUAL_FOLDER:
    os.startfile(MONTH_PATH)

elif MOVE_FILE_OR_DIR:
    file_name = Path(sys.argv[1]).name
    TARGET_PATH = SEPARATOR.join([MONTH_PATH, file_name])
    shutil.move(sys.argv[1], TARGET_PATH)
