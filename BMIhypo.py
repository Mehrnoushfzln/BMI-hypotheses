import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

# load dataset into a pandas dataframe
df = pd.read_csv("/Users/mac/Desktop/lincoln/study/semester 2/research method/hypothesis/diabetes.csv")

# extract the BMI and diabetes columns as numpy arrays
bmi = df['BMI'].values
Diabetes = df['Diabetes'].values

# calculate the Pearson correlation coefficient and p-value
r, p = stats.pearsonr(bmi, Diabetes)

# print the results
print("Pearson correlation coefficient:", r)
print("p-value:", p)

# check if the p-value is less than or equal to your chosen significance level
alpha = 0.05
if p >= alpha:
    print("Fail to reject the null hypothesis: There is insufficient evidence to conclude a relationship between BMI and diabetes")
else:
    print("Reject the null hypothesis: There is evidence of a relationship between BMI and diabetes")

# calculate the mean and standard deviation of BMI
mean_bmi = np.mean(bmi)
std_bmi = np.std(bmi, ddof=1)  # use ddof=1 for unbiased estimator of standard deviation

# calculate the standard error of the mean
n = len(bmi)
se = std_bmi / np.sqrt(n)

# calculate the 95% confidence interval for the mean
t = stats.t.ppf(1 - alpha / 2, n - 1)
ci_low = mean_bmi - t * se
ci_high = mean_bmi + t * se

print("Mean BMI:", mean_bmi)
print("Standard deviation of BMI:", std_bmi)
print("Standard error of the mean:", se)
print("95% confidence interval for the mean BMI:", (ci_low, ci_high))

# create a boxplot of BMI values for people with and without diabetes
labels = ['No Diabetes', 'Diabetes']
data = [bmi[Diabetes==0], bmi[Diabetes==1]]
plt.boxplot(data, labels=labels)
plt.ylabel('BMI')
plt.title('BMI Distribution for People with and without Diabetes')
plt.show()

# create a histogram of BMI values with a standard normal distribution overlay
plt.hist(bmi, bins=40, density=True, alpha=0.6, color='b')
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 300)
p = stats.norm.pdf(x, mean_bmi, std_bmi)
plt.plot(x, p, 'k', linewidth=2)
plt.xlabel('BMI')
plt.ylabel('Density')
plt.title('BMI Distribution with Standard Normal Distribution Overlay')
plt.show()
