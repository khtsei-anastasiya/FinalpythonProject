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