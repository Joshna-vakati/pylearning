import pytest


@pytest.fixture
def setup():
    print("i will execute first")
    
def test_fixtureDemo(setup):
    print("i will execute aftr the fixture method")