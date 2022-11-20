import rich

from rich.console import Console

console = Console()

def Menu():
    """Menu"""
    
    choices = (
        ('Generate a banner in one random font'),
        ('Generate banner with font selection'),
        ('Generate multiple banners with random text')
    )
    
    
    for number, choices in enumerate(
        choices,
        start = 1

    ):
      console.print(
         f'[bold white][{number}] {choices}'

      )






