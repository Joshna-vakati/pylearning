import requests
import random
import json
import string


base_url = "https://gorest.co.in/"

#auth token
auth_token =  "9057bbb0a71efdccaa23fa04f0c78e819c174a8deb2385560b71c181da074e10"

#get random email method
def generate_random_email():
    domain = "automation.com"
    email_length = 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + "@" + domain
    return email

# get request
def get_request():
    print('get url')
    url = base_url + "public/v2/users"
    headers = {"Authorization" : auth_token}
    response = requests.get(url, headers = headers)
    assert response.status_code == 200
    json_data = response.json()  # op will be in one line
    json_str = json.dumps(json_data, indent = 4)
    print('json GET response body: ', json_data)
    print('json response body with indent : ', json_str)


# post request
def post_request():
    print('post url')
    url = base_url + "public/v2/users"
    headers = {"Authorization": f"Bearer {auth_token}", "Content-Type": "application/json"}
    data = {
        "name": "naveen automation222",
        "gender": "male",
        "email": generate_random_email(),
        "status": "active"
    }
    response = requests.post(url, json=data, headers=headers)
    print(f"POST request URL: {url}")
    print(f"POST request Status Code: {response.status_code}")
    print(f"POST request Response Text: {response.text}")
    if response.status_code == 201:
        json_data = response.json()
        json_str = json.dumps(json_data, indent=4)
        print('json POST response body: ', json_data)
        print('json response body with indent : ', json_str)
        user_id = json_data["id"]
        assert "name" in json_data
        assert json_data["name"] == "naveen automation222"
        return user_id
    else:
        print(f"POST request failed with status code {response.status_code}")
        return None



# put request
def put_request(user_id):
    print('get url')
    url = base_url + f"public/v2/users/{user_id}"
    headers = {"Authorization": f"Bearer {auth_token}",}
    data = {
        "name": "JOhn_vijay2",
        "gender": "male",
        "email": generate_random_email(),
        "status": "active"
    }
    response = requests.put(url, json = data, headers = headers)
    assert response.status_code == 200
    json_data = response.json()  # op will be in one line
    json_str = json.dumps(json_data, indent=4)
    print('json PUT response body: ', json_data)
    print('json response body with indent : ', json_str)
    assert json_data["id"] == user_id
    assert json_data["name"] == "JOhn_vijay2"


# delete request

def del_request(user_id):
    print('get url')
    url = base_url + f"public/v2/users/{user_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204






# call
get_request()
user_id = post_request()
put_request(user_id)
del_request(user_id)

