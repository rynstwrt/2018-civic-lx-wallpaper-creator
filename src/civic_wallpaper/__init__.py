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


# from rich import print
#
#
#
# def test():
#     print("[bold cyan on red]test[/bold cyan on red]")
#     print("[yellow]asdfasdf[/yellow]")
#     print("[#FF6600]asdfasdfsadf[/#ff6600]")
#
#     # s = Status("Status...", speed=2)
#     # s.start()
#     # sleep(2)
#     # s.stop()
#
#
#     return
#
#
#     # p = Progress()
#     # p.start()
#     #
#     # try:
#     #     task1 = p.add_task("running...", total=None)
#     #
#     #     while not p.finished:
#     #         p.update(task1, advance=0.1)
#     #         sleep(0.02)
#     # finally:
#     #     p.stop()
#     #
#     #
#     #
#     #
#     #
#     # return
#
#     # for step in track(range(100)):
#     #     print("AAA")
#     #     print(step)
#     #     sleep(1)
#     # return
#     a = Confirm.ask("confirm?")
#     print(a)
#     # a = Prompt.ask("hmM???", default='yeet')
#     # print(a)
