# Final Exam

### Tyler Amos
### MACSS 30000
_December 6 2017_


## Independent Evaluation: Paper 1

#### Edelman and Luca, 2014. _Digital Discrimination: The Case of Airbnb.com_ 

### Summary of Research Design
_How does the paper use computational methods to ask and answer a question?_

The 2014 paper from Edelman and Luca applies an observational approach to data on accommodation listing data collected from Airbnb.com for New York on July 17, 2012. (Edelman and Luca 2014, "About Airbnb") To this 3,752 observation corpus, the researchers apply human computation techniques to process the data. (Salganik, "Mass Collaboration") Specifically, Edelman and Luca hired Amazon Mechanical Turk workers to code Airbnb data in different mediums (image, text) to build a dataset with the following features: 

  * The price the host is asking;
  * Characteristics of the host;
  * Characteristics of the apartment;
  * Number of reviews left by guests at that property;
  * Average ratings for each host, by:
    * Location;
    * Check-in;
    * Communication; 
    * Cleanliness;
    * Accuracy.
  * Quality of the apartment based on host-provided photos;
  * Race of the host as determined by profile photos.
      
Applying an observational research design (Salganik, "Observing Behavior"), Edelman and Luca seek to estimate differences in rents paid to black and non-black Airbnb hosts. This relatively straightforward design involves a series of statistical procedures (e.g., T-statistic tests) to determine if gaps between mean rents paid to hosts of different races are significant. (See Edelman and Luca 2014, "Tables") For this study, "non-black" is inclusive of all other races. Robustness of this design choice is supported by validating the results of the analysis (non-black and black) against the same analysis with just "white" and "black" racial categories. (Edelman and Luca 2014, "Robustness check")

### Evaluation of Research Design Effectiveness

#### What do we learn from the paper? What are the limitations of the paper?

Using Salganik's characteristics of big data as an analytical framework, we can assess this study on its ability to leverage advantages and mitigate disadvantages of social research with big data. A breakdown of the research design by characteristic follows.

__Salganik's Characteristics - Generally Good for Research__

_Big: Poor_

The total size of the corpus collected by the researchers is 3,752 observations. Depending on the characteristic, data is complete for between 99.8% (Number Accommodated) and 100% of total observations.(Edelman and Luca 2014, "Tables")

While larger than many traditional social science datasets, this is not an especially large dataset. Furthermore, it only applies to one city at one given point in time. Nevertheless, it was a large enough dataset to need human computation for coding observations. Thus, we can conclude the study leverages the "big" in big data to some minor extent.   

_Always On: Poor_

The researchers select a cross-section of data from July 17, 2012, effectively providing a snapshot of Airbnb's marketplace at one point in time. (Edelman and Luca 2014, "About Airbnb") This approach does nothing to take advantage of the always-on nature of big data sources. As such, it is more akin to traditional social science research and its static corpora. 

_Non-reactive: Strong_

In this study, the subjects are already aware they are being observed by potential renters on Airbnb. In fact, it is this behavior the researchers are trying to observe. In other words, it is not the underlying internal state of the individuals the researchers are trying to measure, but their public performance in the marketplace that is Airbnb. Thus, the addition of researchers into the ecosystem of Airbnb and their subsequent observation of subjects in that marketplace would have no impact on hosts' behavior. The researchers were able to identify an existing marketplace which they could observe without changing the dynamics of the system itself. This is a textbook example of Salganik's notion of non-reactivity (Salganik, "Non-reactivity"). 

__Salganik's Characteristics - Generally Bad for Research__

_Incomplete: Moderate_

As regards specific types of incompleteness (Salganik, "Incompleteness"):

  * Demographics:
    * The researchers fill in information based on race by collecting profile photos and having Amazon Mechanical Turk workers code them by race.
  * Behavior on Other Platforms:
    * The researchers do not account for this type of incompleteness. 
  * Construct Validity:
    * Researchers make a number of assumptions in order to map their constructs (race, price, discrimination) onto the available data. Specifically:
      * They assume profile pictures are in fact images of hosts;
      * A difference in asking price is a reflection of a rational, self-aware agent's accurate assessment of their good's market value.

Overall, these assumptions and mitigating measures are reasonable, given the point in time (2012) at which the study was conducted. If it were conducted today, there would likely be an expectation for significantly more advanced methods and mitigation measures. Therefore, we can conclude the researchers mitigated incompleteness concerns moderately well, keeping in mind the standards of the time. 

_Inaccessible: Poor_

Airbnb declined to provide access to their internal data for this paper, and as such the researchers were limited to examining only price data on hosts' listings. As a result, the researchers were not able to analyze demand. (Edelman and Luca, "About Airbnb") While this helps to ensure high amounts of completeness in the data (see "Big"), it risks placing researchers in a position of designing studies to fit available data, rather than finding data to answer their own questions.  In other words, the researchers jettisoned their original research question in favor of a more convenient line of inquiry. Thus we can say this study poorly mitigated inaccessibility risks. 

_Non-representative: Moderate_

This study uses cross-sectional data from one day in one city, as has already been noted. This means, effectively that the data can only be said to represent users of Airbnb at that particular time and in that particular place. Given that the number of Airbnb listings has grown rapidly (over 2,000,000 by November 2015 according to Edelman et al. 2017), the dataset has a strong temporal as well as geographic bias. This research design choice means the individual hosts in the dataset are likely poorly representative of black and non-black individuals in the wider vacation accommodation economy. However, given that the researchers explicitly limit their scope to the digital economy, with a case study of vacation accommodation rentals, they anticipate some of these limitations. Thus, we can conclude the research design moderately mitigates issues of non-representativeness. 

_Drifting: Non-issue_

The researchers do not account for system, population, or usage drift within Airbnb, although they do propose reforms based on their findings (namely, reduce the prominence of hosts' profile pictures). However, given the fact their design is cross-sectional, not longitudinal, it is unlikely that drift of any type would be an issue for their findings. Rather, concerns about drift would only arise when trying to generalize the findings to future research. 

_Algorithmically Confounding: Poor_

The researchers do not encounter substantial issues of algorithmic confounding in their study. They merely observe listings and do not interact with users, creating few opportunities for Airbnb's design choices to influence their results. However, because the researchers did not collaborate with Airbnb on this study, it is not possible to know if algorithms affecting search results did in fact shape data collection. As such, because we cannot be sure if there is algorithmic confounding at play, and given the researchers did not lay out the measures they took to mitigate this risk, it is at best a minor oversight, at worst a source of systematic bias in the data. 

_Dirty: Strong_

In order to clean and sort data into analytically convenient formats, the researchers used human computation techniques to outsource coding to Amazon Mechanical Turk Workers. By doing this, they turned an inconvenient data format, (e.g., profile pictures) into a more convenient format (race codes). Using a large number of human coders leveraged heterogeneity to ensure more accurate results as regards the racial identity of hosts. This approach allowed the researchers to clean a dataset that would have been intractably dirty for themselves or their team, but was in fact quite manageable for a distributed network of "Turkers". Overall, we can say the researchers mitigated risks of dirty data quite well. 

_Sensitive: Unclear_

The only sensitivity risks that clearly emerge from the use of this data are those related to the profile pictures and accommodation details of hosts. These hosts have posted their information for use on Airbnb, and did not consent to its distribution elsewhere (e.g., in the researchers' dataset, on Mechanical Turk). In fact, some of this data can be quite personal (e.g., a photo, an address). The researchers did not describe at any point the steps they took to ensure anonymity of their subjects, nor did they confirm if their Institutional Review Board had reviewed their research. While it is of course possible the researchers did take robust steps in this regard, we cannot pass judgement on this criteria with the limited information provided. 

### Summary of Assessment, Edelman and Luca 2014.

| Characteristic              | Conclusion |
|-----------------------------|------------|
| Big                         | Poor       |
| Always-on                   | Poor       |
| Non-reactive                | Strong     |
| Incomplete                  | Moderate   |
| Inaccessible                | Poor       |
| Non-representative          | Moderate   |
| Drifting                    | Non-issue  |
| Algorithmically Confounding | Poor       |
| Dirty                       | Strong     |
| Sensitive                   | Unclear    |

In conclusion, we can say the 2014 paper from Edelman and Luca, given its limitations and strengths, allows an ecologically valid, largely complete insight into an online accommodation marketplace. Within the population, time, and place the study is framed (online marketplaces, in July 2012, in New York) it is highly representative. It successfully manages to distill noisy data into clear results. However: it is limited in scale; does not offer longitudinal insights; is to some extent driven by data availability; and a number of aspects, such as sensitivity, are not addressed. 

Furthermore, the study only tells us that there is significant difference between the economic benefits (earnings) black and non-black hosts expect to receive from Airbnb rentals. It does not tell us about the causal mechanisms at play. That is best explored through an experiment, as is detailed below. 


## Independent Evaluation: Paper 2

#### Edelman et al, 2017. _Racial Discrimination in the Sharing Economy: Evidence from a Field Experiment_

### Summary of Research Design

_How does the paper use computational methods to ask and answer a question?_

This study explores racial discrimination in online marketplaces for accommodation, specifically, Airbnb. In contrast to previous work by some of the authors, this study uses an experimental approach to uncover causal mechanisms at play in rentals to black and white renters and black and white hosts. 

Using manufactured guest accounts, researchers inquired about the availability of 6,400 listings across five US cities. Guest accounts were identical, except for names, which were either "black" or "white" names, per work by Bertrand and Mullainathan. (in Edelman et al 2017, 2)

Subjects (hosts) were contacted by guest accounts with a combination of 2 out of four treatment variables (male/female, black/white), as expressed through their names. From subjects' reaction, combined with observational data, researchers sought to identify causal mechanism at play in hosts' receptiveness to potential guests. 


### Evaluation of Research Design Effectiveness

#### What do we learn from the paper? What are the limitations of the paper?

Using Salganik's characteristics of big data as an analytical framework, we can assess this study on its' ability to leverage advantages and mitigate disadvantages of social research with big data. A breakdown of the research design by characteristic follows.

__Salganik's Characteristics - Generally Good for Research__

_Big: Strong_

At more than 6,200 observations, and with a substantial number of features, this study leverages the size of datasets available in the digital age to provide detailed information on a large number of guests, hosts, and locations. For example, some features in the dataset were: 

  * Race, gender, and age of past guests at a listing;
  * Race, gender, and age of hosts;
  * Price, number of bedrooms and bathrooms, cancellation policy, cleaning fees and ratings of each listing;
  * Whether a listing was for the entire property or just a portion;
  * Location of the listing, which created a linkage to census demographic information.

_Always On: Strong_

One aspect of the study design was to follow-up with listings which had been inquired about to see if they were eventually rented for the weekend requested by the researchers' fake guest accounts. This approach leverages the always-on nature of big data sources to collect unique data on the consequences of non-rental by hosts, thus shedding more light on causal mechanisms at play in this phenomenon. (Edelman et al. 2017, 3)
 

_Non-reactive: Strong_

Although this study design was meant to engage with subjects (as an experiment), it also employed some of the advantages of non-reactivity in big data sources. For example, following up with subject hosts after non-rental to see if the unit was eventually rented for the weekend requested. This measure is simple and carries no risk of influencing the Airbnb ecosystem, but provides valuable data. 

__Salganik's Characteristics - Generally Bad for Research__

_Incomplete and Dirty: Strong_

In order to complete and clean data collected by the researchers, they employed a human computation approach. (Salganik, "Mass Collaboration") Put simply, Amazon Mechanical Turk workers coded host profile pictures for race, gender, and age. Leveraging heterogeneity, the multiple workers were assigned to the same image in to guard against and resolve cases of coding conflicts. This ensured high-quality, clean data from a relatively sparse (it is unlikely hosts mention their race in the text of their posting), dirty (some images were not even human) dataset. This approach allowed them to identify and catalogue a great deal more demographic and ancillary information than in their previous observational work. Researchers also used face detection tools to categorize past guests by race, gender, and age. (Edelman et al. 2017, 4) The weakest part of the study design with respect to incompleteness and data cleansing comes with the use of a single research assistant to code responses to requests. (Edelman et al. 2017, 7) This task would have been better performed with a human computation approach, or with automated methods. This would have mitigated any risks of systematic bias on the part of the research assistant. An additional concern which is common to this design and the observational design, is the potentially ill-fitting variables for the constructs the researchers are studying. Please see the relevant section above (Paper 1, Incomplete) for details on this point. 

_Inaccessible: Poor_

The researchers faced accessibility challenges, and in fact this hampered their data collection significantly. Initially, the researchers wanted to collect data from a far larger sample of cities, but found that Airbnb identified and blocked their data collection tools. (Edelman et al. 2017, 4)


_Non-representative: Strong_

This study used data from Airbnb listings in five major US cities, with varied levels of Airbnb markets and in diverse geographic regions. (Edelman et al. 2017, 4) In the case of hosts holding more than one property, properties were selected at random. Regardless of some accessibility concerns, the researchers took reasonable measures to ensure their sample was representative of the population of interest (black and white renters on Airbnb). Keeping in mind that the researchers explicitly limit their frame to African Americans and Caucasians, we can say that the sample is most likely strongly representative of the Airbnb ecosystem in the cities sampled. 
 
_Drifting and Algorithmically Confounding: Unclear_

While the researchers do discuss changes to Airbnb practices at the end of their article (Edelman et al. 2017, 19), it is unclear to what extent the Airbnb ecosystem could have evolved over the course of their study. The authors do not discuss this explicitly in the context of their results. Thus we cannot make an informed judgement on this aspect of the research design. Furthermore, as this study was not undertaken in collaboration with Airbnb, it is difficult to assess the extent to which Airbnb's design of the platform influences the results. 

_Sensitive: Moderate_

The study design raises a number of issues regarding sensitivity of data, namely that Airbnb users did not consent to their data being shared with researchers or Mechanical Turk workers. However, the study did undergo Institutional Review Board approval, which offers some level of assurance that appropriate measures were taken. (Edelman et al. 2017, 1) Nevertheless, the authors do not elaborate on any anonymizing measures they used during the data collection or analysis process. 

_Validity: Moderate_

The robust experimental design and numerous validation of methods (e.g., the pre-experiment survey to confirm the "white"/"black" character of names) allow us to conclude this study has strong internal validity. (Edelman et al. 2017, 5) Participants were contacted only once, and no subjects had a listing in multiple cities, thus ensuring no subject received multiple treatments. (Ibid, 6) In terms of construct validity, the study design clearly maps the variables of interest (race, discrimination) onto treatments (receipt of inquiry from black or white individual). Thus, we can say that the study also has strong construct validity. However, where the study's validity is weakest is its external validity. Due to Airbnb shutting down the researchers' scrapers, the sample was not of the size originally intended, and only in a smaller subset of cities than originally planned. Moreover, it is difficult to say if the researchers' results would generalize to other accommodation markets, given Airbnb's unique character relative to its competitors.

_Heterogeneity of Treatment Effects: Strong_

The study powerfully leverages heterogeneity of treatment effects to study sub-populations of subjects who receive treatment. For example, by using profile pages and pictures from previous guests, the researchers were able to identify hosts who have had a black guest stay at their property. (Edelman et al., 2) Using this as a control, the researchers found that discrimination essentially "disappears", which implies discrimination is found mostly among a specific subset of the population. (Ibid) In general, the study's substantial set of variables for both subjects and treatment allows for a number of nuanced analyses. 

_Causal Mechanisms: Moderate_

This study usefully uncovers a number of causal mechanisms at play. For example, by verifying if a particular unit was rented for the weekend in question after the researchers' guest accounts inquired, the researchers are able to make a link to lost revenue for hosts who discriminate. (Edelman et al. 2017, 3) However, the study is only able to infer host motivations for behavior, as the researchers do not engage directly with the hosts outside of the treatment. The researchers must assume similarities between hosts on the basis of observed characteristics and attribute any difference in response to the treatment (the race/gender of the prospective guest). 

### Summary of Assessment, Edelman et al. 2017.

| Characteristic                           | Conclusion |
|------------------------------------------|------------|
| Big                                      | Strong     |
| Always-on                                | Strong     |
| Non-reactive                             | Strong     |
| Incomplete and Dirty                     | Strong     |
| Inaccessible                             | Poor       |
| Non-representative                       | Strong     |
| Drifting and Algorithmically Confounding | Unclear    |
| Sensitive                                | Moderate   |
| Validity                                 | Moderate   |
| Heterogeneity of Treatment Effects       | Strong     |
| Causal Mechanisms                        | Moderate   |

In conclusion, we can say this research design is quite robust, leveraging the advantages of big data while mitigating successfully against most of the risks. The weakest aspect of the design is the researchers' willingness to accept the data made available to them by Airbnb (i.e., before Airbnb blocked their collection). This resulted in a sample size substantially smaller than originally planned. Additional information on potential risks of drifting and algorithmic confounding could usefully have been addressed with respect to the study itself, not just in the context of the policy implications of findings. 

## Joint Evaluation

### Value-added of Conducting Both Research Projects

While there is a clear difference in terms of the quality of research design from the first paper to the second, being able to conduct both studies would allow first to quantify and confirm (_what_, _how much_) while the second study would explain _why_ a phenomenon exists. 

To elaborate, the first study is entirely observational, offering a clear picture of the state of online marketplaces - how the world is - and the differential rental rates charged by hosts of different races. The conclusion from this study is that yes, a meaningful and statistically significant difference exists on the basis of host race. An experiment then allows us to explore that difference further and uncover the causal mechanism at play. The experiment has a particular advantage in that it allows the researcher to "control" variables such as location, or guest gender. However, it is financially impractical, conceptually challenging, and risky to conduct experiments without some previous knowledge to focus these efforts. 

For example, consider if the researchers had conducted the experiment first. They would have had to make a number of assumptions about the effect of variables such as gender, race, and location. Even using prior research, these assumptions could introduce systematic error into the study. However, because they conducted an observational study, they had solid foundations upon which to make decisions regarding experimental design. 

In summary, these two approaches are not mutually exclusive, in fact they reinforce each other and when used together or in succession they can result in focused, cost-effective and more robust research. 
 
### Application of a Survey Approach

Research Question, Paper 1<sup>1</sup>: _The extent of racial discrimination against hosts on Airbnb_

Research Question, Paper 2<sup>1</sup>: _The existence and extent of racial discrimination on Airbnb_

Both of these research questions (essentially the same research question, with some variation) could be investigated using a digital survey methodology. This would be implemented through a series of questions on individuals' (hosts') attitudes towards renting to specific races or other categories of guests. This would provide a certain measure of the extent of discrimination on this platform. However, this approach has a number of major drawbacks, as detailed below. 

_What are the potential drawbacks?_

__Representation Error__

There are a number of risks apparent with respect to representation error. Coverage error may result from only surveying Airbnb hosts for particular types of properties, or in a particular date range. If the researchers only engage with individuals from a subset of cities (as they did with the above papers) then they risk sampling error. Lastly, if there is insufficient incentive for individuals to participate, then they risk non-response error.

__Measurement Error__
As a charged subject, it would be very difficult to collect viable response data from hosts without substantial risk of social desirability bias. While it may not be a challenge to draw out honest responses from guests (who may or may not have experienced discrimination), there are strong social norms which would prevent hosts from admitting to prejudiced feelings. In fact, this effect is likely to be so strong that it is unlikely the results would have any meaningful external validity. 

Another potential drawback is that this approach would require permission from Airbnb to engage with their members in a systematic way. The researchers are unlikely to evade detection if they use guest accounts to contact hosts asking them to respond to a survey. This likely violates Airbnb's terms of service. Thus, the only way to conduct this survey would be in collaboration with Airbnb itself. The introduction of a new stakeholder, Airbnb, would be a limiting factor in terms of what can be asked, and how the survey can be conducted. 

One additional risk/drawbacks is the potentially prohibitive cost for running a survey on a valid sample for a diverse population such as Airbnb hosts. This could easily run into hundreds of thousands of individuals to be surveyed, if researchers are seeking a high amount of generalizability. 

__What can mitigate these drawbacks?__

__Representation Error__

Representation error could be mitigated by a clearly defined target population, such as Airbnb hosts renting short-term to guests within the United States. Valid sampling procedures, be they random or non-random (weighting, matching, etc.) would also guard against representation error. Non-response error can be mitigated through ensuring the survey is engaging (see the gamification proposal below) or providing some type of remuneration, if working in partnership with Airbnb (see below).

__Measurement Error__

Measurement error risks could be mitigated through a number of strategies. For example, the researchers could anonymize responses and make it clear to respondents that their responses are anonymized. Alternatively, researchers could present a modified game as the survey - having respondents pick individuals out of a group, providing backstories to each individual. Through varying these backstories, the researchers could leverage heterogeneity in order to identify the effect of race on booking acceptance. These methods might ease some of the charged nature of the topic in question, allowing for more accurate responses. Researchers could also leverage observational data to amplify their findings. (see Salganik, "Amplified Asking") This would enable them to ask questions that serve as useful proxies for attitudes towards individuals of other races (e.g., Current Population Survey question, SPKRAC), and then link that data with past hosting behavior. 

Lastly, the researchers could strategically use deception in their survey. They could inform participants the study is about a plausible, but entirely different topic - host preferences for renter occupations, for example. This deception would not harm the subject, and would offer a way to remove the social desirability bias concerns discussed above. 

One way to defray the potentially prohibitive cost of such a survey would be to partner with Airbnb. Although this has drawbacks (as described above) it could keep costs down and provide access to Airbnb hosts through a reputable interlocutor - Airbnb itself. 

## References

Edelman, B. G., & Luca, M. 2014. "Digital discrimination: The case of airbnb.com." _Harvard Business School_ NOM Unit Working Paper, 14-54.

Edelman, B., Luca, M., & Svirsky, D. 2017. "Racial discrimination in the sharing economy: Evidence from a field experiment." _American Economic Journal: Applied Economics_, 9(2), 1-22.

Salganik. 2017. _Bit by Bit_ http://www.bitbybitbook.com/en/ethics 

--- 

<sub>1</sub>  "In this paper, we empirically investigate the extent of racial discrimination against hosts on the popular online rental marketplace Airbnb.com." (Edelman and Luca 2014, "Introduction")

<sub>2</sub>  "In this paper, we empirically investigate the extent of racial discrimination on Airbnb..." (Edelman et al. 2017, 1)

