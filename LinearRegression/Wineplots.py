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

# sum_x_times_y long variable name
# sum_x_times_y is equal to wine dataframe of the x value times the wine dataframe at the y value 
# that value is we are going to apply the sum function on 
sum_x_times_y = (wine_df[x]*wine_df[y]).sum()

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
print(f"Sum of X Times Y : {sum_x_times_y}")
print(f"Sum of X Sqaureds: {sum_x_squareds}")

# Calculate our Numerator and our Denominator for M calculation 
# Follow Equation 
# should be sum x times y not sum x times sum y
Sxy = sum_x_times_y - (sum_x*sum_y)/n

# Sxx is going to be equal to the sum of x sqaureds minus sum of x times the sum of y divided by n
Sxx = sum_x_squareds - (sum_x*sum_y)/n

# print(f"Sxy: {Sxy} Sxx: {Sxx}")
print(f"Sxy : {Sxy}")
print(f"Sxx : {Sxx}")
# have our statistics 

# Get our Line Variables
# slope m is going to be equal to Sxy divided the Sxx 
# intercept is going to be y mean minus m times the x mean
m = Sxy/Sxx
b = y_mean - m*x_mean
# Print Regression Line 
print(f"Regression Equation: y = {m}x+{b}")

# run program : have a regression equation y is equal to kind of a small number times the x variable plus about 5.7
# so now we have a model 
# implementing equations directly on our data 
# for more complex models , the more complex models the calculations are a lot more arduous  
# wont be implementing the entire models by hand most of the time
# this model is a pretty simple one

# now that we have a regression equation now what we really want to be able to do is predict a value 
# Lets Predict a Value
# lets get a row, say its row 5
row = 5 
# get alcohol value out of that row 
# using wine dataframe locate (loc) , remember with locate we can put an index for the row (5) and then a name for the column (alcohol) 
# get alcohol value out of row 5 
alcohol_val = wine_df.loc[5, "alcohol"]
# this time going to be wine dataframe row 5 quality value 
quality_val = wine_df.loc[5, "quality"]

# going to take our regression equation and apply it on the alcohol value to create a quality prediction 
# then we are going to compare the quality prediction with the actual quality value that exists in the dataset
# implementing our regression equation 
predicted_quality = alcohol_val*m + b

# Print statement to figure out how we did 
# print(f"""text{variable}text""") allows for multiline . newline breaks where you put them
print(f"""For Alcohol Value {alcohol_val}, the predicted quality was {predicted_quality}. 
The actual quality is {quality_val}.""")

# Try a random row , see if it will do a good job with every row 
# row = 1000
# row = 2000
# row = 2500
# alcohol_val = wine_df.loc[row, "alcohol"]
# quality_val = wine_df.loc[row, "quality"]

# basically this model can see the kind of different rows but most of the time it predicts something pretty close to the average value for quality in general
# may not be super useful 

# want to quanitify to the best of our ability how much we can trust the model 
# so we need to create that coefficient of determination 

# Coefficient of Determination 
