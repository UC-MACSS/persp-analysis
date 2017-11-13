Collaboration
-------------

##### MACSS 30000 - Assignment 5

##### Alexander Tyan

##### 11/13/2017

### Kaggle open call projects:

Project of interest: Text Normalization Challenge - Russian Language
(Convert Russian text from written expressions into spoken forms)

Google’s Text Normalization Research Group has a challenge where one
must use machine learning to automate text normalization. Text
normalization is converting text to spoken forms, like $5.44 to “five
dollars, forty-four cents.” Text normalization is used to generate text
that is “machine-speakable.” The challenge provides users with the
column of the “before” text and expects competitors to provide script to
auto-generate the “after” text column. Each of your entries will be
compared to a test set. An entry must be completely right for it to
count toward your score; there is no entry-level partial credit. The
more entries you get right, the higher is your score. This text used is
in Russian, which may require some native intuition about it, so being a
native speaker might help. Of course, one would have to be proficient in
programming and Machine Learning as well.

### Improving a journal article:

I accessed an article entitled “Reevaluating the Middle-Class Protest
Paradigm: A Case-Control Study of Democratic Protest Coalitions in
Russia (Rosenfeld 2017). It studies the political protest movement in
Russia between December 2011 and January 2013 in Moscow. The premise of
the study is a prevalent belief that a growing middle class may lead to
higher political pressure for a state to democratize. However, the
author critiques this idea because it has not been tested in autocratic
settings (such as modern Russia) and because it tends to view the middle
class a monolithic group. In opposition to this, the author evaluates
two hypotheses:

1.  “Middle-class mobilization will exhibit significant sectoral
    differentiation, with state-sector workers less likely to
    participate in anti-regime demonstrations.”
2.  “Protest coalitions will exhibit significant sectoral
    differentiation, with state sector workers less likely to join
    democratic forces.”

In other words, middle class individuals who are state-employed will be
less likely to protest than their private-sector counterparts and those
among them who do participate will be less likely to identify themselves
as “democratic.” In this latter case, state-employees do not seek regime
change; they just want a better deal from the current government.

Traditionally, the data to test such hypotheses has not been available.
This is because surveys of protesters are rare and relying on general
national surveys to study protesters has its own issues. These may
include recollection and reporting biases and, because protesting is a
rare event, not enough protesters captured in the national
representative sample.

As an alternative, Rosefeld uses a variant of the standard case-control
research design, used in epidemiology to study rare events. To test
these hypotheses, Rosenfeld collects a random sample of protesters from
each gathering (there are four of them), and surveys the participants on
their demographic characteristics as well as, of course, employment
status to determine whether to classify them as state-employed and
middle-class or not. He then complements this with a random sample of
the population (from a national pollster) and runs multivariate modeling
to estimate a probability of participating in a protest as a function of
individuals’ characteristics. The results are significant and support
the two hypotheses.

First, the study’s methodology seems quite solid to begin with and, in
my opinion, the author resolved the issue of data availability quite
well by creative employment of a novel (for Political Science) modeling
strategy and small-scale data collection for data that were not
available previously.

The main critique of this study may be that the results of the study may
be not generalizable to all of Russia (or to autocratic settings around
the world), since the study was limited to a sample in the largest
Russian city. And the author does attempt to generalize his results to a
wider setting. It may be hard to extrapolate the results to all of
Russia, by virtue of the country’s size, geographic differences, and
particularities of its capital. Protesters in Moscow may not be
representative of protesters elsewhere.

A natural suggestion may be to collect data from more participants
across more cities. Not only would that make the results more
generalizable, this would also let the author control for regional
confounders, much like he did in controlling for demographic variables
such as gender and age. While the protest which the author studies were
at their largest in Moscow, other major cities across the country were
also hubs of significant protest gatherings. Of course, this may pose a
logistical and financial challenge to do so. Because protests are rare
and can occur over vast geographic distances, how can one survey in many
locations? This is where the author may employ Distributed Data
Collection (DDC) techniques to scale up the data generating process
(Salganik 2017).

DDC is best suited for large scale data-collection, previously performed
by survey companies (Salganik 2017). Indeed, this may be a large-scale
data collection, since the protests were quite massive and all over the
country. And the author did use a survey company to collect in Moscow.
One may instead recruit “research assistants,” who would volunteer to
collect survey data at protest events across the country, wherever they
may live. Their recruitment may be done through the internet.

One potential issue with such data collection is data quality and
systematic approaches to sampling (Salganik 2017). One may argue that
one should collect the data from participants directly, perhaps
distributing survey through mobile platforms. However, given the
political sensitivity of protesting, responses from such a distribution
may be low. This is where volunteer presence is important as it may
induce higher participation, much like a traditional survey
administrator did in case of this study in Moscow.

However, with a non-professional volunteer, the data collection quality
may be not good. There are several ways to improve on this. First, the
volunteer may be shown a training video to become proficient at random
sampling methods at a protest rally (e.g. every n-th entry at the rally
gates, since Russian protest are usually cordoned off). Second,
simplifying the task is another strategy. One may instead distribute the
survey through a mobile app to the volunteer’s smartphone device. Owing
such a device would be a prerequisite to being a volunteer. But,
depending on the recruitment strategy on Russian internet platforms,
many potential volunteers may already own a device. A volunteer would
then administer the survey by following random sampling and approaching
the subject instructions provided beforehand. A survey taker would then
use the device to enter their survey data. Needless to say, much will
have to be tested in the way of mobile device compatibility and ease of
use for survey takers and volunteers before administering the project,
as many participants may otherwise find it difficult to fill a survey on
a screen. However, if done right, this may allow the volunteer to focus
their attention on approaching the subject well and simplify their task
(Salganik 2017). Third, one may use Salganik’s (2017) notion of
leveraging heterogeneity to further cross-validate volunteer’s data
collection and ensure data quality through redundancy.

One natural difficulty with this method is the sensitive political
context, which may hamper the recruitment of volunteers. On the other
hand, this may not be as big of a problem, as many protest-goers already
gather online to organize and end up attending the protest. Perhaps
volunteers could be recruited in such online communities as they may be
a priori motivated to attend. Framing the task as participating in
studying the protest movement and contributing to research may further
motivate such potential volunteers online, as motivation is an important
part of designing a mass collaboration project (Salganik 2017). Although
of course it is hard to predict the success of scaling up such a
recruitment project and it may end up not working out due to volunteers’
privacy concerns for installing said phone applications on their phones.

Another challenge with this DDC is the ethical component. A study may
require the volunteers to be properly trained as defined by the IRB
process. But administering such training to many volunteers across large
geographic distances may be a challenge and it is not clear whether
completing such training online would be sufficient to get the IRB
approval. One must acknowledge that there are many challenges to this
project and perhaps the path already chosen by the original design
method is already doing a sufficiently good job.

### InfluenzaNet:

#### Design:

The design of data generation in Google Flu Trends (GFT) is quite
simple. As we have seen previously in our course, it uses Google search
queries to predict CDC’s traditional reports of influenza cases,
although what specific words and word combinations are used is not
reported (Ginsberg et al. 2008), so the research is not very replicable
(Lazer et al. 2014). The system takes advantage of being always-on and,
therefore, being able to provide real-time data, unlike traditional
systems which have a lag.

In contrast, InfluenzaNet (IN) involved recruitment of participants
through a mass communications campaign in several countries, where the
project was launched at varying start dates in 2000s. (van Noort et al.
2015). Participants were then contacted through a regular distribution
of internet surveys. They completed an intake questionnaire to record
their demographic parameters, vaccination history, as well as any risk
factors (e.g. asthma) and Influenza-like illness (ILI) symptoms. The
scale of data-gathering allows IN to capture smaller-scale epidemics,
track different population groups separately, as well yields
statistically less noisy results (van Noort et al. 2015). This is
advantageous to traditional methods, which do not capture information
about cases where persons do not report to a GP.

Traditional Influenza Tracking Systems rely GP patient visit reports,
where doctors are compile the necessary physician records which are then
aggregated, usually by a national level monitoring institutions, such as
the CDC in the US (Ginsberg et al. 2008; van Noort et al. 2015). This
may be significant because the data is used for a timely detection of
epidemics.

#### Costs:

Out of the three data generating designs, GFT is the least costly, since
it relies on the search engine that is already implemented. In case of
the study presented in class, Ginsberg et al. already had access to the
data as part of their work with Google. However, one opportunity cost
associated with GFT’s simplicity is that it cannot capture data on the
use of health different healthcare services and cannot discriminate
between different types of ILIs (van Noort et al. 2015).

IN is more expensive, as it relies on administering the online surveys
and hosting a web-system capable of interfacing with the participants.
Additionally, participant recruitment is sustained through a public
media campaign, which may be costly. However, marginal costs may be
still relatively small, given the scale of participants recruited.
Moreover, because the study is administered digitally, the costs of
changing questions and even whole questionnaires is small, which
provides additional flexibility in checking on additional population
parameters, such as physical activity (van Noort et al. 2015). And like
with the GFT, it provides a faster means of getting the data compared to
traditional systems.

Traditional systems rely on GP reporting which is already in place
through a healthcare system. The main cost here is time, as there is a
lag between the information is recorded and then when it is aggregated
into actionable data (Ginsberg et al. 2008; van Noort et al. 2015;
Tilston et al. 2010).

#### Likely errors and the effects of unsettled time:

As outlined by Lazer et al. (2014), the GFT design suffered from
predicting without considering potential explanatory mechanisms behind
how search queries may be measuring flu trends. The researchers
overfitted the data. This has resulted in an algorithm that missed the
H1N1 epidemic, because the epidemic did not fall into the regular winter
season cycle, like the regular flu does. Moreover, the data-generating
algorithm confounded the process, because Google implemented suggestive
search mechanisms to aid users (Salganik 2017). Thus, user’s behavior
drifted and confused the method. Furthermore, some studies show that GFT
prediction fared no better than CDC traditional forecasting based on
Traditional Systems (Lazer et al. 2014).

IN largest potential source of error is being unrepresentative of the
larger population. This is in part because internet penetration is not
uniform across the population groups, as well as the fact that
participants are not a random sample; they are self-selected volunteers.
For instance, this caused the surveyed population to underrepresent
younger children and older persons. As a result, the IN missed a flu
strand epidemic striking younger children in Portugal in 2009 (van Noort
et al. 2015). This unrepresentative data makes it harder to draw
conclusions about the larger population (Tilston et al. 2010). Moreover,
there is also a potential response bias, as some respondents may choose
to report only when their symptoms get worse (Tilston et al. 2010).
These distortions may be compensated for partially by weighing and
“censoring” the data set, but this would not account for unknown
confounders (Tilston et al. 2010).

Another difficulty with the IN is the effects of the question wording
bias and the varying reported number of incidences. Using different
definitions of ILI symptoms causes different responses and not all
ILI-symptoms are due to actual flu. Some may be due to H1N1 outbreak.
Because the number of incidences cannot be used to report a measure
(since self-reporting is selective), one must choose a denominator to
divide the number of reports by. However, what this denominator should
may depend on whether a reported case was an ILI or an H1N1 anomaly
(Tilston et al. 2010). This makes adjusting the measurements more
challenging in time of such anomalous outbreaks.

As mentioned, for Traditional Systems, the main source of error is the
self-selection by patients who decide to visit a GP. The problem is
there may be a systematic differences in self-reporting based on
geography and culture. For instance, Southern European states report
persons reporting to a GP sooner, on average, than in the Northern
European states, except Belgium (van Noort et al. 2015). Another
systematic difference is that, within one geographic locale, different
population groups may be reporting in a systematically different manner.
All of this may result in a systematic error in measuring ILI in the
general population and make it hard to compare cross-nationally or
across population groups. In case of H1N1, a panic may have pushed many
individuals to seek a GP contact in the Netherlands, inflating ILI
reports in certain population groups (van Noort et al. 2015). Similarly,
this has led to distorted summer peaks in the UK, as measured by
traditional systems (Tilston et al. 2010).

### Bibiography

Ginsberg, Jeremy, Matthew H. Mohebbi, Rajan S. Patel, Lynnette Brammer,
Mark S. Smolinski, and Larry Brilliant. 2008. “Detecting Influenza
Epidemics Using Search Engine Query Data.” Nature 457
(7232):nature07634. <https://doi.org/10.1038/nature07634>.

Lazer, David, Ryan Kennedy, Gary King, and Alessandro Vespignani. 2014.
“The Parable of Google Flu: Traps in Big Data Analysis.” Science 343
(6176):1203–5. <https://doi.org/10.1126/science.1248506>.

Noort, Sander P. van, Cláudia T. Codeço, Carl E. Koppeschaar, Marc van
Ranst, Daniela Paolotti, and M. Gabriela M. Gomes. 2015. “Ten-Year
Performance of Influenzanet: ILI Time Series, Risks, Vaccine Effects,
and Care-Seeking Behaviour.” Epidemics 13 (Supplement C):28–36.
<https://doi.org/10.1016/j.epidem.2015.05.001>.

Rosenfeld, Bryn. 2017. “Reevaluating the Middle-Class Protest Paradigm:
A Case-Control Study of Democratic Protest Coalitions in Russia.”
American Political Science Review 111 (4):637–52.
<https://doi.org/10.1017/S000305541700034X>.

Salganik, Matthew J. 2017. Bit by Bit: Social Research in the Digital
Age. Princeton, NJ: Princeton University Press.

Tilston, Natasha L., Ken TD Eames, Daniela Paolotti, Toby Ealden, and W.
John Edmunds. 2010. “Internet-Based Surveillance of
Influenza-like-Illness in the UK during the 2009 H1N1 Influenza
Pandemic.” BMC Public Health 10 (October):650.
<https://doi.org/10.1186/1471-2458-10-650>.
