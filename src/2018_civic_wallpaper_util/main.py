from pathlib import Path
from PIL import Image, ImageOps


WALLPAPER_SIZE = (1024, 600)


def make_wallpaper(input_path: Path, output_path: Path = Path.cwd()):
    if output_path.is_dir():
        output_path = output_path.joinpath(input_path.with_suffix(".bmp").name)

    with Image.open(input_path) as img:
        if img.mode in ("RGBA", "P") and output_path.name.lower().endswith(('.jpg', '.jpeg')):
            img = img.convert("RGB")

        # resized_img = img.resize(WALLPAPER_SIZE, Image.Resampling.LANCZOS)
        # resized_img = ImageOps.cover(img, WALLPAPER_SIZE, method = Image.Resampling.LANCZOS)
        # resized_img = resized_img.crop
        resized_img = ImageOps.fit(img, WALLPAPER_SIZE, centering=(0.5, 0.5))
        resized_img.save(output_path, optimize=True, quality=90)

        print(f"Saved wallpaper to: {output_path}!")


def start():
    make_wallpaper(Path("images/original/privacy.JPG").resolve())
    # make_wallpaper()


if __name__ == "__main__":
    start()