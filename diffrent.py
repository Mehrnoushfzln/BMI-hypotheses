import pandas as pd
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt

# load dataset into a pandas dataframe
df = pd.read_csv("/Users/mac/Desktop/lincoln/study/semester 2/research method/hypothesis/diabetes.csv")

# create separate dataframes for people with and without diabetes
diabetes_df = df[df['Diabetes'] == 1]
non_diabetes_df = df[df['Diabetes'] == 0]

# calculate mean BMI values for each group
mean_bmi_diabetes = diabetes_df['BMI'].mean()
mean_bmi_non_diabetes = non_diabetes_df['BMI'].mean()

# calculate the mean difference in BMI values between the two groups
mean_diff_bmi = mean_bmi_diabetes - mean_bmi_non_diabetes

#  calculate the standard error of the mean difference in BMI values between the two groups
std_error_diff_bmi = stats.sem(diabetes_df['BMI']) + stats.sem(non_diabetes_df['BMI'])

# calculate the 95% confidence interval for the mean difference in BMI values between the two groups
ci_low, ci_high = stats.norm.interval(0.95, loc=mean_diff_bmi, scale=std_error_diff_bmi)

# create a histogram of BMI values with overlaid normal distribution
sns.histplot(data=df, x='BMI', hue='Diabetes', element='step', kde=True, fill=False)

# add vertical lines at the mean BMI for each group
plt.axvline(x=mean_bmi_diabetes, color='red', linestyle='--')
plt.axvline(x=mean_bmi_non_diabetes, color='yellow', linestyle='--')

# add vertical lines at the 95% confidence interval limits for the mean difference in BMI values between the two groups
plt.axvline(x=ci_low, color='green', linestyle='-.')
plt.axvline(x=ci_high, color='green', linestyle='-.')
print(mean_diff_bmi)
# add legend
plt.legend(['Diabetes Mean BMI', 'Non-Diabetes Mean BMI','95% CI'], loc='upper right')

# set x and y labels
plt.xlabel('BMI')


# set title
plt.title('Histogram of BMI Values with Overlaid Normal Distribution')

# display the plot
plt.show()
