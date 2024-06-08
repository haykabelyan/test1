import pytest
import requests


@pytest.fixture()
def new_post_id():
    print('+++++++++++++++++++++++++++++++++++++++++++')
    body = {'title':'Barev', 'body':'Barev, hazar barev'}
    headers = {'Content-Type':'application/json'}
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json= body, headers = headers)
    # post_id = response.json()['id']
    post_id = 100

    yield post_id

    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    print('--------------------------------------------')


@pytest.fixture(scope='session')
def hello():
    print('HELLO')
    yield
    print('Bye')
