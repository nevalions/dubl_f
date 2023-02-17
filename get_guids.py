import os.path
import sys
import typing
import requests
import json

from bs4 import BeautifulSoup

from config import URL, vmix_inputs_titles

url = f'{URL}/API/'
foldername = 'data'
xml_filename = 'guids.xml'


def main():
    get_vmix_local_xml(url, foldername, xml_filename)
    pars_vmix_xml(foldername, xml_filename)


def get_vmix_local_xml(u: str, s_foldername: str, s_filename: str) -> typing:
    try:
        if not os.path.exists(s_foldername):
            os.mkdir(s_foldername)
    except Exception as ex:
        print(ex)
        print('Error creating dir')
        sys.exit()

    try:
        r = requests.get(u)
        with open(f'{s_foldername}/{s_filename}', 'w') as file_xml:
            file_xml.write(r.text)
    except Exception as ex:
        print(ex)
        print('Vmix not running, or can not connect')
        sys.exit()


def pars_vmix_xml(o_foldername: str, o_filename: str) -> typing:
    try:
        with open(f'{o_foldername}/{o_filename}') as file:
            src = file.read()
    except Exception as ex:
        print(ex)
        print('Error opening JSON file')
        sys.exit()

    soup = BeautifulSoup(src, 'lxml')

    parsed_match_dict = {}
    for title in vmix_inputs_titles:
        guid = soup.find('input', title=title).attrs['key']
        parsed_match_dict[title] = guid

    with open(f'{o_foldername}/parsed_guids.json', 'w') as output_json:
        output_json.write(json.dumps(parsed_match_dict, indent=4))


if __name__ == '__main__':
    main()
