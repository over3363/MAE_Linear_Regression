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

# Manual Regression Between Alcohol and Quality 

# Get Variables We Need to Make Calculations 

# x variable 
x = "alcohol"
# y variable 
y = "quality"

# n is the number of samples we have total going to say that is going to be the length of the wine dataframe index 
# index gives you all the row indexs on the dataframe 
# the length will give you physical number count 
# n becomes our sample number
n = len(wine_df.index)

# sum of all x values 
# sum of x is equal to the wine dataframe x variable which is alcohol and we are goign to call sum
sum_x = wine_df[x].sum()

# sum of all y values?
# sum y is equal to the wine dataframe at the quality variable y and again take the sum function of dataframe to do this automatically 
sum_y = wine_df[y].sum()

# x mean
# equal to the sum divided by n the number of samples 
x_mean = sum_x/n

# y mean 
# equal to the sum divided by n the number of samples 
y_mean = sum_y/n

# sum_x_times_sum_y long variable name
# sum_x_times_sum_y is equal to wine dataframe of the x value times the wine dataframe at the y value 
# that value is we are going to apply the sum function on 
sum_x_times_sum_y = (wine_df[x]*wine_df[y]).sum()

# sum_x_squareds variable name for sum of x squareds
# wine dataframe at the x value which is alchohol 
# and then we use handy math power function with 2 so we are squaring it 
# then we will take the sum of that
sum_x_squareds = wine_df[x].pow(2).sum()

# sanity check 
# print 
# print the n value of the variable 
# n is equal to : n value of the variable {n}
# inefficient way to do this but create a print statment for each variable 
print(f"n: {n}")
# sum of x values going to be sum_x 
# this is an f stream, so if you put f in front of a stream than if you have curly braces {} you can put variables inside it and it will evaluate to their value inside the string
print(f"Sum of X Values: {sum_x}")
print(f"Sum of Y Values: {sum_y}")
print(f"Mean X Value : {x_mean}")
print(f"Mean Y Value : {y_mean}")
print(f"Sum of X Times Sum of Y : {sum_x_times_sum_y}")
print(f"Sum of X Sqaureds: {sum_x_squareds}")