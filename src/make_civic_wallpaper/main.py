from pathlib import Path
from typing import Annotated
from PIL import Image, ImageOps
import typer
from rich.prompt import Confirm
from .util import (named_function,
                   TARGET_EXT, WALLPAPER_SIZE,
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



@named_function("Path | URL")
def parse_img_path(path_or_url: str) -> UPath:
    return UPath(path_or_url)



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
            )
        ],
        output_path: Annotated[
            Path,
            typer.Option(
                "-o", "--output",
                resolve_path=True,
                # show_default=False,
                help="The directory or file to as save at/as",
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
    img_src = img_src.resolve()
    if not img_src.is_file():
        print_error_message("Given source image is not a file!")
        raise typer.Exit()

    if output_path.exists():
        if output_path.is_dir():
            output_path = output_path / img_src.name
        elif not confirm_overwrite:
            if not Confirm.ask(f'[bold yellow]File "{output_path.relative_to(Path.cwd())}" already exists. Do you want to overwite?'):
                raise typer.Exit()
    else:
        is_hypothetical_file = output_path.suffix
        if is_hypothetical_file:
            if not output_path.parent.is_dir():
                print_error_message("Given output file parent directory does not exist!")
                raise typer.Exit()
        else:
            if output_path.parent.is_dir():
                output_path = output_path.with_suffix(TARGET_EXT)
            else:
                print_error_message("Given output file parent directory does not exist!")
                raise typer.Exit()

    make_wallpaper(img_src, output_path)



if __name__ == "__main__":
    app()
