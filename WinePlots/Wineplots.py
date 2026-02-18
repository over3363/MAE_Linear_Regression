import pandas as pd
from matplotlib import pyplot as plt
# 2 libraries we will start with to get the data in and visualize it

# 1st: Load in the dataset 
# wine_df is the dataframe we are going to be creating is equal to pandas read csv function and then add winequality csv file and pass in the comment because we are using a differnet type of seperator rather than a comma
wine_df = pd.read_csv("winequality-white.csv", sep=";")

