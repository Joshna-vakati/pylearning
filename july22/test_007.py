@pytest.fixture
def loaddata():
    print("i will execute first")
    yield  # similar to post request script
    print('i will execute last ')

