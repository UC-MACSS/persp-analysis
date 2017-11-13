import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in Data
# We have the temperature record for each country for each month
cols_to_keep = ["dt", "AverageTemperature", "Country"]
temperature = pd.read_csv("GlobalLandTemperaturesByCountry.csv", \
						  usecols = cols_to_keep)

# Extract data points in each year
year_dict = {}

for index, record in temperature.iterrows():
	year = int(record["dt"][0:4])
	avg_temp = record["AverageTemperature"]

	if year >= 1890:
		if pd.notnull(avg_temp):
			if year not in year_dict:
				year_dict[year] = [avg_temp]
			else:
				year_dict[year].append(avg_temp)

# Compute the average temperature (all countries have equal weight) for each year. 
year_list = []
avg_temp_year = []

for key, value in sorted(year_dict.items()):
	year_list.append(key)
	
	sum_temp = 0
	count_temp = 0
	for temp in value:
		sum_temp += temp
		count_temp += 1

	avg_temp_year.append(sum_temp / count_temp)

# First figure: line graph plotting computed average temperature for each year of all cities
plt.plot(year_list, avg_temp_year, marker = ".", linestyle='solid')
plt.title('Average Temperature by Year (All Countries)', fontsize = 12)
plt.xlabel(r'Year')
plt.ylabel(r'Average Temperature (in Celsius)')
plt.savefig('assignment5_Kaggle_plot1.pdf')
plt.show()

# Plot a histogram of the avergae temperature in 2013 
year2013_data = np.array(year_dict[2013])
plt.hist(year2013_data, color = "crimson", normed = True)
plt.title("Distribution of Average Temperature by Country in 2013", fontsize = 12)
plt.xlabel("Average Temperature (in Celcius)")
plt.ylabel("Density")
plt.savefig('assignment5_Kaggle_plot2.pdf')
plt.show()