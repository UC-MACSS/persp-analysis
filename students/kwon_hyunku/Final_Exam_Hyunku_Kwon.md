### Introduction

Both articles, “Digital Discrimination: The Case of Airbnb.com” (2014)
and “Racial Discrimination in the Sharing Economy: Evidence from a Field
Experiment” (2017) aim at unpacking the mechanisms of racial
discrimination in online marketplace, especially in Airbnb. Drawing on
Computational methods, both papers find out that race plays a central
role in economic transactions in online marketplace: African Americans
are discriminated against, be they host or guest. Such analysis leads to
the conclusion that Airbnb’s current design choices facilitate racial
discrimination. Similarity in the guiding research question and
computational methods notwithstanding, each paper deals with different
object (the former focuses on guests’ perceptions, while the latter on
hosts’), and employs different research methods (the former makes use of
observational data, the other combines field experiment and
observational data).

This essay will analyze those two papers in detail, in four aspects:
first, I will summarize and discuss the research design, with a special
focus on their computational method. Second, I will assess the
effectiveness of research design of each paper. Third, I will discuss
how combination of both an observational study and a field experiment
complement each other—how we can benefit from combining both research
projects. Finally, I will consider how a digital survey-based research
design would help contribute to the primary question of interest from
these two papers.

### Research design

\*\* Digital Discrimination: The Case of Airbnb.com (2014)\*\*

“Digital Discrimination: The Case of Airbnb.com” (2014) examines the
mechanisms of racial discrimination in the online marketplace. In
particular, they empirically demonstrate how hosts’ personal profiles
facilitate racial discrimination in the Airbnb marketplace. To
understand the impact of host’s race on economic behaviors of consumers,
this article investigates the differences in prices between hosts of
different races.

For the research, the author constructs a data set which includes
pictures of all hosts in New York City, their rental prices, and
information about characteristics and quality of their properties.
Drawing on regression modeling, this article statistically examines the
determinants of prices on Airbnb, and finds out that African American
hosts are charging 12 $ less, controlling for the effects of guest
perceptions of location, quality, and other factors.

This research heavily benefits from computational methods, in both data
collection and data processing. First, computational methods enabled
researchers to gather observational data required for the research. Data
collection might have been very difficult were it not for computational
methods, for mainly two reasons: first, the numeric magnitude of the
dataset, and second, the private character of the dataset. First, the
dataset required for the research is, simply, quite big: many (though
not very many) people (3752 observations) and lots of information per
person (Airbnb hosts’ race, number of reviews, average ratings,
existence of social network service account, and other control
variables). Second, the original dataset was not tailored for
researchers—it was originally created and collected by businesses for
their own purposes, which means that researchers should deploy special
ways to gather and tidy the data. This paper doesn’t explain such data
gathering process in detail, but they would have used web scraping
methods. Such computational methods drastically lower the cost of the
research.

Second, this article used computational methods for data processing. In
particular, the researchers use a special form of collaboration made
possible by computational methods: Amazon Mechanical Turk. Researchers
hired workers from Mturk to classify raw data, such as assessing the
quality of listing and to categorizing characteristics of hosts from the
profile photo.

**“Racial Discrimination in the Sharing Economy: Evidence from a Field
Experiment” (2017)**

Just as the article discussed above, “Racial Discrimination in the
Sharing Economy: Evidence from a Field Experiment” also examines the
mechanisms of racial discrimination in the online marketplace. However,
this article looks at how *guests* are discriminated against race, while
in “Digital Discrimination: The Case of Airbnb.com”, racially
discriminated *hosts* are focused on. To examine the impact of
customer’s race on economic behaviors of hosts, this article
investigates the relationship between customers’ racial profile and the
acceptance rate of their application. The results show that African
American customers are less likely to be accepted than their white
counterparts, who are identical in every respect but for race.

For this research, this paper combines field experiment with
observational research. First, researchers gathered information of all
Airbnb hosts in five big cities. The information gathered includes the
following: host’s race, gender, age, whether the host is professional or
casual, prior experience with African American guests, price of listing,
number and size of the rooms, cancellation policy, cleaning fee,
ratings, and location.

From the data collected above, researchers conduct a *field experiment*,
which combines randomized control experiments in natural settings. They
created Airbnb accounts, identical in every aspect except for names.
Then, the researchers applied treatments to hosts, by sending emails to
hosts to reserve a room. The treatments are varied in names, in two
parameters: race and gender. The treatment was randomized: “Each host
was randomly assigned one of our 20 guest accounts.”(2017: 6) And, such
random treatments are applied to all hosts in big cities. Via field
experiment, researchers examine the impact of potential guests’ race on
hosts’ acceptance.

Investigating the impact of guests’ race on hosts’ behavior, authors
take into account heterogeneity of treatment effects: the possibility
that hosts in different groups might react differently to the
treatments. Thus, they look at the impact of treatment across various
groups. They find robust discriminatory attitudes across various host
characteristics.

After experiment, researchers match their results with observational
research. In particular, this article categorized hosts into two groups
of ones who previously accepted African Americans and ones who didn’t,
and shows how hosts in each category react differently to the treatment.
The results show that the hosts who had at least one recent review from
an African American guest do not show such discriminatory tendency. Such
finding reinforces and complements field experiment.

Computational methods are extremely helpful in this article: it is a “
fully digital experiments” which “make use of digital infrastructure to
recruit participants, randomize, deliver treatments, and measure
outcomes” (Salganik 2017), and even to process the data. First and
foremost, field experiment wouldn’t have been possible were it not for
computational methods. Field experiment and lab experiment have their
own merits: lab experiment offers control, and field experiment realism.
Thanks to the emergence of online economic exchange, and of
computational methods, researchers applied “treatment”, controlling for
other factors, to the “natural setting”—every host in the five cities of
interest. Combining the randomized control experiments with much more
representative population of interest, this research successfully offers
compelling mechanisms of racial discrimination.

Computational methods not only helped field experiment in this article.
They also helped in processing data. For example, researchers used
Face-detection API to categorize past guests. Such process, which
heavily draws on machine-learning technique, drastically lowered the
cost and helped the efficiency of data gathering. Also, collaboration
allowed researchers efficiently process the information into much more
accessible form. In particular, hiring Mechanical Turk workers, this
article could easily classify hosts’ characteristics into race, gender
and age.

### Effectiveness of research

It is true computational methods facilitated both works, but such steps
are not panacea. Those papers make use of several digital techniques,
which have potential drawbacks, including the issue of validity, of
which both papers struggle with. This section discusses the
effectiveness of such struggles.

**Digital Discrimination: The Case of Airbnb.com (2014)**

As stated above, this article heavily benefits from the big data that
they gathered via online. The dataset is big: it includes many people
(3752 observations) and lots of information about the characteristics of
them (including number of review, ratings…). Also, the non-reactiveness
the dataset helps the researchers better answer the question at hand:
discrimination. Since discriminatory behaviors are regarded as negative,
people might change their behavior when they know that they’re being
studied. Non-reactive character of this research prevents such problems.

Such computational advantages notwithstanding, this research still
suffer from some issues concerning causal explanations. While the main
argument of this article is the mechanisms of racial discrimination in
online markets, what they found is not the mechanisms, but the
relationship between race and rental price. Even though they employ
multiple regression models to find the sole impact of race on price, the
results do not uncover the mechanism behind them. In other words, they
found out that there is a racial gap, but they didn’t find out whether
such gap is a result of racial discrimination. Alternative hypotheses
might come up and challenge the results: Foucauldian thinkers might
argue that African Americans, who identify themselves as a marginalized
group, might actually ask for lower costs. In other words, the racial
gap might be attributed to supply-side factors, not demand-side, or
racial discrimination of guests. Such problem is an inherent problem in
observational study.

Also, external validity might be questioned: this research only
investigates Airbnb hosts in New York City. Since hosts in New York City
cannot be a proper representation of Airbnb hosts, the findings might be
limited to Airbnb users in New York City. Construct validity may also be
questioned. This research translates qualitative information, i.e.
photos of the room, into quantitative one, a seven-point scale. MTurk
workers are hired to this job. However, whether such quantification is a
stable index for guest perceptions of quality can be questioned. Whether
Mturk workers results are similar and stable, and whether their works
represent general perception, might be questionable. (This issue is
address in the next article)

**“Racial Discrimination in the Sharing Economy: Evidence from a Field
Experiment” (2017)**

While Edelman and Luca paper (2014) suffers from various issues such as
causal mechanisms and validity, this article (2017) seems to be much
better prepared about those issues. First of all, this article, uncovers
the *causal mechanisms* of racial discrimination. While Edelman and Luca
paper (2014) merely found the relationship between race and price, this
article shows why and how racial discrimination operates in online
marketplace. Such causal claims are made via *field experiment*, by
conducting experiments with different versions (along race and gender)
of the treatment.

Also, this article considers the possibility of heterogeneity of
treatment effects. Taking into account various alternative mechanisms
behind the racial discrimination (e.g. homophily), this article divides
the subject of field experiment (hosts) into various subgroups, and
examine how same treatment leads to varying consequences. Such thorough
consideration of subgroups, in part, benefit from the bigness of this
research. As Gary King, Jennifer Pan, and Molly (2013) produces
estimates for the probability of censorship on around 90 separate
categories using big data, this article successfully compares various
different categories and relations of categories, because their dataset
is large enough.

This article thoroughly considers the internal validity: treatments are
randomized; researchers selected only one listing per host, preventing
hosts from receiving multiple identical messages—which might compromise
the quality of delivery of the treatment. Construct validity is also
much meticulously taken care of in this paper. For example, to prevent
Mturk workers translating subjective, qualitative information into
arbitrary ways, they hired “two Mechanical Turk workers to assess each
image, and if the workers disagreed on race or gender, we hired a third
to settle the dispute. If all three workers disagreed (…) we manually
coded the picture.” (4) Such intersubjective process would enhance the
match between the data and the theoretical constructs. This article also
showcases better external validity, in mainly three ways: first, they
collected more data, spanning five cities, compared with around 4000
observations which all were in New York. Second, they combine field
experiment and observational study, from both of which researchers find
similar findings. (13-14) Third, they also take into account the
possibility that their treatment, which lacked profile pictures, might
have influenced the economic transaction. After thorough literature
review, they conclude that the profile picture issue might not undermine
the generalizability of this experiment.

However, this article still suffers from finding out the deep-lying
mechanism behind racial discrimination in online marketplace: whether
the discrimination is taste-based, i.e, based on pure preference, or
statistical, i.e., grounded in inference that a property has inferior
quality because of the hosts’ race. In other words, though field
experiment effectively unpacks the mechanisms of discrimination, by
showing exact pathways of treatment leading to the effect, it cannot
explain the internal states, which “exist only inside people’s heads.”
Thus, whether someone’s discriminatory behavior stems from preferences
or inference can be better examined via survey methods. This point will
be discussed in detail in the final section.

### Advantage of running both observational research and field experiment

Running two parallel papers with similar research question, but
different methods and object of analysis, each paper benefit from each
other. Empirically, each paper benefits from each other, by illuminating
different aspects of social discrimination. While both papers
investigate racial discrimination in the marketplace, the first paper
focuses on how *hosts* are discriminated, while the second one on how
*guests* are. Put together, these papers show that the racial
discrimination not only exists in online, but also operates in both
sides—supply side and demand side.

Fundamentally, observational and experimental study have different
purposes and characteristics. Observational study shows what happened in
the real world. On the other hand, experiment shows the mechanism behind
the social reality. Such difference might be related more fundamental
theoretical issues in social sciences: whether observing the social
reality in itself, or finding the causal mechanism behind the social
reality, is the purpose of social science; whether history or physics is
the ideal of social sciences. While observational study is a better
reflection of the society as it is, such method cannot capture the
“social laws”; while experimental study better captures the mechanisms
by controlling for various factors and isolating the mechanism from the
complex social contexts, and thus shows higher internal validity (e.g.
randomization and delivery of treatment) it sometimes lacks external
validity—it is a social petri-dish, which cannot be applied to real
contexts.

Seen in this light, combining observational study and experimental study
helps us grasp the full picture of racial discrimination. The first
article shows what actually happened in New York City. The second
article shows how different treatments lead to different behaviors.
Comparing the results of both articles, we can see both what happened
and how it happened, and see whether each research’s findings are
reinforced by articles with different methods—and thus check the
external validity.

Also, observational research helps designing experiment. Observational
study helps researchers see the overall picture of racial discrimination
in online marketplace, though not the exact mechanisms. The
observational work might have worked as an exploratory data analysis,
which might help them elicit intuitions, build theories and construct
better experiment designs.

### Application of digital survey-based research design

Both papers share a primary research question: the mechanisms of racial
discrimination in the online marketplace. Though both articles make use
of various methods to answer the question, both fail to uncover the
fundamental, deep-lying mechanism at work: whether the mechanisms of
racial discrimination are taste-based, i.e, based on pure preference, or
statistical, i.e., grounded in inference that a property has inferior
quality because of the hosts’ race. Since such mechanisms are based on
internal states, “the best way to learn about internal states is to
ask.” (Salganik 2017) Thus, this section proposes a research design
which would help uncover the mechanisms of racial discrimination.

**Research Question: what is the mechanism behind racial discrimination:
statistical or taste-based?**

To this end, we simply conduct survey to Airbnb hosts who were already
the subject of the field experiment. Survey methods will reveal
subjective mentality of the hosts, and thus will help us better examine
the mechanism behind racial discrimination. If one’s discriminatory
behavior stems from one’s preferences, then racial preferences (e.g. I
just don’t want to work with African Americans) would more likely to
explain discriminatory behavior. On the other hand, if one’s
discriminatory behavior stems from inference, then racial stereotypes
(e.g. working with African Americans is not going to be good for me,
because their services are not as good) are more likely to explain the
discriminatory behavior. Then, how can we measure the degree of racial
stereotypes and preferences? Since survey methods are always haunted by
the “measurement” issue (Salganik 2017), I will draw on well-acclaimed
questions to measure both.

\*\* Measurement of racial stereotypes\*\*

I will measure racial stereotypes by directly asking questions about
characteristics of people. The questionnaire draws on American National
Election Studies (2000):

Now I have some questions about different groups in our society. I’m
going to show you a seven-point scale on which the characteristics of
people in a group can be rated. In the first statement a score of 1
means that you think almost all of the people in that group are
“hard-working.” A score of 7 means that you think almost all of the
people in the group are “lazy.” A score of 4 means that you think the
group is not towards one end or the other, and of course you may choose
any number in between that comes closest to where you think people in
the group stand. Where would you rate whites in general on this scale?

Same questions are used to measure each race’s other characteristics,
such as intelligence or trustworthiness. **measurement of racial
preferences**

To measure one’s racial preference, I will make use of feeling
thermometer:

I’d like to get your feelings toward some of our political leaders and
other people who are in the news these days. I will use something we
call the feeling thermometer and here is how it works: I’ll read the
name of a person and I’d like you to rate that person using the feeling
thermometer. Ratings between 50 degrees and 100 degrees mean that you
feel favorable and warm toward the person. Ratings between 0 degrees and
50 degrees mean that you don’t feel favorable toward the person and that
you don’t care too much for that person. You would rate the person at
the 50-degree mark if you don’t feel particularly warm or cold toward
the person.

We can include various control variables such as level of education,
income, partisanship, and social networks. Running regression with the
survey results, we can see which characteristics cause discriminatory
behavior.

**Drawbacks and modifications**

However, such research design has problems, especially those of
construct validity: it is not clear whether those questions actually
measure the degree of preference or stereotype. First of all, since
people are aware of racial problems, they might hide their stereotypes
when filling out the survey questions. Thus, people with racial
stereotypes might actually respond as if they are not ethnocentric.
Second, preferences are both emotional and rational, and the index I
proposed above only measures the former. Also, there is a possibility
that those two indices are actually related with each other. In other
words, those two dimensions (preferences and stereotypes) might be
reduced to one, latent dimension.

To ameliorate such problems, I will do two things. First, I will add
another index that measures stereotypes and preferences. Second, I will
see whether the indices of stereotype and preferences are related with
each other.

First, I will add the following question to measure stereotype:

“Can you guess how many African American people, do you think, are
receiving government assistance?” “Can you guess how many African
Americans, do you think, are involved with violent crime?”

Those questions will be asked open-ended. The discrepancy between the
real numbers and respondents’ estimations would show us the way in which
people make sense of the world vis-à-vis African Americans. While the
original question directly askes about one’s stereotypes, this question
investigates bias embedded in one’s worldview.

Second, I will add the following question to measure preference:

“If given choice, how would you want to work with people from the
following category, other conditions being equal?” “If given choice, how
would you engage in economic exchange with the people from the following
category, other conditions being equal?”

Respondents are going to be asked to answer in the scale of seven, from
negative to positive; they will answer the question on different
categories, including race, partisanship, and gender. This is important,
since including various categories would make people confused about the
purpose of the survey.

That said, I will look at the relations between indices. I would use
correlations to measure the relations between indices. If stereotype
indices are related with each other, and not with preference indices,
and vice versa, then I can posit that there are two dimensions of racial
discrimination: preference-based and stereotype-based. In this case, we
can see which dimension causes discriminatory behavior.
