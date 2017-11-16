#-*- coding:utf-8 -*-
# Peishichao
import pandas as pd

discfile = '../data/discdata.xls'
transformedadta = '../tmp/discdata_processed.xls'
data = pd.read_excel(discfile)

data = data[data['TARGET_ID']==184].copy()

data_group = data.groupby('COLLECTTIME')

def attr_trans(x):
    result = pd.Series(index = ['SYS_NAME','CWXT_DB:184:C:\\','CWXT_DB:184:D:\\','COLLECTTIME'])
    #print(x)
    #print( x['SYS_NAME'])
    #print(x['SYS_NAME'].iloc[0])
    result['SYS_NAME'] = x['SYS_NAME'].iloc[0]
    result['CWXT_DB:184:C:\\'] = x['VALUE'].iloc[0]
    result['CWXT_DB:184:D:\\'] = x['VALUE'].iloc[1]
    result['COLLECTTIME'] = x['COLLECTTIME'].iloc[0]
    return result

data_processed = data_group.apply(attr_trans)

data_processed.to_excel(transformedadta,index = False)
