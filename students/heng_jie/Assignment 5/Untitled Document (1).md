MACS 30000

Collaboration 
 
Jie Heng


# Part 1
## Task 1
My account name is jheng.
## Task 2
I am interested in the WSDM - KKBox's Music Recommendation Challenge. The goal of this competition is to build a better music recommendation system. Using personalizing algorithms, the competitor will solve problems like how to know if listeners will like a new song or a new artist and how would the music app know what songs to recommend brand new users. 

To make a submission, I will use the KKBOX dataset and design an algorithm to predict the chances of a user listening to a song repetitively after the first listening event within a certain time-- if the song is listened the second time within a certain time, the algorithm will mark this song “1”, if not, the song will get a “0”. Then, I will try to find the relations between the repeated music and the user—which makes the users choose to listen the second time in general, the composers, lyricists or genres of the songs. To make the relations easier to be observed, I will plot histograms, and line chart to show the correlations. The algorithm will take in training data and try to get as little bias as possible while applying it to the testing data. 

## Task 3
I choose ‘Climate Change: Earth Surface Temperature Data' this dataset to analyze. And I focus on ‘GlobalLandTemperaturesByMajorCity.csv’, this dataset, which has details of the temperature of the major cities in the world from 1849 to 2013. My code firstly shows the hottest cities in 1849 and 2013 respectively. Then I focus on China, I show the major Chinese cities’ maximum temperature and the temperature changes Beijing, Shanghai, Guangzhou from 1849 to 2013. From the graph, we know that the temperature of the hottest cities is increasing from 1849 to 2013 and the temperature of all the chosen cities is increasing.

Python code:
```sh
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# I choose 'GlobalLandTemperaturesByMajorCity.csv' this data to analyze.
# This dataset includes the temperature of the major cities from 1849 to 2013.
# Firstly, let's take a look at the hottest cities in 1849 and 2013.

# load the data
MajorCity = pd.read_csv('data/GlobalLandTemperaturesByMajorCity.csv',
                        index_col='dt', parse_dates=[0])
# get the top five hottest cities in 1849 
MajorCity[MajorCity.index.year == 1849][['City','Country','AverageTemperature']].groupby(
    ['City','Country']).mean().sort_values('AverageTemperature',ascending=False).head()

# get the top five hottest cities in 2013
MajorCity[MajorCity.index.year == 2013][['City','Country','AverageTemperature']].groupby(
    ['City','Country']).mean().sort_values('AverageTemperature',ascending=False).head()

# Then I will focus on China.
# Let's see Chinese cities maximum temperatures

cities = MajorCity['City'].unique()
Chinese_cities = {'Changchun', 'Chengdu' , 'Chongqing' , 'Dalian', 'Guangzhou', 'Harbin',
                  'Jinan','Nanjing', 'Peking' , 'Shanghai', 'Shenyang', 'Taiyuan', 'Tangshan', 'Tianjin', 'Wuhan', 'Xian'}

cc = pd.DataFrame(MajorCity)       
max_majorcity = cc.groupby(['City']).max()['AverageTemperature']
max_majorcity = max_majorcity.to_frame().reset_index()
max_majorcity.columns = ['City','City Maximum']
max_majorcity = max_majorcity.loc[max_majorcity['City'].isin(Chinese_cities)]

# plot the Chinese Cities Maximum Temperatures
ax = max_majorcity.plot.bar(xticks=max_majorcity.index, rot=100)
ax.set_xticklabels(max_majorcity.City)
plt.xlabel("Chinese City")
plt.ylabel("Max Temperature")
plt.title('Chinese Cities Maximum Temperatures',fontsize=13)

# Finally, let's look at the changes of temperature of China's three major cities: Beijing, Shanghai and Guangzhou.
pd.rolling_mean(MajorCity[MajorCity['City'] == 'Peking']['AverageTemperature'],window=12).plot(x=MajorCity.index)
plt.xlabel("Year")
plt.ylabel("Temperature")
plt.title('Changes of temperature of Beijing')

pd.rolling_mean(MajorCity[MajorCity['City'] == 'Shanghai']['AverageTemperature'],window=12).plot(x=MajorCity.index)
plt.xlabel("Year")
plt.ylabel("Temperature")

pd.rolling_mean(MajorCity[MajorCity['City'] == 'Guangzhou']['AverageTemperature'],window=12).plot(x=MajorCity.index)
plt.xlabel("Year")
plt.ylabel("Temperature")
plt.title('Changes of temperature of Guangzhou')
plt.title('Changes of temperature of Shanghai')

```
# Part 2
## Journal paper
Yair, Omer, and Raanan Sulitzeanu-Kenan. 2015. "Biased Judgment of Political Bias: Perceived Ideological Distance Increases Perceptions of Political Bias." Political Behavior 37, no. 2: 487-507. Political Science Complete, EBSCOhost (accessed November 12, 2017).
## Summary:
This paper drew survey of 1,257 students in social sciences and law faculties in ﬁve Israel universities. It finds that perceived ideological distance between a student and her set of professors substantially increases perceptions of political bias, constituting bias in the judgment of political bias. 
##Improving the article
Since there are only 1,257 participants involved in only five Israel university, this research lacks external validity. What’s more, the research is aimed to show how much students’ political bias is influenced by their professor, conducting a survey right on a mandatory class with the present of a professor is not a wise choice, considering that some students might give an unreal answer while they are rating the professor of the class the survey is conducting in.

To improve it, this paper can be reformulated as a human computation project. Only current university students will be hired. The authors can at first design an online survey and set a database.

The survey includes four parts. First, workers(students) will be asked to write down the total number of the professors who taught her in the current academic year in the relevant department. Second, workers will mark their professors on a 7-point left–right ideological scale. Undecided option is provided. Third, there will be a standard question of self-placement on a similar 7-point left–right scale. While they are doing the survey, the basic information like gender, age, nationality is automatically gathered from their account information are saved in the database. The last question is an instructional manipulation check question. For those workers who fail in the last IMC question, they will not be allowed to do the following tasks and their survey will not be stored in the database.

At the very beginning of this research, workers will only be provided with the survey and no extra tasks. With the increasing number of survey gathered, workers will be asked to analyze the “Perceived Ideological Distance(PID)” by countries. They will receive a training on how to apply the “PID formula” designed by the researchers to the data and map the results in a world map. Researchers can also calculate PID and compared with the result got by the workers.

## The benefits of human computation project:

This project design can improve the paper in several ways. First, it strengthens its external validity as the recruited workers are also research participants who are worldwide university students instead of students from one country. Second, we can compare the results in different countries and answer more questions, for example, which matters more in PID, age factor or geographical factors. Third, researchers can save considerable time and troubles, as they no longer need to analyze all the survey by themselves—most of the work are done by the online workers they hired, and they do not need approval from universities and professors to conduct the survey. Finally, the cost of the human computation project is relatively low as each worker is paid less than one dollar. Overall, this new research design could greatly increase the robustness of the results.

# Part 3
I chose to work on https://www.zooniverse.org, and got involved in four projects.
![](/totall.png)
![](/temperature.png)
![](/elephanttask.png)
![](/leaftask.png)
![](/treetask.png)
