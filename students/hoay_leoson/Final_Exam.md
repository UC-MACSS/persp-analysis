### MACS30000 Final Exam
### Evaluating Research Designs
#### Leoson Hoay
#### December 6, 2017


## Contents
* [Summarize Research Designs](#summarize)
* [Evaluate Research Designs](#evaluate)
* [Value](#value)
* [Digital Survey-Based Research](#digisurvey)
* [References](#references)


## <a name = "summarize"></a>Summarize Research Designs  

### Observational Study (2014)
The authors' objectives were to study digital discrimination using the Airbnb platform. The dataset was obtained as a snapshot of New York City listings on Airbnb, alongside pictures of the landlords. The data included other information such as location, reviews, and photographs. By performing a regression analysis on price and the factors involved, the authors examined the relationship between price and these factors - the most important one being race. To code for the race factor and the quality of apartments, the authors hired workers on Amazon Mechanical Turk (MTurk) to code the race of hosts based on their profile pictures, and the quality of the apartments based on the photos provided in each listing. 

In this observational study, the authors designed their analysis to capture information that was readily available from Airbnb about hosts and listings. Even though there were some information that the authors hoped to obtain from behind closed doors, such as demand information - "Airbnb was not willing to share data for this project" - the information that was openly available was plenty with regards to their core question of examination: the role of race in listing prices. The data also included other convenient information such as location, reviews and property photographs. 

The above demonstrates the authors' use of the always-on, large dataset of Airbnb listings information on the website. While I am unfamiliar with the exact processes of how the data was pulled off the site, it is clear from the authors' description and screenshots - using Airbnb's search engine - that the snapshot data was not difficult to obtain. Also, Airbnb boasts a large dataset of listings - 300,000 as of 2013 - which means that the authors were able to muster computational resources to handle large N-data, which increases the power of their study with regards to detecting significant effects.

The authors also made use of human computation to handle data processing and cleaning - via the MTurk platform, which allowed them to outsource large-scale and repetitive tasks such as the coding of host race and apartment quality to inexpensive, readily available workers online.

### Field Experiment (2017)
In this study, the authors' objectives were to determine if applicant race had an effect on the acceptance rate by apartment hosts on Airbnb. 6400 listings across five cities were sampled from available listings, and the researchers created 10 accounts with "distinctively African-American names" and another 10 with "distinctively white names", from which applications were sent out to the sampled hosts - not repeating requests to any host to account for host specific differences. These names were validated using a pilot survey that asked participants to categorize the names to a race in a quick-response paradigm. The effects of guest race, along with other factors were then analyzed against the rate of positive responses from the hosts. While the authors utilized MTurk to code the other variables such as host race and gender given the accompanying profile pictures of the hosts, they used past review data to estimate if hosts had accepted African-American guests before in recent times. The latter was achieved using a software known as Face++ to categorize guests by their photographs.

Like the observational study, the authors captured information that was readily available from Airbnb via scraping methods and browser automation tools. This enriched dataset allowed them to consider a variety of factors other than race in their analysis. The authors also made use of human computation methodologies in the form of MTurk, to perform the similar tasks of coding host photographs into variables. 

In addition to the above, this study also employed Face++, a face detection API to assist them with categorizing guests. This API has been used by a number of prominent companies including Alibaba, Lenovo, and Meitu([1]).


## <a name = "evaluate"></a>Evaluate Research Designs Independently 

### Observational Study (2014)

It is difficult to estimate causal effects in this study since there was no full control by the researchers over extraneous variables nor was there any researcher intervention. However, this study took advantage of the characteristics of "big data" that was available on Airbnb's website, and transformed it into its own merits. First, the study utilized a snapshot of what should be considered a very large set of data. This, as briefly mentioned in my above sections, makes this data very useful for estimating effects that might be small in size, and only revealed by a study with sufficient power. In this case, while it is not known whether the estimated effect of host race on pricing should be "small" or otherwise, a large dataset boosts the power of the analysis. In addition, given that this snapshot is a wide coverage of Airbnb as a platform, the ability to process such a large dataset is a boon to the study's internal validity.

While it is arguable that the study utilized and collected some possibly "sensitive" data - e.g. photographs of home units and hosts and extracted inferred data from them - I believe that the ethical concern here is minimal based on the principle of Beneficience. Given that the photographs and listing data are themselves publicly accessible as residential market information, and that the results from this study will shed light on and benefit the movement to minimize racial discrimination, it is reasonable to state that the benefits outweigh the potential risks.

Another major benefit of this study that pertains directly to its question of interest is its use of non-reactive data. It is definitely imaginable that once the processes of the study are made known to reactive subjects, these subjects would change their behavior, or the system proprietor will make adjustments to the system itself, based on the knowledge that they are being observed.

A drawback of the study is as already mentioned by the authors in the paper - the inability to incorporate demand-side data in order to account for the market economics of the Airbnb system. However, given that this was data locked behind the corporate gate of Airbnb, I believe that the authors made sufficient consideration given the data that was available to them. In order to approximate the demand patterns on Airbnb, a more complex time-window study such as that used in Hanley and Thompson's 2017 Wikipedia Study([2]) could be conducted in the future.

A second drawback, also mentioned by authors in the paper, is that it is difficult to completely disentangle statistical discrimination and taste-based discrimination. 


### Field Experiment (2017)

In determining whether hosts discriminate against guests based on race on Airbnb, the study does well using the experimental method, by nature of being able to control for extraneous variables. I believe that the authors were thorough both in controlling for variables as well as in validating the methods employed. An example will be how the race-specific names were chosen from actual birth certificates - one may still definitely question the "distinctiveness" given that the names were chosen from certificates from 1974 to 1979 - and the authors went on to validate this list using an additional pilot survey to make sure that the method was valid. Another example is the fact that the authors decided to also consider past review data as a proxy of a measure of acceptance towards African American guests by each host.

Given the above, the experiment should have strong internal validity, as most sources of variability are part of what the researchers are already controlling for. The randomization of groups alongside the consideration of past review data should also minimize participant-side characteristics that may contribute to group hetereogeneity. Possible sources of worry are the performance of Face++ - which has a strong customer base, and thus can be inferred to have a reliable algorithm - and of the MTurk workers in terms of the quality of their task performance. But given that the tasks are not explicitly complex ones, this problem is probably minimal, if not moot.

There is definitely something to be said about incompleteness and the generalizability of the results. It is definitely possible that the relatively smaller sample size and the confinement of the listings to five cities results in some level of incompleteness, and in turn reduces the generalizability of the results to other kinds of settings - for example, other housing ecosystems, other types of online markets. However, as mentioned in my third assignment for this course([3]), the generalizability of this study is "as generalizable as the boundaries imposed by the data of interest and the measurement sample." In the case of this particular study, the authors were explicit in the boundaries and scope of the results - although this field experiment may not necessarily serve as a definite indicator of "evidence of racial discrimination" in all sharing economies.

The is a possibility of some system drift creeping into the study results, given that Airbnb was seemingly aware of the data collection processes that had been going on, and were also themselves becoming concerned with issues of discrimination within their system. Because of this reason, it might be the case that adjustments were made to its platform that affected how the data was being presented or that addressed some process that abetted racial discrimination, while this study was still going on.

Ethics is of some concern here in this study, as the methods used in this study involved contacting hosts directly, who were unaware of their participation in the study. Although the principle of Beneficience can once again be invoked to justify the study's risks based on its potential beneficial outcomes, the risks involve interfering with a person's desire to sublet or rent his or her apartment, and also his or her emotional and temporal investment in interacting with the dummy requester. Although the researchers attempted to "reduce the likelihood of a host holding inventory" for a requester, is it likely that invested Airbnb hosts will do so to some extent. 


## <a name = "value"></a>Value Added By Conducting Both Studies   

The differences in methodology in the two studies allow their results to illuminate different aspects of racial discrimination in the home sharing economy. Although both studies focus on Airbnb as a platform, they differ qualitatively in their inferences on three main aspects, thereby complementing each other.

The first difference lies in the angle of approach - while the observational study focused on the relationship between host race and price, the field experiment focused on the effects of applicant race on their likelihood of receiving a positive response from a potential host. The first study benefits from being designed in an observational manner, because apartment hosting habits are highly likely to be affected by reactive characteristics - it is difficult to design an experiment in which one can manipulate the variables in a way that does not in itself become a factor for the observed differences. Moreover, if we were to replicate dummy hosts - as with dummy requesters in the field experiments - it is arguably more unethical to deceive potential homestay guests, both from a utilitarian and virtue-based standpoint, and perhaps even illegal if it were to violate Airbnb's terms of service. Thus, the observational study tackles the supply and pricing aspect of the issue adequately, while the experiment was well suited to studying the actual behavior of a subset of Airbnb's hosts.

The second difference lies in the magnitude of data being studied. Due to constraints, the field experiment was understandably not able to incorporate as large a dataset as the observational study. As such, while its control over variables allows it to measure causality, it does so within a narrower playing field. The observational study, which draws less on human participants, allows it to take into a account a larger dataset at a lower cost, creating a larger study domain. While the experiment will spur on future replications and differing-context studies in order to confirm domain specific effects, the observational study's results can be taken more generally as a correlation that applies to the Airbnb market as a whole, at least for the specific time period at which the data was retrieved.

The final difference lies in the nature of the inference being made. As mentioned previously, the field experiment is able to make causal inferences - in this case, between the race of potential guests, and their likelihood of receiving a positive response from a host. This can be used to design specific interventions or to ground theories regarding the causal mechanisms that underlie racial discrimination in this specific domain. While this is not as feasible with the observational study results, the results from the observational study can be used to predict trends or estimate Airbnb pricing models, based on the relationships found between race, the other variables involved, and the price variable.

It may be tempting to claim that the experimental method provides more advantages than the observational method, but as we can see from the above, they can work in concert to generate a fuller picture of the issue being studied. Moreover, the observational method in this context allows one to draw from always-on data and previously archived data by researchers or agreeable companies - making future iterations of similar studies that aim to make backward comparisons, or future longitudinal studies that require the use of historical data, very much possible.


## <a name = "digisurvey"></a>Potential Digital Survey-based Research Design
Given the above analysis of the studies already conducted, I would propose a survey-based research design that seeks to find out if there is a correlation between host race (Black or White), and the measured likelihood of a Airbnb guest of applying to the apartment, operationalized as a survey question.

The design of the study will involve embedding a survey - in a form similar to ecological momentary assessments - onto the Airbnb website. The link to the survey will appear as a sidebar if a participant just booked a BnB from a host that is has been classified as being White or Black. Deception will be employed in the form of masking the intention of the survey - it will state that given the participant's recent booking, it would like to run a survey on the types of units that are popular with users. The participants, if agreeable will then be taken to a dummy profile that replicates almost entirely the listing of the one the user just booked, except a few changes to the details such as address and arrangement of photos, and most importantly, the apparent race of the host - which will be White if the user recently booked from a Black host, or Black if the user recently booked from a White host. To complete the survey, the user simply has to indicate on a Likert scale the extent to which the user would have been interested in this apartment if it was available.

The first potential drawback is the difficulty involved with collaborating with Airbnb in order to run the survey. As observable in the two papers studied above, it is likely that Airbnb will be reticent in allowing researchers to tamper with the experience of their site, unless it is shown that there is significant mutual benefit involved. It may be wise to first enter into talks with Airbnb to find out if racial discrimination in the sharing economy is a high-profile concern within their organization, and if so, propose how such research will be beneficial to both the continued development of a more equitable site experience, as well as for their company image.

The second potential drawback has to do demand characteristics and social desirability bias. Some participants may be able to guess the intention behind the survey - and even if they do not, may have their answers trending towards a favorable one due to the innate desire to appear unbiased. To minimize this problem, some effort and resources must go to the user interface (UI) design of the survey to make it seem as native to the Airbnb platform as possible, and approximate the general outlook of a non-intrusive advertisement. To entice participation, a lucky draw could be included for participants of the survey as a form of incentivization.


## <a name = "references"></a>References 

- Edelman, B. G., & Luca, M. (2014). Digital discrimination: The case of airbnb.com. Harvard Business School NOM Unit Working Paper, (14-054).
- Edelman, B., Luca, M., & Svirsky, D. (2017). Racial discrimination in the sharing economy: Evidence from a field experiment. American Economic Journal: Applied Economics, 9(2), 1-22.
- Thompson, N.C., Hanley, D. (2017). Science is shaped by wikipedia: Evidence from a randomized controlled trial. MIT Sloan School of Management Working Paper 5238-17.
- Salganik, Matthew J. (2017) Bit by Bit: Social Research in the Digital Age. Princeton, NJ: Princeton University Press. 

[1]: https://www.faceplusplus.com/
[2]: http://www.nature.com/news/wikipedia-shapes-language-in-science-papers-1.22656
[3]: Assignment_3.md




