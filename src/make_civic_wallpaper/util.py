from pathlib import Path
from urllib.parse import urlparse
from rich import print
from upath import UPath



WALLPAPER_SIZE = (1024, 600)
TARGET_EXT = ".jpg"



def print_success_message(msg: str):
    print(f"\n[bold green]{msg}[/bold green]\n")


def print_error_message(msg: str):
    print(f"\n[bold red]Error: {msg}[/bold red]\n")


def is_url(img_path: str):
    try:
        result = urlparse(img_path)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def resolve_output_path(img_path: UPath, output_path: Path):
    if output_path.exists():
        if output_path.is_file():
            return output_path
        elif output_path.is_dir():
            return output_path.joinpath(img_path.with_suffix(TARGET_EXT).name)
    else:
        if output_path.parent.is_dir():
            return output_path.with_suffix(TARGET_EXT)

    return None
