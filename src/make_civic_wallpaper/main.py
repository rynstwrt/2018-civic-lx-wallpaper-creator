from pathlib import Path
from typing import Annotated

from PIL import Image, ImageOps
import typer
from rich import print
from rich.prompt import Confirm
from rich.console import Console
from rich.style import Style

from .util import resolve_output_path, WALLPAPER_SIZE



success_console = Console(style=Style(color="green", bold=True))
err_console = Console(stderr=True, style=Style(color="red", bgcolor="black"))



app = typer.Typer(
    no_args_is_help=True,
    context_settings={
        "help_option_names": ["-h", "--help"]
    },
    pretty_exceptions_show_locals=True,
    suggest_commands=True
)



def make_wallpaper(input_path: Path, output_file: Path):
    with Image.open(input_path) as img:
        img = img.convert("RGB")

        resized_img = ImageOps.fit(img, WALLPAPER_SIZE, centering=(0.5, 0.5))

        resized_img.save(
            output_file,
            optimize=True,
            quality=100
        )

        print(f"[bold green]Saved wallpaper to: {output_file}![/bold green]")



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
            "-y", "--yes", "--confirm", "--overwrite",
            help="Bypass file overwrite confirmation"
        )
    ] = False
):
    success_console.print("success", end="\n")
    err_console.print("error")

    return

    output_file = resolve_output_path(img_path, output_path)

    if output_file.exists() and not confirm_overwrite:
        if not Confirm.ask(f'[bold yellow]File "{output_file.relative_to(Path.cwd())}" already exists. Do you want to overwite?'):
            raise typer.Exit()

    make_wallpaper(img_path, output_file)



if __name__ == "__main__":
    app()
