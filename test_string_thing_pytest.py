from string_thing import StringThing
from string_thing import counterstring

# Note some pytest examples have `import pytest` at start of script even when 
# not needed as not used within the script and pytest only invoked at 
# command line. However, sometimes is needed as functions from within
# pytest are actually used. This is the case here as using pytest.mark.parameters
import pytest

# The for loops used below aren't ideal as loop will end upon first assertion failure encountered
# - only get full run if no failures. Looks like there are ways around this using some pytest
# decorators such as pytest.mark.parametrize.

def test_length_one():
    value = "123456"
    st = StringThing(value)
    result = st.length()
    assert result == 6, f"Length of {value} - actual result: {result}, expected result: 6"

    
def test_length_multi():
    expecteds = {"a"*i: i for i in range(10)}
    for value, expected in expecteds.items():
        st = StringThing(value)
        result = st.length()
        assert result == expected, f"Length of {value} - actual result: {result}, expected result {expected}" 

# Avoid for-loop problem by using pytest.mark.parametrize to create the set of values to be tested
@pytest.mark.parametrize("value, expected", [("a"*i, i) for i in range(10)])
def test_length_multi_v2(value, expected):
    st = StringThing(value)
    result = st.length()
    assert result == expected, f"Length of {value} - actual result: {result}, expected result {expected}"


def test_substring_count():
    value = "abcaabbbcccc"
    st = StringThing(value)
    # Note could be argued that right result for "cc" should be 3 rather than 2
    expecteds = {"a": 3, "b": 4, "c": 5, "d": 0, "ab": 2, "cc": 2}
    for substr, expected in expecteds.items():
        result = st.substring_count(substr)
        assert result == expected, f"Count of {substr} in {value} found {result} but expected {expected}"

@pytest.mark.parametrize("value", ["abcaabbbcccc"])# need to put the string in a list otherwise will iterate over the string
@pytest.mark.parametrize("substr, expected", [("a", 3), ("b", 4), ("c", 5), ("d", 0), ("ab", 2), ("cc", 2)])
def test_substring_count_v2(value, substr, expected):
    st = StringThing(value)
    result = st.substring_count(substr)
    assert result == expected, f"Count of {substr} in {value} found {result} but expected {expected}"

    

def test_find_first():
    value = "axbxxcxxxd"
    st = StringThing(value)
    expecteds = {"a": 0, "b": 2, "c": 5, "d": 9, "x": 1, "z": -1,
                 "ax":0, "xb": 1, "bxx": 2, value: 0, value+" ": -1}
    for letter, count in expecteds.items():
        result = st.find_first(letter)
        assert result == count, f"Find first {letter} in {value} - actual result: {result}, expected result: {count}"

# Using pytest.mark.parametrize here - lose ability to conveniently include "value" in expected data
@pytest.mark.parametrize("value", ["axbxxcxxxd"])
@pytest.mark.parametrize("substr, count", [("a", 0), ("b", 2), ("c", 5), ("d", 9), ("x", 1), ("z", -1)
                                           ,("ax", 0), ("xb", 1), ("bxx", 2)])
def test_find_first_v2(value, substr, count):
    st = StringThing(value)
    result = st.find_first(substr)
    assert result == count, f"Find first {substr} in {value} - actual result: {result}, expected result: {count}"


def test_find_all():
    value = "abaabaaab"
    expecteds = {"a": [0, 2, 3, 5, 6, 7], "b": [1, 4, 8], "ab": [0, 3, 7]}
    for letter, expected in expecteds.items():
        st = StringThing(value)
        result = st.find_all(letter)
        assert result == expected, f"Find all {letter} in {value} - actual: {result}, expected: {expected}"
    
@pytest.mark.parametrize("value", ["abaabaaab"])
@pytest.mark.parametrize("substr, positions", [("a", [0, 2, 3, 5, 6, 7]), ("b", [1, 4, 8]), ("ab", [0, 3, 7])])
def test_find_all_v2(value, substr, positions):
    st = StringThing(value)
    result = st.find_all(substr)
    assert result == positions, f"Find all {substr} in {value} - actual: {result}, expected: {positions}"
    


def test_counterstring():
    cs = counterstring(35, "#")
    expected = "2#4#6#8#11#14#17#20#23#26#29#32#35#"
    assert cs == expected, f"Counterstring error - expected: {expected}, actual: {cs}"
    