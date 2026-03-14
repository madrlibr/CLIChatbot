from .function import *
from .extraction import extract

def prompting(model, message, data):
    df = data
    extraction = extract(userInput=message, model=model)
    predict, number = extraction.process()

    functionMap = {
        1: df,
        2: describe(df),
        3: info(df),
        4: dropna(df),
        5: head(df, number),  
        6: tail(df, number),
        7: selectColumn(df, number),
        8: meanColumn(df, number),
        9: medianColumn(df, number),
        10: sumColumn(df, number),
        11: checkDtype(df, number),
        12: changeType(message, number, df), 
        13: fillna(df, number, message),
        14: deleteRow(df, number),
        15: modusColumn(df, number)
    }

    respond = functionMap[predict]
    return respond
