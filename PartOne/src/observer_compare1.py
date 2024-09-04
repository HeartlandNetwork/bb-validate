


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

df_acc = pd.read_csv("tbl_TweetyEventObservers.csv")
df_sql = pd.read_csv(

