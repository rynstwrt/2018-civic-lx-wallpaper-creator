from pathlib import Path
from typing import Annotated

from PIL import Image, ImageOps
import typer


WALLPAPER_SIZE = (1024, 600)
BIT_DEPTH = 24


app = typer.Typer(
    no_args_is_help=True,
    context_settings={
        "help_option_names": ["-h", "--help"]
    }
)


# def make_wallpaper(input_path: Path, output_path: Path = Path.cwd()):
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
                help="The directory or file you want to export the wallpaper to"
            )
        ] = Path.cwd()
):
    # input_file_name = input_img.name

    # output_dir = Path.cwd() if not output_path else output_path
    # print(output_dir)


    if not output_path.exists() and len(output_path.suffixes):
        if output_path.parent.is_dir():
            output_path = output_path.with_suffix(".bmp")
        else:
            raise typer.TyperException("That file path does not exist!")

    # if not output_path.exists() and len(output_path.suffixes):
    #     if output_path.parent.is_dir():
    #         output_path = output_path.with_suffix(".bmp")
    #         # output_path = output_path.parent.joinpath(output_path..with_suffix(".bmp").name)
    #     else:
    #         raise typer.TyperException("That file path does not exist!")

    print(output_path)

    if output_path.is_dir():
        pass # add input file name
    # elif

    # output_path = output_dir.joinpath(input_img.with_suffix(".bmp").name) if output_dir.is_dir() else output_dir.
    # output_path = output_dir.joinpath(with_suffix(".bmp")
    # return



    # if not output_path:
    #     output_path = Path.cwd().joinpath(input_img.with_suffix(".bmp").name)

    # print(input_img)
    # print(output_path.exists(), output_path.is_dir())
    # print(output_path.suffixes)


    # print(output_path)


    # print(input_img.with_name("asdf.bmp"))

    # make_wallpaper(input_img, output_path)


if __name__ == "__main__":
    app()