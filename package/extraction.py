import re
import joblib
class extract:
    def __init__(self, userInput, model):
        self.userInput = userInput
        self.model = model
        self.number = 0
    def process(self):
        tfidf = joblib.load('model/tfidf.pkl')
        isdigit = bool(re.search(r'\d', self.userInput))
        if isdigit == True:
            breaking = re.findall(r'\d+', self.userInput)
            number = "".join(breaking)
            self.number = int(number)

        self.userInput = tfidf.transform([self.userInput])
        predict = self.model.predict(self.userInput)[0]
        predict = int(predict)
        number = int(self.number)
        
        return predict, number
