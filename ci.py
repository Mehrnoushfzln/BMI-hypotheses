import pandas as pd
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# load dataset into a pandas dataframe
df = pd.read_csv("/Users/mac/Desktop/lincoln/study/semester 2/research method/hypothesis/diabetes.csv")

# calculate mean and standard deviation of BMI values
mean_bmi = df['BMI'].mean()
std_bmi = df['BMI'].std()

# calculate standard error of the mean
sem_bmi = std_bmi / (df.shape[0] ** 0.5)

# calculate confidence interval for the mean of BMI values
ci_low, ci_high = stats.norm.interval(0.95, loc=mean_bmi, scale=sem_bmi)

# create a histogram of BMI values
sns.histplot(x='BMI', data=df, kde=True)

# plot the standard normal distribution with mean and confidence interval
x = np.linspace(mean_bmi - 4*std_bmi, mean_bmi + 4*std_bmi, 1000)
plt.plot(x, stats.norm.pdf(x, loc=mean_bmi, scale=std_bmi), 'r', label='Normal Distribution')
plt.axvline(x=ci_low, color='g', linestyle='--', label='95% CI Lower Bound: {:.2f}'.format(ci_low))
plt.axvline(x=ci_high, color='g', linestyle='--', label='95% CI Upper Bound: {:.2f}'.format(ci_high))
plt.legend()

# set x and y labels
plt.xlabel('BMI')
plt.ylabel('Frequency')

# set title
plt.title('Histogram of BMI Values with 95% Confidence Interval')

# display the plot
plt.show()
