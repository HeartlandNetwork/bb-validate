

###############################################################
#
#   spatial_updates.py
#   correcting lat/long dd for HOME and HOCU
#   in invasive_plants data package
#
#   Gareth Rowell - 20240909
#
###############################################################

# start the IPython session here:
# C:\Users\GRowell\invasive_plants

import pandas as pd
import matplotlib.pyplot as plt


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# load data

df_inv = pd.read_csv(".csv")
df_sql = pd.read_csv("HTLN_bird_observations_observers_LEFTJOIN.csv")

