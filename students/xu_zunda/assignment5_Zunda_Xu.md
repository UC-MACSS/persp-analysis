##Assignment: Collaboration

**Name**: Zunda Xu (zunda@uchicago.edu)
###TASK 1: Kaggle
**Part I**: My username is winstonxu, under email address xuzunda0817@gmail.com

**Part II**: Explore the Kaggle competitions page

**Question 1**: Describe one competition that you are interested in.

**Answer 1**: 

The competition which I am interested in is named "Porto Seguro’s Safe Driver Prediction".

**Question 2**: What is the goal of the competition?

**Answer 2**:

The prediction of insurance claims is always an important part for Insurance companies to deterimine their products' premium rate. For auto insurance, inaccuracies in claim predictions not only raise the cost of insurance for good drivers, but also reduce the price for bad drivers. Under such circumstance, some drivers who have always been cautious on the road may feel unfair to pay so much for their auto insurance, and then choose some other insurance companies which could provide relatively fair auto insurance plan. As one of Brazil’s largest auto and homeowner insurance companies, Porto Seguro hold this competition aimimg to explore a new and more powerful method to predict the probability that a driver will initiate an auto insurance claim in the next year, so that they could further tailor their prices and make their auto insurance coverage more accessible to more drivers.

**Question 3**: What would you have to do to make a submission?

**Answer 3**:

First of all, we should download and analyze the dataset we will used in this competition, which was seperated into two parts: training data and testing data. Each data record in these two datasets consists of four main types of features(e.g., ind, reg, car, calc), and each type of feature also contains several variables, including binary variables such as the gender of driver, catagorical variables, continuouse variables, etc. There is also a target column in dataset which signifies whether or not a claim was filed for that driver. After we know the structure of the dataset, the next step is to design some algorithgm  which would be able to use these historical data to predict the probability that each driver (distinguished by the id number) will initiate an auto insurance claim. We can first analyze the correlation/covariance between the target column and each variable to determine the possible predictor variables. Since the target question includes multiple-dimension variables, the basic method I would like to use is Monte Carlo Simulation Method. we could construct our model using python, and the result we want get is the probability of each ID (representing different policy holder in this dataset). Meanwhile, we need to use testing data to test the validity of our model. The format of our final submission file only contains two column, one column is ID number, and another column is just the probability that each ID will files a claim next year.
All the above is just what I have to do to make a submission in this competition.

###Task 2:Improving a Journay article

**Summary of the study**

The study I am focus on in this task is an article published on International Journal of Production Economics in 2015 named " [Insights from hashtag #supplychain and Twitter Analytics: Considering Twitter and Twitter data for supply chain practice and research](http://www.sciencedirect.com/science/article/pii/S0925527314004319?via%3Dihub) " written by Bongsug (Kevin) Chae. This research contributes to the Supply Chain Mangement (SCM) community by proposing a novel, analytical framework (Twitter Analytics) including for analyzing supply chain Twitter, highlighting the current use of Twitter in supply chain contexts, and further developing insights into the potential role of Twitter for supply chain practice and research. The main findings of this research include: supply chain tweets are used by different groups of supply chain professionals and organizations (e.g., news services, IT companies, logistic providers, manufacturers) for information sharing, and hiring professionals; some tweets carry strong sentiments about companies' delivery services, sales performance, environmental standards, and risk and disruption in supply chains. Even though the study construct a very innovative framework to bring social media into the feild of SCM, the amount of Twitters analyzed in this research is only 22,399, and I believe human computational techniques would be of great help in obtaining a bigger dataset to make the resarch findings more robust.

**Refomulate data collection**

In fact, in the last part of this article, the author mentioned that the study has limitations, particularly related to data collection. The first is the relatively short duration of data collection, which lasted a little over two months. Data collection for a longer period is expected to develop a more complete picture of the use of Twitter for SCM. The second is the way the data were collected. In this study, the researchers just chose hashtag #supplychain to search and collect Twitter data. Thus, only 22,399 Twitters with hashtag #supplychain were analyzed in this study, while not all the Twitters related to SCM include hashtag #supplychain. And some Twitters with only pictures/photos or videos related to SCM are also ignored in this research,but the truth is that these two types of Twitters usually contains much more information than Twitters with only text. As far as I am concerned, if we can take advantages of human computational techniques and refomulate the data collection process, the drawbacks of the previous dataset may be solved.

***Brief design***

Through human computation portals such as Amazon MTurks, we could design HITs for participants to find out the tweets related to Supply Chain Field as much as possible. In order to assure the accuracy of the search results at most, we could provide all the participants some reference materials, which may include a list of keywords, such as supplychain, manufacturing, logistics, risks, operation, etc; a list of hashtags such as #logistics, #supplychain, #SCM, #manufaturing, etc; and some basic knowledge in supply chain field. About the list of keywords and hashtags, we require our participants to find out all the Twitters including those keywords and hashtags. About the basic knowledge in SCM, we require our participants have a grasp of those easy and readable knowledge in SCM so that they could also provide us some Twitters without listed keywords and hashtags but actually related to the research field, this is really important since the machine may not accurately figure out Twitters related to SCM without specific keywords or hashtags. Meanwhile, the participants are also requried to find out all the Twitters that contains pictures/photos or videos with the themes of supply chai(such as advertisiments of logistics company, introduction of supply chain, etc), since the recognition of pictures and videos is also hard for computers to finish, while usually pictures and videos include much more information we may need than texts. However, about the last two kinds of Twitters provided by participants, the researchers still need to review them to make sure they are valid.

Last but not least, we could set a longer time period of our search of tweets, like two years, which means the participants could help us to search the recent two years' tweets related to Supply Chain as requirement. Also the time range of our HITs posted on the MTurks could last longer, which would help us collect the continuous data to analyze how Twitters related to SCM field change recently. With collected data through human computation portal, we would obviously construct a large scale database for this study. 

***How might this improve the study***

As mentioned before, the main limitations of the study is data collection. However, if we collect our data with the help of human computation portals, first of all, we could obtain a longer period of data. The previous study just use two months' Twitter data, and the new design set the time period as two years, which could help us obtain a better understanding of the use of tweetS for SCM. Meanwhile, we use multiple filtering factors, not only keywords, hashtags, but also considering pictures/photos or videos related to SCM in data collection process. This modified approach would enable research using a large quantity of supply chain-related Twitter data, and the human computational techniques could help us to realize all of these much more easily and conveniently. With a better dataset collected, the study would be definitely improved and the findings and conclusions of this research would also be much more robust.

###Alternative assignment: InfluenzaNet

**Compare and constast**

***design***

We will compare the differences in the design of these three systems. First of all, ***the InfluenzaNet system***. This system will recurite volunteers from the public through Internet. Each volunteer need to fill in an specific questionaire including certain demographic and lifestyle questions to complete the registration process and become a formal participant of this system. After that, all of those participants are requested to report whether they have experienced certain symptoms in the past week. Participants in this system could also create related account for their relatetives such as parents and children. The design of InfuenzaNet system contains the following features:random - control, reported-preference data, adequate auxiliary data information. About the random - control, since all the volunteers are recruited randomly from the general population, dataset in this system could guarantee the prerequisite of random sampling in data collection process. The reported-preference means the data are collected by reporting and surveys, which may result in issue of bias compared with observational data. Since each participant provided their basic demographic information and answers to some life-style questions, the analyst of this system could easily wight the data when they need to constuct some aggregated indicator for estimation. 

Second, ***the google flu***. This innovative "Nowcasting" system track the trend of ILIs according to users' google search on ILIs related information. The basic assumption behind this system is that users who search for ILIs related information are potentially ill. They set up a model which builds connection between the pyhsician-based reporting and the Google common queries, then they use historical data as training data to determin which queries best match the physician-based reporting. The "Nowcast" of the ILIs trend is just based on the best queries they obtained. The main features of Google flu system is large - scale data, observational data. Compared with another two systems, Google flu obviously has the largest dataset, and the data are all observational data collected from users' searching behavior.

Third, ***the traditional influenza tracking systems***. The traditional system relies on the national healthcare service, which means different healthcare institutions such as hospitals, clinics will regularly report the ILIs patients they treated and record the basic information of those patients in the system. Compared with InfluenzaNet and Google flu, the data scale is smallest, however, the data is more accurate since it is reported by professionals and the tracking process is simple.

***Cost***

Considering the cost of these three systems, Google Flu trend obviously cost least, since its dataset collected at an almost zero marginal cost per data. However, the InfluenzaNet system may cost much more than Google Flu trend system, since the InfluenzaNet system may spend money in participants recruitment, promotion, panel dataset maintainance and etc.
While the traditional tracking system also cost a lot, particularly in labor cost.

***Potential errors***

All of these three tracking systems have potential errors. 

For ***the InfluenzaNet system***, the potential errors is the potential selection bias in randomization. To be specific, the children under 7 years old and people older than 60 years old are less likely to be included in this system because of the access to Internet. However, as a matter of fact, these two groups of population are generally more vulnerable to ILIs. The under representation of these two groups of population in this system will definitely influence the accuracy of its estimation.

For ***the Google Flu***, the biggest problems is overfitting. The algorithm in this systems sometimes overfit to some seasonal terms which are totally unrelated with flu. To be specific, since the flu outbreak may have a strong correlation with seasonal pattern, its coincidence with some other seasonal queries does not mean the outbreak of the truly flu. Thus, the overfitting problem in this system may result in potential errors in estimation of flu trend in Google Flu system.

For ***the tradition tracking system***, the biggst problems is the scale of its dataset. Not all ILIs patients will pay a visit to healthcare institutions, which will definitely influence the data coverage in this system and result in selection bias. Meanwhile, usually those patients who do not pay a visit to healthcare institutions are highly correlated with flu trend, thus using dataset stored in traditional tracking system may not obtain accruate estimation of the latest flu trend.


**Potential Errors in unsettled time scenario**

Suppose an unsettled time, such as the swine flu outbreak. First, we consider the potential Errors in InfluenzaNet systems, just like we mentioned before, the children under 7 years old, the older above 60 years old and even the pregnant are usually more vulnerable to the outbreak of some new and unexpected flu. However, these three groups are more easily under-represented in this survey system than other groups of populations. Thus, when the InfluenzaNet system start predicting the trend of this flu, it's possible that the infected population has already been much larger, and the estimation of flu trend has already lost its meaning.

For the Google Flu, as we discussed above, Google Flu's algorithm relies on the historical data. However, the outbreak of some new unexpected flu usually accompany with some different symptoms. So it's highly possible that when people began to search terms related to the symptoms. the infected population has already been much larger, just the same problems as that resulted from using InfluenzaNet systems. 

For the traditional tracking systems, if the outbreak of the new flu starts from some undeveloped area. The lack of healthcare service in those areas will definitely influence the quality and quantily of the dataset used in the tradition tracking system. Meanwhile, the low treatment level in those undeveloped area may also result in some errors, since doctors in that area may have difficulty in recognizing the new flu.

To put it in a nutshell, no tracking system is perfect, however, if we could combine the advantages of each system, and keep modifying the data-collection process, I am pretty sure we can develop a kind of new system which could be of great help in estimating flu trend accurately.