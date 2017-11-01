#Forecasting elections with non-representative polls from college students

##Introduction
Today is recognized as the transition from the 2nd to 3rd generation of survey research. The prediction of election, i.e., representative polling, has long been tightly associated with survey research for over 100 years. Recently, emerging statistical tools and computer-assistant data analysis methods make it possible to predict elections by even non-representative polls. In this digital age, non-probability sampling, computer-administrative interview and linking survey data to other data are becoming the mainstream of survey research in the 3rd era. A recent research conducted by Wei Wang, David Rothschild, Sharad Goel, and Andrew Gelman proposed a new approach to estimate the election result with a decidedly non-random sample of Americans, which opens the door for accurately measuring public opinions on social, economic and cultural issues with even skewed sampling.

In this proposal, we want to obtain accurate, cheap and fast forecasts of elections with non-representative polls, in this case, polls from college students, using proper statistical adjustment. 

##Data and survey design

We plan to conduct an opt-poll for students in 8 ivy league schools, which will last for 2 months preceding the 2020 US presidential election. Students could see this poll every time when they connect to their campus network using their mobile devices. Questions are all closed survey questions. Closed questions possess many characteristics that we want, such as easy to analyze and quick for respondents to answer.

In questionnaire design, the way of asking and specific words used can affect the results that we gathered from respondents. To avoid this, here we use a similar survey design as in Wei Wang's paper. We have one intention question and several demographics questions. The intention question is 

1. If the election were held today, who would you vote for? 

	Candidate 1\ Candidate 2\ Other\ Not Sure'. 

Some demographics questions are: 

1. Who did you vote for in the 2020 Presidential election? 

	Candidate 1\ Candidate 2\ Other\ Did not vote in 2020
2. Thinking about politics these days, how would you describe your own political view point?

	Liberal\ Moderate\ Conservative\ Not sure
	
3. Generall speaking, do you think of yourself as a ...?

	Democrat\ Republican\ Independent\ Other
	
4. Are you currently registered to vote?

	Yes\ No\ Not sure

5. Are you male or female?

	Male\ Female
	
6. What state do you live in?
	
	Dropdown with states; including District of Columbia and "None of the above"
	
7. In what year were you born?

	Before 1998\ 1998\ 1999\ 2000\ 2001\ 2002\ After 2002
	
8. What is your race or ethnnic group?

	White\ Black\ Hispanic\ Other


##Research degisn
We want to adopt a weighting non-probability sampling method because our sample population is not a random sample of all American voters. A weighting of out respondents is necessary to compensate the strong demographic biases in our data. 

###Multilevel regression and Post-stratification 
First, we want to use a method called post-stratification to deduce a representative poll. This method helps us find and eliminate the known biases between our sample population and target population when conducting non-probability sampling. It divides the sample population into many groups based on combinations of characteristics such as demographic information and political attitudes and then use estimated results in each group to extrapolate a picture in whole population by weighting each group by its relative proportion in the whole population.

The underlying assumption of this method is called homogeneous-response-propensities-within-groups, which assumes that within a group, our sample is randomly drawn from the population. To meet this assumption, a way is that we can divide our sample into more and more groups. However, data points could be sparse, resulting a biased estimate for each group. A common approach widely used is multilevel regression and post-stratification (MRP), which has been proved to show decent performace in non-probability sampling researches. 

###Verification
We want to make sure that the voter intent we obtained from our survey corresponds with other well-accepted polling methods before forecasting. After extrapolation, we can plot our MRP-adjusted data points with actual data points about voter intent from Pollster.com. Not only will we compare on national and stats level, but also we want to compare on demographic subgroups, since some today's campagins use targeted strategies on specific ethnic groups.

###Forecasting 
The estimate of voter intent does not directly imply the election result. So we expect that there is a linear regression relation between voter intent and the election result. Using previous data from 2016, 2012 and 2008 election, we can obtain the linear model for predicting. Then we compare the predicted result with actual result on national and state level.


##Justification	
### Digitally-enhanced
This research is largerly enhanced by digital methods in many ways. First, seldom do students have a landline phone in their dormitories. Thus, random digit dialing can hardly get a reasonable size of sample from our target population. Second, online surveys often have quicker responses. Since we are predicting the election, we wish to get the prediction result as soon as possible. Compared to traditional mail survey, which usually takes months to be responded to, digital survey is far better than traditional ways in terms of responding time. Finally, with computer-administrated interviews, the cost is dramatically reduced and the cost is always a constraint to be first considered before doing any survey research.

### Versus observational data

It is impossible to access detailed observational data for elections, though the data is accurate. The only way we can do is polling. Apart from accessibility, we can design our survey in a way that we can acquire even more information than observational data by adding questions about other aspects of one such as salary, family member's political view points or behavioral data, etc. This enables us to dig deeper into other causes of voting and make a more accurate prediction of elections. Our survey research is better than observational data by completeness and accessibility.

### Potential error

However, there are many sources of potential errors that we should be cautious about. Foremost, we selected demographic variables such as sex, age, state, race and party identification, but we only focus on population that is in the progress of college education. They may not represent the whole population due to their education background. Furthermore, the size of some subgroups may result in skewed representation when it has only few respondents. This can be solved by enlarge our sample population to more schools in US. Finally, voter intent is drifting, one may end up changing his mind and voting for a different candidate or making a vote which obeys his intent due to other reasons.

#Conclusion

We want to implement an accurate, cost-effective, accessible and timely approach to predict eletion results on a specific group using non-representative polls. We propose to collect survey data from college students and use multilevel regression and post-stratification to eliminate biases in voter intent. Then we can use voter intent to predict the 2020 eletion result. The research result will provide a guidance on both predicting and explaining researches facing a non-representaive data set. During implementation, we need more history data (2008-2016 eletion data) and be cautious about potential measurement errors.