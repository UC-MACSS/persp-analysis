##Evaluating research designs

### Digital Discrimination: The Case of Airbnb.com

####Research design
##### Research question 
Benjamin Edelman and Michael Luca were interested in evaluating the effect of racial disctimination on rent prices on Airbnb.com, especially for non-black hosts and black hosts. They mainly focus on the question: Do black hosts earn less on Airbnb? Using data combining landlords' pictures, rent prices and other attributes about rentals, they conclude that for equivalent rental, non-black hosts' listing prices are 12% higher than black hosts'. The robustness check confirms that the result is robust.

##### Data and design
In this observational study, Benjamin used listing data containing the price, the chatacteristics of the host and the chatacteristics of apartments of New York city on July 17, 2012 from Airbnb, along with about 3,800 ratings from guests. Besides, to obtain the racial information about the hosts and the information about guests' decision-making, they also recruited MTurk workers to identify the race of each landlord and simulate tenants' intention of renting given the listing quality. In-depth information about the digital discrimination behavior on Airbnb was obtained for this research.

To answer the question about digital discrimination, Benjamin used several methods. He first generally compared the rent price distribution among non-black and black groups and found that the distribution of black hosts had an obvious downwards shift. The average is \$144 for non-black and \$107 for black hosts. Noticing that shift, he applied a T-test and verified that the mean of two groups was different on a 1% level. However, there are many other factors that can affect rent pricing, such as location, number of bedrooms, etc. Benjamin applied several linear regression models with controlling on varibles such as location, the number of bedrooms and picture quality to form control groups. With control groups, non-black hosts had a listing price of 12% more for a similar apartment with similar ratings and photos relative to black hosts.

Then the researchers verified the validity by analyzing the result under the condition that only white and black hosts were used from Airbnb. 

#####Computational methods

A plenty of computational methods were used to leverage this research. The two most important of them are big data and mass collaboration.

This research was improved by Airbnb data mainly because it is big and it is non-reactive. Benjamin was able to collect all listing information of New York city on July 17, 2012, along with about 3,800 ratings coming from guests. There were many people, many observation and lots of information per person in the data, which enabled researchers to detect small difference (12%) in listing price and measure heterogeneity (several control groups). Despite so much information it contained, their unobtrusive measures would not change people's behavior due to the fact that big data is non-reactive. 

Mass collaboration was also introduced in this research, specifically, human computation. Otherwise, this research would not have been done in a time-efficient and economical way. It would take plenty of time and money for researchers, RAs to identify the race of 3,800 hosts by their profile photos and rate on the picture quality for each listing. 

In conclusion, this research was leveraged by big data and mass collaboration to be a digital observational study. 

###Evaluating the effectiveness

####Big data

#####Big
Massive data was extracted from Airbnb, which enables robust conclusions to be drawn from the data. The data is inclusive since all listing information of NYC on July 17, 2012 was contained in that data. Thus, researchers could draw a comprehensive picture of both landlords and guests in NYC on Airbnb at that time and avoid random error. Also, inclusiveness guaranteed that the result would be meaningful from a statistical perspective, since in a small sample, bias could be exaggerated due to several outliers. Besides, as mentioned in the paper, a subgroup of non-black hosts -- white hosts could be used to verify the robustness of the result, while it is almost impossible in a small data sample.

#####Inaccessible
Airbnb was not willing to provide data concerning about consumers' demand (e.g. guests' reviews) so researchers cannot further investigate into the relation between race and demand. However, it would not affect the result much because the measuring on demand effects was not a part of this research. Although if this part of data were accessible, the case study would have been more informative and comprehensive.

#####Non-representative
One thing to notice about is that the data was only collected from New York city, so the result (12% higher listing price) needs to be further verified for a broader conclusion (e.g. national digital discrimination). That is to say, the conclusion is limited to the special case in NYC. For a different place, maybe Paris, IL, the ratio of non-black hosts to black hosts is different from the ratio in NYC, resulting an unbalanced supply for each group, i.e., surplus in non-black group but shortage in black group. So this case study is not representative for the whole country.

#####Drifting
Booming information technology makes more people to have access to online marketplaces. The population who were using Airbnb at 2012 could be totally different from what it is now. Thus, we can draw a conclusion from the study that at NYC in 2012, digital discrimination existed on Airbnb but not the same conclusion for the present. Except the structure of population, people's view is also changing. So when we want to conduce a case study for the current situation, we have to re-collect the data and re-conduct our data analysis. We conclude that trying to expand this result to a broader time frame is effectless.

####Validity
#####Statistical conclusion validity
This reseach possesses good statistical conclusio validity. P-values were correctly calculated in the T-test. The method of controlling
for factors such as location, reviews and photos is reasonable for given data, which avoids the distortion caused by non-racial variables. 

#####Internal
This reseach exhibits good internal validity. Authors took the fact that there could be group drift between non-black and black hosts in terms of the location of their apartments into consideration. So they reduced variables in linear regression models to mitigate this effect. Moreover, the data was collected correctly, which contained almost all aspects of the listing information from Airbnb. So we can reproduce their analysis due to its good internal validity.

#####External

As discussed above, trying to extend the result to the whole country and to a broader time frame is of no use, because the population is drifting and people's views are changing nowadays. However, the research method can be used to draw a more comprehensive conclusion on a specific question.


### Racial Discrimination in the Sharing Economy: Evidence from a Field Experiment

####Research design
##### Research question 
Benjamin Edelman and his coauthors are interested in the racial discrimination to guests who has a distinct African American name on Airbnb. They conducted a field experiment on about 6,400 listings across five cities on Airbnb. They would like to know if there is racial discrimination against African American and found out that people with distinctively African American names are 16% less likely to be accepted bu hosts, compared to guests with a distinct white name. Besides, discrimination happens among hosts of all size, i.e., from small landlords to large landlords with several properties. 

##### Experiment, data and design
Researchers collected data of all listings on Airbnb in Baltimore, Dallas, Los Angeles, St. Louis and Washington, DC on July 2015, where each host is restricted to one transaction in the experiment to avoid bias. At the same time, demographic information about landlords was collected as well. MTurk workers were employed to assess the characteristics of each landlord, such as race, gender and age with cross-validation on their results to minimize error during this step. Other data was also collected, which included variables such as the number of properties one owned, guests' race from ones who posted a review, prices of listings etc.

For the experiment setup, there were four treatment groups: African American males, African American females, white males, and white females, which were classfied by their singal names. That is, a volunteer could easily identify one's race just by his name. Then, 20 accounts were created and adequately assigned to each group with the only difference on names (no profile photos). In the experiment, researchers let 20 accounts randomly send messages to hosts to ask for an 8-week later booking and only used data from available listing.

In the field experiment, 6,400 messages were sent during July 7, 2015 and July 30, 2015. Hosts' responses were coded into 6 groups based on the certainty of the response. But only response of "Yes" was used in following analysis.

#####Computational methods

Many computational methods had been applied to leverage this field experiment. Benefits mainly came from a digital field experiment. Overall, this digital field experiment combined control and realism at scale.

In an analog experiment, delivering treatments and measuring outcomes are usually limited in time. On the contrast, Benjamin Edelman and his colleagues were able to conduct their experiment in a short time (8 weeks), compared to months of experiment in analog era (e.g. mailing). Moreover, this experiment was economical. The only cost was to pay main researchers and MTurk workers, while in a lab experiment, expenses on participants' consists a large amount of cost.

Since the experiment was conducted without notifying hosts, realism was reached. Hosts behaved as usual. But in a lab experiment, subjects could behave innormally, contributing to a distortion on the result. Besides, digital experiments can be conducted on a larger scale. Benjamin Edelman applied automated tools to scrape the data and send messages.

###Evaluating the effectiveness
####Validity
#####Statistical conclusion validity
This research possess good statistical conclusion validity. First, researchers intentionally select five cities because they had varing levels of Airbnb usage and came from diverse geographic regions. So these five cities were accountable for a large amount of variance of nationwide Airbnb hosts. Second, the limit that each host was contacted for no more than one transaction ensured that landlords with multiple properties would have the same weight as small landlord in the data, eliminating potential distortion towards larger landlords.

#####Internal
Internal validity was reached as well. During the experiment, hosts were randomly assigned to one of the 20 hypothetical accounts, so potential bias had been removed from non-randomization before experiment. Delivery of the treatment guaranteed internal validity as well, since the only difference among all 20 accounts was the name, regardless of the slight difference in emails. Last but not the least, when measuring the response, they only considered the simple response--"Yes", which is feasible because they used the same measurement across all treatment groups. Figure 2 explained that the discrimination results occur because of differences in simple “Yes” or “No” responses, instead of being taken as spam or fake account.

#####External
By restricting their analysis to hosts who have had an African American guest in the recent past, Benjamin got the result that discrimination disappers, which reinforced the external validity of the main result. The main result is thus generalized to other situations. External validity was verified.

####Heterogeneity
Authors fully considered the heterogeneity of treatment effects. In the result section, hosts were divided into groups by their race, gender, experience, etc, and effects were measured according to these attributes. Listings were also classifies into groups by listing characteristics and effects were measured accordingly as well. Benjamin not only estimated average treatment effects but also estimated the heterogeneity of treatment effects, which enabled Benjamin to find the most relevant factors in digital discrimination and test new hypotheses. And the test on heterogeneity eventually reinforced the external validity.

####Ethics
However, this research was not rendered as an ethical research. According to Salganik's four principles of ethical research, first, it did not treat people as autonomous and honoring their wishes. Hosts participated Benjamin's field experiment without informed. This is pretty much like the Montana election experiment, where voters received voting information distributed by researcher without being noticed. Second, researchers did something on beneficence. For example, they "replied to the host with a personal message clarifying that we (as the guest) were still not sure if we would visit the city or if we would need a place to stay. We sent this reply in order to reduce the likelihood of a host holding inventory for one of our hypothetical guests.", but not enough. The risks could be an invasion of hosts' privacy. Third, hosts who participated in the experiment were taking the risk that they would lose money since hypothetical guests would not come. Risks were not equally distributed. Finally, they did not check if the automated tools and their experimental methods would violate specific laws or Airbnb regulations. 

### Value-added of combination of observational study and field experiment

When combining the results of both studies, a lot of useful information can be inferred from the combination and we found out that an observational study is indeed complementary to a field experiment or the other way around, mainly in three aspects.

First, field experiments can provide data that would be inaccessible for observational study, i.e. much richer information. For example, in the 2014 study, Airbnb was unwilling to provide demand information, but the supply information was obtained in the 2017 paper, by analyzing hosts' replies, which inspires us that we could conduct a field experiment based on the 2014 study, where we could ask potential tenants about their demand. Besides, we can conclude on the digital discrimination on both buy side and sell side on Airbnb when we combine the results from two researches. We cannot have a comprehensive understanding on the whole market with just one of them.

Second, the external validity of the field experiment can supplement the lack of external validity of the observational study. That is, since the 2014 study is an observational study, its scope is nothing beyond the condition of July, 2012 in NYC on Airbnb. However, along with the 2017 paper, which was conducted on a wider range of cities, we can infer that the result from 2014 paper could be extend to a larger extent (e.g. other cities).

Third, we can extract information about drifting. Two researches were conducted in different time frame, so the drifting pattern of digital discrimination can be seen when we compare two studies. This could have not been done with only one of them.

### Digital survey study 

Since the observational study and field experiemt provide few understanding about the casual relation in digital discrimination, especially people's internal states when making these decisions, a digital survey study can be introduced to investigate potential reasons for digital discrimination. 

####Data and survey design
We plan to conduct a survey study for people who is currently looking for rental information on Airbnb. People who is using Airbnb.com could see the pop-up window once they log into Airbnb.com. As an incentive, each person who finished the survey would be provided with an Airbnb coupon with random value from \$1 to \$10. We are especially interested in people's thinking when making these decisions so we designed our questions accordingly. Questions are all closed survey questions. Closed questions possess many characteristics that we want, such as easy to analyze and quick for respondents to answer.

Example of intention questions are:

1. If the apartments are similar in location, decoration and other aspects, whose apartment would you choose? 

	Host 1, white, male\ Host 2, African American, male\ Host 3, white, female\  Host 4, African American, female 
	
2. What makes you choose your host?

	Race\ Gender\ None above\ Not willing to answer

3. Based on your Q2, what do you think that might be related to your answer?

	Safe\ Rich\ Trust\ Risk\ Not willing to answer

Examples of demographics questions are:
 
1. Are you male or female?

	Male\ Female
	
2. What state do you live in?
	
	Dropdown with states; including District of Columbia and "None of the above"

3. What is your race or ethnnic group?

	White\ Black\ Hispanic\ Other
	
####Drawbacks and solution
One thing we could anticipate is that there are a amount of people who is unwilling to disclose their preference given the survey question above, especially when it is related to racial issue. Another thing is that when participants know that they are in a survey study, they might alter their behavior and act in a way that is expected by the majority. 

For the first problem, we could solve it by designing our questions in a more implicit way. That is, there are many other factors that indicate one's race, so instead of listing hosts' race, we could say that the host grows up in a neighborhood, and the neighborhood is a black neighborhood or present pictures of similar apratments with hosts' photos coming from different races, then ask questions inductively and implicitly.

The second problem can be solved by gamification. A good example is Friendsense, a survey that was packaged as a game on Facebook. So we could design a game on Airbnb and ask "Which is your next dream destination?", along with pictures of similar apratments and hosts' photos coming from different races. The frequency of this kind of questions should be controlled in case that participants realize that they are in a survey study. 
