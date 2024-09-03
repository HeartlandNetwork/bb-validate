


###############################################################
#
#   observer_compare1.py
#   Purpose is to load and do initial comparisons
#   between observer data from MS Access and SQL Server
#
#   Gareth Rowell - 20240903
#
###############################################################

# start the IPython session here:
# C:\Users\GRowell\bb-validate\PartOne\src>

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("tbl_TweetyEventObservers.csv")

