import psycopg2
import requests
from bs4 import BeautifulSoup

db_params = psycopg2.connect(
    database='postgres',
    user='postgres',
    password='postgres',
    host='localhost',
    port='5432'
)

def get_coords(miejscowosc) -> list:
    url = (f'https://pl.wikipedia.org/wiki/{miejscowosc}')
    response = requests.get(url)
    response_html = BeautifulSoup(response.text, 'html.parser')
    longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
    latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
    return [longitude, latitude]





def add_user_to_table(db_params) -> None:
    imie = input('Imie: ')
    nazwiska = input('Nazwiska: ')
    post = input('Post: ')
    miejscowosc = input('Miejscowość: ')

    longitude,latitude=get_coords(miejscowosc)

    sql_add_query = f"INSERT INTO public.users( name, surname, post, location, coords)VALUES ( '{imie}', '{nazwiska}', {post}, '{miejscowosc}', 'SRID=4326;POINT({longitude} {latitude})');"
    cursor = db_params.cursor()
    cursor.execute(sql_add_query)
    db_params.commit()


# add_user_to_table(db_params)


def show_users(db_params) -> None:
    sql_add_query = f"SELECT * FROM public.users  "
    cursor = db_params.cursor()
    cursor.execute(sql_add_query)
    users = cursor.fetchall()
    # print(users)
    # db_params.commit()
    for user in users:
        print(user)


show_users(db_params)


# DELETE FROM public.users
# 	WHERE id=2

def remove_users_from_db(db_params) -> None:
    cursor = db_params.cursor()
    sql_remove_query = f"DELETE FROM public.users where name='{input('Imie: ')}';  "
    cursor.execute(sql_remove_query)
    db_params.commit()

def get_user_id(db_params) -> int:
    print('kogo aktualizować')
    sql_add_query = f"SELECT * FROM public.users where name='{input('Imie: ')}'; "
    cursor = db_params.cursor()
    cursor.execute(sql_add_query)
    id = cursor.fetchall()[0][0]
    return id


def update_users(db_params) -> None:
    cursor = db_params.cursor()
    imie = input(' new Imie: ')
    nazwiska = input('new Nazwiska: ')
    post = input('new Post: ')
    miejscowosc = input('new Miejscowość: ')

    longitude,latitude=get_coords(miejscowosc)

    sql_update_query = f"UPDATE public.users SET name='{imie}', surname='{nazwiska}', post='{int(post)}', location='{miejscowosc}',coords='SRID=4326;POINT({longitude} {latitude})' WHERE id={get_user_id(db_params)}"
    cursor.execute(sql_update_query)
    db_params.commit()


# update_users(db_params)







