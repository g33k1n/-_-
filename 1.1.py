import requests

# URL API GitHub для поиска репозиториев
url = "https://api.github.com/search/repositories"

# Параметры запроса для поиска репозиториев с упоминанием HTML в README файле
params = {
    "q": "html in:readme"
}

try:
    # Отправка GET-запроса к GitHub API
    response = requests.get(url, params=params)

    # Печать статус-кода ответа от сервера
    print("Статус-код:", response.status_code)

    # Проверка успешности запроса (код 200)
    if response.status_code == 200:
        # Печать содержимого ответа в формате JSON
        print("Содержимое ответа (JSON):")
        print(response.json())
    else:
        # Печать сообщения об ошибке при выполнении запроса
        print("Ошибка при выполнении запроса:", response.text)
except requests.exceptions.RequestException as e:
    # Обработка возможных исключений и вывод сообщения об ошибке
    print("Произошла ошибка при выполнении запроса:", e)
