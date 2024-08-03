# no need to give all methods set up , u can wrap into class

import pytest

@pytest.fixture
def setup():
    print("i will execute first")
    yield  # similar to post request script
    print('i will execute last ')

@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureDemo(self):
        print("i will execute aftr the fixture method")

    def test_fixtureDemo1(self):
        print("i will execute aftr the fixture1 method")

    def test_fixtureDemo2(self):
        print("i will execute aftr the fixture2 method")


    def test_fixtureDemo3(self):
        print("i will execute aftr the fixture3 method")