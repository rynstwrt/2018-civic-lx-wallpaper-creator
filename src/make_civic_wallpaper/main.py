from http.client import HTTPResponse
from pathlib import Path
from typing import Annotated
from PIL import Image, ImageOps
import typer
from PIL.ImageFile import ImageFile
from rich.prompt import Confirm
from io import BytesIO
from urllib.request import urlopen
from urllib.parse import urlparse
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



# def make_wallpaper(input_path: Path, output_file: Path):
#     with Image.open(input_path) as img:
#         img = img.convert("RGB")
#
#         resized_img = ImageOps.fit(img, WALLPAPER_SIZE, centering=(0.5, 0.5))
#
#         resized_img.save(
#             output_file,
#             optimize=True,
#             quality=100
#         )
#
#         print_success_message(f"Saved wallpaper to {output_file}!")


def make_wallpaper(img_src: Path | BytesIO, output_file: Path):
    with Image.open(img_src) as img:
        img = img.convert("RGB")

        resized_img = ImageOps.fit(img, WALLPAPER_SIZE, centering=(0.5, 0.5))

        resized_img.save(
            output_file,
            optimize=True,
            quality=100
        )

        print_success_message(f"Saved wallpaper to {output_file}!")




def make_wallpaper_from_url(url: str, output_file: Path):
    url = "https://i0.wp.com/www.roeselienraimond.com/wp-content/uploads/2025/10/red-fox-with-a-mole-prey.jpg"
    # url = "https://www.roeselienraimond.com/wp-content/uploads/2025/07/happy-smiling-zen-fox-roeselien-raimond.webp"
    with Image.open(BytesIO(urlopen(url).read())) as img:
        img = img.convert("RGB")

        resized_img = ImageOps.fit(img, WALLPAPER_SIZE, centering=(0.5, 0.5))

        resized_img.show()
        # resized_img.save(
        #     output_file,
        #     optimize=True,
        #     quality=100
        # )
        #
        # print_success_message(f"Saved wallpaper to {output_file}!")



@app.command(
    no_args_is_help=True,
    help="Convert images to wallpaper size/format for 2018 Honda Civics.",
)
def main(
    img_src: Annotated[
        UPath,
        typer.Argument(
            dir_okay=False,
            resolve_path=True,
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
    # img_src = BytesIO(urlopen(img_src).read()) if is_url(img_src) else Path(img_src)
    # if is_url(img_src):
    #     parsed_url = urlparse(img_src)
    #     url_path = Path(parsed_url.path).name
    #     asdf: BytesIO = BytesIO(urlopen(img_src).read())
        # print(url_path)


    img_src = UPath(img_src)
    print(img_src.name)
    # print(img_src.path)


    return

    output_file = resolve_output_path(img_path, output_path)
    if not output_file:
        print_error_message("Invalid output path given! File path does not exist!")
        raise typer.Exit()

    if output_file.exists() and not confirm_overwrite:
        if not Confirm.ask(f'[bold yellow]File "{output_file.relative_to(Path.cwd())}" already exists. Do you want to overwite?'):
            raise typer.Exit()

    make_wallpaper(img_path, output_file)


if __name__ == "__main__":
    app()
