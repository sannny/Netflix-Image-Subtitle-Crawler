from cleaning_hindi_csv_tests import * 
from imageToText_tests import * 
from srt_to_csv_tests import *
import coverage
cov = coverage.Coverage()
cov.start()

if __name__ == '__main__':
    tests = cropping_img_tests()
    tests.test_None()
    tests.test_emptyList()
    tests.test_alphabets()
    tests.test_numeric()

    getting_end_time_test = getting_end_time_tests()
    getting_end_time_test.test_None()
    getting_end_time_test.test_empty_list()
    getting_end_time_test.test_vals()

    convertSecondsToMinutesTests = convertSecondsToMinutesTest()
    convertSecondsToMinutesTests.test_None()
    convertSecondsToMinutesTests.test_time_sec()
    convertSecondsToMinutesTests.test_time()
    convertSecondsToMinutesTests.test_time_secs()

    final_inter_test = final_inter_tests()
    final_inter_test.test_None()
    final_inter_test.test_empty_left_list()
    final_inter_test.test_two_D_list()
    final_inter_test.test_empty_right_list()
    final_inter_test.test_list_alphabet()
    final_inter_test.test_list()

    merged_tests = merged_test()
    merged_tests.test_None()
    merged_tests.test_empty()
    merged_tests.test_alphabets()
    merged_tests.test_one_blank_list()
    merged_tests.test_the_list()

    putting_subs_together_test = putting_subs_together_tests()
    putting_subs_together_test.test_empty()
    putting_subs_together_test.test_None()
    putting_subs_together_test.test_alphabet()
    putting_subs_together_test.test_correct_case()

cov.stop()
cov.save()

cov.html_report()