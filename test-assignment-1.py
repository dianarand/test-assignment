import csv
import click
import requests

TIMEOUT_IN_SECONDS = 3

def ping_url(name, url):
    try:
        result = requests.get(url, timeout=TIMEOUT_IN_SECONDS)
        click.echo(f'"{name}", HTTP {result.status_code}, time {result.elapsed.total_seconds():.2f} seconds')
    except requests.exceptions.Timeout:
        click.echo(f'Skipping {url}')


def read_csv(input_file):
    with open(input_file) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter='|')
        for line in csv_reader:
            ping_url(line[0], line[1])


@click.command()
@click.option('-i', 'input_file', required=True, help="Path to input file")
def parse(input_file):
    """Parse file of urls and return http status code and how many seconds the request took"""
    try:
        read_csv(input_file)
    except FileNotFoundError:
        click.echo('ERROR: File not found')

if __name__ == '__main__':
    parse()
