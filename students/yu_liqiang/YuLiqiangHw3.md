#Evaluating How Much Negative News Influences Voters's Decision During A Presidential Election Using Amazon.com's Mechanical Turk --- A Lab Experiment Approach

##Introdution
Before the 2016 presidential election results came out, according to [many polls](https://www.realclearpolitics.com/epolls/latest_polls/president/), Hillary R. Clinton was predicted to have a landslide. However, as we saw, the result made many shocked. We start to think about how much the email scandal and other negative news had an impact on the voters' final decisions. The purpose of this research is to explore how much negative news occuring two months proceeding the election could affect voters' final decisions. We will simulate a presidential election and negative news to record participants' behavioral change on a scale of 1 to 10, i.e., voter intent, after being presented with this news. To ensure representativeness, we need a large sample which consists of randomized sampling of people according to their races, gender, education background, one's political point of view as pre-treatment information and which state does one come from. It was nearly impossible to conduct such a research before the digital age, due to its high cost and the amount of time to be consumed. Whereas, Amazon.com's Mechanical Turk (MTurk) enables us a low-cost experiment with a good representativeness. 

##Research Question
We want to quantitatively evaluate (on a scale of 1 to 10) the magnitude of the influence of a piece of negative news about one candidate on both voters who intended to vote for the candidate and who did not. Also, we want to know to what extent the influences of different types of negative news (sexual, corruptive, etc.) can affect the public and within the two groups. 

##Research Plan

###MTurk
MTurk is an online Web-based platform for recruiting and paying participants to finish tasks. MTurk is appealing to many social sciences researchers because of its low-cost of money and time. Due to some intrinsic property of our research question, such as the need to be representative for the who population of voters and the time-cost constraints, we adopt this platform in our research plan.

###Recruiting Experimental Subjects
MTurk is a promising tool for experimental subject recruitment. Expect tasks using human intelligence to identify pictures, it can also be used to assign tasks such as taking surveys with experimental purposes. 

It is easy to create a survey on MTurk. We first establish an account on mturk.com and place fund into our account, then post our job under the Human Intelligence Task with a setting of the amount of compensation to be paid and regions where do they come from. 

###Randomization
In our research, we want to obtain behavioral changes of respondents from each state, each political point of view and different gender and to ensure them as a good representative of the whole population of voters. In each subgroup, we randomly pick a group of people as our control group, feeding them with netural news and feed the left 'compare group' with negative news. 

###Deliver Treatments
When subjects participate in this task, they have to fill out a form about their background information, including their gender, races, where do they live now and their political point of view. Then, according to their background information, people with similar background will be randomly divided into a control group and a compare group. The profiles of two candidates will be presented to both groups and these profiles are constructed to be as indifferent as possible to aviod pre-treatment biases. Participants are asked how certain will they vote for each candidate on a scale of 1 (not likely) to 10 (definite). Then netural news will be given to control group and negative news will be given to compare group. Participants will be asked again about their intent to vote after news feeding.

###Measure Outcomes
Since the survey gives their intent to vote quantitatively, it is easy to measure the results. We will calculate the average intent in each subgroup for both control group and compare group and the difference between control group and compare group, and the outcomes before and after receiving the news. We can then draw conclusion based on subgroups and combination of characteristics such as gender & races or political point of view & states.

##Assessing The Research Design

### External Validity
One thing have to be noticed here is that to what degree can MTurk respondents represent the whole voter population. A good approach is to compare the MTurk subject pool with probability samples of U.S. residents. In a research about MTurk (Berinsky, Huber and Lenz 2012), it concludes that, MTurk sample does not perfectly match the demographic and attitudinal characteristics of the U.S. polulation but does not present a wildly distorted view of the U.S. polulation either. If we treat the MTurk as a means for conducting internally valid experiments other than a representative sample, its subject pool is very attractive.

### Internal Validity

#### Do Participants Violate Assignment by Partcipating in Experiment Multiple Times?

Although we can set to limit the number of times taking this survey to one for each worker on MTurk, they could register many accounts to break this limit, which expose them to more than one treatment condition. However, if we set a low pay rate, our research seems less attracive, considering many other well-paid jobs on MTurk. Besides, we can assess the IP address of one respondence. If more than two results come from the same address, we take that respondence as invalid.

#### Motivation And Attention 
In the research (Berinsky, Huber and Lenz 2012), Berinsky argued that setting an 'approval rate' of 95% encourage respondents to read instructions carefully and consider their respones. So we expect that our respondents would produce high-quality answers to our survey instead of randomly picking up answers.


### Heterogeneity of Treatment Effects
Our research includes the analysis of the heterogeneity of treatment effects on different people. We divided people into many groups according to their races, gender, political points of view and states that they come from but there may also be other attributes that could result in heterogeneity such as education background, salary, etc. One approach is to add questions about these attributes in our background survey and create more subgroups until people in each group reach to a level of similarity. Another approach is to create a test group to test if the effect differs from people to people. If not, we can continue or we have to divide our sample into more groups to make people similar.

### Casual Mechanism
We can dig deeper into the mechanism of people's reaction to negative news during a presidential election. The digital age give researchers the possibility to obtain process data and test many related treatments. 

For the process data, for example, we could add questions such as 'How do you feel about this news? Angry/ Sad/ Betrayed' to psychologically determine one's thoughts upon seeing this news, which allows us to investigate the embedding mechanism of decisions and emotions.

Besides, we could adjust the words used slightly in constructed news such as replace one emotional . In this way, we can factorize our research and find the factors that affect one's vote decision instead of just giving a general picture.




