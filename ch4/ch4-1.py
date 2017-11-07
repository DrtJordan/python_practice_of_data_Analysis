import pandas as pd
from scipy.interpolate import lagrange

inputfile = '../data/catering_sale.xls'
outputfile = '../temp/sales.xls'

data = pd.read_excel(inputfile)
data[u'销量'][(data[u'销量'] < 400) | (data[u'销量'] > 5000)] = None
#过滤异常值，将其变为空值

def ployinterp_column(s,n,k=5):
    y = s[list(range(n-k,n)) + list(range(n+1,n+1+k))]
    y = y[y.notnull()]
    return lagrange(y.index(),list(y))(n)

for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:
            data[i][j] = ployinterp_column(data[i],j)
data.to_excel(outputfile)