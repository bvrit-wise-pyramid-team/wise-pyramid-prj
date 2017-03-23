import pandas as pd
import sys

df = pd.DataFrame()
FILE_MAPPING = { 'Main' : [], 'cars' : {} }

def get_dataframe(file_mapping):
    data = file_mapping['Main']
    header = data.pop(0)
    df = pd.DataFrame(data,columns = header)
    df = df.drop('prefix',axis =1)
    return df
def most_occurance_country(df):
    countryList = pd.Series(df['cars'])
    countryDict = dict(countryList.value_counts())
    countryDict = {FILE_MAPPING['cars'][k]:v for k, v in countryDict.items()}
   
    for key , value in countryDict.items():
        print("most_occurance_country##{0}\t{1}".format(key.replace('\r','').replace('\n',''),value))

def Main(FILE_MAPPING):
    listOfKeys = []
    for keys in FILE_MAPPING.keys():
        listOfKeys.append(keys)
    for line in sys.stdin:
        df = line.split(',')
        if len(df) < 39 :
            if df[0] in listOfKeys :
                FILE_MAPPING[df[0]][df[1]] = df[2]
        else:
            FILE_MAPPING['Main'].append(df)
    df= get_dataframe(FILE_MAPPING)
    del FILE_MAPPING['Main']




 
