import unittest
from cleaning_hindi_csv import *

class convertSecondsToMinutesTest(unittest.TestCase):
    def test_None(self):
        ans  = None
        with self.assertRaises(Exception):
            convertSecondsToMinutes(ans)
    
    def test_time_sec(self):
        ans = 180.724000
        self.assertEqual(convertSecondsToMinutes(ans),'0:03:00.724000')

    def test_time(self):
        ans = '00:02:30.724000'
        with self.assertRaises(Exception):
            convertSecondsToMinutes(ans)

    def test_time_sec(self):
        ans = 170
        self.assertEqual(convertSecondsToMinutes(ans),'0:02:50')

class getting_end_time_tests(unittest.TestCase):
    def test_None(self):
        ans  = None
        with self.assertRaises(Exception):
            getting_end_time(ans)
    
    def test_empty_list(self):
        ans = []
        self.assertEqual(getting_end_time(ans),([],[]))

    def test_vals(self):
        ans = [[0.1,1.9,'Hey! How are you?']]
        self.assertEqual(getting_end_time(ans),([],[]))

if __name__ == '__main__':
    unittest.main()