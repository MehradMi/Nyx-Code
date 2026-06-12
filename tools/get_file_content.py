import os

MAX_CHARS: int = 10000 # TODO: move this to config.py

def get_file_content(working_directory: str, file_path: str) -> str:
	working_dir_abs_path = os.path.abspath(working_directory)
	file_abs_path = os.path.normpath(os.path.join(working_dir_abs_path, file_path))

	is_fpath_valid: bool = os.path.commonpath([working_dir_abs_path, file_abs_path]) == working_dir_abs_path
	if not is_fpath_valid:
		return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
	
	is_file_valid: bool = os.path.isfile(file_abs_path)
	if not is_file_valid:
		return f'Error: File not found or is not a regular file: "{file_path}"'
	
	try:
		with open(file_abs_path, "r") as f:
			file_content: str = f.read(MAX_CHARS)

			# try reading one more character
			# to see if we have already reached the EOF or not
			if f.read(1):
				file_content += f'...File "{file_abs_path}" truncated at {MAX_CHARS} characters'

			return file_content
	except Exception as e:
		return f'Error: failed to open/read the file: {e}'

