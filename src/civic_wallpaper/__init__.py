import time
import typer
from rich.progress import Progress, SpinnerColumn, TextColumn


app = typer.Typer()


@app.command()
def test():
    with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
    ) as progress:
        progress.add_task(description="pasdsdfsf", total=None)
        time.sleep(5)

    print("end")