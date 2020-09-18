"""Command-line interface"""
import random
from time import sleep

import click

from . import __version__, wikipedia


def fancy_print(line: str, title: bool = False):

    color: str = "32"

    if title:
        color = "36"

    for i in range(len(line)):
        print("\033[1;{};1m".format(color) + line[i], sep=",", end="", flush=True)
        sleep(random.uniform(0, 0.5))


@click.command()
@click.option("-i", "--iterations", default=50)
@click.option("-s", "--time_to_sleep", default=2)
@click.version_option(version=__version__)
def main(iterations: int, time_to_sleep: int) -> None:
    """The premier Japanese aesthetic terminal!!!"""

    for _i in range(iterations):
        page = wikipedia.random_page()

        title = page.title
        extract = page.extract
        extract = extract.split("、")

        fancy_print(title, title=True)
        print("\n")
        for line in extract:
            fancy_print(line)
            print("\n")

        sleep(time_to_sleep)
