import get_guids
import inject_urls
from config import URL

url = f'{URL}/API/'
foldername = 'data'
xml_filename = 'guids.xml'
json_file = 'parsed_guids.json'


def main():
    game_id = enter_game_id()

    get_guids.get_vmix_local_xml(url, foldername, xml_filename)
    get_guids.pars_vmix_xml(foldername, xml_filename)

    guids = inject_urls.get_parsed_guid_from_json(foldername, json_file)
    inject_urls.inject_urls_to_vmix(game_id, guids)


def enter_game_id():
    while True:
        try:
            game_id = input('Enter game id: ')
            if not game_id.isdigit():
                raise ValueError
            else:
                return game_id
        except ValueError:
            print('Enter valid number')


if __name__ == '__main__':
    main()
