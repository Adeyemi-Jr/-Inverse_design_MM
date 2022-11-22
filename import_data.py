import numpy as np
import pandas as pd
import os
import io
import re

data_lists = ['1','2']

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






for data_list in data_lists:
    #-------------------------------------------------------------------------#
    #------------------- Import design resonse data --------------------------#
    #-------------------------------------------------------------------------#
    #-------------------------------------------------------------------------#

    '''
    parameter_dir = '../data/raw/Data_'+ data_list+'/parameter_space_'+ data_list+'.csv'
    parameter_df = pd.read_csv(parameter_dir,index_col=False)
    #parameter_df.reset_index(inplace=True)
    directory = '../data/raw/Data_'+data_list+'/Results'
    sub_dir_list  = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]

    true_parameters_list = [word.replace('iteration_','') for word in sub_dir_list]
    true_parameters_list = [ int(element)-1 for element in true_parameters_list]
    true_parameters_list.sort()
    parameter_new_df = parameter_df[parameter_df.index.isin(true_parameters_list)]
    A = 1
    '''

    #-------------------------------------------------------------------------#
    #------------------- Import design resonse data --------------------------#
    #-------------------------------------------------------------------------#
    #-------------------------------------------------------------------------#
    s_par_types = ['SZmax_Zmin','SZmin_Zmin']
    directory = '../data/raw/Data_'+ data_list +'/Results'

    df_tmp = []
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

        new_df.to_csv('../data/processed/'+ s_par_type +'_dataset_'+ data_list +'.csv',index= False)




#pd.concat([parameter_new_df,new_df], axis = 1)
#new_df.to_csv('../data/processed/'+ s_par_type+ '.csv',index= False)




