import os
from enum import Enum

class ToolReturnStatus(Enum):
    ERROR = 1
    SUCCESS = 2

def get_files_info(working_directory: str, directory: str = '.') -> ToolReturnStatus:
    try:
        working_dir_abs: str = os.path.abspath(working_directory)
        target_dir: str = os.path.normpath(
            os.path.join(working_dir_abs, directory))
        is_dir_valid: bool = os.path.commonpath(
            [working_dir_abs, target_dir]) == working_dir_abs
        if not os.path.isdir(directory):
            print(f'Error: "{directory}" is not a directory')
            return ToolReturnStatus.ERROR
        if not is_dir_valid:
            print(f'''Error: Cannot list "{directory}" as it is outside the
                  permitted working directory''')
            return ToolReturnStatus.ERROR
        print(f'Success: "{directory}" is within the working directory')
        return ToolReturnStatus.SUCCESS
    except Exception as e:
        print(f'Error: {e}')
        return ToolReturnStatus.ERROR

