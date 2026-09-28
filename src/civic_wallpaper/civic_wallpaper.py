from pathlib import Path
from typing import Annotated
from PIL import Image, ImageOps
import typer



WALLPAPER_SIZE = (1024, 600)



app = typer.Typer(
    no_args_is_help=True,
    context_settings={
        "help_option_names": ["-h", "--help"]
    }
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

        typer.echo(f"[green][bold]Saved wallpaper to: {output_path}!")



@app.command(no_args_is_help=True)
def main(
        input_img: Annotated[
            Path,
            typer.Argument(
                readable=True,
                file_okay=True,
                dir_okay=False,
                resolve_path=True,
                help="The source image file"
            )
        ],
        output_path: Annotated[
            Path,
            typer.Option(
                "-o", "--output",
                file_okay=True,
                dir_okay=True,
                resolve_path=True,
                help="The directory or file you want to export the wallpaper to",
            )
        ] = Path.cwd()
):
    if output_path.exists():
        if output_path.is_dir():
            output_path = output_path.joinpath(input_img.with_suffix(".bmp").name)
    else:
        if output_path.parent.is_dir():
            output_path = output_path.with_suffix(".bmp")
        else:
            raise typer.TyperException("That file path does not exist!")

    make_wallpaper(input_img, output_path)



if __name__ == "__main__":
    app()