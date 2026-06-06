import os
from enum import Enum

class ToolReturnStatus(Enum):
    ERROR = 1
    SUCCESS = 2

def get_files_info(working_directory: str, directory: str = '.') -> ToolReturnStatus:
	try:
			working_dir_abs: str = os.path.abspath(working_directory)
			target_dir: str = os.path.normpath(os.path.join(working_dir_abs, directory))
			is_dir_valid: bool = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
			if not os.path.isdir(target_dir):
					print(f'Error: "{directory}" is not a directory')
					return ToolReturnStatus.ERROR

			if not is_dir_valid:
					print(f'''Error: Cannot list "{directory}" as it is outside the
								permitted working directory''')
					return ToolReturnStatus.ERROR

			print(f'Success: "{directory}" is within the working directory')

			entries_info: list[tuple] = []
			entries: list[str] = os.listdir(target_dir)
			for entry in entries:
				try:
					entry_size = os.path.getsize(os.path.join(target_dir,entry))
					is_entry_dir = os.path.isdir(os.path.join(target_dir,entry))
					entries_info.append((entry, entry_size, is_entry_dir))
				except Exception as e:
					print(f"ERROR: {e}")
			
			print(f'Results for {"current" if directory == "." else directory} directory:')
			for entry_info in entries_info:
				print(f'	- {entry_info[0]}: file_size={entry_info[1]} bytes, is_dir={entry_info[2]}')

			return ToolReturnStatus.SUCCESS

	except Exception as e:
			print(f'Error: {e}')
			return ToolReturnStatus.ERROR
