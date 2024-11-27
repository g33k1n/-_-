import requests

# URL для выполнения GET-запроса к API JsonPlaceholder
url = "https://jsonplaceholder.typicode.com/posts"

# Параметры запроса для фильтрации по userId
params = {
    "userId": 1
}

try:
    # Отправка GET-запроса с параметрами
    response = requests.get(url, params=params)

    # Проверка успешности запроса
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            # Печать информации о каждом посте
            print(f"ID Поста: {post['id']}")
            print(f"Заголовок: {post['title']}")
            print(f"Содержание: {post['body']}")
            print("---")
    else:
        print("Ошибка при выполнении запроса:", response.text)
except requests.exceptions.RequestException as e:
    print("Не удалось выполнить запрос:", e)
