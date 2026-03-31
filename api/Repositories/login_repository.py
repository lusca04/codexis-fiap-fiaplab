import json, os

LOGIN_FILE = ".cache/userLogin.json"

def get_logged_user():
    if not os.path.exists(LOGIN_FILE):
        return None

    try:
        with open(LOGIN_FILE, "r") as file:
            return json.load(file)
    except:
        return None


def save_logged_user(user):
    with open(LOGIN_FILE, "w") as file:
        json.dump(user, file, indent=4)


def remove_logged_user():
    if os.path.exists(LOGIN_FILE):
        os.remove(LOGIN_FILE)


def is_admin(user):
    return user and user.get("Ocupacao") == "ADMINISTRADOR"