from typing import Callable
from rich import print


WALLPAPER_SIZE = (1024, 600)
TARGET_EXT = ".jpg"


def print_success_message(msg: str):
    print(f"\n[bold green]{msg}[/bold green]\n")


def print_error_message(msg: str):
    print(f"\n[bold red]Error: {msg}[/bold red]\n")


def name_function[T: Callable](function: T, name: str) -> T:
    function.__name__ = name
    return function


def named_function[T: Callable](name: str) -> Callable[[T], T]:
    return lambda function: name_function(function, name)
