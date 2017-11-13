## Improving a journal article 

**Journal**: Huang, R., Zheng, W., & Gui, Y. (2016). Multi-channelled forceful intervention, frames and protest success—a fuzzy-set qualitative comparative study of 40 anti-demolition protests in China. *The Journal of Chinese Sociology, 3(1)*, 23.

### Summary of the Issue

The property law is not well-defined in China. Some people have the property right of their houses while the others only have the ‘use right’ of their property. Owners with “use right” only cannot transfer their properties and can only stay in their properties for 20 years. The ownership of these properties is undecided. Starting from around 2000, local governments in several areas in China have planned to upgrade their city and demolish some old buildings with undecided ownership. The residents, who will have nowhere to live after the demolition, try all means to fight against the local governments and prevent their houses from being demolished. Huang, et. al (2016) are interested in what makes some these collective protests (more successful), while the others are not. They select 40 of over 13,000 anti-demolition social movements from 2002-2013 in China and implement fuzzy-set qualitative comparative analyses (QCA). They have accumulated a large amount of data of each case - detailed news report, disclosed interviews, banners, graphs, blogs etc, and apply a variant of the social movement analysis network proposed by Cress and Snow (2000). Even though they have made an outstanding and valuable research in understanding social movement successes in China, I believe there is still something that can be improved in their research, with human computational techniques.

#### Problems regarding that research

1.	The scores assigned are arbitrary and subject to researchers’ bias. For example, in terms of protest success, even though the authors argue that they have made sure that higher scores indicate greater success, it is suspicious whether the authors have implemented a uniform standard when evaluating the scores.
2.	The authors only implement part of social movement analysis framework developed by Cress, and Snow (2000). Due to political concerns and research interests, the authors mainly discuss the influence of media (e.g. framing) to movement success. A large part of the framework, including agency (individual and collective) and organizational viability are neglected.
3.	The final problem is that the data they have collected do not come in a timely manner. Since the research started in 2014, Huang et. al. only started collecting materials after that year. A lot of valuable internet-based resources may be removed or censored before Huang et. al are able to access them. Considering that China has only got into the digital age lately, for movements starting before 2005, Huang et. al may not obtain enough resources to make a score.

#### Base on the limitations of Huang et. al (2016), here are my extensions:

1.	Design a search algorithm that quickly scrapes all the websites of relevant information as soon as an anti-demolition movement occurs. The websites scraped will go into a database located outside of mainland China, in case that these data will get censored immediately.
2.	Add dimensions of location, organization viability (resources), and agency, in additional to Huang et. al.’s framework (2016). All dimensions are evaluated in a fuzzy score from 0 – 1.0.
3.	Recruit people to participate in a human computational project. Each participant is given some scripts such as news report pertaining to a specific anti-demolition social movement. Each participant can decide the fuzzy score of each dimension from 0 – 1.0. Participants can choose not to assign scores to some dimensions.
4.	Update the data of an anti-social movement in 4-7 days, as new news come out. Recruit people to conduct a similar evaluation in phase (3).
5.	Retrieve coding from the database after approximately 30 days after an event occurs. Hire some graduate students to reevaluate the materials to see if systematic errors exist in coding.
6.	Perform the analysis.

#### Compared with Huang et. al (2016), my project has the following advantages:

1.	A more comprehensive framework is offered to understand the success (and failure) of social movements.
2.	More information is captured by the search algorithm by a timely manner before they are removed or censored. This helps participants and researchers to give an accurate evaluation of a social movement.
3.	Almost no researcher’s bias and removable system errors exist in this research.
4.	Most importantly, the dynamics of an anti-demolition social movement can be understood with this research design. The rich, time-based data accumulated enable researchers to understand the birth and evolution of an anti-demolition movement.

## InfluenzaNet
Graph1. Comparison Between InfluenzaNet, Google Flu Trends, and the Traditional Influenza Tracking System. 
![Why is the picture not showing?](comparison.jpg)

#### Design
**InfluenzaNet** recruits voluntary participants from the general population and records their demographics and life style with a ‘pretest’ survey. Participants enrolled receive a weekly email that take them to an online questionnaire about several (ILI) symptoms that participants might have experienced since their last report. Participants who reports ILI symptoms are asked some follow-up questions, such as whether they have sought medical care. This enables InfluenzaNet to bridge its database to surveillance data (by ECDC). Further, InfluenzaNet uses logistic regressions to predict ILI incidences based on the data in their database.

**Google Flu Trends** (GFT) applies machine learning techniques to predicting influenza epidemic. Engineers in google input the history data of ILI searches and surveillance data provided by CDC. They developed a log-linear regression with correlative relationships between ILI searches and flu prevalence, which later enables them to “nowcast” current flu prevalence with instant number of ILI searches going through the search engine.

**Traditional Influenza Tracking System** (CDC) uses surveillance data, mainly historical data of flu incidences and hospitalization, to predict flu prevalence in the current season. Despite some disputes, CDC researchers are able to develop multiple estimation models that are able to offer decent estimations of flu incidences of a given time-period.

#### Costs

Without doubt, **traditional influenza tracking system** consumes the most recourses. It requires a detailed design of the medical system, from registration, flu diagnosis, hospitalization, as well as private data transmission. Also, the traditional method requires quite a long time to clean, mask (hide personal information), and report the data, which makes it unable to give detailed estimates in a timely manner. Compared with that, **GFT** gives out a fast, cheap way of estimating the current prevalent of flus. The estimate can be generated as long as Google’s search engine is on. Finally, of the middle is the **InfluenzaNet**. It still needs more resources compared with GFT, since well-designed infrastructure is needed to recruit participants, giving out surveys, and store the process data. However, the cost is fairly cheaper than surveillance because data collection is faster and easier.

#### Likely Errors:

**Traditional Influenza Tracking System** will provide the most precise estimation, despite some selection bias. Some people with flus may search on Google to find ways to get better, but they may not go to clinics, hospitals, or private physicians. This will yield an underestimation of flu prevalence of a season. 

**GFT**, despite its low cost and fast estimation, is not without errors. One issue is overfitting. As Lazer, et.al. (2013) has pointed out, Google estimated more than double CDC estimates during late 2012 to early 2013. This example of overfitting is caused by the fact that Google engineers have used multiple predictors and special methods so that the prediction perfectly fits CDC statistics. However, as new data (out of the range where previous data are) are added, the model fails to give a decent estimation. Plus, algorithm confounding is very likely to happen in GFT when researchers are not aware of algorithm construction. For example, if google constantly offers antiviral drugs, the searches of flus and ILIs are certainly going to increase, since people are interested to what these drugs are designed for. A final problem of GFT is that it is a prediction model without explaining casual relationships. Therefore, the models will neglect the influences of several confounding variables and is not helpful when something unexpected (flu breakout) happens.

**InfluenzaNet** is same with GFT as they are both prediction models without causality. Compared with surveillance data, they are likely to yield raw and unprecise estimates. Besides, there may still be potential of measurement bias because the measurements (syndromes) given are not perfect predictors of ILIs. Furthermore, despite authors argument that the underrepresentation of the young and old does not affect the models’ predictive power, I am worried the model will give unstable coefficients when we want to check flu prevalence of several subgroups (e.g. kids).

####  Possible Errors when flu outbreaks in an unsettled time

For **GFT**, I am mainly worried about overfitting. Even the model fits the data (in a given range) perfectly, it is suspicious whether the model can be applied to data outside of the range. I believe GFT will give out an overestimate of ILI searches during an outbreak. The reason has been referred before, that Google is likely to offer more antiviral ads during the outbreak, which in turn make people to make more searches. This is also an explanation why this model failed in late 2012 – early 2013.

For **InfluenzaNet**, I think the main problem stems from the data collection process. In the authors’ report, they underscore that ‘participants who participate at least 3 times during a season are included in the analyses’, and that participants who have already had ILI will be removed from the analyses, I believe that InfluenzaNet will give an (lagging) underestimate of current flu prevalence.

For **Traditional Influenza Tracking System**, I think the problem mainly stems from underestimation and the fact estimates of a period usually come out 7-15 days after outbreak occurs. Underestimation may be a serious problem in this case because traditional estimates usually underreports flu prevalence (generated by hospitalization data). When flu outbreaks in a certain time, even though the prevalence increases by 2 times, the number of physician office visits may increase by 3 times (partly because more people are ill, partly because somebody are worried that they may be ill). Therefore, during an outbreak, I would think an emergent shortage of medical resources will occur.
