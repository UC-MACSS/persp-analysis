# Counting things
Simple counting can be interetsing if you combine a good question with good data
Important and Interesting
Examples of Interesting

## 1 Work behavior of taxi drivers in NY
Henry Farber (2015)
* Question:
two important features about the work environment of taxi drivers:
1) their hourly wage fluctuates from data to day
2) their number of hours they work can fluctuate base on their decisions
* Theory:
1) Necoclassical predict work more on day they have higher hourly wages
2) behavior predict opposite
* Data:
Farber obatined data on every taxi trip by NYC from 2009-2013:
1) start time, location
2) end time and location
3) fare and tip
900 million trip of 40 million shifts
* Statistical Method and results:
1) A random smaple on high wage days:
   Farber found that most drivers work more on days when wages are higher
2) Leverage the size of the data:
   1) over time newer dirvers gradually learn to work more hours on high wage days
   2) new drivers who behave more like target earners are more likely to quit being a tax driver
* Advantage compare to pervious study, not possible for the small size
* Charateristics of good using big data:
1) data were not non representative - because the city required drivers to use digital meters
2) data were not incomplete
3) a good question with good dta


## 2. Friendship formation by students
they try to understand friendship formation and they dealing with the incompleteness of big data
Kossinets and Watts (2009)

* Question: how three factors would interchange with each other in the social network formation
  social network evolution is driven by three features:
  1) the structure of existing relationships
  2) shared activities (ge., dorms, classes)
  3) demographics

* Difficulties in terms of incomplete:
  they started their research vy acquiring the email logs from a large university - they were incomeple
  they don't include everything needed to undsertand the various factors drving netwrok evolution
* Solution: merge sources:
  therefore they merged these Email logs with demographic information collected by the university and informaytion of shared avtivities(e.g., student residence info and complete list of enrollment in courses)
* Difficulties in operationalization of theoretical constructs:
  What is connected?
* Solution: 
  they consider two people were connected at time t i.f. they had exchanged emails in pervious 60 days
  -> a small hint, some specific cutoffs like 60 days instead of 30 days or 90 days: maek sure that your results are not sensitive to this choices

 * Main findings:
   1) people with similar demographics are more likely to form relationships
   2) this pattern was strongly mitigated by exsiting network structure and shared activities


## 3. Social media censorship in China
* Question:
Researchers and citizens have little sense of how these censors deciede what content should be deleted from social media. Some think it about critics of the state, while some think its collective behavior, such as protests.

* Initial Methodlogy
A massive engineering of the post to see which are censored. Those censor usually happen within 24 hours. So it must be fast crawler to collect the data. 

* Difficulties and Process to deal with
2 million of 11 million posts are censored, and the highly senstive topics were censored only slightly more than middle and low sensitivity topics. But this simple calculation of censorship rate could be misleading. Therefore they developed a measure to match the sentiment of each post. They label their 11 million social media posts as to whether they were 1) crtical of state 2) supportive of the state 3)irrelevant of factual reports about the events.



# Forecasting and nowcasting
Predicting future is hard but predicting the present is easier
Flu remedies - google search engine
database of intentions - provide a constanly updated window of collective global consciousness, but turing this stream of information into a measurement of the prevalence of the flu is difficult. There are U.S. Centeros for Disease Control and Prevention has an influenza monitoring system that collects information from doctors around the country. However, one problem with this CDS ssytem is there is a two week reporting lag. Therefore Ginsberg et.al (2009) tried to predict the CDC flu data from the Google search data. 