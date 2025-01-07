#SUMMARY STATISTICS
import pandas as pd #pandas is a library which helps in working with data sets
data = pd.read_excel('Marketing_Campaign_Data_5000.xlsx')
# Selection of the continuous numerical columns
numerical_columns = ['Age', 'Income (in $K)', 'Spending Score (1-100)']
# Calculation of the summary statistics
summary= data[numerical_columns].agg(['mean', 'median', 'std', 'min', 'max'])
print(summary)

import pandas as pd
import matplotlib.pyplot as plt #library used to create visualizations
data = pd.read_excel('/content/Marketing_Campaign_Data_5000.xlsx')
plt.figure(figsize=(12, 8)) #size of the figure 12 width, 8 height
# Age
plt.subplot(3, 1, 1) #3 columns, 1 row, 1st position
plt.hist(data['Age'], bins=20, edgecolor='black') #bins are no. of data we want to be displayed/ no. of vertical bars
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
# Income
plt.subplot(3, 1, 2) #3 columns, 1 row, 2nd position
plt.hist(data['Income (in $K)'], bins=20, edgecolor='black')
plt.title('Income Distribution')
plt.xlabel('Income (in $K)')
plt.ylabel('Frequency')

# Spending Score
plt.subplot(3, 1, 3) #3 columns, 1 row, 3rd position
plt.hist(data['Spending Score (1-100)'], bins=20, edgecolor='black') #edgecolor is optional but preferred for a clean dataset
plt.title('Spending Score Distribution')
plt.xlabel('Spending Score')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel('/content/Marketing_Campaign_Data_5000.xlsx')
plt.figure(figsize=(12, 8))
# Age
plt.subplot(3, 1, 1) #3 columns, 1 row, 1st position
plt.boxplot(data['Age'], vert=False) #Boxplot can be plotted either horizonatlly/vertically by changing Boolean value.
plt.title('Box Plot for Age')
plt.xlabel('Age')

# Income
plt.subplot(3, 1, 2)#3 columns, 1 row, 2nd position
plt.boxplot(data['Income (in $K)'], vert=False)
plt.title('Box Plot for Income')
plt.xlabel('Income (in $K)')

# Spending Score
plt.subplot(3, 1, 3)#3 columns, 1 row, 3rd position
plt.boxplot(data['Spending Score (1-100)'], vert=False)
plt.title('Box Plot for Spending Score')
plt.xlabel('Spending Score (1-100)')

plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel('/content/Marketing_Campaign_Data_5000.xlsx')
plt.figure(figsize=(12, 8))

# Gender
plt.subplot(2, 2, 1) #2 columns, 2 rows, 1st position
data['Gender'].value_counts().plot(kind='bar', color='green',edgecolor='black')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Frequency')

#Married
plt.subplot(2, 2, 2) #2 columns, 2 rows, 2nd position
data['Married'].value_counts().plot(kind='bar', edgecolor='black')
plt.title('Married Distribution')
plt.xlabel('Married')
plt.ylabel('Frequency')

#Children
plt.subplot(2, 2, 3) #2 columns, 2 rows, 3rd position
data['Children'].value_counts().plot(kind='bar',color='maroon', edgecolor='black')
plt.title('Children Distribution')
plt.xlabel('Children')
plt.ylabel('Frequency')

#Product Category Preference
plt.subplot(2, 2, 4) #2 columns, 2 rows, 4th position
data['Product Category Preference'].value_counts().plot(kind='bar',color='peru', edgecolor='black')
plt.title('Product Category Distribution')
plt.xlabel('Product Category')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

#CORRELATION MATRIX
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets #provides tools for machine learning and statistical modeling
import seaborn as sns #statistical graphs and data visualization
numerical_columns = ['Age', 'Income (in $K)', 'Spending Score (1-100)']
correlation_matrix = data[numerical_columns].corr()
print(correlation_matrix)
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='mako', vmin=-1, vmax=1, linewidths=0.8) #vmin and vmax is the range which lies between -1 and 1.
plt.show()
