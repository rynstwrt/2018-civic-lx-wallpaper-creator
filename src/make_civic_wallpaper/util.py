from pathlib import Path
from typing import Callable

import typer
from rich import print
from upath import UPath


WALLPAPER_SIZE = (1024, 600)
TARGET_EXT = ".jpg"


def print_success_message(msg: str):
    print(f"\n[bold green]{msg}[/bold green]\n")


def print_error_message(msg: str):
    print(f"\n[bold red]Error: {msg}[/bold red]\n")


def name_function[T: Callable](function: T, name: str) -> T:
    function.__name__ = name
    return function


def named_function[T: Callable](name: str) -> Callable[[T], T]:
    return lambda function: name_function(function, name)


@named_function("Path | URL")
def parse_img_path(path_or_url: str) -> UPath:
    return UPath(path_or_url)


def validate_img_src(ctx: typer.Context, img_src: UPath):
    if ctx.resilient_parsing:
        return None

    img_src = img_src.resolve()
    if not img_src.is_file():
        print_error_message("Given source image is not a file!")
        raise typer.Exit()

    return img_src


def validate_output_path(ctx: typer.Context, output_path: Path):
    if ctx.resilient_parsing:
        return None

    img_src_param: str | None = ctx.params.get("img_src")
    if not img_src_param:
        return None

    suffixed_img_src_name = UPath(img_src_param).with_suffix(TARGET_EXT).name

    if output_path.exists():
        if output_path.is_dir():
            return output_path / suffixed_img_src_name
        else:
            return output_path
    elif output_path.parent.is_dir():
        return output_path / output_path.with_suffix(TARGET_EXT)

    return None



