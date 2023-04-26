import pandas as pd

# load dataset into a pandas dataframe
df = pd.read_csv("/Users/mac/Desktop/lincoln/study/semester 2/research method/hypothesis/diabetes.csv")

# calculate mean BMI for people with diabetes
mean_bmi_diabetes = df[df['Diabetes'] == 1]['BMI'].mean()

# calculate mean BMI for people without diabetes
mean_bmi_no_diabetes = df[df['Diabetes'] == 0]['BMI'].mean()

print("Mean BMI for people with diabetes: {:.2f}".format(mean_bmi_diabetes))
print("Mean BMI for people without diabetes: {:.2f}".format(mean_bmi_no_diabetes))
