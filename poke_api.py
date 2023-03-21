import requests
import requests


def fetch_pokemon_dtls(nameId):
    """  fetches  info of a Pokemon using PkeAPI.

    Args :
    nameId (str or int): Pokemon Name Enter PokeDex number .

    Returns:
    dictionary of data : A dictionary containing all the Pokemon informatoin from API
    None: None is responded when information of Pokemon is not fetched.
    """

    #  Removes whitespace and turns parameter to string and lowercase
    name_str = str(nameId).strip().lower()

    #  URL using id or name
    link = f"https://pokeapi.co/api/v2/pokemon/{name_str}"

    # a GET req using Id or name
    resp = requests.get(link)

    # Validates if Response is received
    if resp.status_code == 200:
        #  Printing synopsis of actions
        print(f"Retrieved information for {name_str.title()} from API.")

        # Json data from response
        jsontodata = resp.json()

        # Returns dictionary with Pokemon details
        return jsontodata
    else:
        #  Printing synopsis of actions
        print(f" details not fetched for {name_str.title()} from API.")

        # Nome if no information is found
        return None


