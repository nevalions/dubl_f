import urllib.request

from get_guids import teams_guid_pars, tablo_guid_pars, stats_guid_pars, sostav_a_guid_pars, sostav_b_guid_pars, refs_guid_pars

prefix = f'http://'
server = f'127.0.0.1'
sep = f':'
port = f'8088'
vmix_browser = f'{prefix}{server}{sep}{port}/api/?Function=BrowserNavigate&Value='

basket_web = 'http%3A%2F%2Fig.russiabasket.ru%2F'

competition = '%26compId%3D39879%26db%3Dorg%26tab%3D0%26tv%3D1%26color%3D4%26league%3D4%26'
game_id = '169247'

teams_guid = f'&Input={teams_guid_pars}'
teams = f'preview%2F%3FgameId%3D{game_id}{competition}region%3D1%26short%3D0%26teamA%3D%26teamB%3D%26leaguelogo%3D0{teams_guid}'
teams_api = urllib.request.urlopen(vmix_browser + basket_web + teams)

tablo_guid = f'&Input={tablo_guid_pars}'
tablo_teams = f'online%2F%3Fid%3D{game_id}{competition}logo%3D3%26foul%3D1%26white%3D1%26blank%3D6%26short%3D1%26teamA%3D%26teamB%3D{tablo_guid}'
tablo_api = urllib.request.urlopen(vmix_browser + basket_web + tablo_teams)

stats_guid = f'&Input={stats_guid_pars}'
tablo_stats = f'online-stat%2F%3Fid%3D{game_id}{competition}logo%3D3%26foul%3D1%26blank%3D6%26short%3D0%26teamA%3D%26teamB%3D{stats_guid}'
stats_api = urllib.request.urlopen(vmix_browser + basket_web + tablo_stats)

rosters = 'online-roster%2F%3FgameId%3D'
roster_url_part_one = f'{competition}teamNumber%3D'
roster_url_part_two = '%26teamA%3D%26teamB%3D'
sostav_a_guid = f'&Input={sostav_a_guid_pars}'
sostav_a = f'{rosters}{game_id}{roster_url_part_one}1{roster_url_part_two}{sostav_a_guid}'
sostav_a_api = urllib.request.urlopen(vmix_browser + basket_web + sostav_a)
sostav_b_guid = f'&Input={sostav_b_guid_pars}'
sostav_b = f'{rosters}{game_id}{roster_url_part_one}2{roster_url_part_two}{sostav_b_guid}'
sostav_b_api = urllib.request.urlopen(vmix_browser + basket_web + sostav_b)

refs_guid = f'&Input={refs_guid_pars}'
refs = f'online-ref%2F%3FgameId%3D{game_id}{competition}{refs_guid}'
refs_api = urllib.request.urlopen(vmix_browser + basket_web + refs)
