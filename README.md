# Advent of Code

Solving the [Advent of Code](https://adventofcode.com) in Python (mostly).

## AOC Downloader

The `aoc_downloader.py` can be used to create a folder and download the input for a specific day.

### Setup

Place `aoc_downloader.py` in your AOC folder and install the dependencies with `pip install -r requirements.txt`.

The [session cookie](https://github.com/wimglenn/advent-of-code-wim/issues/1) needs to be stored in a file `config.json` in this format:

```
{
    "session_cookie": "your-session-cookie-here"
}
```

### Usage

Running `python aoc_downloader.py` creates a directory with the input file inside.

Passing the optional parameter `--day` or `--year` forces the download for a specific date, otherwise it defaults to the current date (The month is always assumed to be December).
The optional parameter `--py` adds a templated python file to the created directory.

For example, running

```
python path/to/aoc_downloader.py --day 17 --year 2021 --py
```

creates the folder and files as follows:

```
advent-of-code/
|
|-- 2021/
|    |
|    |-- day17/
|         |
|         |-- input.txt
|         |-- day17.py
|
|-- aoc_downloader.py

```