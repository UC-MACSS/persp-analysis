Final Exam
----------

##### Alexander Tyan

##### 12/06/2017

*(3 pts each) Summarize the research design and explain how the research
design leverages computational methods to ask and answer a question.*

1.  “Digital Discrimination: the Case of Airbnb.com”

Overall Design and Goals:

The first article is an example of observational study design. Salganik
would classify this type of observation as “counting things,” though
perhaps “measuring” could be a more appropriate term here. This is so
because the goal of the research is to *measure* race-based
discrimination. Specifically, the authors attempt to measure the gap
between prices proposed by hosts who are black versus non-black on
Airbnb, a popular short-term rental marketplace online. Is race of a
host associated with the level of prices they propose for their listings
on Airbnb? Such a gap would imply that how much a host can charge
depends on their race, i.e. there is a race-based discriminatory
mechanism at play in price formation. Therefore, though not explicitly
stated, the main hypothesis is that black hosts charge lower prices for
their properties than non-black hosts.

Data Collection and Processing Design:

The data used is a snapshot of Airbnb property listings on July 12, 2012
in New York City, NY. The authors do not specify if “snapshot” means all
the listings. A reader must assume that this is true, with close to 3700
observations included. (Otherwise, perhaps the authors would have to use
a representative random sample.) The authors also do not explicitly go
into detail about the mechanics of such large-scale data collection. The
reader can infer that perhaps the researchers used some sort of an
automated web-scraping mechanism, given the detail and scale of
information collected.

The information collected included host characteristics: location,
check-in, communication, and accuracy ratings (all based on reviews left
by previous clients). The authors also collected hosts’ photos and used
Mechanical Turk workers to classify each host into one of eight race
groups, based on these images. Data collection also included property
photos, which other MTurk workers used to classify property’s perceived
quality on a seven-point scale.

Results:

The authors find that there is a price gap between black and non-black
host listings, with blacks charging USD107 per night on average versus
USD144 for non-blacks. This gap persists even when controlling for
property and other host characteristics. The result is robust when
comparing blacks versus whites as well.

Leveraging Computational Methods:

The design aims to study race-based discrimination in an online
marketplace. Thus, it uses a digital environment to conduct research and
collect data. In other words, the research interest predisposes the use
of computational methods, since the data must be collected online.

The digital nature of the environment also allows for a more automated
collection of data, permitting the use of web-scraping tools to gather a
dataset rich with information across many variables of interest. The
range of variable information then allows for a fuller empirical
analysis after the data was collected, allowing to control for host and
property characteristics and, thus, to isolate the association between
race and price.

Furthermore, some of the collected data is pre-processed before analysis
using what Salganik calls Mass Collaboration methods. He would classify
the specific type of collaboration in this research as Human
Computation, where the tasks of classifying material are broken down
into “easy-task-big-scale” for “non-experts.” Here these non-experts are
MTurk workers who classify images to determine host’s race, as well as
property’s perceived quality. Thus, computational methods allow for a
more cost-effective and fast way to pre-process data before statistical
analysis.

1.  “Racial discrimination in the sharing economy: Evidence from a field
    experiment.”

Overall Design and Goals:

The second article is an example of randomized experimental design (with
some observation used for external validation later). Specifically,
Salganik would classify this as a digital field experiment. The goal of
the study is to assess online marketplace discrimination in the context
of short-term property rental. Specifically, the authors use Airbnb
listings to see whether a renter’s perceived race (and gender) are
grounds for discrimination against them by hosts during an application
process to a host’s property. Does a race of a potential guest cause
different rates of approval in property rental applications? The
unstated hypothesis here is that perceivably black candidates will
receive less approval from hosts than white ones.

Salganik identifies four stages in experimental design and
implementation. Here, I summarize the design in terms of these four
stages.

For recruitment of participants, the authors use listings of properties
on Airbnb in July 2015 and identify their owners who then unknowingly
serve as participants (for multiple listings per host, only one listing
per host is chosen). The recruitment is limited to Baltimore, Dallas,
Los Angeles, St. Louis, Washington DC. The initial population of
interest is hosts across twenty major metropolitan areas, but, because
of Airbnb restrictions, researchers limit themselves to these five. The
sample then includes everyone in the (limited) population.

For randomization of treatment, the authors create 20 accounts with
different names, signaling gender (male/female) and race (white/black).
Surveys were used to make sure that these names are indeed associated
with intended gender/race groups (construct validity). Each account is
then in one of four equal groups based on these two splits. Participants
are randomly assigned to one of the four groups.

For delivery of treatment, participants are randomized to receive a
corresponding treatment, which is a message from one of the accounts in
the four groups. The message communicates interest in the property
listed and inquires whether the fictitious client may be accepted to
rent the property eight weeks later. One assumes that this initial
message is done by automation, because there over 6000 such messages
sent.

For measurement of outcomes, the researchers record the message
responses from hosts and classify these into six categories of
responses, including “Yes,” “No”, etc. Only explicit Yes’ and Nos are
used for data analysis later.

Data Collection and Processing Design:

Data collected includes hosts’ characteristics, such as number of
properties and reviews (proxies for hosts’ professionalism versus
occasional Airbnb use), profile pictures, and reviewers’ profile
pictures. Hosts’ pictures were then used to classify hosts by gender,
race and approximate age through hiring MTurk workers. Reviewers’
pictures were classified into similar categories, but using Face++
software.

Additionally, the researchers collect listing characteristics, such as
price, cleaning fees, cancellation policies, number of
bedrooms/bathrooms, geographic coordinates, desirability etc.
Desirability is calculated in terms of statistical probability based on
whether the property was filled eight weeks after the initial contact.

Additional data includes census information, which was then linked to
Airbnb data through geographic coordinates. This was for using
neighborhood information on racial composition and whether this may
influence positive or negative response to a message request.

Results:

The researchers find significant difference in positive response rates
based on client’s perceived race. (42% approval for blacks, 50% for
whites). The results hold when controlling for other variables in host’s
or property’s characteristics, e.g. race, gender, shared/not share
property, host’s professionalism, etc. When “intermediate” responses are
considered, e.g. “conditional yes/no”, such significant difference is
not seen, so the outcome is *not* driven by response types.

The discrimination results hold robustly even when considering other
potential influencers on the measured outcome. Such factors include
host’s race (except for black female hosts to black female guests),
distance to client, host’s professionalism, host’s age, listing’s cost,
listing’s desirability, neighborhood’s black population proportion, and
across client names. The exception is in host’s race case, where black
female hosts are more likely to accept black female guests than any
other group. More on that in task 2.

Leveraging Computational Methods:

The study is inherently digital, since the subject of interest is an
online marketplace. Therefore, the use of computational methods is
natural; they allow for a more automated collection of digital data. In
Salganik’s typology, this digital randomized field experiment would fall
into “use existing systems” type. This type is characterized by low cost
and high realism (and also low control, as the authors discovered when
their accounts were blocked).

The realism aspect of this computational experiment allowed researchers
to collect data in an unobtrusive way, where the risk of polluting the
response data signal with Hawthorne effects is minimal. This is because
the computational design of the research emulated a host’s normal
experience on Airbnb.

The low-cost aspect of the experiment allowed for researchers to extend
not only the breadth and depth of collected pre-treatment data (i.e.
host, property, and neighborhood census information for all of the
population in selected cities), but also automate treatment intervention
in a cost-efficient manner. This included automatically randomizing
treatment assignment and sending over 6000 initial treatment messages to
participants.

Moreover, computation allowed the researchers to scale and outsource
some data processing, whereby they used MTurk workers to classify hosts’
gender, race, and age. This is an example of Human Computation from
Salganik’s Mass Collaboration typology. Similarly, Face++ software was
used to automatically classify hosts’ reviewers’ demographic groups.
Additionally, the study uses surveys to verify construct validity when
it comes to names as signals of race and gender. Though not explicitly
stated, one may suppose that the study used some computational approach,
such as using MTurk workers, to accomplish this as well.

The digital nature of the experiment also allowed for (easier) merging
of two otherwise disparate datasets, the one from Airbnb listing and the
census data. This allowed the researchers to add an additional variable
to their analysis of message responses, namely neighborhood demographic
composition.

Therefore, the study leverages a wide spectrum of computational methods
to produce and analyze the data and answer the research question.

*(4 pts each) Evaluate the effectiveness of each paper's research design
independently. That is to say, what do we learn from each paper on its
own? What are the limitations of each paper on its own? Think back to
Salganik's characteristics of big data and our assessment of
experiments' validity, heterogeneity of treatment effects, and causal
mechanisms. Draw on these methods of assessment as you evaluate the
effectiveness of each paper.*

1.  “Digital Discrimination: the Case of Airbnb.com

The design of this study is observational, based on capturing a wide
range of host and listing characteristics to measure an outcome of
interest: a price gap association with the race variable. The results
are that there is indeed a lower price associated with black hosts’
listings as compared to non-black hosts (see task 1 for more detailed
discussion of results). The overall limitation of this approach is that,
because of the observational nature of the experiment, one may only
assert and explain association between the price and race variables but
not any causal mechanism. On the other hand, the advantage is that the
explanation of this association in the study is quite rich. The authors
go in depth about controlling many other variables potentially
associated with prices and observe that the association between price
and race still holds true.

Therefore, one way the study harnesses the advantage of big data is by
using its bigness. Bigness refers to, in part, many observations and
many variables measured for each observation. Many variables collected
by the Airbnb system allowed for control of a wide range of alternative
variables in host and listing characteristics to then isolate the
association between race and price. Many observations, on the other
hand, allowed the researchers to split their data into groups along many
variable dimensions (along different host and listing characteristics)
and still retain a necessary number of cases per each subgroup for the
purposes of statistical analysis and description.

Another big data advantage harnessed by the study is the data’s
non-reactiveness. Researchers observed the subjects in their natural
environment, where daily activity continued as usual despite
researchers’ observation. This means that the results were not polluted
by researchers’ presence.

One disadvantage of the big data that limited this study is the data’s
inaccessibility. In particular, the authors note that they have to
restrict their study to the relationship between race and price, and not
study demand since information on demand is not publicly available.
Indeed, Airbnb refused to release that information to researchers.

Another potential limitation for the study’s results is that the authors
only used listings from New York City. While this may not be a problem
if there is no systematic difference in price-race association between
that location and other locations nationally, this is by no means
guaranteed. The data is big, but it came only from one place. While the
researchers do not comment on this, this may limit the study’s external
validity and generalization of results to the national level if New York
listings are not representative of the nation-wide patterns of
discrimination in the Airbnb marketplace.

1.  “Racial discrimination in the sharing economy: Evidence from a field
    experiment.”

The design of this study is a randomized field experiment. A general
advantage of this method is being able to assert that the results imply
a causal relationship between variables. In this study’s case, it is the
relationship between race of a potential guest and their rate of
rejection by a host; black guests get a significantly higher rejection
rates than white ones (see Task 1 for more results description). Because
of treatment randomization, (and researchers checking for alternative
variables influencing rejections) one may assert that it is indeed the
perceived race of an application that leads to the variance in the
rejection rate.

However, as is common for randomized experiments, the design does not by
itself explain the causal mechanism behind how race impacts rejection
rates. As the authors note, it may be, for instance, that the
discrimination occurs based on socioeconomic status as well, since
African-American names may be correlated with a lower socioeconomic
status. This experimental design simply does not allow for this kind of
analysis.

The study does harness some big data advantages to perform this
experiment effectively. The size of the dataset means a higher number of
observations and many variables per observation. This allows the authors
to break the observations into many categories across many axes while
retaining the necessary number of cases per group for higher statistical
certainty. For instance, Figure 2 in the publication breaks down the
observations into five categories based on the type of host’s response
to an applicant and then further down into two categories based on
black/non-black race groups. If the initial number of observations was
not very large, such break down into subgroups would not be possible
while retaining the accuracy of measurements as related to the
population of interest (see more in Task 1).

Similarly, data bigness allows the authors to separate the data into
sixteen groups, each representing a proportion of cases between a host
of certain gender and race and a guest applicant of certain gender and
race (Table 4 in the publication). This allows for the analysis of
heterogeneity across genders. The results show that even African
Americans discriminate against African American applicants, but African
American female hosts are more accepting of African American female
guests than other host groups are.

Relatedly, because the big data captures everyone in the population of
interest (i.e. hosts in the five metropolitan areas), there is not a
sampling error, because sample is the population.

Additionally, large number of available variables allow researchers to
test whether variables other than applicant’s race may impact the price.
They find that some, like listing’s photos, do, but when controlling for
those variables, the impact of race still persists.

Always-on aspect of the big data allows the researchers to check whether
a property has been filled eight weeks down the road. This allows them
to calculate the economic opportunity cost of discriminating based on
race by using this data to perform probabilistic calculations. This
allows to see the revenue foregone by hosts because of their choice to
discriminate if the property was not filled.

Another big data advantage that increases the study’s effectiveness is
non-reactivity. Because the experiment is performed in a natural
environment of the study subjects, the hosts’ responses are unlikely to
be polluted by Hawthorne effects. This in turn makes the results of the
study more scientifically sound.

Furthermore, because big data provides the researchers with information
on hosts’ previous clients and their profile images through a review
system, the study can compare its results with whether a host who does
not discriminate also has recent reviews from a black client, as one
would expect. This is indeed true, which externally validates the
experiment.

Further on the topic of validity, the researchers take precaution and
limit themselves to one listing for hosts who have multiple listings, so
as to not introduce additional risks of being detected by hosts, which
may introduce desirability bias in hosts’ responses. This increases the
study’s internal validity.

In regards to construct validity, as mentioned in Task 1, one more way
in which the study uses computational approaches to support its findings
is using Human Computation to support construct validity of different
names signaling gender and race. The results of the survey do validate
authors’ intuition about such names.

One big limitation the authors faced was big data’s inaccessibility,
where the Airbnb started blocking fictitious accounts’ access to sending
messages. As a result, the geographic span for recruiting participants
was limited to only five metropolitan areas. If one chooses to define
the population of interest as the nationwide metropolitan population,
the big data limited to five cities may be unrepresentative of the
nationwide population, effectively undermining the study’s external
validity.

*(3 pts) Identify the value-added of conducting both research projects.
That is, what do we learn from running both an observational study and a
field experiment that we could not learn from just one of these
methods?*

The main advantage of using both methods is that they are complementary
in balancing between causal versus explanatory priorities. As described
in Task 2, the observational study is more appropriate for explaining
the discriminatory patterns based on race, while the experimental design
is better for establishing causal mechanisms for such patterns.
Therefore, together the two studies broadly establish not only the
presence and the extent of discrimination effects in the Airbnb online
marketplace, but also that racial perceptions are indeed the grounds for
such discrimination.

Another way the two studies are complementary is that they study
discrimination against opposite parties of the economic transaction on
Airnbnb. Specifically, the observational study concentrates on studying
racial discrimination against hosts, while the experimental study does
so with respect to discrimination against guests (by hosts).

Therefore, together the studies show that discrimination is a two-way
street on Airbnb rental marketplace, something that neither study can
show alone.

In further detail, the randomization of treatment in the experimental
design allows for the detection of heterogeneity across genders, as
discussed in Task 2. While the observation study does not allow to
differentiate between taste-based versus statistical types of
discrimination, the experimental study has more to say on the topic.
This latter study suggests that this mechanism may be different for
different demographic groups (though the study does not explore this
further).

Moreover, the two studies suggest two different mechanisms through which
a person is racially discriminated against. The observational study
suggests profile images that signal race as a basis for discrimination,
whereas the experimental study suggests racially associated names as the
basis. Together the two studies complement each other in that they
distinguish between two different pathways for discrimination on the
same marketplace platform. Therefore, together they form a more holistic
picture on the topic of Airbnb discrimination.

On a cautionary note, there is some difficulty in forcing on an exact
complementarity between the two studies, as the experimental study was
hampered by Airbnb’s blocking of researchers’ accounts. As a result, the
study did not reach its initial goal of 10000 hosts which aimed to allow
calculating an effect in a subgroup, like African Americans in way that
is comparable with the observational study (see footnote 9 in the
experimental publication).

*(3 pts) Consider how you could apply a digital survey-based research
design to the primary question of interest from these two papers. What
are the potential drawbacks to a survey approach? How might you overcome
these drawbacks?*

One way to conduct a digital survey would be in the form of what
Salganik calls Enriched Asking. In such a design, there would be two
dataset pieces, one similar to the dataset collected by the experimental
study presented, i.e. the “digital traces” on Airbnb for hosts and their
listings. These would include all of the pertinent variables on host
characteristics and listings, as done in the experimental design. The
second would be results of a digitally distributed survey. This survey
would attempt to collect more data that are not available on Airbnb on
hosts. This may include, importantly, more detailed information about a
host to classify, say, how they react to applicants of not only
different races, but also different of socioeconomic statuses.

This would be an advantage over the original experimental study, because
one of the drawbacks mentioned by the authors was their inability to
distinguish a mechanism causing lower rejection rates for African
American names. One proposed explanation was that such names may be
correlated with lower socioeconomic status (SES). So the discrimination
could be based on either race, status or both. Capturing data on such
other potential explanatory variables can be done through a survey,
which would complement whatever is already available online. In this
case, the respondents, who would be a sample of Airbnb hosts, would be
presented with hypothetical scenarios of being contacted by a potential
client. The scenarios may be randomly assigned to each respondent in the
sample and vary from being presented by a non-black/white applicant
scenario with a low SES, a black applicant with a high SES, a
non-black/white applicant with high SES, and a black applicant with a
high SES. The race may be signaled by a profile picture, while the SES
may be communicated through a text prompt describing applicant’s SES
background. A respondent would then have a choice to accept or reject a
request. We could then measure effects of different race and SES
combination “treatments” through survey mechanism to disentangle race
versus SES effects which is hard to do in the experimental (or the
observation) study. Survey’s graphic design would mimic the Airbnb
environment as much as possible.

One advantage of this survey approach is that it is not intrusive on the
Airbnb environment, because the acceptance/rejection is hypothetical. In
the studies presented, participants’ experience did not differ much from
a normal one. However, in the case of the experiment study, the
intrusion was noticed by Airbnb, which blocked researcher’s accounts.
This would not be a risk in this survey-based study.

One potential obstacle to collection of survey data would the
recruitment process. Trying to recruit hosts for the study directly on
Airbnb may be against the Terms of Service for Airbnb. Moreover, some
potential participants may flag recruitment message to Airbnb, which
would result in much the same account blocking or deletion. A different
way to recruit hosts may be through online communities where Airbnb
hosts gather. Fortunately, because of the platform’s popularity, such
host communities are widely available outside of the Airbnb marketplace
and are often in the forms of online forums (e.g. on reddit.com). So we
may recruit there.

Another disadvantage of the survey approach may be that the sample of
hosts recruited is unrepresentative of the Airbnb host population. To
address this, since we are already collecting Airbnb data on host
characteristics through web scraping, one may attempt to measure the
representativeness of the survey sample compared to the Airbnb
population of interest. Discrepancies between the two could be addressed
with MRP techniques to render the sample and respondents’ weights
accordingly to make the survey sample composition approximate
representativeness.

Another potential drawback of this survey study is that the scenarios
are played out in a hypothetical setting and one may argue that the
hosts’ responses would be unrepresentative of how these hosts would
actually behave in the real Airbnb environment, despite our best
attempts to emulate it within the survey instrument. However, since we
are using an enriched survey format, we would ask for participant
consent to link their survey data to their Airbnb profile. We could then
conduct a similar experiment as in the second study and send a request
to a host for one of their listings on Airbnb to check if their survey
responses match their real world behavior. Like with an experiment, one
hopes to do this experimental part without the participant’s prior
knowledge (but with a post-debrief possible) to avoid desirability bias.
We may then weight the response from each respondent based on how
“truthful” their survey responses may have been. For very “untruthful”
respondents, we may exclude them from the final analysis. This would be
the use of the Enriched aspect of the survey design.

One may object that such data linkage request (between Airbnb host data
and host’s survey data) may preclude many participants from joining.
There are two complementary ways to remedy for this. One is to use
inducements for participation. This could be monetary, as well as in the
form of a verbal explanation in the recruitment process that the results
of the study may help improve online marketplaces. Another way would be
to recruit for a longer period of time. Because of the popularity of the
platform, there are many hosts who may be potential participants. Even
if the rate of agreeing to participate in our study is very low, even a
small rate may result in enough recruited participants, since the
initial pool is so large. This would be harnessing the bigness of data
characteristic to recruit enough participants.

The end result would then be data similar to the experimental study, but
different in that it would be complemented with the additional data from
the survey responses. This would help resolve some of the limitations in
the original experimental study; notably, its inability to identify the
underlying mechanism causing worse outcomes for African American
name-holders.
