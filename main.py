import click
from day10.parse import score_lines

@click.command()
@click.argument('file_path', type=click.Path(exists=True))
def main(file_path):
    with open(file_path, 'r') as input:
        lines = [line.strip() for line in input.readlines()]
        print(score_lines(lines))

if __name__ == '__main__':
    main()