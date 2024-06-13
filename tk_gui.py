from tkinter import *
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
users=[]
class User:
    def __init__(self,imie,nazwisko,posty,miejscowosc):
        self.name = imie
        self.surname = nazwisko
        self.posts = posty
        self.location = miejscowosc

def get_coords(miejscowosc) -> list:
    url = (f'https://pl.wikipedia.org/wiki/{miejscowosc}')
    response = requests.get(url)
    response_html = BeautifulSoup(response.text, 'html.parser')
    longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
    latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
    return [longitude, latitude]


def create_user()->None:

    imie=entry_imie.get()
    nazwisko=entry_nazwisko.get()
    posty=entry_posty.get()
    miejscowosc=entry_miejscowosc.get()
    uzytkownik=User(imie,nazwisko,posty,miejscowosc)
    longitude, latitude = get_coords(miejscowosc)
    sql_add_query = f"INSERT INTO public.users( name, surname, post, location, coords)VALUES ( '{imie}', '{nazwisko}', {posty}, '{miejscowosc}', 'SRID=4326;POINT({longitude} {latitude})');"
    cursor = db_params.cursor()
    cursor.execute(sql_add_query)
    db_params.commit()
    users.append(uzytkownik)
    # print(users)
    display_users()
    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_posty.delete(0, END)
    entry_miejscowosc.delete(0, END)
    entry_imie.focus()
def display_users()->None:
    listbox_lista_uzytkownikow.delete(0,END)
    sql_add_query = f"SELECT * FROM public.users  "
    cursor = db_params.cursor()
    cursor.execute(sql_add_query)
    users_db = cursor.fetchall()
    for idx,user in enumerate(users_db):
        print(idx, user[0], user[1], user[3])
        listbox_lista_uzytkownikow.insert(idx,f'{user[0]} {user[1]}, {user[2]}, {user[3]}')


def delete_user()->None:
    i=listbox_lista_uzytkownikow.index(ACTIVE)
    print(i)


    cursor = db_params.cursor()
    sql_remove_query = f"DELETE FROM public.users where name='{users[i].name}';  "
    cursor.execute(sql_remove_query)
    db_params.commit()
    users.pop(listbox_lista_uzytkownikow.index(ACTIVE))
    display_users()



def edit_user_data() -> None:
    """
    Updates the user data and marker on the map with the values from the Entry widgets.

    Args:
        i (int): The index of the user to be updated in the users list.
    """
    i = listbox_lista_uzytkownikow.index(ACTIVE)
    entry_imie.insert(0, users[i].name)
    entry_nazwisko.insert(0, users[i].surname)
    entry_posty.insert(0, users[i].posts)
    entry_miejscowosc.insert(0, users[i].location)

    button_dodaj_uzytkownika.config(text="Zapisz zmiany", command=lambda: update_user(i))


def update_user(i) -> None:
    users[i].name = entry_imie.get()
    users[i].surname = entry_nazwisko.get()
    users[i].posts = entry_posty.get()
    users[i].location = entry_miejscowosc.get()

    display_users()
    button_dodaj_uzytkownika.config(text="Dodaj użytkownika", command=create_user)
    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_posty.delete(0, END)
    entry_miejscowosc.delete(0, END)
    entry_imie.focus()



root=Tk()
root.geometry('800x700')
root.title('Map Book Sg')

# ramki do porządkowania struktury
ramka_lista_uzytkownikow=Frame(root)
ramka_formularz=Frame(root)
ramka_pokaz_szczegoly=Frame(root)
# ramka_mapa=Frame(root)

ramka_lista_uzytkownikow.grid(row=0, column=0,padx=50)
ramka_formularz.grid(row=0, column=1)
ramka_pokaz_szczegoly.grid(row=1, column=0,columnspan=2,padx=50,pady=20)
# ramka_mapa.grid(row=2, column=0)


# ramka lista uzytkownikow

label_lista_uzytkownikow=Label(ramka_lista_uzytkownikow,text="Lista obiektów")
listbox_lista_uzytkownikow=Listbox(ramka_lista_uzytkownikow,width=30)
button_pokaz_szczegoly=Button(ramka_lista_uzytkownikow,text="Pokaz szczegoly")
button_edytuj_uzytkownika=Button(ramka_lista_uzytkownikow,text="Edytuj",command=edit_user_data)
button_usun_uzytkownika=Button(ramka_lista_uzytkownikow,text="Usuń",command=delete_user)

label_lista_uzytkownikow.grid(row=0, column=0)
listbox_lista_uzytkownikow.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly.grid(row=2, column=0)
button_edytuj_uzytkownika.grid(row=2, column=1)
button_usun_uzytkownika.grid(row=2, column=2)

# ramka_formularz

label_formularz=Label(ramka_formularz,text="Formularz edycji i dodawania")
label_imie=Label(ramka_formularz,text="Imie")
label_nazwisko=Label(ramka_formularz,text="Nazwisko")
label_posty=Label(ramka_formularz,text="Posty")
label_miejscowosc=Label(ramka_formularz,text="Miejscowość")

entry_imie=Entry(ramka_formularz)
entry_nazwisko=Entry(ramka_formularz)
entry_posty=Entry(ramka_formularz)
entry_miejscowosc=Entry(ramka_formularz)
button_dodaj_uzytkownika=Button(ramka_formularz,text="Dodaj",command=create_user)


label_formularz.grid(row=0, column=0,columnspan=2)
label_imie.grid(row=1, column=0,sticky=W)
label_nazwisko.grid(row=2, column=0,sticky=W)
label_posty.grid(row=3, column=0,sticky=W)
label_miejscowosc.grid(row=4, column=0,sticky=W)

entry_imie.grid(row=1, column=1)
entry_nazwisko.grid(row=2, column=1)
entry_posty.grid(row=3, column=1)
entry_miejscowosc.grid(row=4, column=1)
button_dodaj_uzytkownika.grid(row=5, column=0,columnspan=2)

# ramka_pokaz_szczegoly
label_opis_uzytkownika=Label(ramka_pokaz_szczegoly,text="Szczegóły użytkownika")
label_imie_szczegoly=Label(ramka_pokaz_szczegoly,text="Imie: ")
label_imie_szczegoly_wartosc=Label(ramka_pokaz_szczegoly,text="... ",width=10)
label_nazwisko_szczegoly=Label(ramka_pokaz_szczegoly,text="Nazwisko: ")
label_nazwisko_szczegoly_wartosc=Label(ramka_pokaz_szczegoly,text="... ",width=10)
label_posty_szczegoly=Label(ramka_pokaz_szczegoly,text="Posty: ")
label_posty_szczegoly_wartosc=Label(ramka_pokaz_szczegoly,text="... ",width=10)
label_miejscowosc_szczegoly=Label(ramka_pokaz_szczegoly,text="Miejscowość: ")
label_miejscowosc_szczegoly_wartosc=Label(ramka_pokaz_szczegoly,text="... ",width=10)

label_opis_uzytkownika.grid(row=0, column=0,)
label_imie_szczegoly.grid(row=1, column=0,)
label_imie_szczegoly_wartosc.grid(row=1, column=1,)
label_nazwisko_szczegoly.grid(row=1, column=2,)
label_nazwisko_szczegoly_wartosc.grid(row=1, column=3,)
label_posty_szczegoly.grid(row=1, column=4,)
label_posty_szczegoly_wartosc.grid(row=1, column=5,)
label_miejscowosc_szczegoly.grid(row=1, column=6,)
label_miejscowosc_szczegoly_wartosc.grid(row=1, column=7,)





root.mainloop()
