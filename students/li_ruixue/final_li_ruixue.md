
# Evaluating Research Designs 
## Li Ruixue

  
  
## Introduction 
In this essay, I'll evaluate two papers on discrimination in the digital market: Digital Discrimination: The case of airbnb.com (Edelman and Luca, 2014) and Racial discrimination in the sharing economy: Evidence from a field experiment. (Edelman, Luca, and Svirsky, 2017). Both papers studied racial discrimination on Airbnb.com, a popular online marketplace for short-term rentals where individuals can rent out their properties ranging from one room to entire dwelling, and the researchers were able to identify the existence of discrimination against black hosts and black guests in both studies. I'll start the remaining part of this essay with a summarization and evaluation of the research design for each paper, with a focus on computational social scientific methods, followed by a discussion on the value-added of the two research studies, and in the end, I'll propose and analyze how a survey-based research design could answer the same research questions. 

## Evaluate individual research paper

1. Edelman, B. G., & Luca, M. (2014). Digital discrimination: The case of airbnb.com. Harvard Business School NOM Unit Working Paper, (14-054).
    
### Summarization of the research design

#### Research question: 

This research empirically investigates the extent of racial discrimination against landlords. More specifically, the researchers want to find out whether black hosts on Airbnb.com charge less price for similar rentals than non-black hosts due to their race.

#### Data:
A snapshot of listings contained on Airbnb for the city of New York as of July 17, 2012. The researchers collected the listing price, the characteristics of the host (), the characteristics of the apartment, the number of guests who left reviews, average rating for each host characteristic. The researchers also produced data on the subjective quality of each listing on a seven-point scale by hiring workers on Amazon Mechanical Turk to visually examine each listing's photos. The race of the hosts was determined by having workers on Amazon Mechanical Turk to look at their profile images and code their races into categories. 

#### Method:
This research used an observational research approach, and if we employ the sub-categories under the observational approaches classified Bit by Bit(Salganik 2017), it falls under the counting things category.   
  
The dependent variable in this study is the rent charged by non-black and black hosts, used by the authors to quantify the discrimination faced by black hosts. Though the authors didn't spend too many words justifying their choice, from an economics perspective, I think that their choice is wise since rent is relatively easily observable in this case, and under a competitive and transparent online market with a large amount of transactions like Airbnb, it's a good reflection of the bargaining power the hosts have, which will likely incorporates the racial discrimination they are subjected to if there's any.   
  
The empirical analysis in this study is mainly done by running linear regression of rental price on some possible determinants of price. The authors first presented results when the independent variables do not include the race of the host, and then with the host being black as a dummy variable. They found that the rental price increases with number accommodated of the property, rating for its location, and social network presence of the host, which is consistent with intuition and preliminarily validated the correctness of their method. They then included an extra indicator for black hosts and run a series of regressions with different model specifications, and concluded that controlling for all other factors, non-black hosts earn roughly 12% more for a similar apartment with similar ratings and photos relative to black hosts. 

### How the research design leverages computational methods to ask and answer a question 
This reserach is a good example of computational social science research.   
  
Firstly, this research question wouldn't even be asked if large-scale share economy, enabled by modern computers and networks, didn't come into existence in the first place. While discrimination in offline markets, as mentioned by the authors, have been relatively thoroughly studied, discrimination in the digital market is a relatively new phenomenon and not sufficiently documented. Therefore, the research itself is the result of increased computational power humans have.     
  
The research question also wouldn't be answered without computational methods. Being an observational study, the data is the key, and the data used in this research is scraped from the Airbnb site with digital methods. Collection of data of this scale would require a lot of manpower and time in the past, but with some programming and data processing skills, it's becoming quite manageable for individual or small groups of researchers.     
  
Besides data acquisition, this research also features another important characteristic that's unique to computational researches, mass collaboration, or more specifically, human computation. There were two cases in this study where the researchers hired workers on Amazon Mechanical Turk to complete small, simple to human and difficult to computers, yet tedious and time-consuming tasks of identifying the race of the hosts and the subjective quality of the listing. Doing so significantly lowered the costs of conducting this research, since the other option - employing research assistants or students to do it - is likely to be more costly. Also, humans have better accuracy in this type of tasks, improving the quality of the data the researchers were able to gather. However, they did not mention whether they built in some redundancy in these tasks, i.e. having multiple workers to look at a same picture, as they did in the later paper, which might compromise the accuracy of the results to some degree.   
  

### Evaluation of the paper
Since observational data and regressions are the keys to this research, I'll discuss the effectiveness of this project from these two perspectives. 
#### Big data: 
The authors used 3752 observations in their study. While this number is certainly not as impressive as some researches in the digital era where number of observations can be in the magnitude of millions, the data demonstrated many characteristics of big data, both that are good for research and those that are bad.  
  
On the positive side, while having thousands of observations itself alone doesn't eliminate the problem with making causal inference from observational data, it makes the study more statistically robust compared to one with a small number of observations. The characteristic of being big also allows the authors to look at some subgroups in order to conduct a robustness check where they compared black hosts to both all non-black hosts and white hosts only and found that the discrimination is present in both cases. Big data is also always-on, and while this research only looks at a snapshot of Airbnb data at one point in time, the fact that Airbnb is always-on makes it possible for others to replicate the study with the same scope, large scope, or data in the future, thus verifying the conclusion and possibly making the causal inference more solid. The non-reactive characteristic of big data is very prominent here, as by scraping public available data and not interacting with any user on Airbnb, the users will not change their behavior in the market. In other words, they will not consciously hide their racial discriminating behavior if they have any, unlike in an experiment or survey where if the participants are aware of the purpose of the research, they will consciously or unconsciously try to conform to the social norm of non-discriminating behavior.     
   
However, this dataset also couldn't avoid some common pitfalls of big data. First, it's incomplete. In fact, the key explanatory variable the researchers want to look at - the race of the host, was not included in the data available online. Luckily, the authors were able to deal with this problem by using computational methods as discussed above. Second, some data is inaccessible. In fact, the authors themselves mentioned that ideally they would also like to study the situation on the demand side, but weren't able to since Airbnb was not willing to provide internal data on guest requests etc. Since as the authors discussed, Airbnb probably doesn't have much incentive to reduce the racial discrimination on their platform and therefore doesn't have much incentive to share data either, so this was one hurdle that they were not able to overcome in this particular study. Third, this dataset is not very representative in two ways: first, Airbnb users are not a perfect representation of users of all digital markets, since the fact that they own vacant properties at least says something about their economical status, and second, the hosts in NY studied in this paper may not be representative of the whole of US since it's often being said that NY is very different from the rest of the US, especially the rural areas. Fourth, while drifting and algorithmic confounding are not major concerns in this paper as it only studies a snapshot of the data, it may become a concern for future researchers who wish to replicate the study. Fifth, the data is certainly dirty, since hosts and guests could post whatever they want on their listings and profiles, as long as it's within Airbnb's regulation. We can easily imagine that the guest ratings may be biased because those who have extreme opinions are more likely to leave reviews, or the host may care enough to adjust his or her listing price according to market demand, introducing noise in both the dependent and independent variables. Finally, while one could argue that the data on Airbnb is publicly available, there's certainly personal information that could be sensitive. And since the researchers distribute the photos of the hosts to Amazon Mechanical Turk workers, privacy may be a concern for the hosts. Though the users may have agreed to some super long Terms of Use that they've never read when they registered for Airbnb agreeing to share they data for internal research, it's hard to imagine that Airbnb would include a clause saying that their data may be scraped and used by external researchers, so the ethical concern here is not non-existent.      

#### Empirical method

As for the design of the empirical analysis, the regression method used in this research is straight-forward. I've already discussed that the authors did a good job in quantifying the racial discrimination and coding the race of the hosts as well as the subjective quality of the listing by using computational methods, and that the results are robust no matter non-white non-black hosts were included in the comparison. Though they were unable to disentangle taste-based and statistical discrimination, one study can't achieve everything. However, I would like to look at the R^2 or adjusted R^2 of their regression results, since they didn't report that in the paper.   
  
Overall, I think this research employed computational methods well to answer a relatively new research question. 

  

2. Edelman, B., Luca, M., & Svirsky, D. (2017). Racial discrimination in the sharing economy: Evidence from a field experiment. American Economic Journal: Applied Economics, 9(2), 1-22.

### Summarize the research design

#### Research question: 
This research studies racial discrimination in the sharing economy by focusing on finding out whether guests face racial discrimination in online rental market. More specifically, the researchers wanted to see whether African Americans are less likely to be accepted as guests on Airbnb compared to guests of other races.

#### Data:
The researchers collected data on all properties offered on Airvnv in Baltimore, Dallas, Los Angeles, St. Louis, and Washington, DC as of July 2015, including information about one randomly selected listing per host, data from each host's profile page, whether the host has multiple listings, whether the host has reviews from at least one African American guest, etc., by scraping the website using automated tool. They also hired workers from Amazon Mechanical Turk to identify the race of the host, and used the geographical location of each listing, linked to a census tract, to access the demographic data of the neighborhood that the property is in. They also checked each listing's availability approximately 8 weeks after their experiment.     

#### Method:
This research used a mainly experimental design combined with observational data.   
  
The gist of the experiment is using fake accounts that are designed to look like a white or black person to send inquiries to potential hosts, and measure the difference in response they get.   
  
The researchers created 20 Airbnb accounts that were identical in all respects except for guest names, which were distinctively black male, black female, white male, white female. The hosts were then randomly assigned to four treatment group, where they were each sent a message from one group of the fake accounts enquiring about one weekend that's about 8 weeks later. The researchers sent out 6400 messages in total with automated tools and tracked their response over the following 30 days. They then had a research assistant to code the responses into a few categories, ranging from definite yes to definite no.   
  
They then conducted a series of statistical and regression analysis of the host acceptance on a few model specifications including the race of the guest requesting accommodation, including: regressing host acceptance on guest race and host characteristics, on host and guest races alone, plotting host responses by category and guest race, looking at proportion of positive responses by race and gender, regressing host acceptance on more host characteristics and location characteristics, and looking at responses received by name of the account. They also compared their results with observational data to make sure that their accounts are not very differently in terms of quality with real accounts. In the end, the researchers estimated the money value that discrimination has cost the hosts by calculating the revenue lost of those listings that were still empty on the day they enquired.   
   

### How the research design leverages computational methods to ask and answer a question
This research, again, is very computational. First, the collection of data and delivery of treatment were all conducted using the automated tools they designed, without which a study like this would involve a large amount of manpower and monetary cost and may even become infeasible. Also, the use of automation reduced the chance of human errors. Second, as in the previous research, this study also employed Amazon Mechanical Turk workers to identify the race of the hosts, and they also built in some redundancy to increase their accuracy by having multiple workers looking at the same image. They also used the workers to category the hosts into age groups to be used in the later stage of the analysis, and though they mainly used face-detection to identify the past guests' race, they introduced AMTurk workers to improve the accuracy of the prediction by computers. The face-detection API, Face++, is the third computational component in this study's methodology, enabling even faster identification of race from profile pictures. Lastly, they combined the location data of the listings with census data to create a measure for neighborhood demographics, which I think is another excellent use of computational methods. 

### Evaluation of the paper
In evaluating this research design, I will again look at the role that big data played, as well as the experiment's internal and external validity, heterogeneity of treatment effects, and causal mechanism. 

#### Big data:
While this research is experiment based, big data still played an important role. Though how big the number 6400 is up for debate, the characteristics of big data are still prominent here.   
  
As for the good characteristics, having big data enabled the authors to identify enough users to run a relatively large-scale experiment with enough number of hosts in each treatment group. The always-on characteristic allowed the researchers to check the availability 8 weeks after the experiment, thus letting them estimate the cost associated with discrimination. Since this is an experiment, the researchers needed to interact with the user, but given the already huge size of the market on Airbnb at the time of this study, this experiment was not very likely to create a noticeable disturbance in the market.  
  
As for the bad characteristics, first, again there is some incompleteness in the data, such as the race of the host and guests leaving reviews and the neighborhood demographics, where were well dealt with by the authors with computational methods discussed above. As for inaccessibility, Airbnb didn't share data as before, and during the experiment, the researchers' tools for logging into guest accounts and communicating hosts were also blocked after they collected data for 5 cities, curtailing their original plan for studying all the top 20 metropolitan areas, making the data less representative as it's supposed to be. Also, rural areas are again not included, reducing representativeness. Drifting also emerges as a potential drawback here because by the time they checked the availability of the listings they experimented on 8 weeks later, some of them had already become unavailable, compromising the validity of their estimate on the cost of discrimination. The author also mentioned that there's a possibility that their accounts may be flagged as spam, especially those with distinctively black person names, which shows that there's a likelihood for algorithmic confounding. Finally, the data could again be dirty due to many reasons including human errors and inaccurate information users provided online, and the some of the information is sensitive as discussed for the previous paper. Moreover, some hosts may have made some more personal information available, such as their name or phone number, after accepting requests from the bogus accounts created by the researchers, making data privacy more of an issue in this research.   

#### Validity:
* #### Statistical conclusion validity: 
With the help of statistical software, I will expect the regressions were run correctly in this paper. However, since the authors revealed adjusted-R^2 in this paper, I noticed that they had very small adjusted-R^2 for all of their models. Whether this posts a serious issue in statistical conclusion validity may need further mathematical discussion, but since they never tried to build a model trying to include all variables tells me that maybe it's because the researchers were not interested in building a complete model explaining what determines whether a host accepts a guest. 

* #### Internal validity:
I think the researchers took great care to ensure the internal validity of their research this time, and in general they achieved internal validity. For example, they had more than one AMTurk worker to look at each host photo to identify host race, decreasing the chance of human errors. They also randomly selected one listing per host to prevent hosts from receiving identical messages and therefore realizing that something's going on. Meanwhile, the automated process generally tends to be less error-prone. Therefore, in general, I think they delivered their experiment cleanly and professionally. 
* #### Construct validity:
There are two main relatively unconventional constructs in this research: host response rate as an indicator for racial discrimination, and price of vacant listings as forgone revenue, and therefore as cost of discrimination to the hosts. In general, I think that they creatively found a way to quantify these two hard-to-measure concepts. Though there are many potential determinants for a host's response, but by having a large sample size, careful randomization and control, the effects of other factors should be evened out. Meanwhile, the way the cost of discrimination was essentially calculated as its opportunity cost, which I find reasonable.   

* #### External validity:
Though the researchers couldn't study all the 20 cities as they planned to and were only able to study 5, I think that since their methods were valid and results robust, external validity should be largely preserved, at least in the US and on similar digital markets where the race of the buyer or seller are known. However, as for the cases in other countries or on digital platforms where the market work differently, for example, on an auction platform, it's questionable whether the results will still hold.   
  
It's worth mentioning that the authors explicitly checked for external validity on Airbnb platform by comparing their results with observational data.  

#### heterogeneity of treatment effects, 
The researchers put in great effort in identify in heterogeneity of treatment effects, and they produced a very thorough analysis. They looked at host and guest race/gender, host characteristics, location characteristics (diversity of neighborhood), breakdown by names of the guests, and even looked at a subgroup of hosts with at least one review from black guests, though the results was not highly significant in that subgroup. However, the authors mentioned that since they couldn't reach their target sample size of 10,000 responses, which was calculated by a power analysis to be the necessary number for certain subgroup analysis such as African American hosts, they ended up not performing that part of the analysis. Therefore, the heterogeneity of treatment effect could be further studied by increasing the sample size.   

#### Causal mechanism
As mentioned by the author themselves, while the experiment identified a causal relationship between race and host acceptance, they could not pinpoint the exact mechanism of this effect. For example, they could neither identify whether the discrimination is also related with the socioeconomic status implied by names nor distinguish between taste-based or statistical discrimination. They did shed some light on this distinction with the analysis of hosts who have previous reviews from black guests. Though they have already looked at a lot of different factors in this study, therefore I wouldn't blame them for not looking into causal mechanism more, but I do think that there's room for further studies on causal mechanism. For example, slight variation in treatment delivered, like something in the guest profile or message indicating different socioeconomic status, could be used to uncover some mechanisms. 
  
Overall, this research did better and more thoroughly in many aspect than the previous paper, and I think they found some interesting and robust results.  


### Value-added of conducting both research projects

I think these two research projects work really well to reveal a whole picture of racial discrimination, probably as the researchers intended them to be.   
  
The two projects each looked at one side of the market: the 2014 paper on the supply side and the 2017 paper on the demand side. In the 2014 paper, the authors mentioned that ideally they'd like to look at demand-side also but couldn't, due to inaccessibility of guest data. In 2017 paper, they not only overcame this problem and completed the demand side's story, but also established causation by running an experiment.   

They selected the right method for the right research question. If we were to reverse the research designs for the two studies, we'll find that it's hard to conduct an experiment identifying whether guests will discriminate hosts, since that'll probably involving setting up fake listings and rejecting many requests from potential guests, or having a hard time finding real hosts to participate in the study and designing a complicated experiment. Theoretically, if we have access to Airbnb's internal data, we could use the requests and responses by real guests and hosts to study the discrimination faced by guests, but that will involving controlling for many factors that might affect host response. A method that could potentially make observational approach work is using matching to identify pairs of guests and hosts that differ only by their race, but that would also be extremely difficult given the fact that there are many subjective information, such as the appearance of the guest or host, that are hard to quantify and match. Therefore, by employing both observational and experimental methods, the researchers were able to measure the discrimination faced by both the hosts and the guests relatively easily and accurately.   

Since these two research projects were done by the same group of researchers, the 2017 research made good use and improved some of the methods that were used and tested in the 2014 study, such as using Amazon Mechanical Turk workers for racial identification. Besides, since the later is also larger in scale, used an experimental approach which requires more preparation and faced more ethical and logistical problems, is more careful in controlling human errors, and more thorough in analyzing heterogeneity in treatment effect, I think that the researchers used the 2014 research as a smaller-scale preliminary study for their bigger ambition of studying discrimination in the digital market.   

The two studies also differed in their scope, with the 2014 one only looking at New York and the 2017 paper looking at 5 other cities. Since one of the drawbacks of the 2014 research is that it only studied New York, which is a city that's somewhat unique, the 2017 study complimented it by extending the scope to other cities and showing that online racial discrimination is present beyond New York. However, I don't think that combining these two research projects will generate perfect external validity yet, since they looked at different sides of the market and both of them are still limited to large metropolitan areas in the US. I would love to see the later study include New York to complete the full picture for its racial discrimination on Airbnb.  

Also, both research projects faced similar limitation, which is unable to identify the causal mechanism. More specifically, the author mentioned that they were unable to differentiate taste-based from statistical discriminations.   


### Consider how you could apply a digital survey-based research design to the primary question of interest from these two papers. What are the potential drawbacks to a survey approach? How might you overcome these drawbacks?

By using a survey-based research design, I could attempt to answer the question of interest from both the two papers, namely, whether there's racial discrimination on Airbnb for the hosts or the guests. I also think a survey study could be the key to uncovering the causal mechanism. However, whether Airbnb is willing to cooperate in delivering the survey could make a big difference. I'd like to focus my discussion on the case where Airbnb doesn't cooperate, and touch on the case where it does at the end.   

#### Survey design: 
Borrowing the constructs for biases used in the two papers discussed above, I would have two surveys, one measuring supply-side discrimination and one measuring demand-side discrimination.   
  
* #### Supply-side: 
The purpose of this survey is to measure whether the price that the guests are willing to accept for a certain property is affected by the host's race. Therefore, we will have many pairs of hypothetical listings, with each pair differs only in the race of the host. The race of the host could either be communicated to the respondents via names that are distinctively black or white, or via photos which have been controlled for attractiveness in other studies. We would then ask the respondents what price they are willing to accept for this particular listing. Meanwhile, we'll also need to collect demographic information of the respondents.   
* #### Demand-side: 
In this survey, we'll assign the survey taker an identity of a host on Airbnb, and ask them whether they'll accept the requests from the hypothetical guests we created. The hypothetical guests will also be in pairs with all other attributes identical and only different races. The way we communicate the ethnicity of the guests will be the same as the previous study. Also, the respondents' demographic information needs to be collected. 

#### Format and distribution method
There are a few choices of getting people to fill out the survey.   
  
For one, we could administer this survey via Social Networking Sites (SNS), and if we do we also have the option of gathering the demographic data of the respondents from their SNS. Of course, that would pose potential ethical issues and is an area that needs to be tread carefully, but one possible way of dealing with this controversy is to state specifically when they open the survey link that by agreeing to take this survey, they agree to have their certain personal information accessed by the researchers who are these distinguished professors from this renowned university. SNS users are generally accustomed to seeing such pages when they want to login or open something with their SNS account, so this shouldn't turn too many users away. While distributing surveys on SNS, we could use some digitally-enhanced survey methods such as making the survey into a mini-game where people could play and compare scores with their friends.  
  
Alternatively, we could also employ workers on sites like Amazon Mechanical Turk. In this case, we need to take some measures, for example, including questions to check whether the workers are reading the instructions, to ensure that the responses are valid.  
  
Lastly, in the unlikely event that Airbnb agrees to participate in this research, we could send links via their internal announcement or messaging systems to users. Of course, this would be an ideal case as the respondents are the more representative.

#### Data analysis
We're likely to use a regression-based approach to analyze the data we obtained from surveys, and the methods should be similar to what the authors of the papers have used. However, we do enjoy a cleaner and more complete dataset with survey answers and the results are potentially more accurate.  
  
 
There are a few benefits and drawbacks of using this survey design I mentioned, which I'll now discuss.

#### Benefit: better validity
Since we have full control over the content of the surveys and we can deliver it to many places around the world, we could improve the internal validity and construct validity of our survey by carefully designing the questions and improve the external validity by having people from a larger geographic location. Statistical validity is also more under control since we're now getting cleaner and more controlled data.

#### Benefit: uncovering causality
Since surveys are hypothetical, we are free to ask a wide range of questions and observe the characteristics that we're interested in, which gives us the ability to ask questions that help us find out the causal mechanism.   
  
For the supply-side survey, we could ask what factors affect their decision in pricing the hypothetical properties. For example, we could ask participants what they like and dislike about the apartment, or the reasons that they think they apartment should be charged less/more for. For the demand-side survey, we could ask the participants the reasons they reject the hypothetical guests. 


#### Potential drawbacks: 
There are three major concerns I have.     
  
First, depending on how we end up administering the survey and who we end up delivering it to, the sample of responses we get may not be as representative as we want them to be. For example, we might get more responses from people who have more free time, therefore implying certain socioeconomic status, or from people who use SNS more. Luckily, this problem could be dealt with reasonably well with statistical methods such as post-stratification.     
  
Second, people's responses under a survey setting may differ from what they'll do in real world. While this is a drawback that's inherent to survey-based approaches, there are always worse and better ways of asking that could induce the survey takers to give answers that are closer to their real opinions. For example, instead of asking them directly what price they are willing to pay for a listing or how much they think the host should charge, we could ask them to play an interactive game where the price is gradually lowered or increased until they become willing or unwilling to accept the price, revealing their true preferences.    
  
Third, if the participant could guess what the purpose of the research is, they may tend to show less discrimination in their answers consciously or unconsciously. To minimize this reactivity, we'll need to make sure that a participant doesn't ever see two listings or two guests that are in the same pair, i.e. identical except for races. We can also use some deceiving in our wording, for example, stating that the research objective is to study how prices on Airbnb is determined, and provide more unrelated options in our questions for identifying causal mechanisms to mask our true purpose.    
  
Overall, I believe that if used correctly, survey-based approach will definitely be a powerful tool in studying discrimination of digital markets.  
  

## References

Edelman, Benjamin G., and Michael Luca. 2014. "Digital Discrimination: The Case Of Airbnb.Com". SSRN Electronic Journal. doi:10.2139/ssrn.2377353.

Edelman, Benjamin, Michael Luca, and Dan Svirsky. 2017. "Racial Discrimination In The Sharing Economy: Evidence From A Field Experiment". American Economic Journal: Applied Economics 9 (2): 1-22. doi:10.1257/app.20160213.

Salganik, Matthew J. 2017. Bit By Bit, Social Research In The Digital Age.

