import pandas as pd

data_xls = pd.read_Excel('DT1_PAINEL_COVIDBR_20200512.xls','Sheet1',index_col=None)
data_xls.to_csv('teste_csv.csv',encoding='utf-8')