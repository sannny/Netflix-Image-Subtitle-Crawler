import unittest
import sys
sys.path.insert(1, 'D:\\linux\\scratches\\Netflix_image_subtitle_crawler')
from srt_to_csv import * 

class final_inter_tests(unittest.TestCase):
    def test_None(self):
        with self.assertRaises(Exception):
            final_interval(None,None)
    
    def test_empty_left_list(self):
        ans = [[0.1, 1.7990000000000002],
                [1.8, 3.799],
                [3.8, 5.7989999999999995],
                [5.8, 7.8]]
        self.assertEqual(final_interval([],ans),ans)

    def test_empty_right_list(self):
        ans = [[0.1, 1.7990000000000002],
                [1.8, 3.799],
                [3.8, 5.7989999999999995],
                [5.8, 7.8]]
        self.assertEqual(final_interval(ans,[]),ans)

    def test_list_alphabet(self):
        input = [
                    ['abcd','bcddd'],
                    ['peta','cheat']
                ]
        input_2 = [
                    ['bbcd','ccddd'],
                    ['oeta','ckeat']
                ]
        with self.assertRaises(Exception):
            final_interval(input,input_2)
        
    def test_list(self):
        input = [1.1,1.5,1.3,1.9]
        input_2 = [1.2,1.4,1.7]
        with self.assertRaises(Exception):
            final_interval(input,input_2)
    
    def test_two_D_list(self):
        input = [
                    [0.1, 1.8],
                    [1.9, 3.8],
                    [4.8, 5.8],
                    [6.8, 7.8]
                ]
        input_2 = [
                    [0.6, 2.0],
                    [1.5, 3.5],
                    [7.8, 8.8],
                    [10.8, 11.8]
                ]
        ans = [
                [0.1, 1.8],
                [0.6, 2.0],
                [1.5, 3.5],
                [1.9, 3.8],
                [4.8, 5.8],
                [6.8, 7.8],
                [7.8, 8.8],
                [10.8, 11.8]
            ]
        self.assertEqual(final_interval(input,input_2),ans)
        
class merged_test(unittest.TestCase):
    def test_None(self):
        with self.assertRaises(Exception):
            merge(None) 

    def test_empty(self):
        ans = []
        self.assertEqual(merge(ans),ans)

    def test_alphabets(self):
        input = [
                    ['ab','bc'],
                    ['bd','cd'],
                    ['po','ed']
                ]
        with self.assertRaises(Exception):
            merge(input) 
    
    def test_one_blank_list(self):
        input = [
                    [],
                    [0.1, 1.8],
                    [0.6, 2.0],
                    [1.5, 3.5],
                    [1.9, 3.8],
                    [4.8, 5.8],
                    [6.8, 7.8],
                    [7.8, 8.8],
                    [10.8, 11.8]
                ]
        with self.assertRaises(Exception):
            merge(input) 
    
    def test_the_list(self):
        input = [
                    [0.1, 1.8],
                    [0.6, 2.0],
                    [1.5, 3.5],
                    [1.9, 3.8],
                    [4.8, 5.8],
                    [6.8, 7.8],
                    [7.8, 8.8],
                    [10.8, 11.8]
                ]
        
        ans = [
                [0.1,3.8],
                [4.8,5.8],
                [6.8,8.8],
                [10.8,11.8]
            ]

        self.assertEqual(merge(input),ans)

class putting_subs_together_tests(unittest.TestCase):
    def test_None(self):
        with self.assertRaises(Exception):
            putting_subs_together(None,None,None) 

    def test_empty(self):
        input = []
        ans = [['start_time', 'end_time', 'hindi', 'english']]
        self.assertEqual(putting_subs_together(input,[],[]),ans)
    
    def test_alphabet(self):
        input_en = [
                    ['ab', 1.8,convertSecondsToMinutes(0.1),convertSecondsToMinutes(1.8),'hey!'],
                    [1.9, 3.8,convertSecondsToMinutes(1.9),convertSecondsToMinutes(3.8),'How are you?'],
                    [6.8, 7.8,convertSecondsToMinutes(6.8),convertSecondsToMinutes(7.8),'Whats going on with you?']
                ]
        input_hing = [
                    ['cd', 2.0,convertSecondsToMinutes(0.6),convertSecondsToMinutes(2.0),'hey!'],
                    [1.5, 3.5,convertSecondsToMinutes(1.5),convertSecondsToMinutes(3.5),'kya haal hai?'],
                    [7.8, 8.8,convertSecondsToMinutes(7.8),convertSecondsToMinutes(8.8),'kya chal raha hai?'],
                ]
        interval = [
                ['ab',3.8],
                [6.8,8.8],
            ]       
        with self.assertRaises(Exception):
            putting_subs_together(interval,input_hing,input_en)

    def test_correct_case(self):
        input_en = [
                    [0.1, 1.8,convertSecondsToMinutes(0.1),convertSecondsToMinutes(1.8),'hey!'],
                    [1.9, 3.8,convertSecondsToMinutes(1.9),convertSecondsToMinutes(3.8),'How are you?'],
                    [6.8, 7.8,convertSecondsToMinutes(6.8),convertSecondsToMinutes(7.8),'Whats going on with you?']
                ]
        input_hing = [
                    [0.6, 2.0,convertSecondsToMinutes(0.6),convertSecondsToMinutes(2.0),'hey!'],
                    [1.5, 3.5,convertSecondsToMinutes(1.5),convertSecondsToMinutes(3.5),'kya haal hai?'],
                    [7.8, 8.8,convertSecondsToMinutes(7.8),convertSecondsToMinutes(8.8),'kya chal raha hai?'],
                ]
        interval = [
                [0.1,3.8],
                [6.8,8.8],
            ]       
        ans = [
                ['start_time', 'end_time', 'hindi', 'english'],
                [0.1,3.8,' hey! kya haal hai?',' hey! How are you?'],
                [6.8,8.8,' kya chal raha hai?',' Whats going on with you?'],
            ]
        self.assertEqual(putting_subs_together(interval,input_hing,input_en),ans)
