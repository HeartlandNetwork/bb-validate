
###############################################################
#
# Detecting missing observers in bird observation data
# and filtering out the missing bird observations
#
# Gareth Rowell - 20240821
#
###############################################################


library(tidyverse)

setwd("../work/ryanburner/20240821-ObserverDataTested")



df_lj <- read_csv("HTLN_bird_observations_observers_LEFTJOIN.csv")
problems(df_lj)
glimpse(df_lj)

# total count of bird observations by ObserverInitials
	
df_lj |>
    count(ObserverInitials) |>
	arrange(desc(n)) |>
	print(n = 102)


# total count of bird observations grouped by ObserverInitials and Year.

df_lj <- df_lj |> 
	mutate(
	    ObsYear = year(EventDateTime)
	)


df_lj |> 
  group_by(ObserverInitials, ObsYear) |> 
  count() |>
  arrange(desc(n))
  
# filtering out NULL observations
# df_no_null could potentially be used for observer analysis
 
 df_no_null <- df_lj |>
	  filter(ObserverInitials != "NULL")
	
	
df_no_null |> 
  group_by(ObserverInitials, ObsYear) |> 
  count() |>
  arrange(desc(n))
  
 
 count(df_no_null) #  count(df_no_null)
  
  
  
  