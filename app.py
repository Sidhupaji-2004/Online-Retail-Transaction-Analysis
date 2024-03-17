import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("shopping.csv")

# Display the first few rows to understand the structure
print(df.head())

# Check for missing values and data types
print(df.info())

# Check summary statistics
print(df.describe())

# Check for outliers
# You can use box plots or histograms to visualize the distributions
plt.figure(figsize=(10, 6))
sns.boxplot(data=df)
plt.title("Boxplot of numerical variables")
plt.show()

# Explore distributions of numerical variables
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="Age", bins=30, kde=True)
plt.title("Distribution of Age")
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="Purchase Amount (USD)", bins=30, kde=True)
plt.title("Distribution of Purchase Amount")
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="Review Rating", bins=5, discrete=True)
plt.title("Distribution of Review Rating")
plt.show()

# Explore categorical variables
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="Gender")
plt.title("Count of Gender")
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(data=df, x="Category")
plt.title("Count of Categories")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(data=df, x="Location")
plt.title("Count of Locations")
plt.xticks(rotation=45)
plt.show()

# Explore relationships between variables
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Age", y="Purchase Amount (USD)")
plt.title("Scatterplot of Age vs Purchase Amount")
plt.show()

# Explore correlations between numerical variables
correlation_matrix = df.corr()
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.show()
