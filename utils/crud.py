def read(users: list[dict[str, str]])->None:
    for user in users[1:]:
        print(f'twój znajomy {user["name"]} opublikował {user["post"]} posty ')