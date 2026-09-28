from pathlib import Path
import typer


WALLPAPER_SIZE = (1024, 600)
# TARGET_EXT = ".bmp"
TARGET_EXT = ".jpg"



def resolve_output_path(img_path: Path, output_path: Path):
    if output_path.exists():
        if output_path.is_file():
            return output_path
        elif output_path.is_dir():
            return output_path.joinpath(img_path.with_suffix(TARGET_EXT).name)
    else:
        if output_path.parent.is_dir():
            return output_path.with_suffix(TARGET_EXT)
        # if len(output_path.suffix) and output_path.parent.is_dir():
        #     return output_path.with_suffix(TARGET_EXT)

    raise typer.TyperException("Invalid output path given! File path does not exist!")

    # if output_path.exists():
    #     if output_path.is_dir():
    #         print("ISEXISTDIR")
    #         output_path = output_path.joinpath(img_path.with_suffix(TARGET_EXT).name)
    # else:
    #     if output_path.parent.is_dir():
    #         if output_path.suffix:
    #             print("D")
    #         else:
    #             print("E")
    #             output_path = output_path.with_suffix(TARGET_EXT)
    #     else:
    #         print("MEME")
    #         raise typer.TyperException("That file path does not exist!")
    #
    # return output_path
