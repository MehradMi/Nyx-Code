import unittest
from tools.get_files_info import get_files_info, ToolReturnStatus

class TestGetFilesInfo(unittest.TestCase):

	def test_current_dir(self):
		result = get_files_info("calculator", ".")
		self.assertEqual(result, ToolReturnStatus.SUCCESS)

	def test_above_dir(self):
		result = get_files_info("calculator", "../")
		self.assertEqual(result, ToolReturnStatus.SUCCESS)
		
	def test_bin_dir(self):
		result = get_files_info("calculator", "/bin")
		self.assertEqual(result, ToolReturnStatus.SUCCESS)
		
	def test_pkg_dir(self):
		result = get_files_info("calculator", "pkg")
		self.assertEqual(result, ToolReturnStatus.SUCCESS)
		
	def test_main_file(self):
		result = get_files_info("calculator", "main.py")
		self.assertEqual(result, ToolReturnStatus.SUCCESS)

if __name__ == "__main__":
    unittest.main()