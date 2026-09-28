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


def make_wallpaper(input_path: Path, output_path: Path = Path.cwd()):
    if output_path.is_dir():
        output_path = output_path.joinpath(input_path.with_suffix(".bmp").name)
    elif output_path.is_file():
        output_path = output_path.with_suffix(".bmp")

    with Image.open(input_path) as img:
        # if img.mode in ("RGBA", "P") and output_path.name.lower().endswith(('.jpg', '.jpeg')):
        img = img.convert("RGB")

        resized_img = ImageOps.fit(img, WALLPAPER_SIZE, centering=(0.5, 0.5))

        resized_img.save(
            output_path,
            optimize=True,
            quality=90
        )

        print(f"Saved wallpaper to: {output_path}!")


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
            Path | None,
            typer.Option(
                "-o", "--output",
                file_okay=True,
                dir_okay=True,
                resolve_path=True,
                help="The directory or file you want to export the wallpaper to"
            )
        ] = None
):
    # print(input_img)
    # print(output_path)
    args = [input_img]
    if output_path:
        args.append(output_path)
    # make_wallpaper(input_img, output_path)
    make_wallpaper(*args)


if __name__ == "__main__":
    app()