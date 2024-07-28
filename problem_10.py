import pandas as pd
import matplotlib.pyplot as plt
from  scipy import stats
import numpy as np
df = pd.read_csv("diabetes.csv")
df['Glucose'] = df['Glucose'].replace(0, df['Glucose'].mean())
df['BloodPressure'] = df['BloodPressure'].replace(0, df['BloodPressure'].mean())
df['SkinThickness'] = df['SkinThickness'].replace(0, df['SkinThickness'].mean())
df['Insulin'] = df['Insulin'].replace(0, df['Insulin'].mean())
df['BMI'] = df['BMI'].replace(0, df['BMI'].mean())
z_scores = np.abs(stats.zscore(df.select_dtypes(include=[np.number])))
df = df[(z_scores < 3).all(axis=1)]
import matplotlib.pyplot as plt
f, ax = plt.subplots(1,2,figsize=(10,5))
df['Outcome'].value_counts().plot.pie(explode=[0,0.1],autopct='%1.1f%%', ax=ax[0],shadow=True)
ax[0].set_title('Outcome')
ax[0].set_ylabel('')
import seaborn as sns
sns.countplot(x='Outcome', data=df, ax=ax[1])
ax[1].set_title('Outcome')
N, P = df['Outcome'].value_counts()
print('Negative(0) ->', N)
print('Positive(1) ->', P)

plt.grid()
plt.show()

"""Dataset is not balanced

Histogram (data is balanced or skewed)
"""

df.hist(bins=10,figsize=(10,10))
plt.show()

"""Analysing relationships bw variables

Correlation analysis
"""

#get correlations of each feature in the dataset
corr_mat = df.corr()
top_corr_features = corr_mat.index
plt.figure(figsize=(10,10))
#plot heat map
g = sns.heatmap(df[top_corr_features].corr(), annot=True, cmap='RdYlGn')
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("diabetes.csv")

# Separate data for outcome 0 and outcome 1
outcome_0_bp = df[df['Outcome'] == 0]['BloodPressure']
outcome_1_bp = df[df['Outcome'] == 1]['BloodPressure']

# Plot the bar chart
plt.bar(x=['Outcome 0', 'Outcome 1'], height=[outcome_0_bp.mean(), outcome_1_bp.mean()], color=['blue', 'orange'])
plt.xlabel('Outcome')
plt.ylabel('Mean Blood Pressure')
plt.title('Mean Blood Pressure by Outcome')
plt.show()

array_1=df["Glucose"]
plt.hist(array_1,bins=40)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Glucose')
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Generate data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create subplots
fig, axs = plt.subplots(2, 1, figsize=(8, 6))

# First subplot
axs[0].plot(x, y1, label='sin(x)')
axs[0].set_title('Sin Function')
axs[0].legend()
axs[0].grid(True)

# Second subplot
axs[1].plot(x, y2, label='cos(x)', color='red')
axs[1].set_title('Cos Function')
axs[1].legend()
axs[1].grid(True)

# Adjust layout and show plot
plt.tight_layout()
plt.show()
