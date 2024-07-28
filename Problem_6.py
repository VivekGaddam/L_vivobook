import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load the dataset
df = pd.read_csv("telangana_weather.csv")

# Display information about the dataset
df.info()
# Display the first few rows of the dataset
print(df.head())

# Check for missing values
missing_values = df.isnull().sum()
print("Missing values in each column:\n", missing_values)

# Handle missing values (if any)
df.fillna(df.mean(), inplace=True)

# Detecting outliers using box plots
plt.figure(figsize=(15, 10))
sns.boxplot(data=df.select_dtypes(include=[np.number]))
plt.xticks(rotation=90)
plt.show()

# Handling outliers
z_scores = np.abs(stats.zscore(df.select_dtypes(include=[np.number])))
df = df[(z_scores < 3).all(axis=1)]
# Descriptive analytics
print(df.describe())

# Pairplot to visualize relationships
sns.pairplot(df.select_dtypes(include=[np.number]))
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# Distribution of each feature

df.hist(bins=20, figsize=(20, 15), edgecolor='black')
plt.suptitle("Feature Distributions")
plt.show()

# Box plot for each feature
plt.figure(figsize=(15, 10))
sns.boxplot(data=df.select_dtypes(include=[np.number]))
plt.title("Box Plot of Each Feature")
plt.xticks(rotation=90)
plt.show()
# Time series plot of temperature data
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

plt.figure(figsize=(15, 6))
plt.plot(df['temp_min (⁰C)'], label='Min Temperature')
plt.plot(df['temp_max (⁰C)'], label='Max Temperature')
plt.xlabel('Date')
plt.ylabel('Temperature (⁰C)')
plt.title('Time Series of Temperature')
plt.legend()
plt.show()
