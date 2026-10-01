from pathlib import Path
from typing import Annotated
from PIL import Image, ImageOps
import typer
from rich.prompt import Confirm
from io import BytesIO
from urllib.request import urlopen
from .util import (is_url, resolve_output_path,
                   WALLPAPER_SIZE,
                   print_success_message,
                   print_error_message)
from upath import UPath


app = typer.Typer(
    no_args_is_help=True,
    context_settings={
        "help_option_names": ["-h", "--help"]
    },
    pretty_exceptions_show_locals=True,
    suggest_commands=True
)



def make_wallpaper(img_src: UPath, output_file: Path):
    img_src = BytesIO(urlopen(str(img_src)).read()) if is_url(str(img_src)) else img_src.path
    with Image.open(img_src) as img:
        img = img.convert("RGB")

        resized_img = ImageOps.fit(img, WALLPAPER_SIZE, centering=(0.5, 0.5))

        resized_img.save(
            output_file,
            optimize=True,
            quality=100
        )

        print_success_message(f"Saved wallpaper to {output_file}!")



@app.command(
    no_args_is_help=True,
    help="Convert images to wallpaper size/format for 2018 Honda Civics.",
)
def main(
    img_src: Annotated[
        str,
        typer.Argument(
            dir_okay=False,
            # resolve_path=True,
            metavar="image",
            help="The source image file",
        )
    ],
    output_path: Annotated[
        Path,
        typer.Option(
            "-o", "--output",
            resolve_path=True,
            show_default=False,
            help="The directory or file you want to export the wallpaper to",
        )
    ] = Path.cwd(),
    confirm_overwrite: Annotated[
        bool,
        typer.Option(
            "-y", "--yes", "--confirm", "--overwrite",
            help="Bypass file overwrite confirmation"
        )
    ] = False
):
    img_src = UPath(img_src)

    output_file = resolve_output_path(img_src, output_path)
    if not output_file:
        print_error_message("Invalid output path given! File path does not exist!")
        raise typer.Exit()

    if output_file.exists() and not confirm_overwrite:
        if not Confirm.ask(f'[bold yellow]File "{output_file.relative_to(Path.cwd())}" already exists. Do you want to overwite?'):
            raise typer.Exit()

    make_wallpaper(img_src, output_file)



if __name__ == "__main__":
    app()
