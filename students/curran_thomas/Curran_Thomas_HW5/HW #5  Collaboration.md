# Kaggle Account

Account: [TCurran4589](https://www.kaggle.com/tcurran4589)

### Kaggle Open Call Projects:

1. Describe one that is of interest to you. What is the goal of the competition? What would you have to do to make a submission?

The project that I would be most interested in the the [Visualize the State of Public Education in Colorado](https://www.kaggle.com/c/visualize-the-state-of-education-in-colorado). The competition sponsored by [ColoradoSchoolGrades.com](www.ColoradoSchoolGrades.com) sought out the Kaggle community to assist in visualizing trends over time, growth in school academic performance, and distribution of "A" schools versus "F" schools. Furthermore, the effort makes it a point to develop visualiations that can help visualize correlations between import education factors such as poverty and demographics with the school's academic performance. 

To make a submission to this competition, I would have to make a series of different plots and graphs to visualize the data provided. Ideally, these plots would be in the form of a dashboard that  made the information easily digestible by non-academic communities (e.g. parents) and made the data interactive. While the former would serve to accomplish the goal of sharing and communicating information, the latter would help infer patterns within the data itself. 
  

2. Download one of the datasets and generate a descriptive plot that highlights some instructive characteristic of the data. Make sure your plot has a title, labeled axes and axis titles, and a legend if necessary. Submit your script (.R or py) and your plot (saved as a PDF). Make sure your script is properly commented and reproducible.

[Students' Academic Performance Dataset](https://www.kaggle.com/ndalziel/massachusetts-public-schools-data)

![frl\_dropout\_plot.png](resources/073C140B4AE151A1AA0862CA88EF1B5B.png)

# Improving a journal Article:

Look through a recent issue of a journal in your field. Find a paper that you think could have been reformualted as a human computation project. How would you formulate the data collection as a human computation project? How might this improve the study? [Link](http://www.ifets.info/journals/20_4/7.pdf)

### Article Summary:

_Student's Reactions to Different Levels of Game Scenarios: A Cognitive Style Approach_

Authors Zhi-Hong Chen, Sherry Y. Chen and Chih-Hao Chien explore the game-based learning in their article _Student's Reactions to Different Levels of Game Scenarios: A Cognitive Style Approach_. Using different modalities of information within game-based environments, the authors explore the impact of that modality on the cognitive styles of students. Using new media technology, the authors measure and examine the different cognitive styles (i.e. Holist/Serliast) reaction to things like images, text, and images with graphics in a game enviornment. 

Chen, Chen, and Chien define what they call "multimedia" learning, style of learning in which students are presented with information from multiple channels (i.e. both image and text or image and audio). They also describe situational learning which is essenitally applied information presented to students and the learning ocurrs by extracting and inferring the information from the scenario presented. These two styles of learning have combine due to the emergence and availability of technology in the classroom. 

For the study, the authors created an english vocabulary game that presented audio elements and had a non-linear learning style. They then split the game into three different versions; a game with text only, one with text with graphics and a context version that included mutliple media channels. The participants in the study were then given both a preference questionaire (to identify learning styles) and an achievement test. For the achievement test, students were given a pre and post test to evaluate the game impact. 

The experiment was deployed at University of Taiwan with 96 second year university students. Those 96 students were then split into three groups and administed a version of the game (as previously mentioned). All sample participants had basic computation and english skills. 

### Findings:

Chen, Chen, and Chien found that in both types of cognitive learning styles (Holist/Serialist), performance improved from pre to post achievement test after using the game in all versions. However, in the context version of the game, Holists made significantly more progress towards mastery of the vocabulary. The result indicate that contextual learning is better for the Holists and not the Serialists. The results of this study, as pointed out by the authors, is the help future educational game developers create better games, and for the application of educational technology games to be properly implemented in a learning enviornment and across domains (i.e. reading, science, math).  

### Reformulated as a human computation project:

While the findings of Chen, Chen and Chien's article are certainly interesting, the sample size and sample population limit the generalizability of the findings to a winder general audience. Specifically, the samples were only applied to university students, and students that spoke a common language. The former indiciates at least some bias in the sample towards people with the same socio-economic strata. However, the digital platform that they use does allow the experiment and applicability to be deployed using a human computation source for data gathering. 

Using Amazon MTurk and a survey instrument such as Qualtrics, I would extend this experiment to collect information on people of different age groups, different primary languages and different learning styles. Using Qualtrics, I would create a screener survey that collected information about the person's primary langauge (if it is english, the respondent would be filtered out), the person's level of education, place of origin and other demographic and "meta" characteristics. Then like the paper's expeirment, I would administer the same study preference survey to identify the respondent's learning style. However, I would potentially expand the type of learning style to be identified beyond Holist and/or Serialist. Then based on that questionaire, the respondent would be given the pre-test and then randomly assigned to one of the three versions of the game with the accompanying post-test. 

### Improvements to Study:

Deploying the experiment in this way presents two primary benefits; First, using Qualtrics makes screening respondents very easy using pre-defined logic gates and Amazon MTurk allows for diversity in a sample size beyond university students. Second, using human computation tools can make the finding more generalizabile. Because we are sourcing our respondents from a diverse pool (inherent to MTurk) we would be able to measure variances and sublties between different groups that could not be done before. For example, using MTurk, we could compare across languages and dialects, even delve into motivation depending on the price set for the task. This is particularly useful in the U.S. given the trend in U.S. classrooms to employ multimedia learning technology and because classrooms are more diverse and "blended" (grouping students of different abilities in the same classroom), therefore MTurk can more accurately reflect the classroom beyond a university setting. 

### Challenges to Experiment Changes:

These changes while good in theory, could be hard to implement practically. The nature of the game could require more time than usual for MTurk tasks with would mean that the respondents would need stronger incentives to complete the game and assessments, meaning that it would cost more money. Second, there are many technological challenges to deploying the game in a format that is accessible via an online browser if the game was originally intended to be installed on a mobile device or computer. Finally, the pool of respondents on MTurk may not necessarily be generalizable to the point of bringing the findings into the classroom becuase they are most likely adults (i.e. over 18) and comparing cognitive learning styles between children and adults can be extremely difficult. 

### Citation

Chen, Z.-H., Chen, S. Y., & Chien, C.-H. (2017). Students’ Reactions to Different Levels of Game Scenarios: A Cognitive
Style Approach. Educational Technology & Society, 20 (4), 69–77.

# Alternative Assignment:

If you are unable to create a worker account on Amazon MTurk, you can complete this alternative assignment.

In the InfluenzaNet project a volunteer panel of people report the incidence, prevalence, and health seeking behavior related to influenza-like-illness (ILI) (Tilston et al. 2010; Noort et al. 2015).

1. Compare and contrast the design, costs, and likely errors in InfluenzaNet, Google Flu Trends, and traditional influenza tracking systems.
 
2. Consider an unsettled time, such as the swine flu outbreak. Describe the possible errors in each system.



### Compare and contrast the design, costs, and likely errors in InfluenzaNet, Google Flu Trends, and traditional influenza tracking systems.

When comparing the InfluenzaNet and Google Flu trends there are stark differences in how the data is captured. Primarly, we see in InfluenzaNet that respondents are required to fill out an online application containing questions about medical history, geographic and behavioral questions. Conversely, Google Flu Trends aggregated their findings using a logit model based on google searches for flu. With InfluenzaNet, there is an increased risk of self-selection bias, wherein respondents are only those people that choose to participate which could inherently bias the reporting. Furthermore, even with the questionaire and surveys, InfluenzaNet still has no way of varifying if the respondent is actually telling the truth or verifying tha accuracy of their answers to the screener. InfluenzaNet also runs the risk of dropout and attrition if people stop reporting the flue.

Conversely, Google Flu Trends only aggregates from search engine queries. Aggregating anonymized queries about flue trends cannot distinguish between, for example, someone who has the flue or someone searhcing for information about the flu. The latter of these realities can lead to false-positives in the model. Using these digitally enhanced tracking systems based on human collaboration also presents a cheaper alternative to traditional trackers. Because things like Google Flu Trends and InfluenzaNet utilize volunteers, the projects have sustained costs (e.g. webhosting, domain name, etc.) and the cost becomes even lower when considering Google Flu Trends because it aggregates information from queries and does not require one to explicitly volunteer. 

We can compare these reporting mechanisms to a traditional reporting center such as the CDC which uses medical records reported from doctors across the country. While The data capture may be more accurate and (potentially) more reliable, it comes at the cost of expediency. This is simply beause InfluenzaNet and Google are digital and a vast majority of medical reporting is not done digitally or has to be transcribed manually but medical professionals. Transcribing could be a low priority during flu season and therfore delay delivery of pertinent data, but also leave room for human error in the records. The delay in the data poses a significant drawback for traditional influenza tracking systems because by the time the information is published, flu season could be over. 

To sum, digitally enhanced reporting sites like InfluenzaNet and Google Flu trends emphasize speed and "real-time" data while sacrificing accuracy, while traditional reporting systems sacrifice expediency for accuracy. 

### Consider an unsettled time, such as the swine flu outbreak. Describe the possible errors in each system.

Applying the methodology of InfluenzaNet and Google Flu Trends so something like swine flu can pose several issus. The most innacurate methodologies for tracking swine flu would be Google Flu Trends. First, because swine flu proved to be a major news story, spikes in search terms would correlate with the amount of news coverage and not because people were suffering from the virus itself. Furthermore, aggregation based on symptoms presents another issue in that symptoms are very general and something like "sore throat" does not necessarily mean that the person searching has the swine flu. 

Using InfluenzaNet for something like swine flu also presents problems. InfluenzaNet is slightly more selective than Google Flu Trends in that there is a screener attached to voluntary reporting, however, the threat to validity persists because InfluenzaNet has no way of knowing if the respondent is telling the truth. Furthermore, the respondent to InfluenzaNet may not have been diagnosed by a doctor, rather, be self-diagnosing. Without medical training a respondent could mistake swine flu for the regular flue or another virus all together. The rate of attrition and dropout persist as well because people may not want to participate any longer after a period of time. 

As with Google Flu Trends, traditional reporting systems may not accurately capture or diagnose the swine flue. Because the risk of swine flu primarily pertains to people that work with animals, there is not a large risk for the general population. However, even if the general population had the same risk as those who worked with animals, the covarying sympotoms of swine flu and regular flu are such that swine flu could easily be mis-diagnosed as the flu. Issues of timeliness persist as well in that it may take a few days for a person to see a doctor before being diagnosed as well as getting the records transcribed and delivered to the reporting authority (i.e. CDC). 