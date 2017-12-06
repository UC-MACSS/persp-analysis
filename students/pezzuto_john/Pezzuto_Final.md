# MACSS Perspectives Final

## Racial Discrimination in the Sharing Economy: Evidence from a Field Experiment

### Research Design

**Summarize the Research Design**

This study uses a field experiment to study racial discrimination on Airbnb. The experiment was conducted by taking all Airbnb listings in 5 cities across the United States. The experimenters created 20 accounts on Airbnb identical in all respects except for the name (no pictures were used). Of these 20 accounts, 10 were given distinctly African American names and the other 10 were given distinctively white names. Of the 10 names for each race, 5 were male and 5 were female. The names were based on the frequency of names from birth certificates of babies born between 1974 and 1979. The name list was then validated by a survey that had participants quickly categorize each name as white or African American within 3 seconds to confirm the names signaled race. 

Hosts were randomly assigned to one of the 20 accounts. Approximately 6,400 hosts were sent messages in July about availability of a certain weekend in September. Hosts were contacted only once in the experiment. When a host replied, a personalized reply was sent back to reduce the likelihood of the host holding inventory for a hypothetical guest. Host’s with pictures had their race, gender, and approximate age determined from their profile pictures via workers on Amazon MTurk. Host’s replies were categorized in 1 of 6 groups: “‘No response’ (if the host did not respond within 30 days); ‘No or listing is unavailable;’ ‘Yes;’ ‘Request for more information’ (if the host responded with questions for the guest); ‘Yes, with questions’ (if the host approved the stay but also asked questions); ‘Check back later for definitive answer;’ and ‘I will get back to you.’” (7). Results were conducted from this information

**Leverage Computational Methods**

•	The experiment used the collaboration element Amazon MTurk to quickly perform menial tasks like discerining the race of the hosts efficiently. 

•	The researchers used automated tools which logged into their accounts and communicated with hosts. 

•	The researchers also used FACE++, which is a face-detection AI to categorize past guests by race, gender, and age. 





### Effectiveness of Research Design

I found this paper to be very effective at setting out what it was trying to prove. The aim of this paper was to discover whether racial discrimination was prevalent on Airbnb, and the researchers attempted to prove this by changing names and controlling for everything else. The limitations of this paper are some things that they are not able to claim with certainty (e.g. how pictures would affect this study or how guests with multiple reviews would fare) although preliminary evidence seems to suggest that this these types of variables would not have so much of an impact. The more significant limitations of this study are that the results cannot identify whether the discrimination is based on race, socioeconomic status, or a combination of the two. However, it does the findings go away when the hosts have had previous African American Airbnb guests suggesting that there is deeper discrimination at play.

More generally speaking the positives of experiments tend to be that they have control of variables and the fact that they are replicable. This study showcased that by only allowing the names to be changed, and the method could likely be replicated to find the same results. 

One disadvantage of this design that the messages that were sent out en masse were all the same, and all came from a profile without pictures or more information. This may have seemed artificial to hosts which is a common fault of experiments.

In regards to *Salganik's characteristics of big data* the experimenters do a good job utilizing the big aspect of big data by contacting thousands of hosts. Because this experiment was intentionally studying Airbnb I do not think bad characteristics like non-accessibility, incompleteness, & non-representiveness were very detrimental to the experiment. 

I think the experiment was statistically valid because the regression yielded informative helpful results. The internal validity was high because experimenters cross validated assumptions like race with multiple MTurk workers. As far as I know the experiment was properly randomized. It is hard to comment on the construct validity of the study as it is not based on theoretical assumptions. However, the authors note at the end that it cannot support any theoretical literature on discrimination (17). This study seems high in external validity because the results seem similar to the findings on other profile websites that the authors cited. The conditions of this study were randomly distributed which is supportive of the causation that the authors inferred. 



## Digital Discrimination: The Case of Airbnb.com

### Research Design

**Summarize the Research Design**

This was an observational study. The research question of this study was to determine the magnitude of racism on Airbnb. The researchers collected information about New York City Airbnb landlords on July 17, 2012 to make their own dataset. The dataset included pictures of the landlords, rental prices, and information about characteristics and quality of their properties. The researchers used MTurk workers to examine photos of the property and rate the quality of each listing on a seven-point scale so that researchers could control for the quality of the apartment as observed by potential tenants on the Airbnb site. The researchers also hired other workers through Amazon MTurk to code the race of the hosts as either Black, White, Hispanic, Asian, Unclear but Non-white, Multiple Races, Not Applicable, or Unclear/Uncertain.

**Leverage Computational Methods**

•	Since the researchers stated that Airbnb was not willing to work with them for this experiment, the researchers likely created their dataset through webscraping. 

•	The researchers also used Amazon MTurk to go through a lot menial tasks like determining the race of hosts and determining the quality of properties


### Effectiveness of Research Design

I would consider this a very effective research design to determine price differences between black, and non-white, Airbnb landlords. The researchers were able to control for all attributes that are readily observable to potential tenant browsing listings on Airbnb, which in my opinion, makes this observational study statistically valid. One weakness of this study was that researchers were not about to infer anything about the type of discrimination (taste-based or statistical discrimination). The results could also be confounded if black people do not share their photos on Airbnb, because this study only looked at users with Airbnb photos. This study was limited to only looking at the supply of hosts on Airbnb and did not factor demand.

Generally speaking, observational designs like the one used in this study are preferred when people can’t use questionnaires and interviews to gather data. The observational design in this study was advantageous, because it is like Airbnb hosts would not likely want to answer surveys. 

In regards to *Salganik's characteristics of big data* this experiment can be defined as being big and non-reactive (the always-on was not relevant). However, as this experiment may have struggled with incompleteness, & perhaps some degree of sensitivity, if the results were to leak (though most of the information seems to have been publically available). As mentioned in the paper, Airbnb was not receptive to working with the experimenters about the “demand side” of the model, so the researchers did face challenges with inaccessibility as well. 


This study did not attempt to prove causality. There were no treatment effects.


## Evaluating the Papers Together

### Value-Added of Conducting Both

Both studies set out to prove different things. From the field experiment we learn more about the causality of having a black name on Airbnb, but no information about being a host. The field experiment is more focused on the demand side of Airbnb. In the observational study, data is collected about hosts on Airbnb. There is no causality inferred. Creating an experiment that involved being a host on Airbnb would be able to show more information about causality, but would not be considered unethical because people would be mislead about having a place to stay and likely Airbnb would be very upset with researchers.

Generally experiments tend to have more internal validity than observational studies because of the amount of control they have over their factors. However, observational studies tend to have more external validity because they are less artificial than experiments. Since both of these studies look at discrimination on Airbnb, together they alleviate some of these stresses that the studies would have individually.


### Conducting a Survey

*I initially thought about conducting a survey on Airbnb users who made reviews on the website, but it is not possible. I then though about surveying hosts, but was concerned that some hosts would not answer honestly due to social desirability bias.*

With this is in mind I decide to conduct my digital survey-based research on Amazon mTurk workers who have used Airbnb in the past. The survey would deem to attempt to ask people about their whether they have ever felt discriminated against on Airbnb and if so, pinpoint why they felt this way (e.g. their name, photo, or other factors). It would also ask users about if they felt discriminated against in other aspects of their life (e.g. at the online marketplaces, by Uber or Lyft drivers) see if people feel like Airbnb is different than other online platforms. 

**Strengths of this Approach**

•	Not too expensive. Amazon MTurk surveys usually costs only a few pennies to do, which would likely mean low overhead for the researchers

•	Amazon MTurk is efficient, fairly easy to use, and can survey numerous people quickly, without the hassle of collecting people on the street or in a classroom

•	Informative about how real people, feel about discrimination on Airbnb. Has the potential to be a catalyst for change

**Drawbacks of this Approach**

•	It is possible that there are fewer minorities on Amazon MTurk than on Airbnb, which would be unfortunate because they are a population of interest

•	 Participants may not answer truthfully. Many people on MTurk are only focused on getting paid, rather than answering questions truthfully, and may falsely present themselves as minorities or an Airbnb user


•	People may be uncomfortable answering questions about discrimination

**Overcoming these Drawbacks**

To incentivize people to take the surveys truthfully, survey takers should be paid a little more than other surveys on Amazon MTurk. Also to keep users truthful about being an Airbnb user, perhaps there is some way to confirm users have an Airbnb account by either using some kind of log in system, or perhaps by posting a screenshot or a link to their account name. Amazon MTurk has demographic information about people, and perhaps the survey can be shown to more minorities to keep information more congruent with Airbnb’s population. To stop people from being uncomfortable about the survey should make it very clear that participation is voluntary and not be too prying about details of peoples’ personal lives.


