from .function import *
from .extraction import extract

def prompting(model, message, data):
    df = data
    extraction = extract(userInput=message, model=model)
    predict, number = extraction.process()

    functionMap = { 
        1: lambda: showAll(df), 
        2: lambda: describe(df), 
        3: lambda: info(df), 
        4: lambda: dropna(df), 
        5: lambda: head(df, number), 
        6: lambda: tail(df, number), 
        7: lambda: selectColumn(df, number), 
        8: lambda: meanColumn(df, number), 
        9: lambda: medianColumn(df, number), 
        10: lambda: sumColumn(df, number), 
        11: lambda: checkDtype(df, number), 
        12: lambda: changeType(message, number, df), 
        13: lambda: fillna(df, number, message), 
        14: lambda: deleteRow(df, number), 
        15: lambda: modusColumn(df, number) 
    }

    if predict in functionMap:
        return functionMap[predict]()
    else:
        return "Fungsi tidak ditemukan"
