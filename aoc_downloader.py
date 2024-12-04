import requests
from pathlib import Path
import datetime
import json
import argparse
from string import Template

class aoc_downloader():
    def __init__(self, args) -> None:
        self.ROOT_DIR = Path(__file__).parent # the main advent-of-code folder
        self.TODAY = datetime.date.today()
        self.args = args
        self.day = self.args.day if self.args.day is not None else self.TODAY.day
        self.year = self.args.year if self.args.year is not None else self.TODAY.year
        
        self.create_folder()
        self.get_input()
        if self.args.py:
            self.create_new_py()
    
    def get_session_cookie(self) :
        try:
            data = json.load(open(self.ROOT_DIR / 'config.json', 'r'))
            return data['session_cookie']
        except:
            print(f"reading config.json failed!")
            raise
    
    def create_folder(self):
        folder_path = self.ROOT_DIR / f"{self.year}" / f"day{self.day:0>2}"
        if not folder_path.exists():
            folder_path.mkdir()
            return
        print(f"folder day{self.day:0>2} already exists")
        return
        
    def get_input(self):
        text_file_path = self.ROOT_DIR / f"{self.year}" / f"day{self.day:0>2}" / f"input.txt"
        if not text_file_path.is_file() or self.args.force:
            URL = f"https://adventofcode.com/{self.year}/day/{self.day}/input"
            COOKIES = {'session': self.get_session_cookie()}
            PARAMS = {
                "User-Agent": 'https://github.com/danpfister/advent-of-code-2023',
            }
            try:
                request = requests.get(url=URL, cookies=COOKIES, params=PARAMS)
                text_file_path.write_text(request.text)
                print(f"downloaded input file to {text_file_path}")
            except:
                print(f"aoc request failed!")
                raise
            return
        print(f"input file for day already exists")
        return
    
    def create_new_py(self):
        py_file_path = self.ROOT_DIR / f"{self.year}" / f"day{self.day:0>2}" / f"day{self.day:0>2}.py"
        try:
            with open('py_template.txt', 'r') as template_file: template_content = template_file.read()
        except:
            print(f"reading python template failed!")
            raise
        template = Template(template_content)
        content = template.substitute(
            root_folder=f"{self.year}",
            day=f"{self.day:0>2}"
        )
        if not py_file_path.is_file():
            with open(py_file_path, "w", encoding="utf-8") as file: file.write(content)
            print(f"created python file at {py_file_path}")
            return
        print("python file for current day already exists")
        return
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Input downloader for Advent of Code")
    parser.add_argument('-d', '--day', help="force download of specific day", default=None, required=False)
    parser.add_argument('-y', '--year', help="force download of specific year", default=None, required=False)
    parser.add_argument('--py', help='set to create an empty python file', action='store_true', default=False, required=False)
    parser.add_argument('-f', '--force', help="force overwrite of input.txt", action='store_true', default=False, required=False)
    args = parser.parse_args()
    aoc_downloader(args=args)