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
        ans = [
                [0.1,1.1,'Hey! How are you?'],
                [1.1,1.9,'Hey! How are you?'],
                [1.8,2.8,'Simba wants to say, hi!'],
                [3.8,4.8,'They he is a big vagina cleaner.'],
                [5.8,6.8,'he is douche']
            ]
        self.assertEqual(getting_end_time(ans),([[0.1,
                                                    1.7990000000000002,
                                                    '0:00:00.100000',
                                                    '0:00:01.799000',
                                                    'Hey! How are you?'],
                                                [1.8, 3.799, '0:00:01.800000', '0:00:03.799000', 'Simba wants to say, hi!'],
                                                [3.8,
                                                    5.7989999999999995,
                                                    '0:00:03.800000',
                                                    '0:00:05.799000',
                                                    'They he is a big vagina cleaner.'],
                                                [5.8, 7.8, '0:00:05.800000', '0:00:07.800000', 'he is douche']],
                                                [[0.1, 1.7990000000000002],
                                                [1.8, 3.799],
                                                [3.8, 5.7989999999999995],
                                                [5.8, 7.8]]
                                                )
                            )
        


if __name__ == '__main__':
    unittest.main()