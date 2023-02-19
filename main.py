from get_guids import get_vmix_local_xml, pars_vmix_xml
from inject_urls import get_parsed_guid_from_json, inject_urls_to_vmix
from parse_game_url import parse_game_url
from config import URL

url = f'{URL}/API/'
foldername = 'data'
xml_filename = 'guids.xml'
json_file = 'parsed_guids.json'


def main():
    game_url = enter_game_id()
    try:
        get_vmix_local_xml(url, foldername, xml_filename)
        pars_vmix_xml(foldername, xml_filename)
        guids = get_parsed_guid_from_json(foldername, json_file)
        ids = parse_game_url(game_url)

        inject_urls_to_vmix(ids['game_id'], ids['comp_id'], ids['league_id'], ids['color_id'], ids['logo_id'], guids)
    except Exception as ex:
        print(ex)


def enter_game_id():
    try:
        return input('Enter game url: ')
    except Exception as ex:
        print(ex)
        print('Enter valid url')


if __name__ == '__main__':
    main()
