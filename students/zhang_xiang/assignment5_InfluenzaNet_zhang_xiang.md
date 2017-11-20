## Perspective on Computational Analysis
#### Assignment 5: InfluenzaNet, Google Flu Trends, and Traditional Influenza Tracking Systems
#### Name: Xiang Zhang

### Design of Three Different Systems
In this section, I discuss how three different systems are designed to collect data and get the epidemics trend.

**The Traditional Influenza Tracking System** relies on the virological and clinical data, including influenza-like illness (ILI) physician visits. Based on these surveillance systems, the CDC form a report on the national or regional epidemics with a one or two weeks lag (Ginsberg et al. 2009).

**The Google Flu Trend** detects influenza epidemics using search engine query data. Based on monitoring health-seeking behavior in the form of queries to online search engines, Google fits a simple linear model using the log-odds of an ILI physician visit and the log-odds of an ILI-related search query and make prediction of the ILI percentage (Ginsberg et al. 2009).

**The InfluenzaNet** monitors the activity of ILI with the aid of volunteers via the internet. As can be seen from its website, Influenzanet obtains its data directly from the population. Every single resident can participate by completing an online application form, which contains various medical, geographic and behavioral questions (InfluenzaNet Website).

Based on the previous description, we can see that:
- Both traditional influenza tracking system and InfluenzaNet directly use reported medical information from the patients (either report to primary care physicians or report online). However, Google Flu doesn't directly use the medical information, instead, it makes use of search query data to make prediction.
- Both Google Flu and InfluenzaNet make use of digital technologies. The former one use big data to make prediction, while the latter one use online website to get reports from the volunteers (patients). While the traditional influenza tracking system still rely on non-digital technologies and require the primary care physicians to report to them.

### Costs of Three Different Systems
We see in previous section that three systems differ from each other in their designs. In this section, we discuss the cost of these three systems.

The cost of traditional influenza tracking system mainly come from the cost of building primary care systems and building the report system. In countries like the United States, the primary care systems are well constructed so that the cost of building monitoring system well be relatively lower. However, to gather the information from primary care physicians required building a reporting system, which is still costly. After all these have been done, the cost of running the system will be relatively low. As for the computation cost, the CDC only have to add up all the reported cases, so the computation cost is relatively low.

The Google Flu prediction requires process very big dataset. As describe in Ginsberg et al. 2009, to build the model, they use all search query log data during 2003 and 2008. Thus, the cost of having such powerful computation ability is high. But after they have such computation resource, the cost of fitting a model is relatively small.

The cost of InfluenzaNet is the smallest, they only have to have a team to build the website, one team to monitor the reported cases and impute the influenza trend. And the computation resource required is also relatively small.

### Possible Errors of Three Different Systems
The errors of traditional influenza tracking system are the smallest among the three methods. It's the most accurate one since it records every single influenza case. The possible error of traditional influenza tracking system comes from the those who are infected by influenza but do not go to visit a primary care physician. If such individuals exists, the number of ILI will be underreported.

The possible errors of Google Flu mainly come from the model error. Using search query data to predict flu trend is like a black box (they don’t rely on virological knowledge). In this way, the design of model really matters. Thus, the choice of model is a possible source of errors of Google Flu. Actually, as can be seen from Lazer et al. (2014), the Google Flu yields very large predication error as time goes by.

The main error of InfluebzaNet comes from the sample non-representativeness.
As noted in Koppeschaar et al. (2014), the data collected is only representative of the population in four countries, while underrepresent the youngest and oldest age groups in 7 countries.

### Possible Errors in Each System when a Swine Flu Outbreak
For traditional influenza tracking system, there might be a lag in reported number of cases. That is, they cannot monitor the influenza trend very fast. Moreover, when a new kind of flu outbreaks, the primary care physicians might not be able to precisely diagnosis the disease, which may lead to errors.

For Google Flu make prediction based on the search query log data related to the flu. However, when a new flu outbreaks, people might get panic and search information about the flu through Internet much more than before. In this way, the Google Flu model might make imprecise prediction.

The InfluenzaNet system might also get some problems when a new flu outbreak happens. First of all, simply based on the information (like the symptoms provided by patients), the InfluenzaNet team cannot precisely detect whether they're affected by certain disease. Secondly, since the citizens might get panic, they may tend to report more ILI than before, thus make the estimation imprecise.

### Reference
Ginsberg, Jeremy, Matthew H. Mohebbi, Rajan S. Patel, Lynnette Brammer, Mark S. Smolinski, and Larry Brilliant. "Detecting influenza epidemics using search engine query data." Nature 457, no. 7232 (2009): 1012-1014.

InfluenzaNet Website: https://www.influenzanet.eu/en/about/

Koppeschaar, Carl E., Vittoria Colizza, Caroline Guerrisi, Clément Turbelin, Jim Duggan, W. John Edmunds, Charlotte Kjelsø et al. "Influenzanet: Citizens Among 10 Countries Collaborating to Monitor Influenza in Europe." JMIR Public Health and Surveillance 3, no. 3 (2017).

Lazer, David, Ryan Kennedy, Gary King, and Alessandro Vespignani. "The parable of Google Flu: traps in big data analysis." Science 343, no. 6176 (2014): 1203-1205.
