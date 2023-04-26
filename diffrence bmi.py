import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

# load dataset into a pandas dataframe
df = pd.read_csv("/Users/mac/Desktop/lincoln/study/semester 2/research method/hypothesis/diabetes.csv")

# extract the BMI and diabetes columns as numpy arrays
bmi_diabetes = df.loc[df['Diabetes'] == 1, 'BMI'].values
bmi_no_diabetes = df.loc[df['Diabetes'] == 0, 'BMI'].values

# calculate the mean and standard deviation of BMI for people with diabetes and without diabetes
mean_bmi_diabetes = np.mean(bmi_diabetes)
std_bmi_diabetes = np.std(bmi_diabetes, ddof=1)  # use ddof=1 for unbiased estimator of standard deviation
mean_bmi_no_diabetes = np.mean(bmi_no_diabetes)
std_bmi_no_diabetes = np.std(bmi_no_diabetes, ddof=1)

# calculate the difference of mean BMI between people with diabetes and without diabetes
diff_mean_bmi = mean_bmi_diabetes - mean_bmi_no_diabetes

# calculate the standard error of the difference of mean
n_diabetes = len(bmi_diabetes)
n_no_diabetes = len(bmi_no_diabetes)
se_diff_mean = np.sqrt(std_bmi_diabetes**2/n_diabetes + std_bmi_no_diabetes**2/n_no_diabetes)

# calculate the 95% confidence interval for the difference of mean BMI
t = stats.t.ppf(1 - 0.05 / 2, n_diabetes + n_no_diabetes - 2)
ci_low = diff_mean_bmi - t * se_diff_mean
ci_high = diff_mean_bmi + t * se_diff_mean

print("Mean BMI for people with diabetes:", mean_bmi_diabetes)
print("Mean BMI for people without diabetes:", mean_bmi_no_diabetes)
print("Difference of mean BMI between people with diabetes and without diabetes:", diff_mean_bmi)
print("Standard error of the difference of mean:", se_diff_mean)
print("95% confidence interval for the difference of mean BMI:", (ci_low, ci_high))
