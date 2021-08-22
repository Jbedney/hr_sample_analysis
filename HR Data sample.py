import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read in data
df = pd.read_csv("core_dataset.csv")

# view schema
df.info()

# view fields
df.head()

# filter by active employees
df = df.where(df['Employment Status'] == 'Active')

# remove whitespace in department names
df['Department'] = df['Department'].str.strip()

# capitalize fields
df['Sex'] = df['Sex'].str.capitalize()

# pivot to calculate average pay rate by department
by_department = pd.pivot_table(df, values='Pay Rate', index=['Department'],
                    columns=['Sex'], aggfunc=np.mean)

# calculate absolute value of pay gap
by_department['gap'] = (by_department['Male'] - by_department['Female']).abs()

# sort by pay gap
by_department = by_department.sort_values(by=['gap'],ascending=False)
by_department

# plot chart
female = by_department['Female']
male = by_department['Male']

X = by_department.index

X_axis = np.arange(len(X))
  
plt.bar(X_axis - 0.2, female, 0.4, label = 'Female')
plt.bar(X_axis + 0.2, male, 0.4, label = 'Male')
  
plt.title("Pay Disparity By Department")
plt.xlabel("Department")
plt.ylabel("Pay Rate")    
plt.xticks(X_axis, X,rotation=45)
plt.legend()
plt.show()

# pivot to calculate average pay rate by position
by_position = pd.pivot_table(df, values='Pay Rate', index=['Position'],
                    columns=['Sex'], aggfunc=np.mean)

# calculate absolute value of pay gap
by_position['gap'] = (by_position['Male'] - by_position['Female']).abs()

# sort by pay gap
by_position = by_position.sort_values(by=['gap'],ascending=False)
by_position

# plot chart
female = by_position['Female']
male = by_position['Male']

X = by_position.index

X_axis = np.arange(len(X))

f = plt.figure()
f.set_figwidth(15)
plt.bar(X_axis - 0.2, female, 0.4, label = 'Female')
plt.bar(X_axis + 0.2, male, 0.4, label = 'Male') 
plt.title("Pay Disparity By Position")
plt.xlabel("Position")
plt.ylabel("Pay Rate")    
plt.xticks(X_axis, X,rotation=90)
plt.legend()
plt.show()
