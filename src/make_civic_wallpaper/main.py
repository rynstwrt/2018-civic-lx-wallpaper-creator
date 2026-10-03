from pathlib import Path
from typing import Annotated
from PIL import Image, ImageOps
import typer
from rich.prompt import Confirm
from .util import (parse_img_path,
                   validate_img_src,
                   validate_output_path,
                   WALLPAPER_SIZE,
                   print_success_message)
from upath import UPath



app = typer.Typer(
    no_args_is_help=True,
    context_settings={
        "help_option_names": ["-h", "--help"]
    },
    suggest_commands=True
)



def make_wallpaper(img_src: UPath, output_file: Path):
    with img_src.open("rb") as file:
        with Image.open(file) as img:
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
    help="Convert images to wallpaper size/format for 2018 Honda Civics LX's."
)
def main(
        img_src: Annotated[
            UPath,
            typer.Argument(
                metavar="image",
                help="The source image file path or URL",
                parser=parse_img_path,
                callback=validate_img_src,
                is_eager=True
            )
        ],
        output_path: Annotated[
            Path,
            typer.Option(
                "-o", "--output",
                resolve_path=True,
                help="The directory or file to as save at/as",
                callback=validate_output_path
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
    if not output_path:
        raise typer.BadParameter("Output path is invalid!")

    if output_path.exists() and not confirm_overwrite:
        if not Confirm.ask(f"{output_path} already exists. Overwrite?"):
            raise typer.Exit()

    make_wallpaper(img_src, output_path)



if __name__ == "__main__":
    app()
