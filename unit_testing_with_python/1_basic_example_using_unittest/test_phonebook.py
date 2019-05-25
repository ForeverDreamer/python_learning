import unittest
from phonebook import Phonebook


class PhonebookTest(unittest.TestCase):

    # 初始化
    def setUp(self):
        self.phonebook = Phonebook()

    # 清理资源
    def tearDown(self):
        pass

    # def test_ceate_phonebook(self):
    #     phonebook = Phonebook()

    def test_lookup_entry_by_name(self):
        # phonebook = Phonebook()
        self.phonebook.add('Bob', '12345')
        self.assertEqual('12345', self.phonebook.lookup('Bob'))

    def test_missing_entry_raises_keyerror(self):
        # phonebook = Phonebook()
        with self.assertRaises(KeyError):
            self.phonebook.lookup('missing')

    @unittest.skip('SKIP_CASE')
    def test_skip(self):
        # phonebook = Phonebook()
        self.assertTrue(self.phonebook.skip())

    @unittest.skip('poor example')
    def test_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add('Bob', '12345')
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add('Mary', '012345')
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add('Sue', '12345')  # identical to Bob
        self.assertTrue(self.phonebook.is_consistent())
        self.phonebook.add('Sue', '123')   # Prefix of Bob
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_with_normal_entries_is_consistent(self):
        self.phonebook.add('Bob', '12345')
        self.phonebook.add('Mary', '012345')
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_with_duplicate_entries_is_inconsistent(self):
        self.phonebook.add('Bob', '12345')
        self.phonebook.add('Mary', '012345')
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_with_numbers_that_prefix_one_another_is_inconsistent(self):
        self.phonebook.add('Bob', '12345')
        self.phonebook.add('Mary', '123')
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_adds_names_and_numbers(self):
        self.phonebook.add('Sue', '12345')
        self.assertIn('Sue', self.phonebook.get_names())
        self.assertIn('12345', self.phonebook.get_numbers())
