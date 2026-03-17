from package.prompting import *
import joblib
import pandas as pd
import os
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import pyfiglet
from colorama import init, Fore, Style

init()

def startchat(model, df, colort='white'):
    #colort = colort.upper()
    cs = Console()

    cs.print('[yellow]reading dataset and model...[/yellow]')
    try:
        df = pd.read_csv(df)
        model = joblib.load(model)
        cs.print('[green]dataset and model readed![/green]')
        chat = True
    except Exception as e:
        cs.print(f"[red]reading fail!!![/red]")
        cs.print(f"[red]Chat fail to open because system encounter:\n{e}[/red]")
        chat = False
    

    while chat == True:
        userInput = input(Fore.YELLOW + 'You: ' + Style.RESET_ALL)
        userInput = userInput.lower()
        if userInput == ':quit':
            print('Chat closed!')
            break

        if userInput == ':cls':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
     
        if userInput == ':welcome':
            ascii = pyfiglet.figlet_format("DCHAT", font="slant") 
            styled = Text(ascii, style="bold green")
        
        if userInput == ':setcolor':
            colort = input('set color: ')
            continue

            cs.print(styled)
            cs.print("Deskripsi", justify="center", style="dim")

            description = (
                "DChat adalah libray chatbot assitant untuk analisa dan manipulasi ringan pada dataset"
            )
            cs.print(Panel(description, border_style="bright_black"))
            continue

        try:
            prompt = prompting(
                model=model,
                message=userInput,
                df=df
            )
            cs.print(f'[{colort}]Bot: {prompt}[/{colort}]')
        except Exception as e:
            cs.print(f"[red]Error: {e}[/red]")


startchat(model='model/panda.joblib', df='data/StudentPerformance.csv', colort='green')
