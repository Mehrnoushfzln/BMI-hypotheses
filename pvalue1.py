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

# plot the scatter plot with r and p
plt.scatter(bmi, diabetes, alpha=0.5)
plt.xlabel('BMI')
plt.ylabel('Diabetes')

# calculate the mean and standard deviation of BMI
mean_bmi = np.mean(bmi)
std_bmi = np.std(bmi, ddof=1)  # use ddof=1 for unbiased estimator of standard deviation

# calculate the standard error of the mean
n = len(bmi)
se = std_bmi / np.sqrt(n)

# calculate the 95% confidence interval for the mean
alpha = 0.05
t = stats.t.ppf(1 - alpha / 2, n - 1)
ci_low = mean_bmi - t * se
ci_high = mean_bmi + t * se

# plot the red line for r value
x_line = np.linspace(np.min(bmi), np.max(bmi), 100)
y_line = r * (x_line - mean_bmi) / std_bmi + np.mean(diabetes)
plt.plot(x_line, y_line, color='red', linewidth=2, label='r = {:.2f}'.format(r))

# plot the yellow point for p-value
plt.plot(mean_bmi, np.mean(diabetes), marker='o', markersize=10, color='yellow', label='p-value = {:.4f}'.format(p))

# plot the confidence interval as vertical lines
plt.axvline(ci_low, color='black', linestyle='--', linewidth=1, label='95% CI')
plt.axvline(ci_high, color='black', linestyle='--', linewidth=1)

plt.legend()
plt.show()
