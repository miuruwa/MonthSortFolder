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


def get_current_date():
    """
    Get current year and month
    """

    moment = datetime.now()

    current_year = str(moment.year)
    current_month_num = moment.month
    current_month_enum = Month(current_month_num)
    current_month = current_month_enum.name.capitalize()

    return current_year, current_month


def get_path(*args):
    """
    get path by keywords
    """

    target_folder = os.getcwd()
    response = os.path.join(target_folder, *args)

    return response


def check_folder(path):
    """
    check folder if it exists and create it
    """

    if not os.path.exists(path):
        os.mkdir(path)


def is_move_multiple():
    """
    check if multiple paths needed to be moved and check for exist    
    """

    if len(sys.argv) <= 2:
        return False

    return False not in map(os.path.exists, sys.argv[1:])


def get_target_path(path: str):
    """
    get target path for given object path
    """

    object_name = Path(path).name
    return get_path(CURRENT_YEAR, CURRENT_MONTH, object_name)


CURRENT_YEAR, CURRENT_MONTH = get_current_date()

YEAR_PATH = get_path(CURRENT_YEAR)
MONTH_PATH = get_path(CURRENT_YEAR, CURRENT_MONTH)

check_folder(YEAR_PATH)
check_folder(MONTH_PATH)

OPEN_ACTUAL_FOLDER = len(sys.argv) == 1
MOVE_FILE_OR_DIR = len(sys.argv) == 2 and os.path.exists(sys.argv[1])
IS_MOVE_MULTIPLE = is_move_multiple()

if OPEN_ACTUAL_FOLDER:
    os.startfile(MONTH_PATH)

elif MOVE_FILE_OR_DIR:
    file_name = Path(sys.argv[1]).name
    TARGET_PATH = get_path(CURRENT_YEAR, CURRENT_MONTH, file_name)
    shutil.move(sys.argv[1], TARGET_PATH)

elif IS_MOVE_MULTIPLE:
    mapped_paths = map(get_target_path, sys.argv[1:])

    for original_path, target_path in zip(sys.argv[1:], mapped_paths):
        shutil.move(original_path, target_path)
