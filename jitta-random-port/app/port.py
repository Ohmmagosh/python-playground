from rich.console import Console
from numpy import random
import numpy as np
import itertools
import csv
import os

console = Console()

class Port:
    JITTAPORT: list = [
            "china",
            "vietnam",
            "United State",
            "India",
            "Hong Kong",
            "Cannabis",
            "Game & E-sport",
            "Cloud computing",
            "Genomic",
            "Semiconductor",
            "Cybersecurity",
            "Technology",
            "Fintech",
            "China Tech",
            "Travel Tech",
            "HealtCare",
            "China HealtCare",
            "Clean Energy",
            "China Clean Energy",
            "Metaverse",
            "Lithium & Battery",
            "AI & Robotic",
            "Internet of Things",
            "E-commerce",
            ]
    def __init__(self):
        ...

    def print_port(self):
        for (index, item) in  enumerate(self.JITTAPORT,1):
            console.print(f"{index}  {item}")

    @staticmethod
    def len_file_in_folder():
        path = "./out"
        for name in os.listdir(path):
            if name.endswith(".csv"):
                console.print(name)
        file = [ name for name in os.listdir(path) if name.endswith(".csv")]
        return len(file)

    @staticmethod
    def generate_combinations(input_list):
        return list(itertools.combinations(input_list, 5))

    @staticmethod
    def create_file_csv(name_file, data):
        with open(f'./out/{name_file}.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            field = ["port1", "port2", "port3", "port4", "port5"]
            writer.writerow(field)
            if data != field:
                writer.writerows(data)

    def generate_possible_port(self):
        if (self.len_file_in_folder() > 0):
            console.print(f"File already exists")
            return
        res = []
        for combination in self.generate_combinations(self.JITTAPORT):
            res.append(combination)
        self.create_file_csv(f"port{random.randint(1000, 9999)}", res)

    @staticmethod
    def get_file_name():
        path = "./out"
        file = [ name for name in os.listdir(path) if name.endswith(".csv")]
        return file


    def read_file_csv(self, name_file):
        ret = []
        with open(f'./out/{name_file}', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                ret.append(row)
        return ret

    def get_data_file(self):
        file = self.get_file_name()
        data = self.read_file_csv(file[0])
        unique_data = []

        for line in data:
            if line == ["port1", "port2", "port3", "port4", "port5"]:
                continue
            for word in line:
                if self.isDuplicate(unique_data, word):
                   break
            else:
                unique_data.append(line)

        name_posfix = file[0].split('.')[0]
        self.create_file_csv(f"unique_{name_posfix}", unique_data)

    @staticmethod
    def isDuplicate(data: list, word: str) -> bool:
        for line in data:
            if word in line:
                return True
        return False

