import requests


def get_character_data_by_name(name):
    response = requests.get(f"https://rickandmortyapi.com/api/character"
                            f"/?name={name.lower()}")

    if response.status_code == 404:
        raise Exception('Not found!(')

    return response.json()


def main(name):

    data = get_character_data_by_name(name)
    character = data['results'][0]

    return "Имя: " + str(character['name']) + \
    "\nСтатус: " + str(character['status']) + \
    "\nСпецификация: " + str(character['species']) + \
    "\nТип: " + str(character['type']) + \
    "\nПол: " + str(character['gender']) + \
    "\nФото " + str(character['image']) + \
    "\nЛокация: " + str(character['location']) + \
    "\nЭпизод: " + str(character['episode'][0])