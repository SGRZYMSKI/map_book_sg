def read(users: list[dict[str, str]])->None:
    for user in users[1:]:
        print(f'twój znajomy {user["name"]} opublikował {user["post"]} posty ')

def add_user(lista: list) -> None:
    user_name = input('Podaj imie: ')
    user_surname = input('podaj nazwisko: ')
    user_post = input('podaj ile postów: ')
    lista.append({'name': user_name, 'surname': user_surname, 'post': user_post})

