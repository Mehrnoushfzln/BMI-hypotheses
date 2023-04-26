import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

# load dataset into a pandas dataframe
df = pd.read_csv("/Users/mac/Desktop/lincoln/study/semester 2/research method/hypothesis/diabetes.csv")

# extract the BMI column as a numpy array
bmi = df['BMI'].values

# calculate the mean and standard deviation of BMI
mean_bmi = np.mean(bmi)
std_bmi = np.std(bmi, ddof=1)  # use ddof=1 for unbiased estimator of standard deviation

# plot the histogram of BMI values with a standard deviation overlay
plt.hist(bmi, bins=100, density=True, alpha=0.6, color='b')
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 300)
p = stats.norm.pdf(x, mean_bmi, std_bmi)
plt.plot(x, p, 'k', linewidth=2)
plt.xlabel('BMI')
plt.ylabel('Density')
plt.title('Standard Deviation of BMI')
plt.show()
