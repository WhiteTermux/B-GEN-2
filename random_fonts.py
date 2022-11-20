import os
import sys
import rich
import random
import pyfiglet

from rich.console import Console
from rich.prompt import Prompt
from pyfiglet import figlet_format

console = Console()

def Random_Fonts():
    get_fonts = pyfiglet.FigletFont.getFonts()

    try:

       text = console.input('[bold red]name your banner[/]> ')

       many = int(Prompt.ask(
          "[bold red]how to many generate?[/]",
          default="10"
        
       ))

    except KeyboardInterrupt:
           console.print('<https://t.me/WhiteTermux')

    try:
        count = 0
        
        while count < many:

              banners = figlet_format(
                text,
                random.choice(get_fonts)
              )      

              file = open('banners.txt', 'a')
              file.write(str(banners))

              file.close()
              
              count += 1
              
              console.print(
                f"[{count}] Generated.",
                style = "bold white"
              )

        console.log('banners save to "banners.txt"')
        
    except Exception as error:
           console.print(
               "[bold red]ERROR [!]:",
               error
            )

