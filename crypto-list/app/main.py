import os
import requests
import json
from rich import print as rprint
from rich import inspect as insp
from dotenv import load_dotenv
from rich.console import Console
import pandas as pd

console = Console()

def coin_list(key):
	url = "https://coingecko.p.rapidapi.com/coins/list"

	headers = {
		"X-RapidAPI-Key": key,
		"X-RapidAPI-Host": "coingecko.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers)

	if response.status_code != 200:
		raise Exception(response.status_code, json.loads(response.text)['message'])
	return response.json()

def create_file(data):
	with open('data.json', 'w') as f:
		json.dump(data, f, indent=4)


def write_data_to_file(data):
	with open('output.txt', 'w') as f:
		f.write(data)

def main():
	load_dotenv()
	key = os.environ['RAPID_KEY']
	try:
		if os.path.exists('data.json') == False:
			data = coin_list(key)
			create_file(data)
		else:
			json_data = pd.read_json('data.json')
			data_string = json_data.to_string(index=False)
			write_data_to_file(data_string)
	except Exception as e:
		print('Error -> ', e)

if __name__ == "__main__":
	main()
