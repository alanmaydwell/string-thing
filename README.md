# String Thing

Mainly created to practice with Python unit test frameworks **unittest** and **pyunit**

Also to try out Github Actions (/.github/workflows/)

The string_thing module was created as something to try on unit tests with but it might eventually be actually useful for something, e.g. used in conjunction with pyperclip module to examine or alter the clipboard contents.

## Initial impressions of frameworks tried
Here are some quick and superficial comparisons.

### unittest

- Part of Python standard library
- Seems to have fixed structure in form of sub-classes of unittest.TestCase class
- Test method names need to start with `test` and conventionally start with `test_`
- Although Python `assert` statement can be used, its associated error text is not displayed upon failure.  Need to use special assertion methods (e.g. unittest.TestCase.assertEqual) to get convenient error output. 
- Need to remember to include call to unitest.main (e.g. in `if __name__ == 'main'`) otherwise nothing happens!
- Can invoke from command line like this `python3 -m test_module`.  Note the last argument is the module name not the filename, so don't include `.py`

### pytest
- Not part of standard library. Can install using pip, e.g. `pip3 install pytest`
- Can be more consise than unittest as no need to create particular type of class.
- Some tutorial examples include `import pytest` line but this doesn't seem to be needed!
- Might only execute functions and these need to have names that start `test_`.
- Test filenames shoud start or end with "test" 
- Unlike unittest, the error text from Python `assert` statement is automatically displayed upon failure.
- Can invoke from command line like this: `pytest test_file.py` (unlike unittest this takes the filename not module name - `.py` included)