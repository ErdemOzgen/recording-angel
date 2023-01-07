"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Recording Angel."""


if __name__ == "__main__":
    main(prog_name="recording-angel")  # pragma: no cover
