# Assignment 3 - Proposing an Experiment - IMDb ratings

## Laurence Warner

### October 2017

### Previous research question

Before exploring my new proposal, I wanted to discuss why I felt an experiment was unsuitable for my previous research question: "Which Chicago venues are most associated with extreme binge drinking?".

Firstly, this question is descriptive, it is not causal. It is merely seeking to empirically measure facts about the social world. Hence, my observational study - "Puke Index" - and survey - "Beer King" - were suitable to the task of gathering this information. We don't necessarily need to identify causal mechanisms - is binge drinking occurring in certain bars due to the people it attracts or the attitude of the bars? If we did want to identify that, then a randomized controlled experiment may be useful in theory. For example, we would want to recruit groups of drinkers and randomize the bars they go to, and then somehow measure their drinking.

However, the problem is that this field experiment is very costly and difficult to perform, largely because it is so difficult to digitize.

1. Recruit
People drink in groups, and it is difficult to recruit "like" groups of drinkers as subjects.

2. Randomize
Allocate groups to different bars.

3. Intervene
Send groups to different bars. If we want to gain a good picture of all of the Chicago venues, the sample size is going to have to be huge to include all Chicago bars. Also, groups of drinkers are difficult to control: i.e. keep in one place.

4. Measure
Subjects will be resistant to researchers measuring their drinking. Also, they will probably exhibit the Hawthorne effect - reducing their drinking because they are in an experiment.

Hence, an experiment is not really feasible, even if we did want to answer that question about causal mechanisms.

### Research question: How does early rating success on IMDb affect different group's ratings?

#### Discussion

User ratings diverge between movie rating websites. To what extent is this due to randomness in early ratings causing path dependence. Moreover, which groups are particularly susceptible to influence by early ratings?

I am influenced by Rijt et al (2014), who study this topic across 4 platforms and find that early success accumulates. However, I extend their analysis to a new platform (IMDb) and investigate heterogeneous treatment effects.

#### Methodology

I describe my experiment below. In terms of Salagnik's typology, it is a digital field experiment. In addition, it uses the approach of "Do It Yourself" by using "Existing Systems".

1. Recruit
Digital. We "recruit" subjects by observing the behavior of IMDb raters in the field.

2. Randomize
Digital. Every time IMDb opens up a new movie for ratings, randomly assign it to either a treatment or control group.

3. Intervene
Digital. For treatment group: give movie x 10* ratings. I discuss the choice of x in the evaluation, but it will be approximately x = 20.

4. Measure
Digital. Measure IMDb ranking of each subset of voters every day for a year.
Subgroups:
* Gender and age: 2 (Male, Female) by 4 (under 18, 18-29, 30-44, over 45)
* Expert status: IMDb staff, top 1000 voters
* Nationality : US vs. non - US

### Evaluation

#### Digital aspects

##### Benefits

1. Scale
The experiment may not have zero variable cost, but it has very low variable cost. There is not cost to recruiting users or new films, as a stream of new films will keep flowing in. The main cost is for researchers intervening (actually doing the votes, discussed below) and measuring effects.

2. Pre treatment information
Not made use of.

3. Long time period
IMDb's cumulative rating system allows us to study long-term path dependence, for an indefinitely long time period (I capped at one year to reduce research costs).

##### Drawbacks
1. Disrupt field system
Our ratings, especially if we replicated de Rijt's results of affecting long-term success, will randomly disrupt IMDb's system of ratings being a signal for popularity of a film. The bigger our x, the more we disrupt the system.

2. Ethics
There is an ethical implication: IMDb ratings provide a public good - people allocated their time to higher rated films. Our disruption will reduce the efficient use of viewer's time.

In addition, our experiment risks ruining IMDb's reputation for reflecting genuine user experience.

#### Rich experiment

##### Validity

1. Statistical conclusion validity
We face a trade-off. The higher we set x, the more likely we are to obtain statistically significant results. IMDb votes are on the order of up to 2 million, and even in a first day a popular film may have hundreds of votes (although the majority of films are not popular). However, the higher we set x, the more ethical downsides there are, the higher the costs, and the more likely that IMDb will act to shut down our study. To play by their rules, we would probably need to have x separate people hired to conduct votes separately. Unless we were willing to ethically dubiously hire Amazon M Turk workers, we would probably be limited to around 10 willing colleagues.

2. Internal validity
Carrying out the steps of the study require daily attention to detail.

3. Construct validity
According to the research question, we measure exactly the construct we are interested in (IMDb ratings).

4. External validity
The external validity is high because our experiment setting is the setting of interest. This is the main advantage of the study. Rather than creating a lab experiment where we ask subjects to watch a video, and rate it after seeing randomly assigned ratings of other subjects, we are able to observe behavior of real voters in the field after they have (presumably) actually watched a movie.

In terms of whether our results replicate to "online rating platforms" in general, we lack that external validity.

By limiting x to ensure we can operate in the field, we are sacrificing statistical conclusion validity for external validity.

##### Heterogeneity of treatment effects

This is the main novelty of our experiment.

IMDb automatically reports voting behavior for the sub groups outlined above. This allows us answer the following types of questions:

1. Which age groups are more swayed by early ratings?

2. Are expert voters (top 1000 voters, IMDb staff) less swayed by early ratings?

Although we aren't interested in causal mechanisms specifically, this level of granular detail may start to shed light on which causal mechanisms we may want to investigate. For example, if the top 1000 voters are unswayed and others are, then maybe bandwagoning is caused by deference from more ignorant groups.

### Conclusion
Whereas studying drinking behavior in the real world was not suitable for a field experiment, the digital environment of online movie rating makes it an ideal setting for a cheap but powerful digital field experiment.
