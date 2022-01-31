import unittest
from main import get_info_of_valid_password, calculate


class TestInfoOfValidPass(unittest.TestCase):

    def test_import_count_valid_pass_true(self):
        self.assertTrue(get_info_of_valid_password('a 1-5: abcdj'))

    def test_import_count_valid_pass_false(self):
        self.assertFalse(get_info_of_valid_password('z 2-4: asfalseiruqwo'))

    def test_import_count_valid_pass_regex(self):
        self.assertFalse(get_info_of_valid_password('z 24: asfalseiruqwo'))

    def test_import_count_invalid_pass_regex(self):
        self.assertFalse(get_info_of_valid_password('a 2-4: azaazaaz'))


class TestCalculate(unittest.TestCase):

    def test_calculate_valid(self):
        self.assertEqual(calculate('data_test.txt'), '3')

    def test_calculate_file_not_found(self):
        self.assertEqual(calculate('data_tes.txt'), 'File not found')

    def test_calculate_type_invalid(self):
        self.assertEqual(type(calculate('data_test.txt')), str)
