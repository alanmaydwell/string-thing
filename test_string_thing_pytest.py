# Note some examples have `import pytest` at start of script
# but doesn't actually seem to be needed. pytest is invoked at 
# command line. This present script works fine without the import.

from string_thing import StringThing


def test_one():
    value = "123456"
    st = StringThing(value)
    result = st.length()
    assert result == 6, f"Length of {value} - actual result: {result}, expected result: 6"

def test_substring_count():
    value = "abcaabbbcccc"
    st = StringThing(value)
    # Note could be argued that right result for "cc" should be 3 rather than 2
    expecteds = {"a": 3, "b": 4, "c": 5, "d": 0, "ab": 2, "cc": 2}
    for substr, expected in expecteds.items():
        result = st.substring_count(substr)
        assert result == expected, f"Count of {substr} in {value} found {result} but expected {expected}"

def test_find_first():
    value = "axbxxcxxxd"
    st = StringThing(value)
    result = st.find_first("b")
    assert result == 2, f"Find first b in {value} - actual result: {result}, expected result: 2"
