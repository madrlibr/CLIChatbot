from src.prompting import *
import joblib
import pandas as pd

df = pd.read_csv('data/StudentPerformance.csv')
model = joblib.load('model/panda.joblib')

while True:
    userInput = str(input('You: '))
    userInput = userInput.lower()

    if userInput == 'quit':
        print('Chat closed!')
        break

    try:
        prompt = prompting(
            model=model,
            message=userInput,
            data=df
        )
        print(f'Bot: {prompt}')
    except Exception as e:
        print(f"Error: {e}")    
