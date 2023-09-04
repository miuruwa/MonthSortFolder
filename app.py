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

    if len(sys.argv) < 2:
        return False

    return False not in map(os.path.exists, sys.argv[1:])


def get_target_path(object_path: str = None):
    """
    get path to folder that needed to be opened or to move to  
    if object path is given then returns new path after moving process  
    """

    current_year, current_month = get_current_date()

    year_path = get_path(current_year)
    check_folder(year_path)

    if object_path:
        object_name = Path(object_path).name
        return get_path(current_year, current_month, object_name)

    month_path = get_path(current_year, current_month)
    check_folder(month_path)

    return month_path


def main():
    """
    main function
    """

    target_path = get_target_path()

    is_open = len(sys.argv) == 1
    is_move = is_move_multiple()

    if is_open:
        os.startfile(target_path)

    elif is_move:
        mapped_paths = map(get_target_path, sys.argv[1:])

        for original_path, target_path in zip(sys.argv[1:], mapped_paths):
            shutil.move(original_path, target_path)


if __name__ == "__main__":
    main()
