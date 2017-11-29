import pandas as pd
import seaborn as sns

# From "https://www.kaggle.com/wsj/college-salaries".

# Load data frame:
df = pd.read_csv("salaries-by-region.csv")

# Put all we need from the original dataframe into this new dataframe:
df1 = pd.DataFrame()

# Need Region:
df1["Region"] = df[["Region"]]

# Convert Salaries right out of graduation and 10 years after graduation to floats:
start_salaries_to_float = df['Starting Median Salary'].replace('[\$,]', '', regex=True).astype(float)
end_salaries_to_float = df['Mid-Career Median Salary'].replace('[\$,]', '', regex=True).astype(float)

# Calculate the difference in medians and push onto our new dataframe:
difference_mid_start = end_salaries_to_float - start_salaries_to_float
df1["Median Mid-Career to Starting Salary Difference, $"] = difference_mid_start

# Plot, dividing by region
plot = sns.boxplot(x="Median Mid-Career to Starting Salary Difference, $", y="Region", data=df1).set_title('Salary Growth in 10 Years After Graduation, by Region')

# Save to pdf:
fig = plot.get_figure()
fig.set_size_inches(11.7, 8.27)
fig.savefig('Alexander Tyan - Assignment 5 Graph.pdf')

