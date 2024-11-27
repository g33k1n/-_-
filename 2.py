#pip install wikipedia-api
import wikipediaapi


def print_paragraphs(page):
    paragraphs = page.text.split('\n\n')
    for i, paragraph in enumerate(paragraphs):
        print(f"Параграф {i + 1}: {paragraph[:200]}...")  # Выводим только первые 200 символов для краткости
        print()


def search_wikipedia():
    wiki_wiki = wikipediaapi.Wikipedia('ru')
    while True:
        query = input("Введите запрос для поиска на Википедии: ")
        page = wiki_wiki.page(query)
        if not page.exists():
            print("Статья не найдена. Попробуйте снова.")
            continue

        while True:
            print("\n1. Листать параграфы текущей статьи")
            print("2. Перейти на одну из связанных страниц")
            print("3. Выйти из программы")
            choice = input("Выберите действие (1/2/3): ")

            if choice == '1':
                print_paragraphs(page)
            elif choice == '2':
                links = list(page.links.keys())
                for i, link in enumerate(links):
                    print(f"{i + 1}. {link}")
                link_choice = int(input("Выберите связанную страницу по номеру: ")) - 1
                if 0 <= link_choice < len(links):
                    new_page = wiki_wiki.page(links[link_choice])
                    while True:
                        print("\n1. Листать параграфы текущей статьи")
                        print("2. Перейти на одну из внутренних статей")
                        print("3. Вернуться к предыдущей статье")
                        sub_choice = input("Выберите действие (1/2/3): ")
                        if sub_choice == '1':
                            print_paragraphs(new_page)
                        elif sub_choice == '2':
                            inner_links = list(new_page.links.keys())
                            for j, inner_link in enumerate(inner_links):
                                print(f"{j + 1}. {inner_link}")
                            inner_link_choice = int(input("Выберите внутреннюю статью по номеру: ")) - 1
                            if 0 <= inner_link_choice < len(inner_links):
                                new_page = wiki_wiki.page(inner_links[inner_link_choice])
                        elif sub_choice == '3':
                            break
                        else:
                            print("Неверный выбор. Попробуйте снова.")
                else:
                    print("Неверный номер. Попробуйте снова.")
            elif choice == '3':
                print("Выход из программы.")
                return
            else:
                print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    search_wikipedia()
