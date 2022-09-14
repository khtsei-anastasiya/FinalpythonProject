import requests


def add_user_to_store(user_id: int, username: str, firstname: str, lastname: str, email: str, password: str, phone: str,
                      user_status: int) -> object:
    global user_data

    user_data = {
        "id": user_id,
        "username": username,
        "firstName": firstname,
        "lastName": lastname,
        "email": email,
        "password": password,
        "phone": phone,
        "userStatus": user_status
    }

    response = requests.post(url='https://petstore.swagger.io/v2/user', json=user_data)
    assert response.status_code == 200, f'Error! New {username} was not added!'


def login_user(username: str, password: str):
    response = requests.get(url=f'https://petstore.swagger.io/v2/user/login?username={username}&password={password}')
    assert response.status_code == 200, f'Error! {username} cannot be logged in!'


def get_user_data(username: str):
    response = requests.get(url=f'https://petstore.swagger.io/v2/user/{username}')
    assert response.status_code == 200, f'Error! {username} not found!' \
                                        f'status code {response.status_code} has the next info {response.json()}'


def logout_user():
    response = requests.get(url='https://petstore.swagger.io/v2/user/logout')
    assert response.status_code == 200, f'Error! Cannot execute operation!' \
                                        f'status code {response.status_code} has the next info {response.json()}'


def delete_user(username: str):
    response = requests.delete(url=f'https://petstore.swagger.io/v2/user/{username}')
    assert response.status_code == 200, f'Error! {username} is not deleted!' \
                                        f'status code {response.status_code} has the next info {response.json()}'


def add_new_pet_to_store(pet_id: int, category_id: int, category_name: str, pet_name: str, tags_id: int,
                         tags_name: str, status: str) -> object:
    global pet_data

    pet_data = {
        "id": pet_id,
        "category": {
            "id": category_id,
            "name": category_name
        },
        "name": pet_name,
        "photoUrls": [
            "photoUrls"
        ],
        "tags": [
            {
                "id": tags_id,
                "name": tags_name
            }
        ],
        "status": status
    }

    response = requests.post(url='https://petstore.swagger.io/v2/pet', json=pet_data)
    assert response.status_code == 200, f'Error! New pet {pet_name} was not added!' \
                                        f'status code {response.status_code} has the next info {response.json()}'


def check_added_pet(pet_id: int):
    response = requests.get(url=f'https://petstore.swagger.io/v2/pet/{pet_id}')
    assert response.status_code == 200, f'Error! New pet {pet_id} was not added!' \
                                        f'status code {response.status_code} has the next info {response.json()}'


def update_pet_data(pet_id: int, category_id: int, category_name: str, pet_name: str, tags_id: int,
                    tags_name: str, status: str) -> object:
    global pet_data

    pet_data = {
        "id": pet_id,
        "category": {
            "id": category_id,
            "name": category_name
        },
        "name": pet_name,
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": tags_id,
                "name": tags_name
            }
        ],
        "status": status
    }

    response = requests.put(url='https://petstore.swagger.io/v2/pet', json=pet_data)
    assert response.status_code == 200, f'Error! New pet {pet_id} {pet_name} was not updated!' \
                                        f'status code {response.status_code} has the next info {response.json()}'


def check_pet_updates(pet_id: int, pet_name: str):
    response = requests.get(url=f'https://petstore.swagger.io/v2/pet/{pet_id}')
    upd_name = response.json()
    assert upd_name["name"] == pet_name, f'Error! {upd_name["name"]} is not equal to updated {pet_name} !'
