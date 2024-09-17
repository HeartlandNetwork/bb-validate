


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


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# load data

df_acc = pd.read_csv("tbl_TweetyEventObservers.csv")
df_sql = pd.read_csv("HTLN_bird_observations_observers_LEFTJOIN.csv")

# Next section is making two dataframes formatted the same 
# --------------------------------------------------------

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

df_sql.count()

# filter out years 2014 and earlier from SQL data

df_sql['SampleYear'] = df_sql['EventID'].str.slice(4,8)
# This next step will fail if there are any problems 
# with EventID format in the SQL data
df_sql['SampleYear'] = pd.to_numeric(df_sql['SampleYear'])

df_sql.groupby(['SampleYear']).size()

df_sql = df_sql[df_sql['SampleYear'] < 2015]

df_sql.count()


# remove SampleYear

df_sql = df_sql[['EventID','ObsInits']]


# remove "Tweety" from df_acc EventID

df_acc['EventID'] = df_acc['EventID'].str.replace('Tweety', '')

df_acc


# So now the question is whether df_acc contains any observer data
# thats not already contained in the df_sql dataframe
# hopefully yes
# also interested in whether the sql db contains any observer data
# not in the original accdb file - there shouldn't be any at all!!

# Essentially, what we want is a left join on EventID where df_acc
# is the left table and df_sql is the right table. We are expecting to 
# see EventIDs in df_acc along with their obsinits that do not occur
# in df_sql

# This is the left join in pandas

# Perform a left join

df_acc_lj = df_acc.merge(df_sql, on='EventID', how='left', suffixes=('_left', '_right'))

df_acc_lj.head()

df_acc_lj.count()


# This shows that there were some EventIDs with obsinits not occuring in df_sql
# Let's filter for only the NaNs

df_acc_lj = df_acc_lj[df_acc_lj['ObsInits_right'].isnull()]

df_acc_lj.head()

df_acc_lj.count()



# Looking at the swapped out join (df_sql on the left)
# We would expect all the df_sql rows (filtered < 2015) to match
# And the count after filtering left join for nulls is zero so that
# expectation is met.

df_sql_lj = df_sql.merge(df_acc, on='EventID', how='left', suffixes=('_left', '_right'))

df_sql_lj.head()

df_sql_lj.count()

df_sql_lj = df_sql_lj[df_sql_lj['ObsInits_right'].isnull()] 

df_sql_lj.head()

df_sql_lj.count()


# What years had missing observer initials in the final set? 
# These should be 2014, 2013, 2012, 2011, and 2010

df_acc_lj

df_acc_lj['SampleYear'] = df_acc_lj['EventID'].str.slice(4,8)

df_acc_lj['SampleYear'].unique()
 
df_acc_lj.groupby(['SampleYear']).size()
 

df.groupby(['col1','col2']).size()







