import click
from day10.score import score_corrupted_lines

@click.command()
@click.argument('file_path', type=click.Path(exists=True))
def main(file_path):
    with open(file_path, 'r') as input:
        lines = [line.strip() for line in input.readlines()]
        print(score_corrupted_lines(lines))

if __name__ == '__main__':
    main()