# Tests for week 5 notebook

import pandas as pd
import warnings

warnings.simplefilter(action="ignore")


class tester:
    def __init__(self, student_dataset):
        self.student_dataset = student_dataset
        self.right_answer = pd.read_csv(
            "https://ndownloader.figshare.com/files/17980802"
        )

    def dataset_read_in(self):
        """Tests that the dataset is read in properly"""

        student_points_problem_1 = 0

        # Reading in the right answer to compare
        right_answer_problem_1 = self.right_answer.head()

        # Tests that the datset is a pandas dataset
        if type(self.student_dataset) == pd.DataFrame:
            print("Data read in as a DataFrame, well done!")
            student_points_problem_1 += 1
        else:
            print(
                "Data is not a Dataframe. Make sure to run the cell directly "
                + "above this one immediately before running these tests."
            )

        # Tests that the correct Pandas Dataframe was read in
        if self.student_dataset.equals(right_answer_problem_1):
            print("The dataframe contains the correct data, nice!")
            student_points_problem_1 += 4
        else:
            print("The dataframe contains different data then expected.")

        print("Points out of 5: {}".format(student_points_problem_1))
        return student_points_problem_1

    def modified_acre_size(self):
        """Tests that the acre size was properly modified"""

        student_points_problem_2 = 0

        # Reading in the right answer to compare
        right_answer_problem_2 = self.right_answer.tail()
        right_answer_problem_2["fire_size"] /= 2.47105

        if self.student_dataset.equals(right_answer_problem_2):
            print("Correctly modified the data, good job!")
            student_points_problem_2 += 5
        else:
            print(
                "Data was not correctly modified. Make sure you divided the correct"
                + " column and only displayed the last few rows of the dataset "
                + "with datset.tail()"
            )

        print("Points out of 5: {}".format(student_points_problem_2))
        return student_points_problem_2

    def max_fire_dataframe(self):
        """Tests that a new dataset was created with the maximum fire values for
        each year."""

        student_points_problem_3 = 0

        # Reading in the right answer to compare
        right_answer_problem_3 = self.right_answer.groupby(["year"])[
            ["fire_size"]
        ].max()
        right_answer_problem_3["fire_size"] /= 2.47105

        if self.student_dataset.equals(right_answer_problem_3):
            print("Correctly created maximum fire size by year datset!")
            student_points_problem_3 += 12
        else:
            print("The dataset doesn't match with the expected dataset.")

        print("Points out of 12: {}".format(student_points_problem_3))
        return student_points_problem_3

    def max_fire_dataframe_index(self):
        """Checks that the students correctly reset the index on their fire datset"""

        student_points_problem_4 = 0

        # Reading in the right answer to compare
        right_answer_problem_4 = self.right_answer.groupby(["year"])[
            ["fire_size"]
        ].max()
        right_answer_problem_4["fire_size"] /= 2.47105
        right_answer_problem_4.reset_index(inplace=True)

        if self.student_dataset.equals(right_answer_problem_4):
            print("Correctly reset index of maximum fire size by year datset!")
            student_points_problem_4 += 12
        else:
            print("The dataset doesn't match with the expected dataset.")

        print("Points out of 12: {}".format(student_points_problem_4))
        return student_points_problem_4
