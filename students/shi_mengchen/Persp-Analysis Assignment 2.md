# Persp-Analysis Assignment 2

#### Name: Mengchen Shi

#### Date: October 22th, 2017

## Social networks and risk preference

### Introduction
Traditional portfolio theories suggest that investment decisions are based on the investors’ risk preference. Weber and Morris (2010) found that social networks have influence on one’s risk preference such that those with strong social networks tend to be less risk-averse. Weber and Hsee (1999) pointed out that China is a typical relationship society, and Chinese people’s economic behaviors are affected by social networks. They held that when Chinese people suffer from investment loss, they are more likely to get help from social networks. That is, social networks act as cushion to investment risks. Chua et al. (2009) found that networks reduce potential investment risks, and that investors with strong social networks tend to become risk-seeking.	

Does the relationship between social networks and risk preference exist? We plan to validate this theory by conducting a survey on WeChat, the most popular social media mobile application software in China. 

### Research Plan
We plan to combine observing data and asking questions in the research. As Salganik (2017) mentioned in Bit By Bit: 

> The best way to think about the relationship between asking and observing is that they are complements rather than substitutes… When there is more big data, people want more surveys.

We will construct independent variables and control variables with observed data collected on WeChat, and construct dependent variables with survey data. Before we begin our research, there are two questions need to be answered first: 

##### Why WeChat? 
By August 2017, WeChat was one of the largest standalone messaging apps by monthly active users, with over 963 million monthly active users. It is known as China's "App for Everything" with its many functions and platforms. Apparently, WeChat can provide a large scale of users’ information, including demographic, numbers of friends, on-line chat habits and so on, which is essential for us to construct variables.

##### How to persuade WeChat to grant our access to data? 
As an “App for Everything”, WeChat also offers finance services such as offering investment funds products. Therefore, WeChat group will be interested to know how users’ choices of financial products are related to their networking characteristics. As risk preference is strongly related to investment choice, our research can provide WeChat with a perspective on analyzing users’ behaviors and to promote their products in a more efficient way. As for the concern of privacy, since we only need the characteristics of users without their true identifications, there will not be privacy leaking problems.

#### Observed data
We will utilize cross-section data and build a multivariate regression model to analyze this question. Each user is an observation unit. We need to collect each user’s basic demographic information, including age, gender and residence. Information about marriage, education and wealth are also important to the research, but they are not available directly. However, we believe WeChat can easily infer the information based on users’ activities on the platform. For instance, users’ wealth can be analyzed by their shopping, payment, and transfer records on WeChat. All the information mentioned above will be used to construct control variables.

The independent variables represent users’ social networks. WeChat records how many contacts a user has and how frequently a user contact with friends on WeChat, which could be utilized as measurement of a user’s social circle and closeness with friends. In addition, WeChat has a function called “Red Packet”. It is a popular way to transfer money between friends to express one’s blessing, gratitude, and other positive emotions to each other, especially in special days such as New Year and birthdays. The amount and frequency of “Red Packet” can be utilized to measure one’s social networks as well. 

#### Survey method
One’s risk preference, namely, how he/she is risk-averse or risk-seeking, is the dependent variable in the study. Data for risk preference cannot be directly observed on WeChat, because it exists only inside one’s head. This is where survey comes in. 

The survey will be in a form of “a test for fun” to be spread across WeChat “Moment”, a platform to share users’ photos, ideas and any interested things. The test should be called “Will you have more luck of fortune in the coming year?”. We will release the test during Spring Festival, when people are enjoying their holidays (more leisure time) and are looking forward to a lucky new year.

As “a test for fun”, the survey will contain only two simple questions. The questions are motivated by Charness and Genicot (2004):

> The first question: if you have 10,000 RMB to invest, how will you allocate the money to two different assets? The gain from the assets are determined by rolling a 10-dimension die.
Assets S: Multiplied by 1 regardless of die throw	
Assets R: Multiplied by 0 if die is 1, 2, 3, 4, 5; multiplied by 2.5 if die is 6, 7, 8, 9, 10. 
> 
> The second question: the same as the first, but the assets are different.
Assets S: Multiplied by 1 regardless of die throw	
Assets R: Multiplied by -2 if die is 1, 2, 3, 4, 5; multiplied by 4.5 if die is 6, 7, 8, 9, 10. 

We can measure the respondents’ risk preference by analyzing their investment allocation between safe and risky assets.

### Discussion
#### What about the survey makes it digitally-enhanced?
We will apply a new way of asking questions – gamification – to make the process of answering questions more enjoyable and game-like. The online “test for fun” is popular with WeChat users. Tests like “Want to know how lucky your name is?” and “How would you look like if you lived 1000 years ago?” attract a lot of users to click. Even though users might not believe in these tests, they are curious about the results and have fun in those tests. Besides, people will be interested in our test because they are more concerned about “luck” during Spring Festival. All the points above make it possible that our online survey can be popular as well.

There are some nationwide interview-based surveys in China such as China Household Finance Survey (CHFS) that cover similar questions. What are the advantages of our survey compared with interview-based surveys? First, we only ask a few questions, instead of a hundred of pages of questions, which reduces the chance of impatience of respondents and thus increase the quality of answers. Second, with assistance of observed data, our research eliminates the privacy concern that usually come up when people are asked about social life and wealth. Third, as respondents are easily accessible online, the costs of on-site interviews no longer exist. Last but not the least, collecting responses on WeChat enlarges the number of respondents dramatically with high efficiency. For example, it took 500 volunteers three months to visit 30,000 households in 2011 to complete the interviews (Gan, 2012). With the assistance of WeChat, however, our test can reach millions of people in a few seconds.

#### How would a survey be better than an observational study?
Risk preference is hard to be observed and measured on WeChat, because it is an internal state that exists only inside one’s head. Some might argue that we can use observed data about how people invest in different kinds of finance products to measure their risk preference. It is not applicable in practice. First, WeChat does not provide sufficient financial products, so their data are not complete; second, the investment data held by banks or financial companies are not accessible because these companies should protect clients’ privacy strictly.

#### Potential error
Our survey might suffer from severe representative error. First, there will be coverage error because not all people in China use WeChat. Thus, we cannot conclude our result to be a representative of all people in China. Second, our knowledge about users’ social networks is limited in WeChat. We have no idea how his/her life outside WeChat is. Third, the survey will suffer from sampling error. Even though we do not have a sampling process literally, the survey does select a sample with bias. Our survey only reaches the users who are willing to have a “test for fun”, which itself is not a random sampling. We can minimize the error by reframing the way we distribute the survey. For instance, users are required to do the test if they want to receive “Red Packets” from others, which, obviously, requires consent from WeChat. Or, we can “tempt” users by offering respondents a chance to win a red packet after finishing the test, which will produce more costs. 

Measurement error is another potential problem because risk preference is a state inside one’s head. Perhaps people cannot tell it clearly by themselves. Therefore, we must design our questions very carefully to enhance the measurement accuracy. We refer to a classic test created by Charness and Genicot (2004), to measure people’s risk preference. Another way to reduce measurement error is to add more detailed questions at the cost of losing the acceptability of our survey. 

### Reference
[1] Weber E U, Morris M W. Culture and Judgment and Decision Making: The Constructivist Turn.[J]. Perspectives on Psychological Science, 2010, 5(4):410.  
[2] Weber E U, Hsee C K. Models And Mosaics: Investigating Cross-Cultural Differences In Risk Perception And Risk Preference[J]. Psychonomic Bulletin & Review, 1999, 6(4):611-617.   
[3] Chua R Y J, Morris M W, Ingram P. Guanxi vs Networking: Distinctive Configurations of Affect- and Cognition-Based Trust in the Networks of Chinese vs American Managers[J]. Journal of International Business Studies, 2009, 40(3):490-508.   
[4] "WeChat's world". The Economist. 2016-08-16. ISSN 0013-0613. Retrieved 2016-08-08.  
[5] Charness, Gary, and G. Genicot. "An Experimental Test of Risk-Sharing Arrangements." Meeting Papers Society for Economic Dynamics, 2004.  
[6] Li, Gan. "Findings from the China Household Finance Survey." (2012).  

