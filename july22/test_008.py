import pytest
@pytest.fixture()
def loaddata():
    print("user profile data is being created")
    return ['Joshna', 'Nellore']


@pytest.fixture(params = [("chrome", "Joshna", "Nellore), "firefox", "IE"])
def crossBrowser(request): #even u use @pytest.mark.usefixtures("loaddata") , u need to pass fixture name as a parameter , if it has return statement
    return request.param

def test_crossBrowser(crossBrowser):
    print(crossBrowser)





