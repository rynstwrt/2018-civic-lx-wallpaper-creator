from pathlib import Path
from PIL import Image, ImageOps
# import typer


WALLPAPER_SIZE = (1024, 600)
BIT_DEPTH = 24


app = typer.Typer()


def make_wallpaper(input_path: Path, output_path: Path = Path.cwd()):
    if output_path.is_dir():
        output_path = output_path.joinpath(input_path.with_suffix(".bmp").name)

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


def start():
    make_wallpaper(Path("images/working/wallpaper2.bmp").resolve())
    # make_wallpaper()


if __name__ == "__main__":
    start()