# coding=utf-8

import pandas as pd

import os

os.system("mkdir pasta1")
os.system("gsutil -m cp gs://composer-teste/HIST_PAINEL_COVIDBR_20200517.xlsx pasta1")
os.system("mkdir pasta2")


df = pd.read_excel("pasta1/HIST_PAINEL_COVIDBR_20200517.xlsx")  # sheetname is optional
df.to_csv('pasta2/novo1.csv', index=False,encoding='utf-8')  # index=False prevents pandas to write row index

os.system("gsutil -m cp pasta2/novo1.csv gs://composer-teste")