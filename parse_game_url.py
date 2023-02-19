import sys


def main():
    game_url = 'http://ig.russiabasket.ru/game/?id=163326&tab=0&compId=39874&league=27&color=5&logo=4&db=org'
    print(parse_game_url(game_url))


def parse_game_url(u: str) -> dict:
    keys = {
        'game_id_key': '?id=',
        'comp_id_key': 'compId=',
        'league_id_key': 'league=',
        'color_id_key': 'color=',
        'logo_key': 'logo='
    }

    try:
        ids = {
            'game_id': find_id_in_url(keys['game_id_key'], u),
            'comp_id': find_id_in_url(keys['comp_id_key'], u),
            'league_id': find_id_in_url(keys['league_id_key'], u),
            'color_id': find_id_in_url(keys['color_id_key'], u),
            'logo_id': find_id_in_url(keys['logo_key'], u)
        }
        return ids
    except Exception as ex:
        print(ex)
        print('Error finding id by key')
        sys.exit()


def find_id_in_url(key: str, u: str) -> str:
    try:
        f = u.find(key)
        if f > -1:
            index = f + len(key)
            value = ''
            while True:
                num = u[index]
                if num.isdigit():
                    value += str(num)
                    index = index + 1
                else:
                    break
            return value
        else:
            raise ValueError
    except ValueError as ex:
        print(ex)
        print(f'Key "{key}" not found in {u}')
        sys.exit()


if __name__ == '__main__':
    main()
