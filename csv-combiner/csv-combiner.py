'''
PMG coding challenge submission csv-combiner

Run in commandline 

python3 csv-combiner.py ./fixtures/accessories.csv ./fixtures/clothing.csv > output.csv, where the last argument is the output file

'''

import pandas as pd
import sys



'''
Combine Files takes two lists of the same length as inputs

filenames: list of strings with the specified file name

filelist: list of dataframes

Combine files, will combine the list of dataframes, adding a column that specifies each items file origin.

'''

def combineFiles(filenames,filelist):
    #Add the appropriate filename column to each dataframe
    for idx in range(0,len(filenames)):
        column = [filenames[idx]]*(len(filelist[idx]))
        filelist[idx].insert(len(filelist[idx].columns),"filename",column)
    #Concatenate all dataframes
    finaldf = pd.concat(filelist,axis=0)
    return finaldf


def main():
    args = sys.argv[1: ]
    filenames = []
    filelist = []
    for file in args:
        try:
            df = pd.read_csv(file)
            filelist.append(df)
            filepath = file.split("/")
            filenames.append(filepath[-1])
        except:
            raise RuntimeError('An input file ',file," could not be opened")
    fd = combineFiles(filenames,filelist)
    try:
        fd.to_csv(sys.stdout,index=False)
        #print()
    except:
        raise RuntimeError('Specified output file does not work')
    
    


if __name__ == '__main__':
    main()
