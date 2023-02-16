import urllib.request

from get_guids import teams_guid_pars, tablo_guid_pars, stats_guid_pars, sostav_a_guid_pars, sostav_b_guid_pars, refs_guid_pars

localhost_vmix_browser = 'http://127.0.0.1:8088/api/?Function=BrowserNavigate&Value='
basket_web = 'http%3A%2F%2Fig.russiabasket.ru%2F'
game_id = '169247'

teams_guid = teams_guid_pars
input_vmix_teams = f'&Input={teams_guid}'
teams = f'preview%2F%3FgameId%3D{game_id}%26compId%3D39879%26db%3Dorg%26tab%3D0%26tv%3D1%26color%3D4%26league%3D4%26region%3D1%26short%3D0%26teamA%3D%26teamB%3D%26leaguelogo%3D0{input_vmix_teams}'
teams_api = urllib.request.urlopen(localhost_vmix_browser + basket_web + teams)

tablo_guid = tablo_guid_pars
input_vmix_tablo = f'&Input={tablo_guid}'
tablo_teams = f'online%2F%3Fid%3D{game_id}%26compId%3Da39879%26db%3Dorg%26tab%3D0%26tv%3D1%26color%3D4%26league%3D4%26logo%3D3%26foul%3D1%26white%3D1%26blank%3D6%26short%3D1%26teamA%3D%26teamB%3D{input_vmix_tablo}'
tablo_api = urllib.request.urlopen(localhost_vmix_browser + basket_web + tablo_teams)

stats_guid = stats_guid_pars
input_vmix_stats = f'&Input={stats_guid}'
tablo_stats = f'online-stat%2F%3Fid%3D{game_id}%26compId%3D39879%26db%3Dorg%26tab%3D0%26tv%3D1%26color%3D4%26league%3D4%26logo%3D3%26foul%3D1%26blank%3D6%26short%3D0%26teamA%3D%26teamB%3D{input_vmix_stats}'
stats_api = urllib.request.urlopen(localhost_vmix_browser + basket_web + tablo_stats)

sostav_a_guid = sostav_a_guid_pars
input_vmix_sostav_a = f'&Input={sostav_a_guid}'
sostav_a = f'online-roster%2F%3FgameId%3D{game_id}%26compId%3D39879%26db%3Dorg%26tab%3D0%26tv%3D1%26color%3D4%26league%3D4%26teamNumber%3D1%26teamA%3D%26teamB%3D{input_vmix_sostav_a}'
sostav_a_api = urllib.request.urlopen(localhost_vmix_browser + basket_web + sostav_a)

sostav_b_guid = sostav_b_guid_pars
input_vmix_sostav_b = f'&Input={sostav_b_guid}'
sostav_b = f'online-roster%2F%3FgameId%3D{game_id}%26compId%3D39879%26db%3Dorg%26tab%3D0%26tv%3D1%26color%3D4%26league%3D4%26teamNumber%3D2%26teamA%3D%26teamB%3D{input_vmix_sostav_b}'
sostav_b_api = urllib.request.urlopen(localhost_vmix_browser + basket_web + sostav_b)

refs_guid = refs_guid_pars
input_vmix_refs = f'&Input={refs_guid}'
refs = f'online-ref%2F%3FgameId%3D{game_id}%26compId%3D39879%26db%3Dorg%26tab%3D0%26tv%3D1%26color%3D4%26league%3D4{input_vmix_refs}'
refs_api = urllib.request.urlopen(localhost_vmix_browser + basket_web + refs)
