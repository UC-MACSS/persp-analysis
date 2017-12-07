# Final Exam         


### The First Paper      
#### Research Design

Using an observational data set and other existing information, the researchers in this paper explores racial discrimination against landlords/hosts on Airbnb. Specifically, they investigate and estimate the price gaps between black and non-black hosts by controlling non-race variables, and thereby evaluate the racial discrimination on Airbnb.

- They first collect the data set consisting of a snapshot of listings from Airbnb for New York City as of July 17, 2012. Furthermore, they collect useful information from these listings, including the price asked by the host, the characteristics of host, the characteristics of the apartment, the number of review left by guests, a set of average ratings evaluating several dimensions of the host.    

- They hire workers on Amazon Mechanical Turk to identify the photo in each listings. The workers are told to rate the quality of the apartment reflected by the photos on seven-point scale ranging from bad to good quality.      

- In order to get the racial information about the hosts on Airbnb, they also downloaded all public profile pictures of the hosts in New York City and then still let workers on AMT to identity hosts' race.     

- In the stage of statistical analysis and model building, they sequentially controlled the variables in linear regression models in order to avoid the confounding effects caused by them.    

Finally they find from the regression results that non-black hosts charge approximately 12% more than black hosts for the equivalent rental.        

This study leverages two kinds of computational methods. The first is scraping observational data from the Internet for study and combine them with relevant existing information, including the dependent variable (price) and other control variables containing the information of quality and rating for apartments and hosts. They also take advantage of human computation project through  Amazon Mechanical Turk to rate the apartments in photos and to identify the races of the hosts in pictures. The ratings are used as control variable and the races are used as independent variable. Therefore, they obtain the dependent variable, the independent variable and the control variables through computational methods.    


#### Evaluation of Effectiveness      

This study has some good features of digital data. First, their data is non-reactive and thereby can improve the accuracy of evaluation. Racial discrimination is one of the most sensitive topics in contemporary United States. Many actual racists would disguise their identity if the have the time to react. Besides, racial discrimination is structural. Many people will have unconscious racist behavior but do not realize them as long as they are not in a non-reactive situation. Therefore, the non-reactive data from Airbnb website in this study can avoid the error caused by respondents' reaction and evaluate people's behavior in the natural field.      

Second, their research design (observational data and human computation project) can get a considerably large and plentiful information at a very low cost of time, energy and money. If we adopt traditional methods to study this topic, we have to visit these apartment one by one and also cannot obtain the information about rating for controlling variables.        

Finally, due to the always-on of the online data, their data can be longitudinal so that they can further enrich their data by time and then do a longitudinal analysis.        

However, there are still some drawbacks in their research design. First and most importantly, they should have put the variable "time" into their regression model. As we know, the demand and the supply in house rental marketplace can be seasonal so that time has a very large influence on the price. As long as we don't know whether differently racial hosts have different preferences of renting out their houses and setting the price, the variable "time" should be put into the model. For example, if black are more likely to rent this houses in slack season than other races, the price difference is not necessarily derived from discrimination. Besides, the variable "time" can also reduced the influence from user shift. For example, assuming that in some time periods lots of black landlords start to use Airbnb and lead to an average lower price, we cannot correctly evaluate the real difference between black and non-black if we just use mixed data sets. Since the variable "time" usually (not always) reflects user shift, it is very important in regression model. In the same logic, the variable "time" can also partly reduce the impact derived from algorithmic confounding.

Second, it is very obvious that their data is complete. Although they wanted to get more complete data from Airbnb but failed. Therefore, they can only use the incomplete information to build models. Without other very important variables, such as demand, supply and hosts' anticipatory prices, their results should be doubted even though they can use variable "time" to very partly supplement the incompleteness. 

Third, as the biggest city in the United States, New York City can not represent the majority of other cities. Therefore, it is not suitable to make a conclusion of the racial discrimination in the whole online marketplace simply according to the data about NYC. Finally, this paper does not mention how they can evaluate the results of rating. Seven-point-scale (large-scale) ratings are full of uncertainty when they are done by lots of people.   


### The Second Paper    
#### Research Design        

Using an experiment on Airbnb, the researchers in this paper explores racial discrimination against guests in house rental marketplace. Specifically, they evaluate the rental acceptance rate gap between black and non-black, and thereby evaluate the racial discrimination on Airbnb.      

- They first collect the data on all properties on Airbnb (similar to the first paper) in five metropolitan areas and the data about detailed host characteristics and images from their profile homepage. After data collection, they hire workers on Amazon Mechanical Turk to identify race, gender and age according to host images and also use Face++, a face-detection API, to categorize past guests by age, race and gender from reviews. Besides, they also link to census demographic data through the collected data and thereby obtain neighborhood demographics and discrimination.     

- They set four main treatment groups based on race and gender which are perceived by survey-validated names signaling black males, black females, white males and white females. The 20 identical Airbnb accounts except for guest names are divided into four same-number groups according to race and gender mentioned above. Identical messages except for data and name are sent to prospective hosts through these 20 accounts and each account would only sent one message to one randomly selected host.  The rental date were the weekend that were eight weeks distance from the time of sending message and they made sure the hosts they selected had room at that time. Finally around 6400 messages were sent to host between July, 25, 2015 and July 30, 2015. The researchers tracked host responses over 30 days and coded them into categories. Finally, they calculated the difference of replied acceptance rate between accounts with black and non-black names based on different subgroups divided by many control variables, and also computed the cost of host incurred by discrimination.     

Finally they find that guests with black names are 16% less likely to be accepted than non-black and this result is caused by the discrimination from a subset of hosts (those who never had an black guest). Besides, discrimination would incur a cost with the median between $60 and $100 revenue.     

This study takes advantage of several computational methods. They scraped the observational data from Airbnb and coded them into categories through human computation project (AMT). Parts of them became control variables in  the experiment and another parts were used for designing the experiment (e.g. selecting target hosts in experiment). Besides,  the experiment is also digital because it was conducted directly on Airbnb. Finally, when researcher identified the demographic information in reviews they also uses a face-detection API "Face++".


#### Evaluation of Effectiveness       


