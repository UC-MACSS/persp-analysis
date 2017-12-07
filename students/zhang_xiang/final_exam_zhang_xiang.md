## Perspective on Computational Analysis
### Final Exam: Evaluating Research Designs
#### Name: Xiang Zhang
#### Email: snzhang@uchicago.edu
#### Date: December 6th, 2017

### Question 1a: Research Design of Edelman and Luca (2014)
#### Summary of Research Design
In Edelman and Luca (2014), the authors use observational study methods to test the existence of discrimination in online marketplace (using the example of Airbnb). Using observational data of New York landlords on Airbnb, the authors measure the magnitude of discrimination by evaluating the rental price differences between black hosts and non-black hosts, and they find that non-black hosts charge much more than black hosts.

The research design of this paper could be break down into two parts, the data collection part and the data analysis part. In the following paragraphs, I will talk about these two parts separately.

For data collection, the authors first construct a dataset consisting of all listings on Airbnb for the Now York city as of July 17, 2012. The information of dataset includes the rental price, characteristics of the apartment, and the review information (for example, ratings). Secondly, they hired workers on Amazon MTurk to examine each listing's photos to construct a variable (which is used to control for apartment quality) for future use. Finally, they download all public profile pictures of New York hosts and hire workers on Amazon MTurk to code the race of the hosts.

For data analysis, the authors first draw summary statistics without any control. Through simple t-test, the authors find significant difference in the price charged by black hosts and non-black hosts. Then the authors turn to regression analysis and control for some observable characteristics to get better estimation. Finally, to test for the robustness of their results, the authors further try different regression specifications and find that their results are robust, which suggest that non-black hosts fo charge more than black hosts.

#### How They Leverage Computational Methods
As far as I can see, the authors leverage computational methods in the following two ways.

First of all, the authors make use of online big data. As they note in their paper, they collect the data themselves, which requires them to harness advanced computational technologies. Such tasks are quite easy for computers, but collecting information manually will be quite difficult. By applying advanced computational technologies, the authors successfully get the dataset to be used.

Secondly, they take advantage of mass collaboration in the form of human computation through Amazon MTurk. As we can see, to better assess the quality of the apartment, the authors hire workers on Amazon MTurk to rate the quality of listings on a seven-point scale. Also, to better identify the race of hosts on Airbnb, the authors hire workers on Amazon MTurk to code the race of the hosts. Conceptually, these two tasks are pretty easy for human beings, however, they are pretty hard or impossible for computers to finish. For example, the first task is about people's subjective ratings, which cannot be finished with computers. Similarly, the second task is about image identification, which can be quite difficult for computers.

### Question 1b: Research Design of Edelman, Luca, and Svirsky (2017)
#### Summary of Research Design
In Edelman, Luca and Svirsky (2017), the authors run a digital-enhanced online experiment to test for the existence and measure the magnitude of discrimination in online marketplace. More specifically, they create fake accounts and send fake messages to prospective hosts, by comparing the positive response rate of different treatment groups, they show that discrimination do exist. In this section, I will first describe the experiment preparation, which is an important part in their research design, and then describe the experiment process.

In their experiment design, the target hosts are those who offer properties on Airbnb in five USA cities as of July 2015, and there are four treatment groups, which are signaled based on the perceived race and gender (African American or white, male or female).

When preparing for the experiment, the authors first collect data on all properties on Airbnb in five cities and their hosts. After they have the hosts’ profile information, they hire MTurk workers to code hosts’ race, gender and age group. They also use Face++ to process guests’ information to detect whether the hosts have received African American guests before.

When conducting the experiment, the authors first created 20 Airbnb accounts, which are all identical except for the names. Among these 20 Airbnb accounts, 10 have distinctively African American male name, and another 10 have distinctively white names, with five for female and five for male within each group. Secondly, to justify that these names do signal races, the authors run a small survey which asks participants to categorize names in short time. After doing this, they sent 6400 messages to hosts between July 7, 2015 to July 30, 2015, with each message inquiring about the availability during a specific weekend in September. After sending the messages, they track the hosts' responses and classify the responses into six group. Finally, in their analysis, they compare the positive response of different treatment groups and do some heterogeneity analysis. More specifically, they regress whether getting positive response (a 0/1 variable) on several controls using regression methods and get their estimation of the magnitude of discrimination.

#### How They Leverage Computational Methods
As far as I can see, the authors leverage computational methods in the following three ways.

First of all, they scrap data and communicate with hosts using automated tools. These computational methods could save them a lot of time and human power. The authors collect information on roughly 6400 apartments, considering the number of characteristics each apartment has, the total number of data points could be super large, which cannot be finished in a short time without the help of computational technologies. Furthermore, they have to send fake applications to the apartment hosts and record their feedback, which cannot be done efficiently without utilizing computational tools.

Secondly, they take advantage of mass collaboration in the form of human computation through Amazon MTurk. As described in the paper, the authors hire workers to assess hosts' image to get their race, gender and age. This task is simple for human beings, but may be quite difficult for computers.

Thirdly, the authors use Face++ to process the information of previous guests. By using this API. The authors could get the past guests’ race, gender and age easily, which also save them tremendous time.

### Question 2a: Effectiveness of Research Design of Edelman and Luca (2014)
Edelman and Luca (2014) use observational study method to test for the existence of discrimination in online marketplace. In this section, I will discuss the advantages and drawbacks of their research design separately.

#### Advantages of Its Research Design
This paper takes advantages of many good features of big data.

First, the research design uses “big data”, and thus, they take advantages of the `big` feature of big data. As we can see, the dataset they collect contains rich information for their research. For example, in their regression, they control for many host characteristics, apartment characteristics and review information. By controlling for these factors which can also determine the rental price, the authors could get a more precise estimation on the magnitude of discrimination.

Secondly, the data is `non-reactive`. The target of this research is to test for the existence of discrimination, which is a quite sensitive issue to be talked about. Thus, if the researchers directly ask the guests about whether they won’t choose to live in black-hosts’ apartment, they might hide their true preference. However, the data on Airbnb is non-active and the authors can directly observe the rental price of both black-hosts and non-black hosts. After ignoring demand effects (as mentioned in the paper), they could estimate the magnitude of discrimination using observed price. Such non-reactive feature of the data provides them with a good opportunity to test for the discrimination.

Last but not least, it's `always-on`. This feature allows the researchers to observe the information they want any time. For example, the authors in this paper collect data as of July 17, 2012. Moreover, this paper only uses the data on a single day, however, such good feature allows them to further extend their research, which further support the goodness of their research design.


#### Drawbacks of Its Research Design
While the research design is overall good, there are still many limitations of it.

First of foremost, the authors get their result using data from only one city (New York), such `non-representative` sample will render their result unconvincing as it stands. Such use of non-representative sample might introduce systematic bias to the authors' estimation. The authors are talking about the digital discrimination on Airbnb, however, the sample they choose is neither a complete universe of all apartments (i.e. all apartments on Airbnb in the United States) nor a randomly select representative sample. Thus, the discrimination they observe may only be true in New York, but not on Airbnb as whole.

Secondly, the data from Airbnb may suffer the `incomplete` problem. As we all know, Airbnb does not require apartment hosts to provide all information about their properties, then we can expect a pretty high missing rate of some variables in their regression.

Thirdly, the data itself is `dirty`. That is, the data collected from Airbnb is not well-formatted. Furthermore, the authors have to process pictures to get more information. For example, the authors hire workers on Amazon MTurk to better code the race of hosts and evaluate the apartment quality, which will cost lots of money.

Fourth, since the rental data might `drift` over time (for example, during the holiday, the rental price might increase), then the estimated magnitude of discrimination might actually change over time. In this research, the authors only use rental price in a single day to estimate the magnitude of discrimination, in this way, they might possibly get a biased estimation.

Moreover, the data could be quite `sensitive` and may involve some ethical issues. Firstly, it's not clear whether collecting data from Airbnb without the permission from the company is legal or not. Secondly, the information they collect includes some personal information, so they might have to inform the hosts the use of their information, or at least, they should ask Airbnb for permission on the use of data.

Last but not least, it's hard to go directly from observational data to `causal mechanisms` using just a cross-sectional data. As we all know, even the authors control for many factors relating to the apartment quality and the hosts' demographic background, it is still impossible to say the correlation they observe to be causal. There are still many unobserved factors related to race that can affect the rental price. In this way, such research design cannot support a causal claim.

### Question 2b: Effectiveness of Research Design of Edelman, Luca and Svirsky (2017)
#### Advantages of Its Research Design
The first advantage of the research design is its ability to draw `causal inference`. An evident advantage of using experiment to study social problem is its ability to draw causal inference. Unlike Edelman and Luca (2014), the evidence provided in this paper strongly support the existence of discrimination in online marketplace.

Secondly, this research design allows the authors to test for some of the `mechanisms` through which the discrimination might affect hosts’ decision, Although the authors did not directly detect through which channels discrimination affect people’s decision, they did rule out some possibilities. For example, in the paper, the authors hypothesized that neighborhood characteristics may affect the extent of discrimination, however, they actually found no such effect. Another example is the test of Becker’s racial discrimination theory (Becker 1957). In the paper, by conducting sub-sample analysis, the authors found no support for the theory.

Thirdly, the authors explore some of the `heterogeneities` in the treatment effects. First, they run regressions by subgroups (by gender, age group, for example) and they found no evident heterogeneity exists.  Secondly, they run regression by whether the hosts have received African American before, then they find that the discrimination exists in a subset of the whole population.

Last but not least, the experiment design is `valid` in some perspectives (though I will discuss the invalid part in the next section). First of all, it is statistically valid in some sense (I will discuss its statistically invalid in next section) since the authors are actually using standard evaluation strategy of Randomized Control Trails (RCTs). Also, the internal validity was high because they use digital-enhanced technologies and make sure the treatment is delivered as designed and the outcomes are digitally recorded. Moreover, the research design is construct valid. In this paper, the authors want to test for the existence of discrimination and their research design directly address this issue.  

#### Drawbacks of Its Research Design
Although the research design has many advantages regarding drawing causal inference and exploring heterogeneity, there are still many downsides of the research design.

##### Validity
When assessing whether an experiment design is good or not, the first thing we should keep in mind is its validity. As discussed above, the authors’ research design is valid in terms of internal validity and construct validity, and in terms of statistical validity in some sense. However, the external validity of this research design might be quite weal in this research.  

External validity asks the question of whether these findings can be generalized to other situations (Salganik 2017). However, due to the block of Airbnb, they only get apartment listings in five cities. The question is, can the five cities selected be representative of all cities in the United States? The answer might be no. If so, their estimation results might not be directly applicable to other cities in the United States. Secondly, I noticed that the authors created their Airbnb account with no profile pictures. However, in Airbnb, many users have their profile pictures. Since they don’t have profile pictures, the cautious hosts might choose not to respond to the messages. In this way, the response the authors get are not representative of all hosts on Airbnb, in this way, the magnitude of the discrimination they get cannot be used to infer the discrimination on Airbnb.

Also, the experiment is statistically invalid in some sense. As noted by the authors, they should collect 10000 responses based on the power analysis. However, since Airbnb shut down the experiment accounts after they collect 6400 responses, they can only do their analysis using the data they have. In this sense, the statistical power of the estimation is weakened, which in some sense is statistically invalid.

##### Causal Mechanisms
In this paper, the authors found no evidence that neighborhood characteristics and distaste for interactions are the channels through which discrimination cause worse outcomes for guests with distinctively African American names. However, they provide no clear explanations for why the worse outcome do exists. As noted in their paper, “Our findings cannot identify whether the discrimination is based on race, socioeconomic status, or a combination of these two”. Thus, the research design could be improved if it can test for the existence of such channels.

### Question 3: Value-added of Conducting Both Research Projects
These two papers both test for the existence of discrimination in online marketplace, with one using observational study methods and one using experiment design. Combining this two research together, we can actually learn much more.

Firstly, the observational study focuses more on `finding the patterns` in existing data but not good at `drawing causal inference`. As noted in Salganik (2017), in observational study, there are generally many confounders which might "wreaks havoc on researchers’ ability to answer cause-and-effect". However, on the other hand, experiment design could directly create data and draw causal relationships. In the context of these two papers, the authors want to find evidence supporting the existence of discrimination in online marketplace. However, in Edelman and Luca (2014), even the authors control for as many factors as they can, they cannot control for all confounders. As a consequence, even they detect clear patterns in the discrimination (large difference in rental price between black and non-black), they can say nothing causal since there might be other unobserved factors other than discrimination that drive this difference. Things are different in Edelman, Luca and Svirsky (2017). In this paper, the authors directly test the existence of discrimination using a randomized control trails design. In this way, the difference in the response rate between African American guest and white guest is the consequence of discrimination. Thus, while the 2014 paper can only reveal some patterns of discrimination, the 2017 paper directly measures the consequence of it.

Secondly, however, the experiment design might in Edelman, Luca and Svirsky (2017) suffers from the `external validity` issue, the observational study in 2014 can somewhat alleviate such concern. As I mentioned above, the researchers created fake account with no profile picture, no past transaction records and no valuable information, which is quite different from actual users. However, the observational data directly use real-world data, which can largely attenuate our concern on external validity. By using observational study methods, we are actually analyzing what is going on in real-world, in this way, the results we get is more external valid.

Thirdly, the Edelman and Luca (2014) paper focus more on the describing patterns of discrimination in demand-side (the renters). However, in Edelman, Luca and Svirsky (2017), they focus more on the discrimination from supply-side (apartment owners). In the online marketplace, both supply and demand side play an important role. Combining these two papers together, we can see a clear picture that discrimination exists in both side and thus we can have a better understanding of the real situation of discrimination.

### Question 4: Digital Survey-based Research Design
The primary question of interest of these two papers is whether discrimination in online marketplace exists and how large is it. In this section, I proposed a digital-enhanced survey to try to test for both supply-side discrimination and demand-side discrimination.

#### Survey Design
Basically, I will conduct my survey on Amazon MTurk, the survey will be in a wiki-survey form and mainly contain two parts, the filter questions and the survey questions.

The first part of the survey is consisting of several filter questions. In this section, I will ask about respondents’' demographic background and their user experience of Airbnb.
- Firstly, I will ask them about their age group, gender, education level, city/town they live in and their race.
- Secondly, I will ask them _"Are you a host on Airbnb?"_ and _"Have you ever used Airbnb?"_.
  - If the respondent’s answer to these two questions are "No", I will thank him/her and end the survey.
  - If he or she is the host on Airbnb, then he or she will be lead to the `Host Survey` block.
  - If he or she is the user of Airbnb, then he or she will be lead to the `Guest Survey` block.
  - If he or she is both host and user, then he or she will be lead to both `Host Survey` and `Guest Survey` block.

Secondly, the respondents will be directed to their corresponding blocks (`Host Survey` or `Guest Survey` or both). In my design, the `Host Survey` is mainly used to test supply-side discrimination and the `Guest Survey` is mainly used to test demand-side discrimination. I describe the block design in detail below.

In `Host Survey`, the respondents will be asked about _"What are the reasons that you reject the application of a guest?"_. I will provide several choices (for example, guests' nationality, gender, age, race, etc.) for the respondents to choose from and they can choose multiple answers one time. After they made their choice, the computer will record their answer. If they say they care about guests' race, then I will direct them to a "case study" section. In this section, I will provide them with five fake guest profiles which are identical except for the name of guests. Following Edelman, Luca and Svirsky (2017), some of the names will signal African American roots, and some of the names will suggest the guests are white.

In `Guest Survey`, I will do similar surveys as the `Host Survey`. In this section, the respondents will be asked about _"What are the reasons that you choose not to rent certain apartment on Airbnb?"_. I will provide several choices (for example, the location of the apartment, the size of the apartment, the race of the hosts, etc.) for the respondents to choose from and they can choose multiple answers one time. After they made their choice, the computer will record their answer. If they say they care about hosts' race, then I will direct them to a "case study" section. In this section, I will provide them with five fake hosts profiles which are identical except for the name of guests. Again, following Edelman, Luca and Svirsky (2017), some of the names will signal African American roots, and some of the names will suggest the guests are white.

Finally, in both `Host Survey` and `Guest Survey `, to reduce potential bias, 40% of those who say they donot care about hosts'/guests' race will be directed to "Case Study" section to test whether they really donot care about hosts'/guests' race.

#### How Can This Survey Design Answer the Research Question
After conducting the survey, I can first, compute the proportion of hosts/guests who care about guests'/hosts' race. Furthermore, as a double check, by having a "case study" section, I can further check whether the hosts/guests really care about the race of guests/hosts.

One may wonder why I do not directly lead the respondents to the “case study” section, but instead, I ask them to first report whether they care about race. The reason for doing this is because not everyone was able to detect the race of someone from their name. As can be seen in the online appendix of Edelman, Luca and Svirsky (2017), 26% individuals are not able to tell that “Jermaine Jones” is an African American Male and 12% individuals are not able to tell that “Greg O’Brien” is a white female. Thus, to minimize the bias caused by such recognition error, I first ask about the preference directly and then use the “case section” to double check the answers.

#### Potential Drawbacks and How to Overcome
A potential drawback of the survey design is, when asked about _"whether you care about hosts'/guests' race"_, people may hide their true thoughts since they know they are been surveyed. To minimize the bias, as you can see, no matter whether the respondents say they care about race or not, they have a chance to be directed to the "case study" section (40%). Since I have data on “revealed discrimination” (although there might be some bias caused by recognition errors), I can somewhat adjust for my results on “reported discrimination”. Also, I will inform the participants that the survey is for academic-use only and I will encourage them to express their true thoughts.

Secondly, I may face with some non-response issue since people may quit the survey before they finish it. In this way, I may use the demographic background to predict the likelihood of quit and adjust for the sample weights of those “unfinished sample”.

Thirdly, the composition of population on Amazon MTurk might be different from the composition on Airbnb. For example, the people on Amazon MTurk might have higher education level and their job might be more related to computer science/ social science. To address this issue, I will assign different weight to the survey respondents based on their demographic background.

**My answer ends here, thank you!**

### Reference
Becker, Gary S. The economics of discrimination. University of Chicago press, 1957.

Edelman, Benjamin G., and Michael Luca. "Digital discrimination: The case of Airbnb. com." (2014).

Edelman, Benjamin, Michael Luca, and Dan Svirsky. "Racial discrimination in the sharing economy: Evidence from a field experiment." _American Economic Journal: Applied Economics_ 9, no. 2 (2017): 1-22.

Salganik, Matthew J. 2017. Bit by Bit: Social Research in the Digital Age. Princeton, NJ: Princeton University Press. Open review edition.
