## Part I: Digital Discrimination: The Case of Airbnb (2014)
#### Research Summary 
Edelman and Luca (2014) try to find whether there exists racial discrimination against hosts in the Airbnb Marketplace. They collect data from the Airbnb website (by taking snapshots), run a regression model (holding covariates constant), and find that nonblack hosts charge approximately 12% more than black hosts for the equivalent rental. Their research implies even though great progress against discrimination has been made in offline markets, more efforts are needed to reduce racial discrimination on online markets.
#### Research Design
The research design of Edelman et al. (2014) is summarized in fig 1. There are several components of their design:
![alt text](slide1.jpg)

**Data Collection**: Researchers collect their data from the listings of Airbnb.com. The researchers implement their search in New York, NY and include 3752 listings in their data set. A snapshot is saved for each listing, which is later coded into a series of variables, “price asked by the host”, “characteristics of the apartment”, “characteristics of the host”, “number of reviews”, and “average rating”. Further, Amazon MTurk users are provided with the photos of the hosts and their apartments. They are invited to identify the race of hosts and give a 1-7 rating to his/her apartment. 

**Data Analysis**: A preliminary two independent sample t-test and a multiple regression are conducted. In the regression, they implement a hierarchical design and find that nonblack landlords tend to charge 12% more than black landlords when holding every observed variable constant.

#### Computational Methods Applied in Edelman et al. (2014)
**Automated Data Collection**: This research applies a search and scraping algorithm that will record all the available listings as soon as the algorithm is implemented. Since Airbnb applies a complex algorithm to decide the price and availability of the listings, this method enables the researchers to collect a large dataset with as little drifting effect as possible.

**Mass Collaboration**: This research uses Amazon MTurk to categorize and code some of the variables at a very low cost. The classification tasks (race and rating) are not error-prone and take a little time to code, thus applicable to mass collaboration.

**Data Characteristics**: The data collected are nonreactive and always on. This character does not only grant external validity to this research but also enables future longitudinal and repeated researches.

#### Evaluation of Edelman et al. (2014) (Merits)

**Interesting Way to Get Data**: It is clear that Airbnb is not cooperative with this research, yet the researchers are able to find a good way to generate the dataset to examine their research ideas.

**Nonreactive**: The hosts are not aware that their information posted are scraped by the researches. This gives the research great external validity and makes it less subject to bias.

**Always-on**: The always character enables researchers to conduct longitudinal and repeated researches in the future.

#### Evaluation of Edelman et al. (2014) (Demerits):
There are many things I would like to discuss about the research, which can be summarized into the following:

**Insufficient Justification for Research Design**: The researchers do not explain fully why they choose New York, NY as the target area and why they collect data on July 13rd. The failure to provide enough justification for their design costs the research both internal and external validity. An extension of this would be **drifting**, and I believe the research results can be quite different if researchers conduct their researches in winter rather than summer.

**Unclear Description of Research Design**: It is unclear whether July 13rd is the day of collecting data or the criteria to filter listings. I think the research does not inform its readers are their search criteria. Further, they may be quite few unavailable listings if the researchers do not conduct the search early enough. Therefore, it might be possible that the researchers only sampled a part of all the listings in New York, NY, thus threating the external validity of this research. Finally, the researchers do not provide details of the coding process in MTurk so that we are not sure about data quality.

**Abuse of variables**: The research uses *’location rating’* to be one of the three main explanatory factors of price disparities. However, location rating is not a correct reflection of location, let alone land price. The guest strongly affects location rating. A business man will give a similar location rating to his downtown apartment to the rating of a UChicago apartment given by a visiting scholar. Therefore, location rating is not a good explanatory factor of land price. Finally, there is insufficient reason the researchers think location rating has a quadratic rather than a linear relationship with the price.

**Unobservable covariates**: Even though the researchers emphasize they try to mitigate the bias brought by unobservable covariates, comparing column 2 and column 3 in Table 3, we can observe the coefficient of race decreases impressively with the introduction of social network presence variables. I guess there may be other factors that may decrease the effect of race, but more evidence is needed.

**Algorithmic Confounding**: The prices of housing on Airbnb changes based on the availability of housing and number of searchers in an area. Since the researchers do not obtain the raw data from Airbnb, I suspect that ‘price’ researchers obtained are very likely to be flawed and biased.

**Sensitiveness**: I think the researchers do not obtain the informed consents from the hosts whose information is used in this research. Even though I doubt if it is a good way to conduct the research, I think more importantly the researchers should encrypt the data and avoid sharing data with everyone else.

## Part II: Racial Discrimination in the Sharing Economy: Evidence from a Field Experiment (2017)

#### Research Summary

Like the 2014 paper, Edelman et al. (2017) try to do a research to understand discrimination against guests in Airbnb. This time, they do it using a field experiment rather than observational research. They sent pseudo requests with easily identified Black/White names to each landlord with available listings. They find that discrimination against the African American guests occur among landlords of all sizes, and the effect is most prominent in those who have never had an African American guest. The race of hosts seems do not have much impact on discrimination against African American guests.

#### Research Design
The research design of Edelman et al. (2017) is summarized in fig 2. There are several components of their design:
![alt text](slide2.jpg)
**Host as the Unit of Analysis**: Considering that some hosts may have more than one offering properties, and sending identical requests to one host may be regarded as spam, the unit of analysis is determined to be a host (rather than a listing). A host will only receive one request from the researcher.

**Observational Data**: This research scrapes the websites of each listing and records the basic demographics (similar to the 2014 paper) as well as number of properties, number of reviews, and whether the host has any African American guest before.

**Random Assignment**: Hosts are randomly separated into 4 treatment groups. Hosts in each of the four groups will receive a booking inquiry from a personal with a name that can be easily identified as White or Black and male or female. The responses of the hosts are coded into 11 categories. Later the responses are presented into two categories: ‘positive’ or ‘not positive’ response.

**Data Analysis**: The researchers then find if different gender/race subgroups would have difference positive response rate (yes), whether the race and gender of host will influence the response rate (not clear, possibly not), and whether there is a heterogenous effect of the discrimination (yes, hosts who have a least one African American guest is much less likely to discriminate).

#### Computational Methods Applied
**Automated Tools**: This research applies a special automated tool. It enables not only automated scraping but also automated inquiry sending. 

**Mass Collaboration**: Like Edelman et al. (2014), this research uses Amazon MTurk and Face++ to categorize and code their data at a very low cost. The classification tasks (race, gender, and age) are not error-prone and will not take long to code, thus applicable to use mass collaborative to do this.

**Data Characteristics**: Like Edelman et al. (2014), the data collected are nonreactive and always on. This character does not only grant external validity to this research but also enables longitudinal researches possible.

#### Evaluation of Edelman et al. (2017) (Merits)

**More Details, More Persuasive**: Compared with the 2014 paper, this paper offers a lot of details of this research design and it is much easier to replicate this research (e.g. coding rules).

**Random Assignment**: The use of experiment design prevents this research from potential biases of unobserved covariates.

**Heterogenous Effects**: The researchers are very impressive in pointing out that people who have African Americans guests are not likely to discriminate this subgroup of guests.

#### Evaluation of Edelman et al. (2017) (Demerits)
**Sensitivity and Ethical Issues**: Unlike the paper in 2014, this paper comes with a field experiment design. That is, it needs to ‘disrupt’ the natural environment surrounds the human beings so that a small change can be measured. John Patty points out that only by this change can we know whether discrimination exists or not, however, this also poses a hazard of ethics, since the researchers do not obtain enough authorization from Airbnb (in fact they are blocked from the server half way) but also do not obtain informed consent from the landlords they send requests to. 

**Causal Inference Not Explained**: Even this study uses an experiment design, as the researchers indicate, the researchers cannot ‘identify the mechanism causing worse outcomes for guests with distinctively African American Names’ (p.17). Honestly, after the researchers observe that there is a pervasive discrimination against African American guests, they do not make the best use of this experiment design to get more details under the hood, 

## Part III: The Value of Conducting Both Researches.
The question seems to ask me to put these two papers (and the methods they use) in a parallel fashion. However, I think these two papers embodies how researchers improve their research ideas and research design as they get more knowledge about the subject.

**Observational study precedes field experiment.** The observational study is best conducted when the researcher knows little about the subject and want to gather information and (or) run an exploratory analysis. As we can observe in the 2014 paper, the researchers have a coarse research idea, and I think the researchers in the end do not find enough support for their conclusion and fail to explain well about their research idea. For example, it is very strange for me to understand discrimination based on the sellers set different price for their products (and therefore more information is needed). However, as we observe in the 2017 paper, the researchers do many improvements based on the 2014 paper. They frame an impressive research topic, and they come with a very well-developed design to support their findings. The 2017 paper is like an enhanced version of the 2014 one. In conclusion, I think an observational study and a field experiment may be suitable for researchers in different stages of their researches. 

**The iteration between these two methods.** Further, I believe the relationship between observational studies and field experiments can be extended to an iterative process rather than a linear fashion. That is, even after we have conducted a field experiment, we can expand our knowledge with an observational research. For example, with a strong RCT experiment research finding at hand, we can find some indicator variables for one construct that is difficult to measure (but can predict our target social phenomenon quite well). Specifically, combining the papers in 2014 and 2017, Edelman et al. can create a variable called rent differences. If there is an observable rent difference between the non-black and the black, we would know that discrimination has occurred, and therefore social changes are recommended.

**Field experiments are best for policy interventions.** Finally, I believe the result of the experiment is best to develop intervention policies as well as offering strong facts to encourage stakeholders to participate into public affairs. Interestingly, Airbnb does not offer any formal support for this project and does not respond to the research findings until Edelman et al.’s paper has been accepted to a journal. Rather than thinking Airbnb are too sticking to themselves, I think the attitudinal change of Airbnb proves that good researches are the key of social change. Social scientists should bolster their research finding with strong facts, upon which we can design better interventions.

## Part IV: A digital survey-based research design

First of all, we have the two following topics to cover in our survey:

1.	Do non-black hosts charge more than black hosts for equivalent rental? (The primary question in 2014 paper)

2.	Do landlords discriminate against (give lower positive response rate to) African American guests? (The primary question in the 2017 paper)

Before designing my survey, I would like to compare the strengths and weaknesses of surveys with observational studies and field experiments. One strength of surveys, clearly, is that it is the best tool we can have to ask people’s attitudes. Also, surveys, especially those digitally enhanced ones, would be easier to administrate compared with observational studies (if data collection methods have not been designed) and field experiments. The weaknesses of surveys are clear as well. People are unlike to answer in the ways that would put them in an unfavorable manner. Therefore, it is extremely not advisable to ask hosts questions such as “Do you think there exists discrimination against African American guests among Airbnb hosts?” The principle of my digitally-enhanced survey, in contrast, would be asking hosts’ feelings about price discrimination and guests’ feelings of booking discrimination. I believe these two groups would report any possible discrimination, since it is best to their interest.

If possible, the questions of the surveys are to be administered and maintained by the Airbnb, so that Airbnb can put the problems into their customer service questionnaire. Consequently, there will be less ethical concerns. The following are the set of questions to be asked:

1.	For the hosts:

	a)	Do you charge less than other hosts for similar rental? If so, why?

	b)	Have you ever been forced to charge less than other hosts for similar rent? If so, why?

2.	For the guests:

	a)	Have you ever found yourself hard to secure a booking on Airbnb? If so, why?

	b)	Have you ever been discriminated against when you try to book on Airbnb? If so, can you provide us with more details of that?

However, very likely, Airbnb would reject our request. When this happens, I would like to propose the following solutions. First, we can discuss with the directors of Airbnb about whether we can add some questions into their customer service questionnaire. As researchers, we will be step away from the administration as well as daily maintenance of the database. We would only want to know the results of the survey after a period amount of time. Second, since Edelman et. al (2014, 2017) do not only focus on Airbnb but more generally on the rising sharing economy, I would suggest cooperate with other organizations that can satisfy our research goals. This could be online teaching (a teacher and a student who use cameras and microphones to practice a foreign language), or online car sharing, where the lender and borrower need to know each other before a deal is done.
