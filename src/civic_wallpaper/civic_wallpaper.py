import time
from pathlib import Path
from typing import Annotated
from PIL import Image, ImageOps
import typer
from rich import print
from rich.progress import Progress, SpinnerColumn, TextColumn


WALLPAPER_SIZE = (1024, 600)
BMP_EXT = ".bmp"

app = typer.Typer(
    no_args_is_help=True,
    context_settings={
        "help_option_names": ["-h", "--help"]
    },
    rich_markup_mode="markdown"
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
                # rich_help_panel="Required Arguments"
            )
        ],
        output_path: Annotated[
            Path,
            typer.Option(
                "-o", "--output",
                resolve_path=True,
                show_default=False,
                help="The directory or file you want to export the wallpaper to",
                # rich_help_panel="Image CLI Options"
            )
        ] = Path.cwd()
):
    if output_path.exists():
        if output_path.is_dir():
            output_path = output_path.joinpath(img_path.with_suffix(BMP_EXT).name)
    else:
        if output_path.parent.is_dir():
            output_path = output_path.with_suffix(BMP_EXT)
        else:
            raise typer.TyperException("That file path does not exist!")



    if output_path.exists():
        typer.confirm(f"File already exists. Overwite?", abort=True)

    print("CONFIRM!")

    with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            # transient=True
    ) as progress:
        progress.add_task(description="Creating image...", total=None)
        make_wallpaper(img_path, output_path)
        # time.sleep(2)

    print("end")


    # with Progress(
    #         SpinnerColumn(spinner_name="dots"),
    #         TextColumn("[progress.description]{task.description}"),
    #         # TextColumn("[bold green]{task.fields}[/bold green]", justify="right"),
    #         # BarColumn(bar_width=None),
    #         # "[progress.percentage]{task.percentage:>3.1f}%",
    # ) as progress:
    #     task = progress.add_task(description="tasking", start=False)
    #     # progress.start_task(task, )
    #     # progress.start()
    #     progress.update(task, increment=1)
    #     time.sleep(5)

    # with Progress(
    #         SpinnerColumn(),
    #         TextColumn("asdfsadf"),
    #         transient=True
    # ) as progress:
    #     task1 = progress.add_task("yeet", start=False)
    #
    #     for i in range(10):
    #         progress.update(task1, advance=1)
    #         time.sleep(1)


# progress.start()
# time.sleep(2)
# progress.stop()

# progress = Progress(
# SpinnerColumn(),
# TextColumn()
# )

# progress.start()
# progress.print()
# progress.update()

# time.sleep(2)
# progress.stop()

# with Status("asdfasdf") as status:
#     status.start()
#     make_wallpaper(img_path, output_path)
#     status.stop()
#     print("DONE!")


if __name__ == "__main__":
    app()
