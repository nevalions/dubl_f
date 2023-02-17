import json
import sys
import urllib.request

from config import URL

folder = 'data'
json_file = 'parsed_guids.json'


def main():
    game_id = '169247'

    guids = get_parsed_guid_from_json(folder, json_file)
    inject_urls_to_vmix(game_id, guids)


def get_parsed_guid_from_json(foldername: str, json_filename: str) -> dict:
    try:
        with open(f'{foldername}/{json_filename}', 'r', encoding='utf-8') as file:
            guids = json.load(file)
    except Exception as ex:
        print(ex)
        print('Error opening JSON file')
        sys.exit()

    return guids


def inject_urls_to_vmix(g_id: str, parsed_guids: dict):

    vmix_browser = f'{URL}/api/?Function=BrowserNavigate&Value='
    basket_web = 'http%3A%2F%2Fig.russiabasket.ru%2F'
    competition = '%26compId%3D39879%26db%3Dorg%26tab%3D0%26tv%3D1%26color%3D4%26league%3D4%26'

    teams_guid = f'&Input={parsed_guids["teams"]}'
    teams = f'preview%2F%3FgameId%3D{g_id}{competition}region%3D1%26short%3D0%26teamA%3D%26teamB%3D%26leaguelogo%3D0{teams_guid}'
    urllib.request.urlopen(vmix_browser + basket_web + teams)

    tablo_guid = f'&Input={parsed_guids["tablo"]}'
    tablo_teams = f'online%2F%3Fid%3D{g_id}{competition}logo%3D3%26foul%3D1%26white%3D1%26blank%3D6%26short%3D1%26teamA%3D%26teamB%3D{tablo_guid}'
    urllib.request.urlopen(vmix_browser + basket_web + tablo_teams)

    stats_guid = f'&Input={parsed_guids["stats"]}'
    tablo_stats = f'online-stat%2F%3Fid%3D{g_id}{competition}logo%3D3%26foul%3D1%26blank%3D6%26short%3D0%26teamA%3D%26teamB%3D{stats_guid}'
    urllib.request.urlopen(vmix_browser + basket_web + tablo_stats)

    rosters = 'online-roster%2F%3FgameId%3D'
    roster_url_part_one = f'{competition}teamNumber%3D'
    roster_url_part_two = '%26teamA%3D%26teamB%3D'
    sostav_a_guid = f'&Input={parsed_guids["sostav_a"]}'
    sostav_a = f'{rosters}{g_id}{roster_url_part_one}1{roster_url_part_two}{sostav_a_guid}'
    urllib.request.urlopen(vmix_browser + basket_web + sostav_a)
    sostav_b_guid = f'&Input={parsed_guids["sostav_b"]}'
    sostav_b = f'{rosters}{g_id}{roster_url_part_one}2{roster_url_part_two}{sostav_b_guid}'
    urllib.request.urlopen(vmix_browser + basket_web + sostav_b)

    refs_guid = f'&Input={parsed_guids["refs"]}'
    refs = f'online-ref%2F%3FgameId%3D{g_id}{competition}{refs_guid}'
    urllib.request.urlopen(vmix_browser + basket_web + refs)


if __name__ == '__main__':
    main()
