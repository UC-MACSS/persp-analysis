
## Edelman 2017

### Summary of the research design

The primary question of this paper is to investigate whether racial discrimination against African American guests persists on the online rental market. To do so, the researchers leveraged a typical field experiment design to answer this question thoroughly. 

The main strategy, in short, is to utilize the distinction of common names for different racial groups to signal the race of guests and track host responses. This is a canonical approach to study the discrimination on the market. 

They perform this experiment on Airbnb. First, they collected the hosts' information in five cities, a comprehensive coverage of the levels of Airbnb usage and geographic regions. This information includes host characteristics, property characteristics, and the rental history of a host. Roughly 6,400 hosts are involved in the research.

They created 20 aritifical Airbnb accounts to contact these hosts. The accounts were identical in all respects except for the names. 10 of the accounts were given distinctively white names and the other 10 were given African American names.

Researchers used these accounts to send messages to hosts to inquire about the availability during a specific period. Hosts' responses are recorded and analyzed. 

They compared the percentage of a "yes" response between two "races" of the guests and found that the race gap is constantly at 8 percentage points. Using the information collected in the first step, they also showed the heterogeneity of treatment effects by the hostscharacteristics.

This study relies hugely on the computational methods in research. After all, the research question itself is a digital-age topic. The discrimination in offline markets has already been documented by researchers, and well-regulated by the government. However, the discrimination in online markets has not been fully-aware yet. 

Therefore, the whole experiment is fully digitalized, and the research also benefits from computational methods.

First, the nature of an online research gives the researchers great accessibility of data. In a traditional field research, researchers' ability to access data is limited geographically. It is difficult to run the same experiment across the country, which limits the representativeness of their sample. Also, they have to rely on a survey to collect information, which is expensive and may be biased. However, in this study, since the profile of the hosts and their properties are public, researchers can obtain the information directly on the website without geographical restriction.

Second, computational methods facilitate the collection of the data. Instead of collecting data manually for themselves, they used automated tools to collect the information from the website and sending inquiries. These automated tools also improve the standardization of the experiments. Besides, they also employed MTurk workers to encode the information collected by the scrapers. 

Third, the manipulation is also easier with computational methods. In order to control the confounding variables, the guests should be identical in every aspect except for the race. This cannot be achieved perfectly in offline markets. Due to the anonymous feature of the internet, researchers are able to create arbitrarily many "guests" that only differ in the variables of interest.


### The Analysis of the Effectiveness

The main result of this research is that black guests are more likely to be rejected (or negatively responded) by the hosts on Airbnb. Yet the researchers also presented a thorough and informative analysis of heterogeneity of treatment effect, thanks to their comprehensive dataset.

Interestingly, they did not find too much heterogeneity, indicating that discrimination is quite ubiquitous. The acceptance gap persists among both African American hosts and white hosts, persists among female hosts and male hosts, and also among experienced hosts and new hosts. The characteristics of the apartments do not affect the gap, either.

One of the interesting discoveries they made is that discrimination is most pronounced among hosts who have never had an African American guests but not significant among others. This suggests that discrimination persists in a certain subset of hosts.

The manipulation of treatment is clear and effective, and the confounding variables are well-controlled. Thus, the study achieved strong internal validity. The experiment also targeted clearly on the discrimination by analyzing the acceptance ratio. Hence, the construct validity is also fulfilled.

For statistical validities, it might have some defects. This paper argues that the acceptance gap is at the same magnitude among different groups. However, in order to argue for a null hypothesis, one should have a relatively large sample size. Otherwise, it cannot be determined whether the insignificant results are due to the null hypothesis or the lack of statistical power. The authors admitted in the discussion for the interactions of the races of the hosts and the guests that the statistical results are noisy and they cannot reject coefficients of zero. However, they can also not argue there is no heterogeneity, unless they do an analysis of the statistical power for their intended size of interactions.

Since the experiment is too well-controlled in order to achieve better internal validity, it may relatively lack a strong external validity. The experiment has only shown the acceptance gap between the guests under black-sounding names and white-sounding names. The account is artificial, with no photo on the profile and no rental history. It is hard to be generalized to the real life, i.e, how large discrimination an African American will suffer in real life when he uses his own account which has a searching apartments on Airbnb. Hosts may reject the artificial black guests because the lack of history and more information of black people makes them feel unsafe, but such discrimination can be easily mitigated by a complete profile and history. The calculation of the costs of discrimination is also theoretical instead of empirical.


## Edelman 2014

### Summary of the research design

This research, on the contrary, is aimed at investigating the discrimination against African American hosts in the online rental market. Furthermore, instead of simply pointing out the existence of discrimination, they estimated the economic loss of African American hosts due to discrimination. 

The research design is straightforward. They employed an observational study design. They collected a data set consisting of a snapshot of listings contained on Airbnb for New York as of July 17, 2012. The data set contains information about the price of a list, the characteristics of hosts and apartments, the rental records and ratings. In short, they collected everything that is visible to a guest on the website. Most information on Airbnb can be quantified and directly used in statistical methods. For photos of apartments, they hired workers on MTurk to encode it into 1 to 6 ratings with respect to its quality. The race of hosts is also identified by MTurk workers.

After collecting data and encoding, they built an OLS model to identify each determinant of prices on Airbnb. They found that after controlling for all of these factors, black hosts earn roughly 12% less for a similar apartment with similar ratings and photos.

Similar to the other one, the topic of this study is an internet-based question, and hence it is also fully digitalized, especially in the aspects of collecting data and encoding data. 

### The Analysis of the Effectiveness

The main result of this research is that black hosts earn 12% less than non-black hosts. Though the statistical tools are traditional and simple, this study generates convincing results. 

One of the common criticisms of observational study is that such research often cannot generate causality, that is, in the terminology of econometrics, this kind of research has **endogeneity**.  Three kinds of endogeneity will arise in an observational study: Simultaneity, omitted variable, and Measurement error. However, for this research, these three kinds of endogeneity are not likely to happen.

Simultaneity means that the explained variable and the explanatory variables are codetermined. We can readily rule out such possibility, since the race of the hosts cannot be influenced by the price.

Measurement errors are very common in research pertaining prices, especially for those survey-based studies. For this paper, measurement error may exist but will not be a vital issue. In this paper, the prices are the real prices in the rental market without any error. For other variables, they were also directly obtained from the website except for the races of the hosts and quality of the houses, whose measurement errors can be deemed as negligible.

Normally, omitted variables will be the most severe issue for such studies. This is often the case for an offline market, since it is impossible to completely record all the aspects that enter consumers' consideration. However, thanks to the computational methods, it becomes possible in this study. Due to the online nature of Airbnb, transactions have to be made purely online before the guest can visit the apartment in person. Therefore, all the information the potential guests can access is on the website. Therefore, researchers are able to collect all the information that is visible to the guests, or put it in another way, all the factors that influence the prices. Therefore, it is very unlikely the price gap is created by the omitted variables.

Captiously speaking, there are always some unobservable factors that may affect the tenants' decision. For example, the interaction between potential guests and the black hosts. It is reasonable to conjecture that the black hosts have relatively lower selling skills so they have to lower the prices; the lower estimation of the prices by the hosts themselves can also explain the lower prices on the market. However, these factors are not likely to create a price gap at the size of 12 percent points.

Therefore, the identification of this study is clear and convincing. There is not too much to criticize about the validity of the results. However, with such a comprehensive dataset, they can do more than what it is. 

For example, they can include more cities instead of restricting their sample only in New York. The costs would be relatively low, since the data collection and analysis are both similar, while there are several benefits. First, using the sample in New York only is not representative enough. A broader coverage is needed in order to draw a nationwide conclusion. Second, geographic variation can be utilized to support the results. For instance, if the price gap is indeed mainly driven by discrimination, we may be able to observe that in cities where the percentage of Black guests are higher, the price gap will be smaller.



# Value-added of conducting both studies

These two studies are complementary to one another. 

In terms of the topic, these two research investigated into the two sides of the market, the demand side and the supply side.

The experimental research gives a very detailed and reliable proof of the existence of discrimination against black tenants. It cannot be replaced by an observational study, because the focus of the research is on the acceptance ratio, which is unobservable if the transaction does not happen at all. However, as we have discussed above, their results are hard to be interpreted and generalized, since their results are mostly meaningful in their research but may not reveals the true market preference. Their estimates of the loss caused by discrimination are also not very reliable.

On the contrary, the observational study focuses on the prices. Since the prices are the results of an equilibrium, it is impossible to be manipulated in experiments. Actually, the discrimination against the supply side is hard to study with an experiment, as it is too expensive to create host accounts with an apartment to rent. It can only be studied by the observational data. The results of the observational study are more economically meaningful, since it can estimate the true loss of black hosts empirically.

Combine both studies, we can have a big picture of discrimination on the Airbnb, for both supply side and demand side, from the perspective of micro individuals to the macro influences on prices.

# A Complementary Survey-based Research

Both of the studies focus on the implicit discriminations. For the experiment, the hosts did not manifest strongly that African American are not welcomed; instead, they only replied the apartment is not available at that time. For the observational study, no one is asked about their attitude toward African American guests directly, while the prices revealed the market preference.

However, sometimes we also want to compare the explicit attitude and the implicit attitude towards black hosts and guests. Also, we want to know what are the reasons for discrimination. To achieve such aim, we need to utilize a survey-based design.

Our survey-based research consists of two parts, one for measuring respondents' explicit attitude by asking them directly and another for measuring their implicit and true preference. The second part is the normally hard to achieve in a survey. Thus, to do so, we need to use some special techniques. In our research, we will use an Implicit-Association Test (IAT) design, which we will introduce later.

We will make the survey on a webpage and send the link to both tenants and hosts on Airbnb. Respondents can get $5 as compensation once they complete the survey. 

The first part of the survey consists of scales measuring the explicit attitude of discrimination, designed for tenants and hosts respectively. Sample items are: "Apartments of black hosts are always not preferable to me"; "My furniture can be easily damaged by Black tenants", etc. The respondents are asked to rate to what extent they agree with these words on a 5-point Likert scale. If they reveal the discrimination to some extent, they are also asked about why they hold such opinion.

The second part is an IAT program. IAT can measure the implicit association of concepts. The procedures are as follows: In the first stage, respondents are asked to sort words relating to the concepts (e.g., Black hosts, White hosts) into left-right categories. They are asked to press "f" once they have presented a picture of black people, and press "j" once they are presented a white people. They are required to give the respond as fast as possible.

In the second stage, they are asked sorted words based on the evaluation (good, bad). For example, they are required to press "f" for good things and "j" for the bad things.

In the following stages, they are presented with the different combinations of words from the first two stages. For example, they are required to sort the combination of "black people" and "good" to the left ("f") and "white people" and "bad" to the right ("j"). Different sets of combinations are all tested.

The main point of the IAT is that people will react more quickly toward a strongly connected combination of words. Thus, the gap of speed between the reaction toward black-good combinations and black-bad combinations measures the implicit discrimination toward black tenants or black hosts. For a more thorough introduction to IAT, see [here](https://implicit.harvard.edu/implicit/iatdetails.html).

Demographic information is also asked in the survey. After collecting all the information, the respondents can get the compensation and exit.

With the data from the survey, we can answer questions including:
- How strong is the explicit discrimination against the black on the online rental market?
- How strong is the implicit discrimination against the black on the online rental market? 
- How large is the gap between explicit and implicit discrimination?
- What are the characteristics of those people who are discriminating the black on the online market?
- What are the reasons for discrimination?

