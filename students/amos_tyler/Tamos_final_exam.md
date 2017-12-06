# Final Exam

### Tyler Amos
### MACSS 30000
_December 6 2017_


## Independent Evaluation: Paper 1

#### Edelman and Luca, 2014. _Digital Discrimination: The Case of Airbnb.com_ 

### Summary of Research Design

Summarize the research design and explain how the research design leverages computational methods to ask and answer a question. (yellow)

_How does the paper use computational methods to ask and answer a question?_

The 2014 paper from Edelman and Luca apply an observational approach to data on accomodation listing data collected from Airbnb.com for New York on July 17, 2012. (Edelman and Luca 2014, "About Airbnb") To this 3,752 observation corpus, the researchers apply human computation techniques to process the data. (Salganik, "Mass Collaboration") Edelman and Luca hired Amazon Mechanical Turk workers to code Airbnb data in different mediums (image, text) to build a dataset with the following features: 

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
  * Quality of apartment based on host-provided photos;
  * Race of the host as determined by profile photos.
      
Applying an observational research design (Salganik, "Observing Behavior") Edelman and Luca seek to estimate differences in rents paid to black and non-black Airbnb hosts. This relatively straightforward design involves a series of statistical procedures (e.g., T-statistic tests) to determine if gaps between mean rents paid to hosts of different races are significant. (See Edelman and Luca 2014, "Tables") For this study, "non-black" is inclusive of all other races. Robustness of this design choice is supported by validating the results of the analysis (non-black and black) against the same analysis with just "white" and "black" racial categories. (Edelman and Luca 2014, "Robustness check")

### Evaluation of Research Design Effectiveness

#### What do we learn from the paper?

Using Salganik's characteristics of big data as an analytical framework, we can assess this study on its' ability to leverage advantages and mitigate disadvantages of social research with big data. A breakdown of the research design by characteristic follows.

__Salganik's Characteristics - Generally Good for Research__

_Big: Poorly-leveraged_

The total size of the corpus collected by the researchers is 3,752 observations. Depending on the characteristic, data is complete for between 99.8% (Number Accomodated) and 100% of total observations.(Edelman and Luca 2014, "Tables")

While larger than many traditional social science datasets, this is not an especially large dataset. Furthermore, it only applies to one city at one given point in time. Nevertheless, it was a large enough dataset to need human computation for coding observations. Thus, we can conclude the study leverages the "big" in big data to some minor extent.   

_Always On: Poorly-leveraged_

The researchers select a cross-section of data from July 17, 2012, effectively providing a snapshot of Airbnb's marketplace at one point in time. (Edelman and Luca 2014, "About Airbnb") This approach does nothing to take advantage of the always-on nature of big data sources. As such, it is more akin to traditional social science research and its static corpora. 

_Non-reactive: Well-leveraged_

In this study, the subjects are already aware they are being observed by potential renters on Airbnb. In fact, it is this behavior the researchers are trying to observe. In other words, it is not the underlying internal state of the individuals the researchers are trying to measure, but their public performance in the marketplace that is Airbnb. Thus, the addition of researchers into the ecosystem of Airbnb and their subsequent observation of subjects in that marketplace would have no impact on hosts' behavior. The researchers were able to identify an existing marketplace which they could observe without changing the dynamics of the system itself. This is a textbook example of Salganik's non-reactivity. 

__Salganik's Characteristics - Generally Bad for Research__

_Incomplete: Moderately Well-mitigated_

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

_Inaccessible: Poorly-mitigated_

Airbnb declined to provide access to their internal data for this paper, and as such the researchers were limited to examining only price data on hosts' listings. As a result, the researchers were not able to analyze demand. (Edelman and Luca, "About Airbnb") While this helps to ensure high amounts of completeness in the data (see "Big"), it risks placing researchers in a position of designing studies to fit available data, rather than finding data to answer their own questions.  In other words, the researchers jettisoned their original research question in favor of a more convenient line of inquiry. Thus we can say this study poorly mitigatated inaccessibility risks. 

_Non-representative: Moderately Well-mitigated_

This study uses cross-sectional data from one day in one city, as has already been noted. This means, effectively that the data can only be said to represent users of Airbnb at that particular time and in that particular place. Given that the number of Airbnb listings has grown rapidly (over 2,000,000 by November 2015 according to Edelman et al. 2017), the dataset has a strong temporal as well as geographic bias. This research design choice means the individual hosts in the dataset are likely poorly representative of black and non-black individuals in the wider vacation accomodation economy. However, given that the researchers explicity limit their scope to the digital economy, with a case study of vacation accomodation rentals, they anticipate some of these limitations. Thus, we can conclude the research design moderately mitigates issues of non-represenativeness. 

_Drifting: Non-issue_

The researchers do not account for system, population, or usage drift within Airbnb, although they do propose reforms based on their findings (namely, reduce the prominence of hosts' profile pictures). However, given the fact their design is cross-sectional, not longitudinal, it is unlikely that drift of any type would be an issue for their findings. Rather, concerns about drift would only arise when trying to generalize the findings to future research. 

_Algorithmically Confounding: Poorly-mitigated_

The researchers do not encounter substantial issues of algorithmic confoundment in their study. They merely observe listings and do not interact with users, creating few opportunities for Airbnb's design choices to influence their results. However, given that the researchers did not collaborate with Airbnb on this study, it is not possible to know if algorithms affecting search results did in fact shape data collection. As such, because we cannot be sure if there is algorithmic confoundment at play, and given the researchers did not lay out the measures they took to mitigate this risk, it is at best a minor oversight, at worst a source of systematic bias in the data. 

_Dirty_



_Sensitive_

#### What are the limitations of the paper?

_Validity_

_Heterogeneity of Treatment Effects_

_Causal Mechanisms_
Think back to Salganik's characteristics of big data and our assessment of experiments' validity, heterogeneity of treatment effects, and causal mechanisms. Draw on these methods of assessment as you evaluate the effectiveness of each paper.






## Independent Evaluation: Paper 2

#### Edelman et al, 2017. _Racial Discrimination in the Sharing Economy: Evidence from a Field Experiment_


### Summary of Research Design

(3 pts each) Summarize the research design and explain how the research design leverages computational methods to ask and answer a question.

_How does the paper use computational methods to ask and answer a question?_

### Evaluation of Research Design Effectiveness

_What do we learn from the paper?_


_What are the limitations of the paper?_

Think back to Salganik's characteristics of big data and our assessment of experiments' validity, heterogeneity of treatment effects, and causal mechanisms. Draw on these methods of assessment as you evaluate the effectiveness of each paper.


## Joint Evaluation

### Value-added of Conducting Both Research Projects
(3 pts) Identify the value-added of conducting both research projects. That is, what do we learn from running both an observational study and a field experiment that we could not learn from just one of these methods?

### Application of a Survey Approach

_What are the potential drawbacks?_

__What can mitigate these drawbacks?__

(3 pts) Consider how you could apply a digital survey-based research design to the primary question of interest from these two papers. What are the potential drawbacks to a survey approach? How might you overcome these drawbacks?