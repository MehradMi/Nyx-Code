import unittest
from tools.get_file_content import get_file_content

class TestGetFileContent(unittest.TestCase):
	def test_lorem(self):
		result = get_file_content("calculator", "lorem.txt")
		self.assertNotIn("Error", result)
	
	def test_main_file(self):
		result = get_file_content("calculator", "main.py")
		self.assertNotIn("Error", result)

	def test_calculator_file(self):
		result = get_file_content("calculator", "pkg/calculator.py")
		self.assertNotIn("Error", result)
	
	def test_cat_file(self):
		result = get_file_content("calculator", "/bin/cat")
		self.assertNotIn("Error", result)

	def test_doesnotexist_file(self):
		result = get_file_content("calculator", "pkg/does_not_exist.py")
		self.assertNotIn("Error", result)

if __name__ == "__main__":
	unittest.main()