from package.prompting import *
import joblib
import pandas as pd
import os


print('reading dataset and model...')
try:
    df = pd.read_csv('data/StudentPerformance.csv')
    model = joblib.load('model/panda.joblib')
    print('dataset and model readed!')
except Exception as e:
    print(f"reading fail: {e}")

while True:
    userInput = str(input('You: '))
    userInput = userInput.lower()

    if userInput == 'quit':
        print('Chat closed!')
        break

    if userInput == 'cls':
        os.system('cls' if os.name == 'nt' else 'clear')
        continue

    try:
        prompt = prompting(
            model=model,
            message=userInput,
            data=df
        )
        print(f'Bot: {prompt}')
    except Exception as e:
        print(f"Error: {e}")    
