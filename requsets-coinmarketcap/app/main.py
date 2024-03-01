import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
from rich import print as rprint, inspect as insp
from time import sleep
from lxml import etree
import math

def create_soup(content: bytes):
	return BeautifulSoup(content, 'html.parser')

def get_header(content: bytes):
	soup = create_soup(content=content)
	headers = []
	table_head = soup.table.thead
	if table_head:
		header_row = table_head.find('tr')
		if header_row:
			for th in header_row.find_all('th'):
				p_tag = th.find('p')
				if p_tag:
					headers.append(p_tag.text.strip())
				else:
					headers.append(th.text.strip())
	return headers

def get_data_row(content: bytes):
	soup = create_soup(content=content)
	crypto_info = {}
	tbody = soup.table.tbody
	if tbody:
		for row in tbody:
			list_row = list(row)
			if len(list_row) > 6:
				name_sym = list(list_row[2].find_all('p'))
				name = name_sym[0].text.strip()
				symbol = name_sym[1].text.strip()
				price = list_row[3].find('span').text.strip()
			else:
				name_sym = list(list_row[2].find_all('span'))
				name = name_sym[1].text.strip()
				symbol = name_sym[2].text.strip()
				price = list_row[3].text.strip()
			crypto_info[name] = [name, symbol, price]
	return crypto_info


def get_page_size(url: str) -> int:
	content = get_content(url)
	soup = create_soup(content=content)
	body = soup.find('body')

	xpath_coin = "/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[6]/span"
	xpath_show = "//*[@id='__next']/div[2]/div[1]/div[2]/div/div[1]/div[6]/div[2]/div/div"

	dom = etree.HTML(str(body))
	text = dom.xpath(xpath_coin)[0].text.split(' ')
	show_row = dom.xpath(xpath_show)[0].text.split(' ')[0]
	return math.ceil(int(text[-1]) / int(show_row))


def get_content(url:str):
	r = requests.get(url)
	if r.status_code != 200:
		raise Exception(f"{r.status_code}")
	return r.content


def get_data_crypto(page_size: int):
	for i in range(1, page_size + 1):
			get_data_by_page2(i)


def get_data_by_page2(page: int):
	url = f"https://coinmarketcap.com/?page={page}"
	content = get_content(url=url)
	data_crypto = get_data_row(content=content)
	for key, data in data_crypto.items():
		rprint(f'[yellow1]{key} [gray42]{data[1]} [green1]{data[2]}')

def main():
	URL = "https://coinmarketcap.com/"
	try:
		page_size = get_page_size(URL)
		for i in range(1, page_size + 1):
			get_data_by_page2(i)

	except HTTPError as http_error:
		rprint(f"[red]HTTP Error -> [yellow]{http_error}")
	except Exception as err:
		rprint(f"[red]Exception Error -> [yellow]{err}")
	finally:
		rprint(f"[green] Success!!")


if __name__ == "__main__":
	main()
