import numpy as np
import pandas as pd
import os
import io
import re


def read_CST_results(path,s_par_type):
    '''
    :param path:
    :param s_par_type:
    :return:
    '''

    data_string = open(path).read()

    ignore_lines = 2
    New_string = data_string.split('\n', ignore_lines)[ignore_lines]
    # replace multiple spaces with empty space
    New_string = re.sub(" +", " ", New_string)
    # New_string = New_string.replace(' ',';')
    data_tmp = io.StringIO(New_string)
    df = pd.read_csv(data_tmp, names=['col'])

    # convert list to df and
    df_list = df['col'].to_list()
    df[['test', 'freq', s_par_type]] = df['col'].str.split(' ', expand=True)
    df.drop(['test', 'col'], inplace=True, axis=1)
    return df





#----------------------------------------------------------#
#------------------- Import data --------------------------#
#----------------------------------------------------------#
#----------------------------------------------------------#
s_par_types = ['SZmax_Zmin','SZmin_Zmin']
directory = '../data/raw/Data_1/Results'

for s_par_type in s_par_types:

    #Get list of sub directory names
    sub_dir_list  = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
    sub_dir_names = [x.replace('iteration_', '') for x in sub_dir_list]
    sub_dir_names = [int(x) for x in sub_dir_names]
    sub_dir_names.sort()

    #sub_dir_names = sub_dir_names[:20]

    transmittance =[]
    for x in sub_dir_names:
        path = directory + '/iteration_'+ str(x)+'/'+ s_par_type
        df = read_CST_results(path, s_par_type)
        transmittance.append(df[s_par_type].values.tolist())


    freq = df['freq'].values.tolist()
    new_df = pd.DataFrame(data=transmittance, columns= freq)
    index = pd.Index(sub_dir_names)
    new_df.set_index(index,inplace=True)

    new_df.to_csv('../data/processed/'+ s_par_type+ '.csv',index= False)





'''
#----------------------------------------------------------#
#------------------- SZmax_Zmin  --------------------------#
#----------------------------------------------------------#
#----------------------------------------------------------#
s_par_type = 'SZmin_Zmin'
directory = '../data/raw/Data_1/Results'

#Get list of sub directory names
sub_dir_list  = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
sub_dir_names = [x.replace('iteration_', '') for x in sub_dir_list]
sub_dir_names = [int(x) for x in sub_dir_names]
sub_dir_names.sort()

sub_dir_names = sub_dir_names[:20]

transmittance =[]
for x in sub_dir_names:
    path = directory + '/iteration_'+ str(x)+'/'+ s_par_type
    df = read_CST_results(path, s_par_type)
    transmittance.append(df[s_par_type].values.tolist())


freq = df['freq'].values.tolist()
new_df = pd.DataFrame(data=transmittance, columns= freq)
index = pd.Index(sub_dir_names)
new_df.set_index(index,inplace=True)

new_df.to_csv('../data/processed/'+ s_par_type+'.csv')
'''