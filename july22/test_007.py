import pytest
@pytest.fixture
def loaddata():
    print("user profile data is being created")
    return ['Joshna', 'Nellore']

@pytest.mark.usefixtures("loaddata")
class loader:
    def test_importdata(self, loaddata): #even u use @pytest.mark.usefixtures("loaddata") , u need to pass fixture name as a parameter , if it has return statement
        print(loaddata)



