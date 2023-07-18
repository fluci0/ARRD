# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 11:12:57 2023
@author: Lujay
Title: Script to create Random Relational Databases to Practice
Version:
Python 3.9
"""

import random as rd
import string
import pandas as pd
from datetime import timedelta
import xlsxwriter
from datetime import datetime
import os
string.ascii_letters

#Parameters
N = 4 #Number of tables
start_date = datetime.now() - timedelta(days = 922)
end_date = datetime.now()
min_value = 0
max_value = 10000000 
sk_min_value = 1
sk_max_value = 100
min_fvalue = 0.001
max_fvalue = 9999999.9 
nmin_fvalue = -9999999.9 
nmax_fvalue = 9999999.9 
min_ncolumns = 6
max_ncolumns = 12
min_nrows = 20
max_nrows = 30000
min_ncharacters = 3
max_ncharacters = 10

#Remove csv files (Previoulsy created)
#Note: Run this script and move csv files to your desired folder
for file in os.listdir():
    if file.endswith('.csv'):
        print('File to remove:', file)
        os.remove(file)


def random_ncolumns(): #Random n_columns
   c_i = rd.randint(min_ncolumns, max_ncolumns)
   print('c_i =', c_i)
   return c_i

def random_nrows(): #Random n_rows
   r_i = rd.randint(min_nrows, max_nrows)
   print('r_i:', r_i)
   return r_i

def random_cnames(c_i): #Random Column Names
    names_lst = []
    for j in range(c_i):
        r_dummy = rd.randint(min_ncharacters, max_ncharacters)
        chars = ''
        for k in range(r_dummy):
            char = rd.choice(string.ascii_letters)
            chars = chars + char
        cnames_i = chars
        #print('cnames_i:', cnames_i)
        names_lst.append(cnames_i)
    #print('names_lst:', names_lst)
    return names_lst

def random_vals(r_i,c_i, i, names_lst):
    #{1: Date, 2: Integer, 3: Float, 4: Text, 5: Float negative numbers, 6: Categorical Values}
    #print('Values_i of tabla:', i + 1)
    values_lst = [0] * c_i
    #values_lst[1] = [p for p in range(1, r_i + 1)] #Consecutive ID records // Not necessay
    values_lst[0] = [rd.randint(sk_min_value, sk_max_value) for iter in range(r_i)] #Relate tables with others
    cat_values = ['YES', 'NO']

    for m in range(1, len(values_lst)):
        dum = rd.randint(1, 6)
        if dum == 1:
            values_lst[m] = [start_date + (end_date - start_date) * rd.random() for iter in range(r_i)]
        elif dum == 2:
            values_lst[m] = [rd.randint(min_value, max_value) for iter in range(r_i)]
        elif dum == 3:
            values_lst[m] = [rd.uniform(min_fvalue, max_fvalue) for iter in range(r_i)]
        elif dum == 4:
            values_lst[m] = random_cnames(c_i = r_i) 
        elif dum == 5:
            values_lst[m] = [rd.uniform(nmin_fvalue, nmax_fvalue) for iter in range(r_i)]
        elif dum == 6:
            values_lst[m] = [rd.choice(cat_values) for iter in range(r_i)]

    names_dict = dict(zip(names_lst, values_lst))
    #print('names_dict:', names_dict)
    return names_dict

def to_csv(names_dict, i):
    Day = datetime.now().strftime('%d')
    Month = datetime.now().strftime('%h')
    Year = datetime.now().strftime('%Y')
    Hour = datetime.now().strftime('%H')
    Minute = datetime.now().strftime('%M')
    VName = Day + Month + Year + '-' + Hour + '_' + Minute
    print('VName:', VName)
    NameFile = 'DF_' + str(i) + '_' + VName
    df_i = pd.DataFrame(names_dict)
    df_i.to_csv(NameFile + '.csv')

def random_rrd():
    global mydict_i
    global names_lst
    for i in range(N): #i is the number of the table
        print('------------------Creating table #', i + 1) #Just for debugging
        c_i = random_ncolumns()
        r_i = random_nrows()
        names_lst = random_cnames(c_i)
        names_dict = random_vals(r_i, c_i, i, names_lst)
        _ = to_csv(names_dict, i)

def create_table():
    print(N)

if __name__ == "__main__":
    random_rrd()
