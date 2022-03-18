import unittest
import new_py_file


class NewFileTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(new_py_file.add(3, 4), 7)

    def test_divide(self):
        self.assertEqual(new_py_file.divide(6, 2), 3)
        # self.assertRaises(ValueError, new_py_file.divide, 10, 0)  # not so used in testing exceptions below
        with self.assertRaises(ValueError):  # preferred way of testing exception error catching
            new_py_file.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
