## Persp-Analysis Final Exam

Author: Andi Liao

Date: 12/06/2017


## Evaluating research designs

#### I. Research design and methods

This part will summarize the research design and elaborate computational research methods of each paper individually.

**1. Edelman paper 2014**

  The Edelman paper of 2014 utilized the method of **digital observational study** to show the extent of existing race discrimination towards hosts on Airbnb.

  The **core research questions** are:
  * What factors are affecting prices in Airbnb?
  * Do black hosts earn less than their non-black counterparts on Airbnb? If so, how differ?

  The data needed is ready on the Airbnb platform - host personal information, apartment characteristics, reviews and rating. All researchers have to do is to use automatic tools to collect data directly from the Airbnb platform and analyze. As this research doesn't require extra manipulation over users or hosts, the digital observational study method can satisfy the demands well.

  Specifically, researchers used profiles to identify the race, used lists to collect asking prices, host characteristics, apartment characteristics, guests reviews and rating and combined all the variables collected into a dataset. The Airbnb prices are regarded as dependent variables, and the rest of variables are viewed as independent variables or controlling variables.

  To answer the first research question, researchers constructed a regression model using the collected observational data to find the determining factors of Airbnb prices. These factors turned out to be accommodation number, location rating as well as social network presence, and they are all positively related with Airbnb prices.

  Then the hosts are divided into non-black hosts and black hosts. Researchers figured out that when other variables are controlled, black hosts earn 12% less than their non-black counterparts with similar photos, rating and apartments. Therefore, the first part of the second research question is solved: indeed, black hosts earn less on the Airbnb platform.

  Researchers also detected the difference between black hosts and non-black hosts in terms of properties, that is, black hosts are more likely to have inferior locations and worse-looking property pictures. Based on this finding, the second part of the research question is fully answered, though researchers are unable to derive the mechanism only using the digital observational study.

  In order to check the robustness of the price gap, researchers repeated the procedure above using data of black hosts versus white host, and the result stays basically the same.

  All in all, researchers employed the digital observational research method to assess Airbnb data, and built their regression analysis and contrast analysis on the basis of the observational data.

**2. Edelman paper 2017**

  The Edelman paper of 2017 majorly utilized the method of **digital field experiments** to show the existing race discrimination towards applicants on Airbnb. A supplementary **digital observational study** was conducted to support the patterns of race discrimination indicated by the results of the field experiment.

  The **core research questions** are:
  * Do applications sent from users under African-American names receive more rejections than users of other races?
  * If the race discrimination exists, what factors are influencing the discrimination effect and what are the costs of the discrimination effect?
</br>
</br>
**2.1 Digital field experiments**
</br>

  To be specific, researchers created 20 Airbnb accounts with identical information under typical African-American/white and male/female names, and sent out 6400 requests to contact hosts on Airbnb and check the availability of a potential book. Therefore, there are 4 treatment groups (African-American male, African-American female, white male, and white female) in the study, indicating two independent variables, race and gender.
</br>
</br>
  The responses of hosts were collected and treated as the dependent variables in the research. The personal characteristics of hosts (including race, gender, proximity to guests, rental history with African-American guests, property and reviews), the features of listing (including prices, neighborhoods and desirability) were scraped and used as conditions or controlling variables.
</br>
</br>
  Digital field experiments make it possible to gather necessary data and answer the research questions. As the research questions need extra manipulations like controlling the race and gender of names on Airbnb applications, an experiment in real-world is needed here.
</br>
</br>
  By creating fake Airbnb accounts, researchers are able to send out the massive amount of requests in a relatively short period of time, manipulate the treatment group conditions and control irrelevant variables tightly. In addition, the responses as well as host characteristics and listing characteristics are collected automatically, more important, precisely.
</br>
</br>
  The major part of the research questions are answered by the digital field experiment, which shows that the race discrimination towards African-American exists on Airbnb, and the effect is fairly robust across different controlling variables except for the variable of rental history with African-American guests.
</br>
</br>
**2.2 Digital observational study**
</br>
</br>
  To have more confidence in their digital field experiment, researchers conducted a relatively small observational study to collect the ten most recent reviews from each listing page. The personal information like race and gender of guests can be assessed from the review.
</br>
</br>
  As expected, the main conclusion of digital field experiments are supported by the review observational data, especially the race gap of hosts with rental history with African-American guests.
</br>
</br>
  This supplement is essential as the results of the digital field experiment are based on fake Airbnb accounts, and real-world interactions between African-American applicants and hosts can serve as a verification towards the experiment results. The observational method is the most suitable tool here, because the rental transactions have completed and are openly accessible.

#### II. Effectiveness of research design

This part will evaluate the effectiveness of research design of each paper individually.

**1. Edelman paper 2014**

* **1.1 Pros**
  Like other "big-data" research, this study benefits from the three typical features of big data, "big", "always-on" and "non-reactive".
</br>
  * **Big**: Though the exact sample size number was not mentioned in the paper, it can be treated as "big" when compared to traditional observational study and survey study.
</br>
</br>
  The dataset contains listings of New York City on July 17, 2012. Given the city scale of New York City, an approximate number of sample size can be estimated - the number should be counted by thousands, or even more. More importantly, the sample is large enough for researchers to distinguish the price gap between black hosts and non-black hosts. Therefore, this research still enjoys the advantage of "big" of big data.
</br>
</br>
  * **Always-on**: Researchers can assess the public Airbnb platform data whenever they like, as the Airbnb platform is always on. Researchers can pick a random date to collect listing from Airbnb, without much consideration about working days or weekends, day or night, etc. The feature of "always-on" makes it easy for researchers to collect data.
</br>
</br>
  * **Non-reactive**: In this study, hosts and users were not required to take any reactions in response to researchers. They didn't probably even realize that they were being observed and their data were collected. The "non-reactive" characteristics is ideal here as researchers intended to observe the Airbnb price under real settings.
<br>

  </br>
  This observational research used counting-things as the research strategies. Though simple, this strategy is appropriate for the interesting research questions about online race discrimination. To find the price gap of hosts from different races, counting things is exactly the most efficient way to accomplish the goal.
</br>

* **1.2 Cons**
</br>
</br>
  This study also have some limitations. Not only did this research suffer from "incomplete", "inaccessible" and "sensitive" brought by using big data, it also failed to clarify the mechanisms between black hosts and price gap of Airbnb.
</br>
  * **Incomplete**: Researchers also mentioned in the study that there were some profile photos of hosts classified as "not applicable" or "uncertain". The incomplete personal information could influence the research conclusion, as researchers were forced to delete some of the data entries before analyzing the data.
</br>
</br>
  The sample would become biased if hosts with complete information asked for different prices compared with hosts with incomplete information. Under this situation, the research conclusion would be affected as researchers observed only the subgroup of complete information and generalized it to the whole Airbnb hosts population.

  * **Inaccessible**: As authors pointed out in the paper, researchers planned to consider both price effects and demand effects. However, due to the inaccessibility of complete demand data from Airbnb, they were unable to analyze demand effects. This obvious drawback of the study might not affect the current research conclusion directly, but the research would be more powerful if the consumer demands could be taken into consideration.

  * **Sensitive**: Given that this research utilized personal information of Airbnb hosts, the problem of sensitive should be carefully handled. The photos of hosts and apartments as well as other information were downloaded and analyzed, and it would be more than dangerous if someone utilize the research data to infer the concrete location of apartments or the accurate person of hosts and commit crimes. Therefore, the potential risk of leaking sensitive information should be paid attention to.

  * **Mechanisms**: Just as researchers stated in the article, this observational study didn't manage to distinguish between taste-based discrimination and statistical discrimination. Considering the nature of observational study, this limitation is natural because observational study did nothing but observe, and researchers were unable to manipulate the variables to test two different models of discrimination. To further explore the underlying mechanisms, the method of experiments is essential here.


**2. Edelman paper 2017**

* **2.1 Pros**
</br>
</br>
  Thanks to the "big", "always-on" and "non-reactive" characteristics of big data, the Edelman paper of 2017 are able to measure what they intended to do.
</br>
</br>
  It's hard to imagine how researchers can implement the treatment condition and gather relevant data without the help of big data. It might take them weeks or months to register as new users, filter qualified hosts and send out requests manually, and they have to spend even more time waiting for responses and identifying host characteristics and listing characteristics one by one.
</br>
</br>
  * **Big**: A large sample of Airbnb hosts information as well as their responses is easily captured for researchers, as they utilized automatic tools to scrape the information and communicate with hosts. Furthermore, with the help of large sample size, researchers can set up four treatment groups as they designed with enough responses for every treatment group, and divide hosts into different subtle categories to analyze the data thoroughly.
</br>
</br>
  * **Always-on**: The Airbnb platform is always on, therefore, researchers can send out requests whenever they like, and collect the responses the moment Airbnb hosts reply. The information of hosts and listing is also always open to public, which makes it easy for researchers to download and analyze.
</br>
</br>
  * **Non-reactive**: The Airbnb hosts are unlikely to change their response patterns as reactions towards the manipulation of researchers, as they are unable to distinguish fake Airbnb users from real ones. The non-reactive feature ensures that what researchers collected in the study is consistent with what Airbnb hosts usually behave.
</br>

  </br>
  This research is also an outstanding digital field experiment for the following aspects.

  * **External validity**: Given the fact that the digital field experiment is conducted on the real Airbnb platform, and the results of the observational study are the same as those of field experiments, the results of this study can be easily applied and generalized to real-world settings. Therefore, this research has a high external validity.
</br>
</br>
  * **Heterogeneity of treatment effects**: In the analysis part, researchers divide Airbnb hosts by different standards to test the robustness of discrimination effect. And for only one variable, "rental history", will dramatically reduce the race gap observed in all other conditions.
</br>
</br>
  This finding indicates that the treatment effect is different for various Airbnb hosts, when they are divided by the variable "rental history". Those hosts having rental history with African-American guests will not be affected by the manipulation, and they accept African-American guests as much as they would to other races. But hosts without previous African-American guests will be affected, as they decline the African-American guests more.
</br>
</br>
* **2.2 Cons**
</br>
</br>
  There are also some limitations about this research as discussed below.
</br>
</br>
  From the big data perspective, "incomplete", "drifting" and "non-representative?" are the three possible problems of this research. And from the angle of experiment, the weakest point is "mechanisms".
</br>
</br>
  * **Incomplete**: As authors mentioned in the paper, there are missing information in the profiles of some Airbnb hosts because the personal information are provided by hosts voluntarily.
</br>
</br>
  The incomplete information might affect the research conclusions, if hosts providing complete personal information are more likely to turn down requests from African-American users. In this case, researchers would wrongly generalize the conclusion of this subgroup of hosts to the whole Airbnb hosts population. Therefore, the incompleteness can be a potential problem of the study.
</br>
</br>
  * **Drifting**: When the researchers build models to estimate the economical loss of rejecting African-American guests, they stated that about 36.1% of the properties were no longer listed in the platform. This is a high percentage number that cannot be ignored, and the reason could be population drift, behavior drift or system drift. Maybe hosts left the Airbnb platform, or the system experienced a major update in between.
</br>
</br>
  Although researchers used two different ways to treat the 36.1% part of the property data, drifting itself might affect other data in an unexpected way. Therefore, drifting can be a significant problem in this study.
</br>
</br>
  * **Non-representative?**: The paper didn't compare the demographic information of sample hosts with the whole hosts population of Airbnb, so it's hard to know whether the sample used in the study is representative of the Airbnb hosts population. (I add a question mark here to show that this is a problem that lack enough information to infer.)
</br>
</br>
  * **Mechanisms**: As authors "confessed" in the discussion part, this research cannot reject taste-based discrimination model and statistical discrimination model. Some of the results support both models, while other parts of the results reject both models.
</br>
</br>
  Although this study utilized the method of digital field experiments, this research didn't identify a clear mechanisms for discrimination towards African-American users. To validate the two discrimination theories, a more tightly controlled lab experiments as well as a more complex statistical analysis is indispensable.


#### III. Joint analysis
</br>
**1. Added-value**

The first project of observational study is from the perspective of discrimination received by Airbnb hosts. The second project of field experiment study views the issue of discrimination from the angle of Airbnb applicants. The two projects supplement each other in the different objects of study, i.e. hosts and applicants; they also enhance each other in the terms of research method.

Combing the observational study and field experiment together, researchers were able to establish a relatively complete logical chain of racial discrimination on Airbnb.

The logical chain can be summarized as:

* showing that the race discrimination existed in Airbnb
* indicating that the causal relationship between black applicants and lower positive response rates

Using observational study, researchers were able to observe the behavior patterns of Airbnb hosts, and they discovered that black hosts earn less than their non-black counterparts.

The results were exciting for two reasons:

* first, researchers found evidence to support that online discrimination exists and it is relatively serious reflected by the price gap;

* second, the study was collected from the real-world Airbnb platform without artificial intervene, therefore, it had high external validity.

However, there were lots of confounding variables in the process of doing observational study. To have a better control over these variables, researchers utilized the field experiment. The main goal was to concentrate on the "race" variable, control other irrelevant variables like profile photos, and establish a relationship between race of applicants and responses of hosts.

By conducting the field experiment, researchers were able to indicate that only using a typical African-American name would result in a lower rate of acceptances of Airbnb requests.

If researchers chose to only use one of these research methods:

* **Observational study only**:
  We could observe the correlation between race and responses, but we wouldn't be confident to announce that there are casual relationship between race and responses.

* **Field experiment only**:
  We might have a hard time comprehending why the field experiment is designed this way. As there are too many factors related to applicants, like gender and age, why did researchers focus on the relationship between race and responses?

In a word, running both observational study and field experiments enable us to have a deeper understanding of online race discrimination by constructing a complete logical chain.


**2. Digital survey**

If I am allowed to apply survey-based approach to the online discrimination problem, I will do it as follow:

* design questionnaires using scenarios questions.
  * for hosts:
    * provide participants with some background information
    * present a series of requests of applicants with different **names** at random, other personal information sta the same
    * ask participants to respond to the requests as they want

  * for applicants:
    * provide participants with some background information
    * present a series of lists of apartments with different **locations** at random, other apartment information stay the same
    * ask participants to guess the price of apartments

* recruit Airbnb hosts and Airbnb applicants by launching ads of questionnaires on the Airbnb platform

* collect data, analyze data and draw conclusions

The host scenario aims at answer the research question of the field experiment paper, and the applicant scenario tries to solve the research question of the observational study.

There are three potential drawbacks of survey-based research design, "social desirability", "sampling" and "cooperation with platform". Fortunately, they could be overcome to some extent.

* **Social desirability**:

  It is not easy to use survey-based approach to conduct researches related to discrimination, as participants might give answers under social desirability, rather than their true thoughts.

  In today's world, few people will admit that they discriminated against certain races; nearly everyone will answer that they treat every other race equally. But as a matter of fact, people still have discrimination in the depths of their hearts, which might reflected on their behaviors. Therefore, we can infer from participants' behaviors instead of asking straight-forward questions about discrimination.

  The survey questions should be designed as more implicit so that participants can safely give their real thoughts about discrimination.

  In the survey research I design, I utilize scenario questions to reduce the social desirability pressures and allow participants to express their truly thoughts. They can reject requests from a certain race subconsciously, and more importantly, without guilty, and I can identify their attitudes towards different races by studying their acceptance patterns.

* **Sampling**:

  It is always bothering researchers how to extract a representative sample from the whole population, and it is highly likely that those who are willing to take part in the survey are different from those who are not.

  To overcome this problem, I come up with two possible solutions.

  The first one is to distribute recruiting ads on Airbnb platform, trying to ensure that participants are active users of Airbnb. This solution aims at resembling the distribution of the whole Airbnb population from the start.

  The second one is post hoc testing. After collecting data, I would summarize the demographic information of participants and compare them with the statistics of the whole Airbnb hosts and applicants population.

  This approach can not prevent biased sampling if the sample is actually sampled. However, it might offer me with some consideration about adjusting weight index of different categories of participants in the process of data analysis.

* **Cooperation with platform**:

  The last one is quite difficult, because it sounds impossible to persuade Airbnb to cooperate in a study which indicates that race discrimination exists on its platform. But it's better not to give up on Airbnb yet - if succeed, Airbnb might provide access to their internal data, like the distribution of the whole Airbnb users, which will be fairly helpful for my study.

  However, I would like to extend my research a little bit so that the conclusion can be utilized to improve users experience when using Airbnb. By extending the research applications, I am able to coordinate my research interest with the commercial interest of Airbnb to some extent. Therefore, there will be a higher chance that Airbnb will agree to cooperate with my study.
