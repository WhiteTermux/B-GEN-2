import random
import rich
import os
import sys
import pyfiglet

from rich.console import Console
from rich.prompt import Prompt
from pyfiglet import figlet_format

console = Console()

def One_Banner():
    """Generate one random banner"""
    
    try:

       text = console.input('[bold red]text your banner[/]> ')
       color = console.input('[bold red]color[/]> ')

       get_fonts = pyfiglet.FigletFont.getFonts()

       banner = figlet_format(
            text = text, 
            font = random.choice(get_fonts)
       )

       console.print(f'[{color}]{banner}')
      
       if Prompt.ask('[bold red]save to file?', choices=['y', 'n']) == "y":
          with open('banners.txt', 'a') as file:
               file.write(str(banner))

               file.close()
               console.log('[bold green][+] Save')

        
    except Exception as error:
           console.print(
              f'[bold red][!] Failed generate to banner!',
              error
           )    
       


