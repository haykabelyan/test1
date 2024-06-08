import requests
import pytest
import random
import allure


@allure.feature('POSTS')
@allure.story('GET ONE POST')
@allure.title('get one post title')
@allure.description('get one post description')
@pytest.mark.smoke
def test_get_one_post(new_post_id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}')
    assert response.status_code == 200, "ERROR: Incorrect status code"
    assert response.json()['id'] == new_post_id


@allure.feature('POSTS')
@allure.story('GET POSTS')
@pytest.mark.smoke
def test_get_all_posts(hello):
    response = requests.get('https://jsonplaceholder.typicode.com/posts/')
    assert response.status_code == 200, 'ERROR: Incorrect status code'
    assert len(response.json()) == 100, 'Error.'


@allure.feature('POSTS')
@allure.story('GET MESSAGE')
@pytest.mark.xxx
def test_get_message_by_post_id():
    post_id = random.randint(1, 100)
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}/comments')

    assert response.status_code == 200, 'Error: Status Code is Incorrect'

    error_id = 0
    messages = response.json()

    for message in messages:
        if message['postId'] != post_id:
            error_id = message['id']
            break

    assert error_id == 0, f'Error: post Id - {post_id}, message id - {error_id} '



@allure.feature('POSTS')
@allure.story('ADD POST')
@pytest.mark.regression
def test_add_post():
    body = {
        "userId": 1,
        "title": "hayk",
        "body": "Lorem ipsum"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts/',
        json = body,
        headers=headers
    )

    assert response.status_code == 201, 'Status Code incorrect'
    assert response.json()['title'] == 'hayk', 'Title Error'


@allure.feature('POSTS')
@allure.story('PUT POST')
def test_put_post(new_post_id):
    body = {
        "userId": 1,
        "title": "kim",
        "body": "Lorem Ipsum"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'https://jsonplaceholder.typicode.com/posts/{new_post_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Error: Status Code incorrect'
    assert response.json()['title'] == 'kim', 'Error: Title'
    assert response.json()['body'] == 'Lorem Ipsum', 'Error: Body'


@allure.feature('POSTS')
@allure.story('PATCH POST')
def test_path_post(new_post_id):
    body = {
        "body": "Lorem Ipsum"
    }
    headers = {'Content-Type': 'application/json'}

    response1 = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}')

    response2 = requests.patch(
        f'https://jsonplaceholder.typicode.com/posts/{new_post_id}',
        json=body,
        headers=headers
    )

    assert response2.status_code == 200
    assert response2.json()['body'] == 'Lorem Ipsum'
    assert response1.json()['title'] == response2.json()['title']


@allure.feature('POSTS')
@allure.story('DELETE POST')
def test_delete_post(new_post_id):
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}')
    assert response.status_code == 200


@allure.feature('Example')
@allure.story('Equals')
def test_one():
    assert 1 == 1


@allure.feature('Example')
@allure.story('Equals')
@pytest.mark.parametrize('x', [random.randint(1, 100)  for _ in range(0, 5)])
def test_two(x):
    assert 2 == 2


@allure.feature('POSTS')
@allure.story('Negative Test')
def test_negative_delete_post(new_post_id):
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}')
    requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}')
    assert response.status_code == 200




