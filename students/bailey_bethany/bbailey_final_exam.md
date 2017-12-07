
EVALUATING RESEARCH DESIGNS
===========================

By: Bethany Bailey

Paper 1
-------

### 1. Research Design (Paper 1)

#### Summary

In the 2014 paper, "Digital Discrimination: The Case of Airbnb.com,” the researchers compared similar Airbnb listings in NYC with black hosts and white hosts in order to see if there was a price difference in their listings. They were asking whether there is discrimination in the online Airbnb marketplace. They used the listing price difference to operationalize discrimination. They then used regression analysis to determine the average price of each unit by race, and what factors influenced these prices. They found that discrimination in the marketplace existed, as white hosts' listings were 12% higher than black hosts, controlling for the following using observational data from Airbnb's site and human computation methods:

-   Number of bedrooms
-   Shared property vs. not shared
-   Guest ratings
-   Location
-   Listing quality (quality of residence photos)

The data on which the researchers conducted this analysis was a snapshot of the Airbnb listings in New York, NY as of July 7, 2012, including the price, the host characteristics, the apartment characteristics, and review/rating information. They used the pictures of the hosts to operationalize race.

#### Leverage of Computational Methods

The analysis of this data used computational methods. It collected data from an online data source. Though the authors did not explicitly say how this data was collected and analyzed, they likely used computational methods such as web scraping to collect the data and computational data analysis tools such as R or python to evaluate the data.

Additionally, this research used human computation in the form of Mechanical Turk workers to code the quality of the Airbnb rooms and the races of hosts. They had Mechanical Turk works rate rooms on a seven-point scale, from "This is a terrible apartment. I would not stay here at any price" to "This is an extremely nice apartment. I would stay here even if it were a lot more expensive than a nice hotel room." These workers also coded the hosts' races into the following categories: "White, Black, Hispanic, Asian, Unclear but Non-white, Multiple races, Not Applicable (no people in picture), or Unclear/Uncertain".

### 2. Effectiveness of Research Design (Paper 1)

#### What We Learn and Limitations

From this paper, we learn that there is a price difference between similar Airbnb listings with black and white hosts. This difference persists once the researchers control for room characteristics.

However, this research is limited for a few reasons. Below, I outline the strengths and weaknesses of this research, and how it utilizes or fails to utilize the characteristics of big data, measure the heterogeneity of treatment effects and causal mechanisms, and ensure validity of its approach.

#### Characteristics of Big Data

This research had all of the positive characteristics of big data: (1) it was big, (2) it was always-on, and (3) it was non-reactive. The researchers used an online data source with 3,752 observations of each of the above characteristics. Thus, this data is big because it had a large number of participants, but more importantly it had a lot of information per listing. This allowed the researchers to control for many host and unit characteristics in order to strengthen their results. Further, the data they collected were always-on, which might be useful for future studies, such as if the researchers wanted to do a comparative study of discrimination over time. Lastly, the data the researchers collected were non-reactive, meaning that the participants were not aware their data was being collected and could not react to hide discrimination. This also strengthens the results.

The data also had a few negative characteristics associated with big data, which weakened the results. The main characteristics are (1) the data was incomplete and parts were inaccessible, (2) the data may have been non-representative, (3) the data may have been algorithmically confounded, and (4) portions of this data were sensitive.

Though the researchers wanted to do an analysis of unit demand, Airbnb was unwilling to provide information beyond guest reviews; thus, like a lot of big data, some of the data in this research was incomplete/inaccessible. This hindered the researchers' ability to make claims about demand. Further, the researchers did not clarify their selection methodology in their write-up; thus, the data was likely non-representative. On a broader level, the data was non-representative because Airbnb users in NYC are likely not random sample of the public (they might skew younger and more tech-savvy, and likely exclude business travelers). This might cause systematic bias that makes the occurrence of discrimination seem higher or lower than it actually is. Additionally, this data might be algorithmically confounded. We know nothing about the ways Airbnb's platform might have influenced how individuals priced their units. For example, Airbnb might propose a price to hosts based on a variety of factors. Without knowledge about Airbnb's platforms and policies, we cannot determine how much of the price difference is due to race and how much is due to other system factors. Drift would have been a concern if the researchers were interested in measuring changes in discrimination over time, but since that was not their research question, this did not influence their results. Airbnb did not provide this information partially because of the last characteristic: this data was sensitive. Airbnb's proprietary algorithms were not released to researchers likely because they want to keep them from the competition. Further, due to the sensitivity of the topic, Airbnb was unlikely to want to provide additional information, and the user information is personal and therefore sensitive.

#### Heterogeneity of Treatment Effects

In this study, there was not a large enough sample to measure the heterogeneity of treatment effects. The researchers did not ask questions about how prices differ among different types of hosts within the race groups (e.g. do black men receive higher prices than black women, is there a difference in age, etc.)? Thus, this lack of analysis of differences in price among different subgroups is a weakness of this research.

#### Validity

Additionally, though this was not a digital experiment, we can look at the sampling methodology in order to determine whether the results were internally and externally valid. The population sampling methodology in this paper was a snapshot of NYC Airbnb hosts. Though the sample size was fairly large (almost 4,000 observations), the authors did not say anything else about their selection methodology, so it is difficult to say whether they randomly selected individuals to participate in the study or their sample was skewed. Without further information on this, we cannot determine whether the results are internally valid. Additionally, because the researchers only collected data on one city (NYC), these results may not be externally valid. There could be differences in racial attitudes or geographical differences that cause changes in prices in other cities, but this study does not measure them.

Additionally, the construct of discrimination, as measured by Airbnb price, may not be valid in this research. As the authors stated, these apparent differences in listing price by race may actually be the result of unobserved characteristics, perhaps ones that are correlated with race. They attempted to mitigate this by controlling for other listing information. However, I do not think this study effectively argues why discrimination should be operationalized using listing price. Thus, there may be a difference between the construct the researchers are trying to measure (discrimination) and what they are actually measuring (Airbnb price). Because of these validity issues, this study's validity is limited.

#### Causal Mechanisms

We do not learn anything about the causal mechanism behind this price difference. As the authors said themselves, this paper does not analyze consumer demand. Thus, the price could be driven by something other than demand, which could mean that it was not caused by racial discrimination. For example, perhaps white hosts are on average more likely to price their listings higher, and black hosts lower.

#### Overall: Effective?

Overall, this research found an interesting difference in the price of black and white hosts' listings on Airbnb. It does a good job using the positive aspects of big data to strengthen its results. However, on its own, I do not believe it effectively demonstrates discrimination in the online Airbnb marketplace, because of the issues I stated above (not doing enough to mitigate the weaknesses of big data, validity issues, no identification of a causal mechanism, not measuring differences between groups, etc.).

Paper 2
-------

### 1. Research Design (Paper 2)

#### Summary

In the 2017 paper, "Racial Discrimination in the Sharing Economy: Evidence from a Field Experiment," the researchers conducted a digital experiment. In this experiment, the researchers sent inquiries about approximately 6,400 Airbnb listings in five cities (St. Louis, Baltimore, Los Angeles, Dallas, and Washington, DC). They created Airbnb accounts that differed only in the guest name, selecting from two sets of names that suggested blackness or whiteness. They found that African American profiles received positive responses approximately 42% of the time, 8% lower than the rate of white responses (50%). Additionally, the hosts used observational data from Airbnb to dig deeper into this difference, which allowed them to evaluate heterogeneity of treatment effects (see section 2). They found that discrimination was remarkably consistent throughout the population, and varied only slightly when they controlled for age, sex, experience, race, price, location, etc.

The researchers found that the difference in response rate disappeared once they removed hosts without any prior African American guests. They also used data of prices, fees, and fill rates (the percentage of units that were filled) to calculate the average net revenue lost by hosts. This varied from approximately $64 to $98 depending on the calculation method.

#### Leverage of Computational Methods

This research utilized computational methods in multiple ways. First, the researchers hired Mechanical Turk workers to determine the hosts' race, gender, and age. Utilizing this human computation allowed the researchers to analyze a larger set of data than they could if they were coding each host by hand.

The researchers used computational data collection and analysis tools. The response was measured computationally by collecting host responses and other data using web scrapers. The treatment was also delivered computationally, because the researchers sent the inquiries using automation tools. The randomization of treatment assignment was also conducted computationally. This experiment was designed from the ground up (from host selection to analysis of treatment effects) using computational methods.

### 2. Effectiveness of Research Design (Paper 2)

#### What We Learn and Limitations

This digital experiment demonstrated that hosts are significantly less likely to respond to guests who have a typically African American name than guest with a typically white name. This experiment was much more effective than the observational study at producing valid results and identifying discrimination as a causal mechanism in response rate. However, it is limited in its ability to identify why hosts respond less to black inquiries, and has limited application to other online and offline marketplaces with different structures.

#### Characteristics of Big Data

The data the researchers collected was strong for three main reasons: (1) it was big, (2) it was always-on, and (3) it was non-reactive. First of all, the data was big - it consisted of inquiries into 6,400 Airbnb listings in five cities, in addition to observational data on each of the listings and hosts. This allowed the researchers to compare responses among different subgroups, which I discuss in more depth in the heterogeneity of treatment effects section. Additionally, the size of this data allowed the researchers to detect a relatively small difference (8%) that may not have been apparent using a smaller population. It allowed them to control for many factors, including previous guests, which made their case for discrimination as the cause of non-response more solid. Because the observational data the researchers' used to supplement their analysis was always-on, they were able to travel back in time to find whether hosts had hosted previous African American guests. This greatly strengthened their results because it showed that discrimination is the most likely cause of the difference in response rates. The always-on nature of this data also allowed the researchers to see how many residences were occupied on the date after which they inquired. Thus, they were able to use this to measure the net revenue lost by each host through discrimination. These data were non-reactive in that the participants were unaware their data was being collected; thus, they could not change their behavior because they were participating in a study.

However, this data also had some of the common weaknesses associated with big data. Mainly, it was potentially non-representative of the overall population of the United States, because individuals have different likelihoods of utilizing Airbnb. It was potentially algorithmically confounded. As previously mentioned, these researchers could have missed information on Airbnb's policies and algorithms that might influence the likelihood of hosts to respond to certain messages.

#### Validity

The results of this digital experiment have high internal validity. The researchers randomly assigned hosts to 20 guest accounts, and all were sent with approximately the same time frame. Because the sample size was large and the treatment assignment was random, these results are likely true for this population. Since the treatment was delivered and the results were collected and processed using automated tools, the treatment and outcome measurements were reliable.

Further, this experiment has high external validity for a digital experiment, with caveats. The data was collected on five different and diverse cities; thus, this data would likely generalize to Airbnb in other cities. However, it is not clear whether the Airbnb population is representative of the overall population; thus, like the previous observational study, this study may not be fully generalizable to the entire US population. Further research in additional cities using other messages on diverse marketplaces is necessary in order to determine external validity.

There were two main constructs in this study: (1) race, as measured by names and (2) discrimination, as measured by non-response rate. The authors make a compelling case for using names to signal race, citing Bertrand and Mullainathan (2004) and their own survey to verify that people categorized each name as white or African American. This construct has strong construct validity. The response they were measuring, how the host responded to the inquiry, operationalized discrimination. This is a clear measurement of the theoretical construct of racial discrimination because it matches the definition of discrimination closely (the difference in treatment of different races); thus, I believe this construct has high validity as well.

#### Heterogeneity of Treatment Effects

The researchers had a large pool of host participants and a lot of information on each of the hosts, which enabled them to measure different responses to the same treatment among different groups. They found a persistence of discrimination among different types of hosts (male/female, black/white, experienced/inexperienced, young/middle aged/old), guests (male/female), and property types (whole property/shared, high price/low price, diverse/homogeneous location, desirable/less desirable). They found that hosts who had no previous African American guests were much more likely to discriminate against black names; in fact, once they removed these hosts, discrimination disappeared. Thus, the amount of information that the researchers had on each participant allowed them to move beyond the average level of discrimination and ask questions about how it varies among groups and what causes it.

#### Causal Mechanisms

The researchers stated that they could not "identify the mechanism causing worse outcomes for guests with distinctively African American names" (17). Since previous research shows that black names are often associated with lower socioeconomic status, the reason for the lower response rate could be due to the lower SES associated with the name, or a combination of factors. However, when the researchers removed hosts who had no previous black guests from their analysis, the rate of responses to black and white guests equalized. Thus, this suggests that racial discrimination is the main factor in the lowered response rate. The researchers were able to conduct this analysis because they had both data collected from a digital experiment and additional observational information on the participants.

This research does not identify why hosts are likely to discriminate against black hosts. Further research, such as a survey, that studies hosts attitudes would be necessary to determine this causal mechanism.

#### Overall: Effective?

I think this paper was much more effective than the previous observational study at measuring discrimination at Airbnb for a few main reasons: (1) the operationalization of discrimination was clearer (whether the inquiries received a positive response) and had a more direct relationship to discrimination, (2) the researchers had a larger sample size across many cities, so the research is more externally valid, and (3) by using an experiment, the researchers were able to identify differences in treatment effects and more convincingly identify race as a causal mechanism.

3. Better Together: Observational Study and Field Experiment
------------------------------------------------------------

Utilizing both an observational study and a field experiment allowed the researchers to learn more than they could have using just one of these methods. Each method added to the other in the following ways: (1) the researchers were able to observe behavior in the uncontrolled "real world" as well as control the behavior and response; (2) the researchers could collect information in the digital experiment that they would not have been able to collect with only an observational study; (3) the researchers were able to identify clearer causal mechanisms and potential confounders by using both methods; and (4) using two methods strengthened the validity and credibility of the results through iteration. The weaknesses of an observational study, such as a mismatch between theoretical constructs and missing data, were minimized in the digital experiment because these characteristics are strengths of a digital experiment. In contrast, the weaknesses of a digital experiment (mainly, the potential lack of generalizability) were strengthened by conducting an observational study in addition.

### Controlled vs. Natural Environment

First of all, conducting both a controlled experiment and observing individuals in the natural Airbnb environment added greatly to the understanding of discrimination in this online marketplace. By conducting an observational study in addition to the field experiment, the researchers demonstrated that discrimination occurs in natural settings as well as in a controlled environment. In the observational study, there may have been factors other than race that influenced the price of units. However, the experiment generated results that suggested the same mechanism, discrimination, was at play in Airbnb while controlling everything about the message other than the signaled race. Thus, nothing else could influence the host's likelihood to discriminate. The experiment strengthens the clarity and verifiability of the results, whereas the observational study shows that the results persist in uncontrolled, everyday situations.

### Different Types of Information

Additionally, by conducting the experiment in addition to the observational study, the researchers were able to collect information that they could not directly observe using found data. In the first study, the researchers were unable to access all of the hosts' previous communications with potential guests; thus, they could not use this data as part of their observational study. With the observational data they had access to, the researchers could only ask whether race affected the prices on Airbnb, which was a measure for the presence of discrimination. By conducting an experiment, the researchers were able to gain access to different data in order to ask a slightly different question that built on the first findings; that is, whether the race of potential guests affected the likelihood they were responded to (also a measure of discrimination).

### Causal Mechanisms and Confounders

One of the weaknesses of the observational study was its inability to control for all possible confounders and identify a clear causal mechanism for the price difference. By conducting the digital experiment, the researchers were able to more concretely identify the causal mechanism behind different responses (that is, race). They were able to randomly assign groups in the field experiment, which minimized the potential effects of confounders. This built on the observational study which showed that some sort of discrimination was happening in the Airbnb marketplace.

### Iteration: Strengthening Validity

Because they used two different operationalizations of the discrimination construct (price and response rate) and achieved similar results, the validity of the researchers' results was strengthened by utilizing the two methodologies. One of the issues with both digital experiments and observational studies is reproducibility. It is difficult to say whether the results of a study are a result of the population sampled, the data collected, or an actual outcome of the treatment/construct measured. By conducting two studies that used different methods and asked slightly different questions that measured the same construct and getting similar results for both, the external validity and construct validity of both studies were made more concrete.

4. Survey Research
------------------

### Design

As the researchers did in the field experiment, in designing a survey to answer the question: "Does discrimination occur in the Airbnb marketplace?" I would use a computer program to randomly choose hosts from the pool of all hosts. Using the same message for all hosts, I would request that they participate in a survey about guests. I would do the same thing for the pool of guests on Airbnb.

In this survey, researchers could ask questions such as the below:

1.  If a potential guest is African American, how likely are you to accept their request for a room?
2.  If a potential guest is white, how likely are you to accept their request for a room?
3.  Would you accept a guest with the name \_\_\_\_\_?

Additionally, researchers could use computational survey methods, such as an Ecological Momentary Assessment. With the help of Airbnb (potentially using the Airbnb app/website), researchers could ask hosts to answer questions throughout the day. This would allow researchers to ask more questions over a longer period of time. Also, researchers could ask questions at times that were relevant to the research. For example, if a host responded to a request for a room, researchers could ask them questions about their response, for example:

1.  Why did you reject/accept that potential guest?
2.  Was race a factor in your acceptance/rejection of that potential guest?

Similarly, if guests were using Airbnb and scrolled through different rooms, researchers could ask them questions about why they did or did not choose to stay in those rooms.

A final component of the survey would be semi-experimental - throughout the day, researchers could present hosts and guests with potential guests/units (varying by race and little else) and ask them if they would be willing to host them/stay in the unit. Researchers could add questions about the prices at which they would be willing to host the guests/stay in the unit.

### Benefits

Conducting a survey to analyze discrimination in Airbnb could allow researchers to find out more about the causal mechanism behind discrimination. Asking questions could reveal something about the internal states of participants, and why they discriminate. For example, if researchers followed up the digital experiment with a survey of the participants, they may be able to clarify the relationship between SES and race, and how it played into hosts' decisions not to host black participants. If SES was unrelated to this, they may be able to determine other reasons why the hosts react negatively to African Americans through a series of questions.

### Drawbacks

However, survey research has drawbacks that would be present in this study. The most obvious potential complication is the validity of the responses. Because discrimination and race are both touchy subjects, the hosts and guests might lie or under/over report incidents of discrimination. Further, there may be a response bias. For example, hosts who discriminate more often may not want to participate in the study because of the stigma associated with discrimination. Thus, less discriminatory hosts might be overrepresented in the population that responded, which could skew the results.

Additionally, any survey design could have issues with measurement and the questions asked. Discrimination is a difficult concept to operationalize in any research. In surveys, the choice and order of words matters greatly, and responses could vary due to the specific questions. Thus, in any survey to measure this topic, it would be difficult to determine whether researchers were actually measuring discrimination or some other construct.

Finally, the cost of conducting survey research is often high and might be prohibitive. In order to get individuals to participate, researchers may have to incentivize them, which quickly becomes expensive with a large number of participants. If researchers wanted to conduct an EMA, they might have to design a phone application, which could be costly. Overall, these three drawbacks of the survey design (validity/representation, measurement/questions, and cost) make it difficult to measure this construct using only a survey.

### Overcoming the Drawbacks

The most obvious way to overcome the drawbacks of a survey design would be to run a survey in combination with other methods, such as the observational research or digital experiment discussed in this paper. This would help verify the validity of responses and point out further potential research. However, in the absence of this approach, researchers can attempt to overcome the three main drawbacks in the below ways.

In order to maximize the validity of responses, researchers could compare survey responses to the actual actions of participants (e.g. if a host says they would host a black participant, do they have any history of doing so in practice?). Additionally, researchers could take steps to ensure confidentiality, such as encrypting data and anonymizing results, and communicate these steps to participants to lessen the effect of stigma. In order to overcome non-response, researchers could incorporate our survey with existing programs already used by participants and spread the survey out over participants' lives by hosting it in the Airbnb app/website or using an EMA format.

In order to overcome issues of measurement and question formation, researchers could do a few things. First of all, researchers could ask questions in multiple different ways and compare the results of the different questions to ensure that they are not influenced by order language. Researchers could ask questions in the form of a wiki survey with only a few answers available to each individual at a time. This would help measure small differences in the ways people discriminate.

To overcome the issues of cost, researchers could skip the EMA and conduct a survey using Mechanical Turk workers, asking them how they would respond to potential guests/hosts. If they wanted to do a survey of actual Airbnb participants and utilize an EMA but this was cost prohibitive, they could partner with Airbnb and use existing technology to find participants and host the survey.

Conclusion
----------

In conclusion, these two studies, one using observation methods and the other using an experimental design, measured discrimination on Airbnb and contributed to a better understanding of discrimination in the online marketplace. Though the digital experiment provided a more concrete and clear measurement of the discrimination construct, both studies found compelling results about host and guest behavior on Airbnb. Taking a survey approach to this research would be most helpful if it supplemented these other methodologies; otherwise, it would be difficult to achieve significant results due to the sensitive nature of discrimination. Overall, reviewing these three methods shows that all of them have flaws, and using them in conjunction with one another can help to overcome their weaknesses.
