import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("shopping_2.csv")

# Display the first few rows to understand the structure
print(df.head())

# Check for missing values and data types
print(df.info())

# Check summary statistics
print(df.describe())

plt.figure(figsize=(12, 6))
sns.countplot(data=df, x="shopping_mall")  # Adjust column name as per your dataset
plt.title("Count of Shopping Malls")
plt.xticks(rotation=45)
plt.show()
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="price", bins=30, kde=True)  # Adjust column name as per your dataset
plt.title("Distribution of Price")
plt.show()
exit()

# Check for outliers
# You can use box plots or histograms to visualize the distributions
plt.figure(figsize=(10, 6))
sns.boxplot(data=df)
plt.title("Boxplot of numerical variables")
plt.show()

# Explore distributions of numerical variables
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="age", bins=30, kde=True)  # Adjust column name as per your dataset
plt.title("Distribution of Age")
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="price", bins=30, kde=True)  # Adjust column name as per your dataset
plt.title("Distribution of Price")
plt.show()

# Explore categorical variables
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="gender")  # Adjust column name as per your dataset
plt.title("Count of Gender")
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(data=df, x="category")  # Adjust column name as per your dataset
plt.title("Count of Categories")
plt.xticks(rotation=45)
plt.show()

# Explore relationships between variables
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="age", y="price")  # Adjust column names as per your dataset
plt.title("Scatterplot of Age vs Price")
plt.show()

# Explore correlations between numerical variables
correlation_matrix = df.corr()
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.show()
