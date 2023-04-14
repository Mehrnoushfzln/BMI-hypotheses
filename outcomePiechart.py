import pandas as pd
import matplotlib.pyplot as plt

# read the dataset into a pandas dataframe
df = pd.read_csv('/Users/mac/Desktop/lincoln/study/semester 2/research method/hypothesis/diabetes.csv')

# group by the Diabetes column and count the values
diabetes_count = df.groupby('Diabetes')['Diabetes'].count()

# create a pie chart with pink for 0 and green for 1
colors = ['#FFC0CB', '#00FF00']
labels = ['No Diabetes', 'Diabetes']
plt.pie(diabetes_count, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('Diabetes in Dataset')
plt.axis('equal')
plt.show()
