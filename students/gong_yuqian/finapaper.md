# Evaluating Research Design
 
Yuqian Gong


## Paper 1: Digital Discrimination: The Case of Airbnb.com  
### 1.Summary 
In this research paper, the researchers examine the extent of racial discrimination against hosts on Airbnb, which is facilitated by the public profiles of hosts where a host?s race can be identified. The theoretical construct of race discrimination is operationalized as prices charged by hosts for their housing listings. Specifically, the research is ?focused on estimating the price gaps between black and non-black hosts?. Computational methods are adopted by the researchers through analyzing the observational data set containing the housing lists on Airbnb for New York city on a single day in 2012, which contain all information observed on a housing list including locations, reviews and photos. The method to address the question is to approximate an experiment, a common approach in observational study, by controlling all significant factors and study the effects of the single treatment or factor, which is whether hosts are black or not revealed from their Airbnb profiles. Firstly, after deciding the variable price to operationalize the theoretical dependent variable, researchers try to find out all the determinants of prices available to be observed from the listing page. Noticeably, the researchers assume that the quality of listing photos can affect the price. Therefore, they resort to the computational method of mass collaboration to quantify this variable by recruiting workers from Amazon Mturk and making them rate the photos on a seven-point scale. After regressing all the possible factors on the dependent variable price, researchers select the variables to be controlled such as number accommodated, location ratings, the number of bedrooms, the quality of listing photos and etc.

The second step researchers take is to add these controls and find out the effect of the hosts? race. It is found that after adding all the controls and running the regression, ?non-black hosts earn roughly 12% more for a similar apartment with similar ratings and photos relative to black hosts.

### 2.Effectiveness and limitations

**Effectiveness:**

This research design takes great advantage of the characteristics of big data. Firstly, the selected dataset contains almost all quantified information listed on each housing page that would potentially affect the price charged for each list. So the issue that prices or racial differences are correlated with unobserved differences can be mitigated as researchers incorporate ?all the information that a guest sees when examining the Airbnb results.? The large dataset also enables researchers to get better causal estimates for each control factor considering its big characteristic. Therefore, given almost all the control factors and their casual estimates, we can achieve a rather accurate measurement of the effect of hosts? race on prices.

Besides, the big dataset makes it possible for researchers to measure the heterogeneity of treatment effects among subgroups. In this research, in addition to finding out the average price gaps charged by black and non-black hosts, it is also found that the racial discrimination is worse in subgroups of hosts whose properties are in a poor location.

Another advantage of using observational data in this case is that users on Airbnb are non-reactive to the experiment we approximate.

In all, this research design is rather effective in controlling most influential factors and the result of 12% average price gaps for black and non-black hosts has considerable credibility given this dataset and research design.

**Limitations: **

Despite those advantages of this research design, there are still many limitations.

Firstly, it is highly debatable whether the price gaps between black and non-black hosts is an effective and credible construct to measure the racial discrimination caused by hosts? public profiles. In fact, the combination of prices charged by hosts and demands by users together would reveal any racial discrimination. However, in this case the dataset is incomplete in that they lack the data of users? demand as researchers have no access to them. Therefore, they actually don?t have the most ideal data to operationalize the theoretical constructs and have to ?forego analysis of consumer demands? and make the assumption that the price gaps alone reflect racial discrimination. This assumption is apparently problematic if those listings with lower prices charged by black hosts actually attract more users to book. Hence, the incompleteness of this dataset and inaccessibility of demand data could raise problems of construct validity.

Secondly, the research design may also lack external validity as the dataset from the New York city is not representative of all Airbnb listings across the U.S. or even outside U.S. It could be the case that Airbnb hosts in different regions experience different levels of racial discrimination or some regions don?t have any. This research fails to validate these assumptions and is of little value to studies in a broader setting.

To categorize the photos into different quality levels, the researchers hire Amazon Mturk workers to rate the photos on seven-point scale. This approach has one potential drawback that these Amazon Mturk workers might not be representative of real Airbnb users. Airbnb users might be mainly young people with middle income level while Mturk workers? age and income level are unknown. Rating photo qualities are highly correlated with personal tastes and the tastes of Mturk workers might differ a lot from those of real users. Researchers also don?t explain why seven-point scale is a good measure to quantify the photo qualities.

Lastly, I think that the research fails to take advantage of the always-on feature of big data and doesn't fully explore the heterogeneous effects among subgroups. The data is collect from Airbnb website on a single day. It doesn't show users? changing behaviors and degrees of racial discrimination overtime, which might deliver more interesting insights using longitudinal data. Similarly, the research only examines the heterogeneous effects among subgroups with good or poor locations. Given so much detailed information on each listing, comparable conclusions can be drawn from more subgroups of hosts.

## Paper 2: Racial discrimination in the Sharing Economy: Evidence from a Field Experiment

### 1.Summary 

In this paper, the research question is to study whether racial discrimination exists against Airbnb users from hosts. The researchers applied a field experiments to simulate the real accommodating procedures on Airbnb and compare the hosts? acceptance rates of accommodation requests from African-american users and white users. To run the experiment, a total number of twenty fake guest accounts were created to send requests to hosts using web browser automation technology. The accounts are divided into four treatment groups: half of the accounts had typical black names and the other half had typical white names; within each racial group, half were female names and the other half were male. These four treatment groups had identical information except for their names and all of the accounts had no picture profiles. Then requests were sent from these five accounts to listings from five selected cities which were available then at a specific weekend in September. Hosts? responses were collected during the period until that weekend. The research actually leveraged a lot the existing Airbnb platform to conduct experiments instead building an experiment from complete scratch.

In addition to the simple digital experiment, many computational methods were adopted to collect additional observational data to be used for more complicated analysis of the experiments? results such as comparing levels of racial discrimination among subgroups of hosts with different characteristics. The data that characterized the hosts and listing feature were collected using the web scrapping technique. To identify the race of previous guests who reviewed a guest from their profile pictures, a face-detection API was applied. The researchers also created a probability model to predict how likely the listing would be filled by the specific weekend. Mass collaboration also helped the researchers to collect the data that were hard to capture through digital methods. For instance, Amazon Mturk workers were hired to identify the race and gender information of the hosts. Other participants were recruited to identify the most typical black or white names?which guaranteed that the name selected could easily reveal a person?s race. To sum up, the researchers were quite good at applying computational methods in this research.

### 2.Effectiveness and limitations

**Effectiveness:**

 This research design does a good job at choosing a measurable variable operationalize the theoretical construct, which is users? names and dividing treatment groups based on gender and name groups. Creating fake accounts with identical information and different names and genders eliminates all other influential factors from a guests? profile that could affect the hosts? decision making.

I think what is most impressive about this experiment is the combination of observational data and experiments to conduct more complicated analysis and therefore deliver more interesting insights. Data representing the characteristics of both the hosts and the listings were scrapped from the pages to measure heterogeneity of treatment effects among groups with various characteristics. For instance, through comparing the results for more experienced hosts or hosts with multiple properties and those less experienced ones, we can measure if there exists a race gap. The linkage of census data with observational data scrapped from the listings resolved the problem of incomplete demographic information, allowing researchers to examine whether the racial discrimination was worse in areas with larger proportion of black residents. Although from the results we observed that the racial gap was significant among almost all subgroups and there were no obvious heterogeneous effects, the combination of observational data and experiments expanded research questions we can ask.

Besides, the observational data can be used as evidence to support the validity of our results. In this case, we scrapped data from the reviews of our hosts and studied race discrimination gaps between hosts who accommodated black guests before and those who didn?t. Interestingly, the former group had a higher probability to accept housing requests from black users compared with the latter group, which backed the external validity of our experiment results to a great extent.

To evaluate the causal mechanisms, comparing internal data from Airbnb with our results, we were able to find out that profile pictures wouldn't help improve the acceptance rate gaps a lot. This could rule out the possibility that lack of profile pictures would cause racial discrimination.

I think what differentiated this research design from others also involved the efforts they put in building a model to estimate the revenue cost caused by racial discrimination. This showed the potential economic consequences, which helped add social-economic value to this study.

**Limitations: **

Although we found that lack of profile pictures is not a major factor to cause the racial gap, the study involved no methods to exactly examine the causal mechanism of the racial discrimination. The reason was that there was not much room for different variations for the treatment and the treatment of different names and genders were too simple.

Also, the simple fake accounts were still different from real accounts in that they contained homogenous information so we were not able to compare the racial discrimination levels against different black groups. Questions might arise such as whether discrimination from hosts were severe towards poorer black users? Or black users from specific regions?

Another limitation would be that the research didn?t fully take the advantage of the always-on feature of the Airbnb platform and we couldn't? infer the changing trend of racial discrimination over time.

## Value-added of conducting both projects

Firstly, although the two projects both study the racial discrimination on Airbnb, the objects of interest are quite different. The observational study examines the discrimination from users against hosts while the experimental study examines the discrimination phenomena the other way around. We learn from the two projects that racial discrimination exists from both sides. The two projects let us study the question from two different angles and both deliver new research significance.

Secondly, the experimental study actually plays a better role in adding strict controls on objects of interest to rule out confounders, only focusing on the treatment effect the researchers care about. In the experiments, the only treatment is the name and race. However, in the observational study, even if we control almost all information available to user, we may still omit any differences unobserved that could affect the prices charged, such as the hospitality revealed from the hosts in their private interactions with users. In this case, the observational study could serve as additional evidence to support the external validity of the experiments and expands the population being discriminated to hosts as well.

## Survey design

There are two sets of surveys, one survey is treating the participant as host while the other is treating the participant as an Airbnb user. For each participant, which survey he or she will take will be randomly assigned. Suppose the survey assigned to one participant is targeted to a host. The survey will actually contain ten fake Airbnb users and their background information. One group of five users have typical black names while the other group of five have typical white names. The background information of each user will include such as their age, hometown, job, gender, interests and so on. The users in the two name groups have identical five sets of background information, which means one user from the black name group must have the same background information as one user from the white name group except for their different names. Then survey will contain ten questions. For each question, one user?s name and his or her information from the set of ten users will pop up and the question will be shown to the participant asking whether the participant is willing to have the user as his or her guest if he or her is an Airbnb host. The options will only be Yes or No. And the time allowed to answer each question is very short, about ten seconds, which is only enough for a participant to read through the users? background and make an instinct choice of either Yes or No. The order that each user pops up in the survey is randomized. For participants who are assigned the user survey, the procedure of the will be the same except that the question will be asking whether he or she wants to select the fake user as his or her Airbnb guest.

Besides the ten questions, the participants? information will also be collected at the very beginning of the survey. Information will include the participant?s race, gender, age, hometown and etc.

After we collect the data from the surveys, we will compare the selection rates of two users with identical background information but different names revealing their races. And we will see if racial discrimination exists if the black name group has lower selection rates than the white name group.

The survey link will be posted on Facebook and twitter with hashtag ?Airbnb?.

### Potential drawbacks:

One drawback of the survey design would be that the participants of this survey, who are either Facebook users or twitter users will not be representative of the Airbnb hosts or users. We solve this question by asking if they are Airbnb users or hosts or not in the survey. If they are users, the survey will be the one targeted to the users. If they are hosts, the survey will be one targeted to the hosts. If they are not in either group, we take the approach of amplified asking by matching their personal features with the features of real users and hosts. In this way, we would generate possible question answers for real users and hosts, who share same features with a participant from our sample pool.

Another drawback of the survey is that the lack of background information of the participants that can be used to measure heterogeneous effects among subgroups because we cannot ask too much about the participants in the surveys. We can solve this problem by collecting their information from their Facebook or twitter pages and categorize them through web scrapping features.

## References: 
[1] Edelman, B. G. and M. Luca (2014). Digital discrimination: The case of airbnb. com. Harvard Business School NOM Unit Working Paper (14-054).
 [2] Matthew J. Salganik. Bit by Bit: Social Research in the Digital Age. Princeton University Press. (2017) 
 [3] Edelman, B. G. and Luca, Michael, Svirsky, Dan. Racial discrimination in the Sharing Economy: Evidence from a Field Experiment. American Economic Journal: Applied Economics. (2017)
