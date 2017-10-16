# A Proposal of Oberservation Data

## Research Question
I want to make a "current" prediction of labor market situtation. We could use the quantity and quality online posting as proxy to study the labor market condition across the sector and across location. 


## Plan for Using the Data

### Collection of Data
Frist the research project needs to use web crawler to collect job posting from the career internet for the job posting. There are few options for collecting our data. The first one is linkedin, it not only posting new jobs advertisement, but aslo retain job posting in the past. It has a good feature for benchmark and comparison. The second one is indeed, which is the highest traffic job website in the United States, which has a better representation of different sector compared to linkedin. But the disadvantage is that it does not have the past job posting stored. The third one is google for jobs, whihc could used as a gengeral tools for job. But the searching results from google could be huge and difficult to categorial.

### Raw Manipulation
The main part of the data collected from the website is their job name, company name, position, deadline time, job posting time, sector, function, qualification, skill requirements. By this categorization, we could have a sense of how the working opportunity expand across industry. Potentially we might also have salary information, so that we could monitor labor market condition in wage side as well.

### Training Period
We could associate the data with textual analysis to see how this jobs are connected. What could be further conducted are analysis the change of job posting network, such as connectess, degree and betweeness. We could analysis the change of job clustering.

We could also develop an algorithm to monitor the change of job posting, so that we could have a raw understanding of how the labor market is, such as tight or loose. How many jobs are on the website and what is actually the statistics is. 


## How does this project illustrate the good characterstic of big data
### Big Data - Location Information
This data have the company name, thus we could tried to figure out the location of the job and we could let our data down to more local level, thus a more acurate measure of the unemployment situation across the country, rather than a overall country data, which tells your the whole picture, but might ignored the local information.

## How this project illustrate the bad charateristic of big data and plan to overcome
### A Trend of age of Internetlized World
It might be that we have to take care of the trend that over the time a large porportion of people might goes on internet. Therefore we need to seperated this trend out compared with the real labor market fluation. Moreover the data might be focused on the white collar job in linkedin or more general purpose job on the website of indeed. This fixed effects of the websites should be also addressed.
