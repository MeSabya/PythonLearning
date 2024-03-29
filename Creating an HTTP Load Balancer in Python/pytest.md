## Pytest - Fixtures

Fixtures are functions, which will run before each test function to which it is applied. Fixtures are used to feed some data to the tests such as database connections, URLs to test and some sort of input data. Therefore, instead of running the same code for every test, we can attach fixture function to the tests and it will run and return the data to the test before executing each test.

A function is marked as a fixture by −

>@pytest.fixture

>A test function can use a fixture by mentioning the fixture name as an input parameter.

Create a file test_div_by_3_6.py and add the below code to it

```python
import pytest

@pytest.fixture
def input_value():
   input = 39
   return input

def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0
```

Here, we have a fixture function named input_value, which supplies the input to the tests. To access the fixture function, the tests have to mention the fixture name as input parameter.

Execute the test using the following command −

```
pytest -k divisible -v
```

The above command will generate the following result −

```
test_div_by_3_6.py::test_divisible_by_3 PASSED
test_div_by_3_6.py::test_divisible_by_6 FAILED
============================================== FAILURES
==============================================
________________________________________ test_divisible_by_6
_________________________________________
input_value = 39
   def test_divisible_by_6(input_value):
>  assert input_value % 6 == 0
E  assert (39 % 6) == 0
test_div_by_3_6.py:12: AssertionError
========================== 1 failed, 1 passed, 6 deselected in 0.07 seconds
==========================
```
However, the approach comes with its own limitation. A fixture function defined inside a test file has a scope within the test file only. We cannot use that fixture in another test file. To make a fixture available to multiple test files, we have to define the fixture function in a file called **conftest.py**. conftest.py is explained in the next chapter.

https://www.tutorialspoint.com/pytest/pytest_fixtures.htm

