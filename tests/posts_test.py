
import requests


def test_get_all_albums() -> None:
    response = requests.get("https://jsonplaceholder.typicode.com/albums", timeout=10)
    assert response.status_code == 200

def test_get_an_album() -> None:
    response = requests.get("https://jsonplaceholder.typicode.com/albums", timeout=10)
    album = response.json()
    title_content = [album["title"] for album in album]
    assert "quidem molestiae enim" in title_content

def test_create_resource() -> None:
    payload =  {
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    }
    headers = {
        "Accept": "application/json"
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload, headers=headers, timeout=10)
    assert response.status_code == 201
