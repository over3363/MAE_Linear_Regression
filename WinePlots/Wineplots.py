import pandas as pd
from matplotlib import pyplot as plt
# 2 libraries we will start with to get the data in and visualize it

# 1st: Load in the dataset 
# wine_df is the dataframe we are going to be creating is equal to pandas read csv function and then add winequality csv file and pass in the comment because we are using a differnet type of seperator rather than a comma
wine_df = pd.read_csv("winequality-white.csv", sep=";")

# do a really basic plot 
# plt calling the matplotlibrary
# scatter plot 
# what we want to plot is the wine dataframe alchol that will be our independent x variable 
# output variable we care about is the wine dataframe quality 
# xlabel and ylabel are scatter axis labels
# title VS
plt.scatter(wine_df["alcohol"], wine_df["quality"])
plt.xlabel("Alcohol")
plt.ylabel("Quality")
plt.title("Alcohol vs Quality")
plt.show()
#using pandas might want to use plt.savefig("your figure") that should create a figure in your folder
#plt.savefig("plot.png")
# save and run 
# see that maybe there is a slight positive correlation between the alchol and quality 
# when we did data exploration we could see .4 positive correlation of alchol and quality so not a huge one but a potentially existing one
# function or command explinations 

