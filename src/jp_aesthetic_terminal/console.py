import random
from time import sleep

import click
import requests

from . import __version__

API_URL = "https://ja.wikipedia.org/api/rest_v1/page/random/summary"


def fancy_print(line):

    for i in range(len(line)):
        print("\033[1;32;1m" + line[i], sep=",", end="", flush=True)
        sleep(random.uniform(0, 0.5))


@click.command()
@click.version_option(version=__version__)
def main():
    """The premier Japanese aesthetic terminal!!!"""

    with requests.get(API_URL) as response:
        response.raise_for_status()
        data = response.json()

    title = data["title"]
    extract = data["extract"]
    extract = extract.split("、")

    fancy_print(title)
    print("\n")
    for line in extract:
        fancy_print(line)
        print("\n")
