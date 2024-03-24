import unittest,os

import sys
sys.path.append('../')

from data_access_layer.HighScoreRepository import *

class HighScoreRepositoryTest(unittest.TestCase):

    def test_reading_high_score_file(self):
        self.create_test_file("./test_high_score.csv")
        high_score_dict = read_highscore_from_file("./test_high_score.csv")
        self.assertEqual(high_score_dict["Krakon"], 1)
        self.assertEqual(high_score_dict["Bob"], 3)
        self.assertEqual(high_score_dict["Fred"], 10)

    def test_creating_new_high_score_file(self):
        test_file = "./test_high_score.csv"
        if os.path.exists(test_file):
            os.remove(test_file)
        write_highscore_to_file("./test_high_score.csv", "Krakon", 100)
        high_score_dict = read_highscore_from_file("./test_high_score.csv")
        self.assertEqual(high_score_dict["Krakon"], 100)

    def test_appending_high_score_to_file(self):
        test_file = "./test_high_score.csv"
        if os.path.exists(test_file):
            os.remove(test_file)
        write_highscore_to_file("./test_high_score.csv", "Krakon", 100)
        write_highscore_to_file("./test_high_score.csv", "Bob", 23)
        high_score_dict = read_highscore_from_file("./test_high_score.csv")
        self.assertEqual(high_score_dict["Krakon"], 100)
        self.assertEqual(high_score_dict["Bob"], 23)

    def create_test_file(self, file_name):
        if os.path.exists(file_name):
            os.remove(file_name)
        write_highscore_to_file(file_name, "Krakon", 1)
        write_highscore_to_file(file_name, "Bob", 3)
        write_highscore_to_file(file_name, "Fred", 10)

if __name__ == '__main__':
    unittest.main()

