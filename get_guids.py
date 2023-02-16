import os.path
import sys

import requests
from bs4 import BeautifulSoup

from config import URL

url = f'{URL}/API/'

try:
    if not os.path.exists('data'):
        os.mkdir('data')
except Exception as ex:
    print(ex)
    print('Error creating dir')
    sys.exit()

try:
    r = requests.get(url)
    with open('data/guids.xml', 'w') as file_xml:
        file_xml.write(r.text)
except Exception as ex:
    print(ex)
    print('Vmix not running, or can not connect')
    sys.exit()

with open('data/guids.xml') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
teams_guid_pars = soup.find('input', title='teams').attrs['key']
tablo_guid_pars = soup.find('input', title='tablo').attrs['key']
stats_guid_pars = soup.find('input', title='stats').attrs['key']
sostav_a_guid_pars = soup.find('input', title='sostav_a').attrs['key']
sostav_b_guid_pars = soup.find('input', title='sostav_b').attrs['key']
refs_guid_pars = soup.find('input', title='refs').attrs['key']
