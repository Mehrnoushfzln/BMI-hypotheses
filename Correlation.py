import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np
# load dataset into a pandas dataframe
df = pd.read_csv("/Users/mac/Desktop/lincoln/study/semester 2/research method/hypothesis/diabetes.csv")

# extract the BMI and diabetes columns as numpy arrays
bmi = df['BMI'].values
diabetes = df['Diabetes'].values

# calculate the Pearson correlation coefficient and p-value
r, p = stats.pearsonr(bmi, diabetes)

# create a scatter plot of BMI vs. diabetes
plt.scatter(bmi, diabetes)

# add a linear regression line to the scatter plot
slope, intercept, r_value, p_value, std_err = stats.linregress(bmi, diabetes)
x = np.linspace(np.min(bmi), np.max(bmi), 100)
y = slope*x + intercept
plt.plot(x, y, 'r', label='Regression line')

# add the Pearson correlation coefficient to the plot title
plt.title(f"BMI vs. Diabetes (r={r:.2f})")

# add legend and axis labels
plt.legend()
plt.xlabel("BMI")
plt.ylabel("Diabetes")

# show the plot
plt.show()
