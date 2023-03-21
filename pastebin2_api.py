import pastebin_api
import poke_api
import sys


def main():
    Pokename = getpokename()
    Pokedata = poke_api.fetch_pokemon_dtls(Pokename)
    datatuple = get_paste_create(Pokedata)
    API_POST_URL = pastebin_api.create_paste(datatuple[0], datatuple[1], '1Y', 1)
    print(API_POST_URL)


def getpokename():
    try:
        param1 = sys.argv[1]
    except IndexError:
        print("No Command Line Parameter Provided")
        sys.exit(1)
    name = param1
    return name


def get_paste_create(data):
    title = getpokename().capitalize() + 's Abilities'
    body = data['abilities']
    res = tuple([title] + body)
    return res


if __name__ == '__main__':
    main()
