from models.data import users
from utils.crud import read, add_user,search,remove_user,update_user,map_single_users,map_all_users

if __name__ == '__main__':
    print(f'witaj {users[0]["name"]}')

    while True:
        print('0. zakończ program ')
        print('1. wyświetl znajomych ')
        print('2. dodaj znajomego ')
        print('3. szukaj znajomego ')
        print('4. usuń znajomego ')
        print('5. kogo zaktualizować')
        print('6. wyświetl mapę dla każdego użytkownika')
        print('7. wyświetl zbiorczą mapę')
        menu_option = input('wybierz opcje menu: ')
        if menu_option == '0': break
        if menu_option == '1': read(users)
        if menu_option == '2': add_user(users)
        if menu_option == '3': search(users)
        if menu_option == '4': remove_user(users)
        if menu_option == '5': update_user(users)
        if menu_option == '6':
            for user in users:
                map_single_users(user['name'],user['post'],user['location'])
        if menu_option == '7':map_all_users(users)