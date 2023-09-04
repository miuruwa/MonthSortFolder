"""
create actual month folder
"""

import os
import shutil
import sys

from utils import get_target_path, is_move_files


def main():
    """
    main function
    """

    target_path = get_target_path()

    is_open = len(sys.argv) == 1
    is_move = is_move_files()

    if is_open:
        os.startfile(target_path)

    elif is_move:
        mapped_paths = map(get_target_path, sys.argv[1:])

        for original_path, target_path in zip(sys.argv[1:], mapped_paths):
            shutil.move(original_path, target_path)

if __name__ == "__main__":
    main()