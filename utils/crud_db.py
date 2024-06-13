import psycopg2

db_params = psycopg2.connect(
    database='postgres',
    user='postgres',
    password='postgres',
    host='localhost',
    port='5432'
)


def add_user_to_table(db_params) -> None:
    imie = input('Imie: ')
    nazwiska = input('Nazwiska: ')
    post = input('Post: ')
    miejscowosc = input('Miejscowość: ')

    sql_add_query = f"INSERT INTO public.users( name, surname, post, location, coords)VALUES ( '{imie}', '{nazwiska}', {post}, '{miejscowosc}', 'SRID=4326;POINT(21.0 52.23)');"
    cursor = db_params.cursor()
    cursor.execute(sql_add_query)
    db_params.commit()


def show_users(db_params) -> None:
    sql_add_query = f"SELECT * FROM public.users  "
    cursor = db_params.cursor()
    cursor.execute(sql_add_query)
    users = cursor.fetchall()

    for user in users:
        print(user)


def remove_users_from_db(db_params) -> None:
    cursor = db_params.cursor()
    sql_remove_query = f"DELETE FROM public.users where name='{input('Imie: ')}';  "
    cursor.execute(sql_remove_query)
    db_params.commit()


def update_users(db_params) -> None:
    cursor = db_params.cursor()
    sql_update_query = f"UPDATE public.users SET name='{input('Imie: ')}', surname='{input('surname: ')}', post='{int(input('post: '))}' WHERE id=4"
    cursor.execute(sql_update_query)
    db_params.commit()
