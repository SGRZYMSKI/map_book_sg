from models.data import users
from utils.crud import read


if __name__ == '__main__':
    print(f'witaj {users[0]["name"]}')


    read(users)

