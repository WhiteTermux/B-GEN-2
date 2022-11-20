import rich
import os
import sys

from misc import Menu
from rich.console import Console
from rich.prompt import Prompt
from gen_one import One_Banner
from choice_fonts import Choice_Fonts
from random_fonts import Random_Fonts

console = Console()

os.system('figlet B-GEN-2 | lolcat')

def Main():

    try:
        Menu()
        
        choice = console.input('\n[bold white]>> ')
        
        if choice == "1":
           One_Banner()

        elif choice == "2":
             Choice_Fonts()

        elif choice == "3":
             Random_Fonts()

        elif choice == "4":
             pass
                          
    except KeyboardInterrupt:
           console.print('<https://t.me/WhiteTermux>')
           sys.exit()
           
Main()           
