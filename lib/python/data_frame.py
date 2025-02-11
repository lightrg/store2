import pandas as pd, numpy as np
import re

def readFolderContent(names_data, folder):
    '''Reads a file from a folder and outputs the text from that folder.
    Inputs: names_data: txt file name 
            folder: the folder where the file is located
    Output: text data from the file'''
    
    with folder.get_download_stream(names_data) as stream:
        text_data = stream.read()

    if type(text_data) == str:
        return text_data
    else:
        return text_data.decode('utf-8')
    

def parseColumns(text_data):
    '''Takes in the names txt file and parses out the column names in the
    appropriate order for the data files.
    Input: names txt data
    Output: column names'''
    
#     with folder.get_download_stream(names_data) as stream:
#         text_data = stream.read()
    
    namesRegex = re.compile(r'Attribute Information(.*)the predicted attribute', re.DOTALL)
    names = namesRegex.search(text_data).group().split('\n')
    
    column_names = []

    for name in names:
        nameRegex = re.compile('\((.+)\)')
        col_name = nameRegex.search(name)
        if col_name:
            column_names.append(col_name.group(1))
    
    return column_names


def stackData(training_data, folder):
    
    dfs = []

    for path in training_data:

        with folder.get_download_stream(path) as stream:
            data = pd.read_csv(stream, on_bad_lines='skip', header=None)

        data['location'] = path.split('.')[1]

        dfs.append(data)
    
    return pd.concat(dfs)


def nameColumns(df, column_names):
    
    column_names.append('location')
    df.columns = column_names
    
    df.replace('?', np.nan, inplace=True)
    
    return df