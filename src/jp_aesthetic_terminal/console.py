import random
from time import sleep

import click
import requests

from . import __version__, wikipedia

API_URL = "https://ja.wikipedia.org/api/rest_v1/page/random/summary"


def fancy_print(line, title=False):

    color = "32"

    if title:
        color = "36"

    for i in range(len(line)):
        print("\033[1;{};1m".format(color) + line[i], sep=",", end="", flush=True)
        sleep(random.uniform(0, 0.5))


@click.command()
@click.option("-i", "--iterations", default=50)
@click.option("-s", "--time_to_sleep", default=2)
@click.version_option(version=__version__)
def main(iterations, time_to_sleep):
    """The premier Japanese aesthetic terminal!!!"""

    for i in range(iterations):
        data = wikipedia.random_page()

        title = data["title"]
        extract = data["extract"]
        extract = extract.split("、")

        fancy_print(title, title=True)
        print("\n")
        for line in extract:
            fancy_print(line)
            print("\n")

        sleep(time_to_sleep)
