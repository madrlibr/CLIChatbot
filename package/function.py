import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


def showAll(data):
    return f"Menampilkan semua baris\n{data.to_string()}"

def describe(data):
    data = data.describe()
    return f'Menampilkan deskripsi dataset\n{data}'
        
def head(data, n):
    data = data.head(n)
    return f'Menampilkan {n} baris awal\n{data}'

def info(data):
    try:
        return f"Menampilkan informasi dataset\n{data.info()}"
    except Exception as e:
        return f"Terjadi kesalahan: {e}"
def dropna(data):
    try:
        return data.dropna()
    except:
        return "Error!"
    
def tail(data, n):
    data = data.tail(n)
    return f'Menampilkan {n} baris akhir\n{data}'

def deleteRow(data, n):#this function is still not working properly
    try:
        return data.drop(n)
    except:
        return "Error!"
    
def selectColumn(data, n):
    try:
        column_name = data.columns[n]
        return f'Menampilkan kolom {column_name} dengan index ke-{n}\n{data.iloc[:, n]}'
    except:
        pass

def meanColumn(data, n):
    column = selectColumn(data, n)
    try:
        mean = round((column).mean(), 2)
        column_name = data.columns[n]
        return f"mean dari kolom {column_name} adalah {mean}"
    except:
        return "Kesalahan! tidak dapat melakukan operasi, pastikan kolom ada dan tipe data kolom adalah integer atau float"

def medianColumn(data, n):
    column = selectColumn(data, n)
    try:
        median = round((column).median(), 2)
        column_name = data.columns[n]
        return f"median dari kolom {column_name} adalah {median}"
    except:
        return "Kesalahan! tidak dapat melakukan operasi, pastikan kolom ada dan tipe data kolom adalah integer atau float"

def sumColumn(data, n):
    column = selectColumn(data, n)
    try:
        if column.dtype.kind in 'ifu':
            summ = column.sum()
            return f"sum dari kolom {data.columns[n]} adalah {summ}"
        else:
            return "Kesalahan! tidak dapat melakukan operasi, pastikan kolom ada dan tipe data kolom adalah integer atau float"
        
    except:
        return "Kesalahan! tidak dapat melakukan operasi, pastikan kolom ada dan tipe data kolom adalah integer atau float"

def modusColumn(data, n):
    try:
        column = selectColumn(data, n)
        column_name = data.columns[n]
        modus = column.mode()
        return f"modus dari kolom {column_name} adalah {modus}"
    except:
        return "Kesalahan! tidak dapat melakukan operasi modus!"
    
def checkDtype(data, n):
    try:
        column_name = data.columns[n]
        column = selectColumn(data, n)
        dtype = (column.dtype)
        return f"Tipe data kolom '{column_name}' (index-{n}) adalah {dtype}"
    except:
        return f"Kesalahan! tidak ada kolom dengan index ke-{n}"
    
def changer(type, input, n, data):
    input = input.split()
    n = int(n)
    column_name = data.columns[n]
    getdtypef =  data.iloc[:, n].dtype
    if type in input:   
        try:
            data[column_name] = data[column_name].astype(type)
            getdtypen = data[column_name].dtype
            return f"Mengubah kolom '{column_name}' (index {n}), dari {getdtypef} ke {getdtypen}"
        except Exception as e:
            return f"Terjadi kesalahan: {e}"

def changeType(user_input, n, data):
    targets = {
        "int": "int",
        "float": "float",
        "string": "string"
        }  
    try:
        for key, val in targets.items():
            if key in user_input:
                return changer(val, user_input, n, data)

    except:
        return f"Terjadi kesalahan!"
        

def fillna(data, n, user_input):
    method_list = {"mean": "mean", "median": "median"}
    keyword = ["semua", "seluruh", "semuanya"]
    user_input = user_input.split()
    method = next((val for key, val in method_list.items() if key in user_input), None)

    try:
        if any(k in user_input for k in keyword):
            fill_values = getattr(data, method)(numeric_only=True)
            data.fillna(fill_values, inplace=True)
            return data
        else:
            column_name = data.columns[n]
            fill_value = getattr(data[column_name], method)()
            data[column_name] = data[column_name].fillna(fill_value)
            return data[column_name]
            
    except Exception as e:
        return f"Terjadi kesalahan: {e}"
