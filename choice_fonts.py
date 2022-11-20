import rich
import random
import pyfiglet

from rich.console import Console
from rich.prompt import Prompt
from pyfiglet import figlet_format

console = Console()

def Choice_Fonts():
    get_fonts = pyfiglet.FigletFont.getFonts()

    count = 0
    
    for fonts in get_fonts:

       count += 1
       console.print(f'[bold red][{count}][/] {fonts}')

    try:
    
        choice = int(Prompt.ask(
           '\n[bold magenta]choice fonts[/]',
           default=str(len(get_fonts))
        ))

        choice = get_fonts[
            int(choice)
        ]
    
        text = console.input('[bold red]name your banner[/]> ')
        color = console.input('[bold purple]color[/]> ')
    
        banner = figlet_format(
              text = text, 
              font = str(choice)
        )
    
        console.print(f'[{color}]{banner}')

        if Prompt.ask('[bold red]save to file?', choices=['y', 'n']) == "y":
           with open('banners.txt', 'a') as file:
                file.write(str(banner))

                file.close()
                console.log('[bold green][+] Save')

                
    except Exception as error:
           console.print(
              '[bold red]ERROR [!]',
              error
           )


