# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # load dataset into a pandas dataframe
# df = pd.read_csv("/Users/mac/Desktop/lincoln/study/semester 2/research method/hypothesis/diabetes.csv")

# # create a histogram of BMI values for people with and without diabetes
# sns.histplot(data=df, x='BMI', hue='Diabetes', kde=True, alpha=0.5)

# # set x and y labels
# plt.xlabel('BMI')
# plt.ylabel('Count')

# # set title
# plt.title('Histogram of BMI by Diabetes Status')

# # display the plot
# plt.show()
import pandas as pd
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# load dataset into a pandas dataframe
df = pd.read_csv("/Users/mac/Desktop/lincoln/study/semester 2/research method/hypothesis/diabetes.csv")

# create a histogram of BMI values with a standard normal distribution overlay
sns.histplot(data=df, x="BMI", hue="Diabetes", kde=True)

# calculate the mean and standard deviation of BMI
mean_bmi = np.mean(df['BMI'])
std_bmi = np.std(df['BMI'], ddof=1)

# calculate the standard error of the mean
n = len(df['BMI'])
se = std_bmi / np.sqrt(n)

# calculate the 95% confidence interval for the mean
t = stats.t.ppf(1 - 0.05 / 2, n - 1)
ci_low = mean_bmi - t * se
ci_high = mean_bmi + t * se

# add a vertical line at the 0.05 significance level
plt.axvline(ci_low, color='r', linestyle='--')
plt.axvline(ci_high, color='r', linestyle='--')

# set x and y labels
plt.xlabel('BMI')
plt.ylabel('Count')

# set title
plt.title('BMI Distribution with Diabetes')

# display the plot
plt.show()
