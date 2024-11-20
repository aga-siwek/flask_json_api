import json
from pathlib import Path


def check_and_create_data_file_users():
    checked_directory = Path(Path.cwd(), "data")
    checked_file = Path(Path.cwd(), "data", "user_data.json")

    if Path.exists(checked_directory):
        if Path.exists(checked_file):
            print("Directory and file exist")
            return checked_file
        else:
           with open(checked_file, "w") as file:
               setup_data = {}
               json.dump(setup_data, file)
               file.close()
               print("File was created")
               return checked_file

    else:
        Path.mkdir("data")
        with open(checked_file, "w") as file:
            setup_data = {}
            json.dump(setup_data, file)
            print("File and data was created")
            return checked_file


def next_id(json_file):
    with open(json_file, "r+") as file:
        json_data = json.load(file)
        if bool(json_data):
            return max(list(int(num) for num in json_data.keys()))+1
        else:
            print(json_data)
            return 0

def create_data_file_tasks():
    pass


def check_user(user, json_data):
    if bool(json_data):
        for key, value in json_data.items():
            if value["user"] == user:
                return True
        return False



def check_password(user, password, json_data):
    if bool(json_data):
        for key, value in json_data.items():
            if value["user"] == user and value["password"] == password:
                return True
        return False

def register(user, password):

    json_file = check_and_create_data_file_users()
    user_id = next_id(json_file)
    with open (json_file, "r+") as file:
        json_data = json.load(file)
        if check_user(user, json_data):
            print("User exist in data base")
            return False
        else:
            new_user_json = {str(user_id): {"id":str(user_id), "user":user, "password": password}}
            json_data.update(new_user_json)
            file.seek(0)
            json.dump(json_data, file)
            return True



def login(user, password):
    json_file = check_and_create_data_file_users()
    with open (json_file, "r+") as file:
        json_data = json.load(file)
        if check_password(user, password, json_data):
            return True
    return False



def add_task():
    pass


def see_all_tasks():
    pass


def see_task():
    pass


def delete_task():
    pass

