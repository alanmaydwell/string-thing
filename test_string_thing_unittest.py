import unittest

from string_thing import StringThing


class TestStringThing(unittest.TestCase):

    def test_one(self):
        value = "123456"
        st = StringThing(value)
        result = st.length()
        self.assertEqual(result, 6, f"Length of {value} - actual result: {result}, expected result: 6")

    def test_substring_count(self):
        value = "abcaabbbcccc"
        st = StringThing(value)
        # Note could be argued that right result for "cc" should be 3 rather than 2
        expecteds = {"a": 3, "b": 4, "c": 5, "d": 0, "ab": 2, "cc": 2}
        for substr, expected in expecteds.items():
            result = st.substring_count(substr)
            self.assertEqual(result, expected, f"Count of {substr} in {value} found {result} but expected {expected}")

    def test_find_first(self):
        value = "axbxxcxxxd"
        st = StringThing(value)
        result = st.find_first("b")
        self.assertEqual(result, 2, f"Find first b in {value} - actual result: {result}, expected result: 2")


if __name__ == '__main__':
    unittest.main()
