import pandas as pd
from matplotlib import pyplot as plt
# 2 libraries we will start with to get the data in and visualize it
# pip install scikit-learn
# conda install scikit-learn on terminal
# documentation for scikitlearn sometimes python versions have slightly differences in how the API is implemented 
# not a ton of differences for scikit learn but there are a few
# if having issues check documentation there might be a slightly different call
# linear model and selection are submodules of the sklearn library which is quite large 
# allows us to limit our imports to the ones we are using
# importing a speciifc class (Linear Regression , train test split) that belongs to this sub module (linear_model)
# that class has associated variables and functions we can use to run our code
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 1st: Load in the dataset 
# wine_df is the dataframe we are going to be creating is equal to pandas read csv function and then add winequality csv file and pass in the comment because we are using a differnet type of seperator rather than a comma
wine_df = pd.read_csv(r'C:\Users\Tori\Documents\MAELecture\LinearRegression\LinearRegression\winequality-white.csv', sep=";")

# do a really basic plot 
# plt calling the matplotlibrary
# scatter plot 
# what we want to plot is the wine dataframe alchol that will be our independent x variable 
# output variable we care about is the wine dataframe quality 
# xlabel and ylabel are scatter axis labels
# title VS
#plt.scatter(wine_df["alcohol"], wine_df["quality"])
#plt.xlabel("Alcohol")
#plt.ylabel("Quality")
#plt.title("Alcohol vs Quality")
#plt.show()
#using pandas might want to use plt.savefig("your figure") that should create a figure in your folder
#plt.savefig("plot.png")
# save and run 
# see that maybe there is a slight positive correlation between the alchol and quality 
# when we did data exploration we could see .4 positive correlation of alchol and quality so not a huge one but a potentially existing one
# function or command explinations 


