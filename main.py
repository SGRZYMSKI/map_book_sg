from models.data import users
from utils.crud import read, add_user,search,remove_user,update_user,map_single_users,map_all_users
from utils.crud_db import show_users,remove_users_from_db,get_users,update_users,add_user_to_table,get_user_id,db_params
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
        if menu_option == '1': show_users(clinic_list)
        if menu_option == '2': add_user_to_table(clinic_list)
        if menu_option == '3': get_user_id(clinic_list)
        if menu_option == '4': remove_users_from_db()
        if menu_option == '5': update_users(clinic_list)
        if menu_option == '6':
            for user in get_users(clinic_list):
                map_single_users(user['name'],user['post'],user['location'])
        if menu_option == '7':map_all_users(get_users(db_params))

