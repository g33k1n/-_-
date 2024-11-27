import requests

# URL для отправки POST-запроса к API JsonPlaceholder
url = "https://jsonplaceholder.typicode.com/posts"

# Подготовка данных для создания новой записи
payload = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

try:
    # Выполнение POST-запроса с отправкой данных
    response = requests.post(url, json=payload)

    # Вывод статус-кода ответа
    print(f"Статус-код ответа: {response.status_code}")

    # Проверка успешности запроса и вывод полученных данных
    if response.status_code == 201:
        print("Созданная запись (JSON):")
        print(response.json())
    else:
        print("Ошибка при выполнении запроса:", response.text)
except requests.exceptions.RequestException as e:
    print("Произошла ошибка при выполнении запроса:", e)
