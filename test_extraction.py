import unittest
import json
import os
import subprocess

class TestContentExtraction(unittest.TestCase):

    def setUp(self):
        # Run the script to generate the output files
        subprocess.run(["python3", "extract_content.py"], capture_output=True, text=True)

    def tearDown(self):
        # Clean up generated files
        if os.path.exists("exercises_clean.json"):
            os.remove("exercises_clean.json")
        if os.path.exists("quizzes_clean.json"):
            os.remove("quizzes_clean.json")

    def test_quiz_extraction(self):
        # Check if the quizzes_clean.json file was created
        self.assertTrue(os.path.exists("quizzes_clean.json"), "quizzes_clean.json was not created.")

        # Read the content of the quizzes_clean.json file
        with open("quizzes_clean.json", "r") as f:
            quizzes = json.load(f)

        # Assert that the file is not empty and contains questions
        self.assertGreater(len(quizzes), 0, "No quizzes were extracted.")

        # Check for a specific key in the first quiz to be more certain
        self.assertIn("correct_answer", quizzes[0])

    def test_exercise_extraction(self):
        # Check if the exercises_clean.json file was created
        self.assertTrue(os.path.exists("exercises_clean.json"), "exercises_clean.json was not created.")

        # Read the content of the exercises_clean.json file
        with open("exercises_clean.json", "r") as f:
            exercises = json.load(f)

        # Assert that the file is not empty and contains exercises
        self.assertGreater(len(exercises), 0, "No exercises were extracted.")
        self.assertIn("expected_output", exercises[0])

if __name__ == "__main__":
    unittest.main()
