Hunting for the Russian Trolls (Part 2)
---------------------------------------

##### MACSS 30000 - Assignment 2

##### Alexander Tyan

##### 10/23/2017

### Introduction

Previous study explored alleged Russian interference in the 2016 US
presidential election. In particular, it aimed at developing an
algorithm that would help identify which activity on social media
outlets (Facebook and Twitter) was likely to have been the work of
Kremlin-sponsored users (also known as Kremlin “trolls”). This would
then help gauge the extent to which such activity took place, as well as
discover any patterns, such as behavior’s timing and specific population
targeting by these users.

This current study will continue exploring this topic, but will
concentrate instead on another pro-Kremlin actor in the social media
space, the RT (formerly Russia Today) America channel (RT’s broadcast
for North America). Much like with the Kremlin “trolls,” this media
outlet is accused of channeling Kremlin’s political agenda onto cable
television and social media, in part to influence the outcome of the
election (Goldman 2017; Defense Intelligence Agency 2017). And similarly
to the “troll” case, there is not a systematic evaluation of its effects
on the voting behavior in the 2016 presidential election. This project
would fill that gap.

Hence this study will attempt to answer the following research question:
how did the interaction with RT America (RTA) content on Facebook affect
individual voting behavior in the 2016 presidential election in the US?

### Research Design and Plan

Formally, the independent variable is individual’s interaction with RTA
content on Facebook. This could be further classified into different
types of interaction, such as following the RTA Facebook page or liking
it, posting comments on the page or on individual posts, using the
built-in “like”, “laugh”, “anger” and other emoticon reactions, etc.
Prior to executing the project, a pre-study would have to determine how
to take such metadata to operationalize our independent variable. A
tentative plan is to use existing Natural Language Processing software
packages and techniques on texts and code the rest of data types to then
calculate an “RTA favorability disposition.” This would be a measurement
of whether a user’s interaction signals favorable, neutral, or
unfavorable (or absent, if there was no interaction) reaction. This
could be potentially a discrete or a continuous variable.

The dependent variable would take on discrete values of which candidate
a person voted for, or whether they did not vote.

Since we would evaluate a causal relationship (interaction with RTA
content may lead to certain voting behavior), the ideal approach would
be an experiment, randomly assigning RT content interaction as treatment
and seeing what the voting outcome would be. Because the election has
already occurred, we cannot perform a traditional experiment. Instead,
we propose leveraging digital traces to run an experiment approximation.
There are two options: natural experiments and matching (Salganik 2017).
A natural experiment would assume that treatment (RTA content
interaction) was assigned as if randomly. This is likely not the case,
because previous reports indicate that the information campaign
conducted by the Kremlin may have been targeted to certain population
groups, like conservatives (Weisburd, Watts, and Berger 2016; Watts and
Weisburd 2016). Hence, matching is the only option.

We would need demographic data to match individuals that are alike, with
the exception of differing on the RTA interaction independent variable.
We would also need individuals’ Facebook metadata on interaction with
the RTA content on Facebook, as well as their voting record.

First, to collect demographic data, we would advertise to US individuals
through Facebook (assuming Facebook ad-space allows such targeting) to
participate in our survey. The link banner URL leading to a custom-built
Facebook app would present them with the IRB-approved informed consent
information and explanation of risks. The survey itself (part of the
app) would copy the demographic questionnaire used by Wang et al.
(2015), a study which predicted US electoral behavior by using a
non-representative sample of Xbox platform players. Some of the
questions are:

-   Generally speaking, do you think of yourself as a …? (Democrat∖
    Republican∖ Independent∖ Other)
-   Are you male or female? (Male∖ Female)
-   In what year were you born? (1947 or earlier∖
    1948–1967∖1968–1982∖ 1983–1994)

There are also questions about race, education, state etc. This choice
is for several reasons. First, the Xbox study resembles our project in
that it uses a non-representative sample in the study of election of
outcomes. Second, this allows for cross-comparisons with this similar
study and ensures we are using a tested questionnaire to minimize
question-form biases, as per Salganik’s (2017) suggestion. Third, we
would need such range of data to do reasonable matching of individuals.
Finally, we would use such data to build a data link to the individual
voting record (which individuals would be consenting to if they
participate).

We would only update some of the questions to make them relevant to our
study. For instance, we would change “Who did you vote for in the 2008
Presidential election?” to “Who did you vote for in the 2012
Presidential election?” (i.e. previous election).

Second, to collect data on RTA interaction, the informed consent would
request user’s access to their Facebook behavior. This would allow us to
match individual’s survey responses to their Facebook activity.

Third, we would partner with a company specializing in US voting record
collection. Similar to Ansolabehere and Hersh (2012), this could be a
company like Catalist, LLC. Like in that study, we would match
individuals’ Facebook activity and survey responses to their record in
the election. Ansolabehere and Hersh also provide us with the
methodology to ensure the company data linkage is of good quality. For
instance, one way to do so is to check the results against the
MITRE-naming challenge, an independent matching competition
(Ansolabehere and Hersh 2012, 443).

Merging the survey data, the Facebook activity data and the voting
records would allow us to build our matching pairs to approximate an
experiment.

In terms of the formal sampling typology (Salganik 2017), our Target
Population is Americans who were eligible to vote in the last
presidential election. We are including all potential voters instead of
just Americans on Facebook. This is because American voters not on
Facebook are not exposed to the RTA content, so they could be important
as a point of comparison to those who do interact with the RTA. The
Frame Population (i.e. where we draw) and the Sample Populations (i.e.
whom we draw) are the same in our case, because both are American
Facebook users. Our Respondents are those who will click the
advertisement banner and consent to and complete our survey study. Our
sample size could aim to be similar to Wang et al. (2015), where the
researchers collected 750,148 interviews from 345,858 respondents.
However, we could adjust our aims accordingly to satisfy the minimal
number of responses required for our MRP adjusment to work (see below),
subject to funding constraints affecting our ability to advertise on
Facebook. (Hopefully, current political saliency of the topic would
allow for greater funding opportunities.) We will address the errors
associated with the representation of our target population later in the
proposal.

### Justification

As mentioned above, the general justification behind using digitally
enhanced data is that it allows to simulate an experiment through
matching retroactively, thanks to its always-on property (Salganik
2017). Such data is also necessary since we want data linkage with the
digitized voting records and on a massive scale (more on the size
later).

Digital sources of information are also a natural choice because our
research question is centered on a certain Facebook behavior. So the
digital trace is a core measure and the design calls for an Enriched
Asking model of survey data (Salganik 2017). Going digital is inherently
necessary for our research question.

Another reason is that the digital traces of such behavior allow us to
avoid using a survey to ask about user’s interaction with the RTA
content. Subjective survey reporting may be subject to memory failure
and desirability biases (Salganik 2017). Thus, pulling digital traces
directly with user’s consent makes for a better measurement. Similarly,
the objective voting record in the election is better than asking about
people’s voting, since they may lie about their voting (Ansolabehere and
Hersh 2012).

The big size characteristic of available data would also allow us to do
MRP adjustments while satisfying the
homogeneous-response-propensities-within-groups condition. We will
discuss this more in addressing representation errors.

The demographic data we collect is through a survey, rather than an
observational study. This is because much of the demographic data may be
unavailable through Facebook profiles. We need such data to do data
linkage with voting records, as well as matching pairs to approximate
experimental design. Doing a survey addresses such data inaccessibility
(Salganik 2017).

A more practical issue is that doing the project digitally would be less
costly and faster than doing a similar survey project using more
traditional methods. Record matching with paper surveys, while investing
into costly telephone-administered questionnaires would simply not be
feasible, especially with the need of scale to perform MRP group
breakdown. Digital records of voting and survey disseminated on Facebook
allow for a faster, cheaper reach of our sample population.

### Challenges

Some challenges come from our sampling methodology, since we are using
non-probability sampling (Salganik 2017). While we would not have a
sampling error because our frame and sample populations are the same,
coverage and non-response errors are an issue. Coverage is an issue
because Facebook users, much like the Xbox users, are heavily
non-representative of the general US population of potential voters. For
example, they are probably younger. Non-response may be an issue because
there could be a systematic relationship between propensity to respond
to our survey and the voting behavior; e.g. supporters of one candidate
could be less prone to respond to participating in such a research.
These errors would skew our data and we would not be able to generalize
to our population of interest.

To address these issues, we propose using the MRP method, similar to
Wang et al. (2015). Breaking our respondents into small groups based on
their demographic dimensions, Facebook and voting behavior, we can
satisfy the homogeneous-response-propensities-within-groups condition,
but the number of cases in each group might be too small. The big aspect
of our data may help with some of that, as scaling up in the digital
realm would allow us to collect a lot more responses with less cost.
Additionally, however, MRP would allow us to infer voting behavior
within each group and weight each respondent type appropriately to get a
proper estimate for more general voting population. We suggest following
Wang et al. (2015) method of using Current Population Survey in
combination with the 2012 exit poll data to perform the weighting part.

In conclusion, building on the previous survey and data linkage
practices would hopefully allow us to execute matching pairs to infer
causality of interacting with the RTA on the voting behavior patterns in
the 2016 presidential election.

### Bibliography

Ansolabehere, Stephen, and Eitan Hersh. 2012. “Validation: What Big Data
Reveal About Survey Misreporting and the Real Electorate.” Political
Analysis 20 (4):437–59.

Defense Intelligence Agency. 2017. “2017 Russia Military Power Report.”
In . Defense Intelligence Agency.

Goldman, Russell. 2017. “Russia’s RT: The Network Implicated in U.S.
Election Meddling.” The New York Times, January 7, 2017, sec. Europe.
<https://www.nytimes.com/2017/01/07/world/europe/russias-rt-the-network-implicated-in-us-election-meddling.html>.

Salganik, Matthew J. 2017. Bit by Bit: Social Research in the Digital
Age. Princeton, NJ: Princeton University Press.

Wang, Wei, David Rothschild, Sharad Goel, and Andrew Gelman. 2015.
“Forecasting Elections with Non-Representative Polls.” International
Journal of Forecasting 31 (3):980–91.
<https://doi.org/10.1016/j.ijforecast.2014.06.001>.

Watts, Clint, and Rew Weisburd. 2016. “How Russia Wins an Election.”
POLITICO Magazine. December 16, 2016. <http://politi.co/2gD19if>.

Weisburd, Andrew, Clint Watts, and JM Berger. 2016. “Trolling for Trump:
How Russia Is Trying to Destroy Our Democracy.” War on the Rocks.
November 6, 2016.
<https://warontherocks.com/2016/11/trolling-for-trump-how-russia-is-trying-to-destroy-our-democracy/>.
