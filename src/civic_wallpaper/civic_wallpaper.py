from pathlib import Path
from typing import Annotated
from PIL import Image, ImageOps
import typer
from rich import print



WALLPAPER_SIZE = (1024, 600)
BMP_EXT = ".bmp"



app = typer.Typer(
    no_args_is_help=True,
    context_settings={
        "help_option_names": ["-h", "--help"]
    },
    # rich_markup_mode="markdown",
    pretty_exceptions_show_locals=True,
    suggest_commands=True
)



def make_wallpaper(input_path: Path, output_path: Path):
    with Image.open(input_path) as img:
        img = img.convert("RGB")

        resized_img = ImageOps.fit(img, WALLPAPER_SIZE, centering=(0.5, 0.5))

        resized_img.save(
            output_path,
            optimize=True,
            quality=90
        )

        print(f"[bold green]Saved wallpaper to: {output_path}![/bold green]")



@app.command(
    no_args_is_help=True,
    help="Convert images to wallpaper size/format for 2018 Honda Civics.",
)
def main(
    img_path: Annotated[
        Path,
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
            "-y", "--yes", "--confirm",
            help="Bypass file overwrite confirmation"
        )
    ] = False,
    display_img: Annotated[
        bool,
        typer.Option(
            "-s", "--show",
            help="Open the wallpaper image after creation"
        )
    ] = False
):
    if output_path.exists():
        if output_path.is_dir():
            output_path = output_path.joinpath(img_path.with_suffix(BMP_EXT).name)
    else:
        if output_path.parent.is_dir():
            output_path = output_path.with_suffix(BMP_EXT)
        else:
            raise typer.TyperException("That file path does not exist!")

    if output_path.exists() and not confirm_overwrite:
        typer.confirm(f"File already exists. Overwite?", abort=True)

    make_wallpaper(img_path, output_path)

    if display_img:
        with Image.open(output_path) as img:
            img.show()


if __name__ == "__main__":
    app()
