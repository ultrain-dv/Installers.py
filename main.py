from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import os

console = Console()
title = Text("Installers.py", style="bold #90ee90", justify="center")

os.system("clear")
console.print(Panel(title, border_style="#6B8E23"))

console.print(Text("", style="bold #90ee90"))

input()