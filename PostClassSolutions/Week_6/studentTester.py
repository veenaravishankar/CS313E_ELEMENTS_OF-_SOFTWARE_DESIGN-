import unittest

from student import Course,Student

class TestStudent(unittest.TestCase):
    def test_generate_email001(self):
        cs313e = Course('CS313E',3,3000)
        ph201e = Course('PH 201E', 3, 3000)
        course_list = [cs313e,ph201e]

        john = Student('John','Doe','1/1/2000',course_list)
        self.assertEqual(john.generate_email('utexas.edu'), 'John.Doe@utexas.edu')

    def test_generate_email002(self):
        cs313e = Course('CS313E', 3, 3000)
        ph201e = Course('PH 201E', 3, 3000)
        course_list = [cs313e, ph201e]

        john = Student('John', 'Doe', '1/1/2000', course_list)
        self.assertTrue("@" in list(john.generate_email("utexas.edu")))

    def test_generate_email003(self):
        cs313e = Course('CS313E', 3, 3000)
        ph201e = Course('PH 201E', 3, 3000)
        course_list = [cs313e, ph201e]

        john = Student('John', 'Doe', '1/1/2000', course_list)
        self.assertIn("@", list(john.generate_email("utexas.edu")))

if __name__ == '__main__':
    unittest.main()