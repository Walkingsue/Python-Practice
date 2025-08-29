import requests

base_url = "https://pokeapi.co/api/v2/"

def get_poke_data(poke_name):
        url = f"{base_url}/pokemon/{poke_name}"
        response = requests.get(url)

        if response.status_code == 200:
            poke_data = response.json()
            return poke_data
        else:
            print("Error: Unable to fetch data from the API.")

poke_name = "pikachu"
poke_info = get_poke_data(poke_name)

if poke_info:
    print(f"Name: {poke_info["name"].capitalize()}.")
    print(f"ID: {poke_info["id"]}.")
    for a in poke_info["moves"]:
         print(f'{poke_name} can learn: {a["move"]["name"]}')