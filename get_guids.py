import os.path

import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:8088/API/'
r = requests.get(url)

if not os.path.exists('data'):
    os.mkdir('data')

with open('data/guids.xml', 'w') as file_xml:
    file_xml.write(r.text)

with open('data/guids.xml') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
teams_guid_pars = soup.find('input', title='teams').attrs['key']
tablo_guid_pars = soup.find('input', title='tablo').attrs['key']
stats_guid_pars = soup.find('input', title='stats').attrs['key']
sostav_a_guid_pars = soup.find('input', title='sostav_a').attrs['key']
sostav_b_guid_pars = soup.find('input', title='sostav_b').attrs['key']
refs_guid_pars = soup.find('input', title='refs').attrs['key']
