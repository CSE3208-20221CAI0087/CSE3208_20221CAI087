# -*- coding: utf-8 -*-
"""lab1_AI_In_Practice

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CG9ngQTg-o67ZXB-iTnoBDAOXA4_sdDM
"""

file = open("/sample.txt","r")
text = file.read()
print(text)

file2 = open("/sample.txt","r")
text = file2.readlines()
print(text)

def count_lines(file_path):
  with open(file_path,'r',errors= 'ignore') as file:
    lines = file.readlines()
    return len(lines)

file = open("/content/training_set_rel3.tsv","r",errors= 'ignore')
text = file.readlines()
print(text)
line_count = count_lines("/content/training_set_rel3.tsv")
print("Number of lines is ",line_count)

def count_fields(file_path):
  with open(file_path,'r',errors= 'ignore') as file:
    lines = file.readlines()
    fields = lines[0].split('\t')
    return len(fields)

file = open("training_set_rel3.tsv","r",errors= 'ignore')
field_count = count_fields("/training_set_rel3.tsv")
print("Number of fields is ",field_count)

import pandas as pd
df = pd.read_table("training_set_rel3.tsv",sep='\t',encoding= 'latin-1')
print("Number of columns is ",len(df.columns))
print("Number of rows is",len(df.index))