import pytest


@pytest.fixture
def setup():
    print("i will execute first")
    yield                 # similar to post request script
    print('i will execute last ')
    
def test_fixtureDemo(setup):
    print("i will execute aftr the fixture method")