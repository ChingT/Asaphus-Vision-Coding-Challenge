import click

from coding_challenge.functions import run


@click.command()
@click.argument("input_file_path", type=click.Path(exists=True))
@click.argument("output_file_path", type=click.Path(), default="./output.txt")
@click.option(
    "-l",
    "--substring-len",
    type=int,
    default=5,
    show_default=True,
    help="The length of a substring to be found, should be at least 1.",
)
@click.option(
    "-n",
    "--num-largest-substrings",
    type=int,
    default=4,
    show_default=True,
    help="The number of lexicographically largest substrings to be found, should be "
         "at least 1.",
)
def main_cli(input_file_path, output_file_path, substring_len, num_largest_substrings):
    run(input_file_path, output_file_path, substring_len, num_largest_substrings)


if __name__ == "__main__":
    main_cli()
