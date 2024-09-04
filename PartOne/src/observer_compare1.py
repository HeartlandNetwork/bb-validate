


###############################################################
#
#   observer_compare1.py
#   Load and compare observer data through 2014
#   between  MS Access and SQL Server
#
#   Gareth Rowell - 20240903
#
###############################################################

# start the IPython session here:
# C:\Users\GRowell\bb-validate\PartOne\src>

import pandas as pd
import matplotlib.pyplot as plt





# load data

df_acc = pd.read_csv("tbl_TweetyEventObservers.csv")
df_sql = pd.read_csv("HTLN_bird_observations_observers_LEFTJOIN.csv")

# select columns

df_acc = df_acc[['EventID','ObsInits']]
df_sql = df_sql[['EventID','ObserverInitials']]

# make column names match

df_sql.rename(columns={'ObserverInitials':'ObsInits'}, inplace=True)


# remove nulls and blanks from observer initials

df_acc = df_acc[df_acc['ObsInits'].notnull()]
df_sql = df_sql[df_sql['ObsInits'].notnull()]

# remove duplicate values

df_acc = df_acc.drop_duplicates(subset=['EventID', 'ObsInits'], keep='last')
df_sql = df_sql.drop_duplicates(subset=['EventID', 'ObsInits'], keep='last')

# filter out years 2014 and earlier from SQL data

df_sql['SampleYear'] = df_sql['EventID'].str.slice(4,8)


#  ValueError: Unable to parse string "023J" at position 6752

df_sql['SampleYear'] = pd.to_numeric(df_sql['SampleYear'])





df_sql = df_sql[df_sql['SampleYear'] < 2015]

df_sql


# Convert column to integer
df['column_name'] = df['column_name'].astype(int)

