Research designs and computational methods
------------------------------------------

The two studies, [Edelman et al.
(2014)](https://github.com/UC-MACSS/persp-analysis/blob/master/assignments/final-exam/articles/digital-discrimination-airbnb-2014.pdf)
and [Edelman et al.
2017](https://github.com/UC-MACSS/persp-analysis/blob/master/assignments/final-exam/articles/digital-discrimination-airbnb-2017.pdf),
both utilize research designs that rely on significant computational
methods not present in other studies. Thus, to truly understand them, it
is important to understand what they are doing and how they rely on
computational methods.

### Research designs

The former study, (Edelman et al. 2014) is interested in measuring the
level of racism on AirBnB, which it operationalizes as the price of
rooms for black sellers relative to whites. Because Airbnb allows
sellers to put up photos of themselves (and people do so in order to not
look suspicious), it is customary for everyone to do so. However, this
added transperency also adds the possibility of racism since black
sellers might be discriminated against when everyone can see a photo of
them. The authors wanted to measure this and see if racism did indeed
play a role. Thus, this can be classified as an observational study. To
use [Salganik's
(2017)](http://www.bitbybitbook.com/en/observing-behavior/designs/forecasting/)
term's, it is a non-forcasting "rain-dance" study because it tries to
uncover the causal mechanism (racism) behind lower prices, rather than
simply predict how low the price will be. Likewise, as an observational
study, it only measures available data that is not otherwise intervened
upon by the researcher.

In the latter study, Edelman et al. 2017 look at racism in Airbnb from
the buyers' perspective. Similar to [Milkman et al
(2015)](http://web.a.ebscohost.com.proxy.uchicago.edu/ehost/detail/detail?vid=0&sid=f913e5bc-1acc-41ff-ba06-3c614b8e0a2f%40sessionmgr4008&bdata=JnNpdGU9ZWhvc3QtbGl2ZSZzY29wZT1zaXRl#AN=2015-15680-001&db=pdh),
they do digital experiment where they create profiles of people with
black or white sounding names and proceed to send rent requests from
those names and measure if there are systemic differences. The idea
being, given that the only information is from the name, if black
sounding names were systemically more likely to be denied rent, then it
shows that there is a bias against black renters. Here, again, the
independent variable is race (and gender) and the dependent is whether
they are accepted as renters. Thus, this can be considered an
experimental design since the researchers are actively intervening by
sending fake requests.

### Computation

Both use computational methods to leverage their research designs.
First, they each require large-scale computational methods to run the
projects, making them "big data." In both studies, there were around
4000 and over 6000 observations respectively, using complex tasks that
would take a long time if it was done by the few researchers. In these
cases, identifying the race of thousands of people, or having several
accounts send over 6000 fake rent requests would have taken months by
hand from the researchers. Instead, the authors of the 2017 paper used
software such as the Face++ API to analyze past guests and programming
to send the requests. Likewise, they used the collaboration of Amazon
M-Turk workers to classify the host's age, sex and race. Finally, in the
2014 study they also carried out a digital survey to see if name
perceptions line up with theory.

They also made use of the "always on" feature of digital data, in that,
because it is based online, they could get information in real time
instead of just from the past. Here, the study was taken the latest year
the authors wanted to know the question around 2014 and 2017. This was
especially prescient with the 2017 study which made use of the most
current sellers. Finally, the studies were "non-reactive" in that they
did not require participants to come down from a lab but instead could
simply run tests of subjects who were online. As Salganik notes, this
non-reactivity reduces the possibility for experimenter bias and thus
get more accurate results.

Effectiveness
-------------

### Edelman et al. (2014)

This paper, perhaps showing why it is unpublished, has some serious
limitations in its findings. First, when it comes to the construct
validity (or how well the research design was set up) it is inherently
limited by its observational design. First it is worth noting that the
concept of internal validity, or how effective randomization was carried
out, does not apply since it did not have any randomization within the
design. Thus, it is fundamentally a study that uses external validity,
or whether it is able to generalize to the larger population. However,
here it falls flat, the paper only looks at Airbnb hosts in New York
City, which, despite being an important global hub, is not
representative of most cities and probably not even of most large cities
in the United States. However, one positive is that, because it is an
observational study, there is no Hawthorne effect or experimenter bias
influencing the study.

When it comes to issues of heterogeneity, or differential effects among
different groups within the study, it makes little distinction on the
ultimate dependent variable beyond whether the sellers were black or
white. This could be problematic since there might be divergent effects
from different groups, for instance there could be large differences
between the prices black men and black women set (and similarly for
white people) which might need to be accounted for. However, they did
use numerous controls for various quality and social media indicators,
such as whether black sellers had social media like LinkedIn and
Facebook listed or the photo quality of the seller, ultimately finding
it made no difference. These controls somewhat help the study's
findings. Finally, there was no real testing for the causal mechanism,
or the process that explains the outcome, outside of using the
previously mentioned proxies. Of course, sites like Airbnb do not have
direct measurements of racism and the design depends on proxies. Thus,
especially given an observational design, it is inherently difficult to
gauge the mechanisms involved.

Ultimately, the study's findings give decent external validity for
whether there is racism in the selling of Airbnb spots in New York City.
However, when it comes to going beyond that one city, the study is
limited.

### Edelman et al. (2017)

The later Edelman et al. is highly effective in the way it is
constructed. First on the topic of construct validity, it is somewhat
mixed when it comes to internal validity, or the effectiveness of
randomization. For instance, while as an experiment it attempts to have
clear controls by gender and race, one thing it does not do is control
for is the geography among the different treatment groups. That is, an
ideal experiment would use different race/gender requests in highly
similar areas to show that there are not different biases within
different geographic areas. Likewise, they write that they were unable
to control for possible socioeconomic associations with racial names (ie
such as testing for the difference between a poor white name and a rich
white name) which might harm their inference. Thus, while there is
randomization, it is somewhat mixed in what it gets us.

In contrast, the external validity is high. Here they look at the top 20
metropolitan areas in the United States which is where most Airbnb
renting would occur. Likewise, despite being an experiment there was no
Hawthorne effect because it involved getting people who are online and
thus unaware of the experiment. That is, people were not biased by being
observed by the experimenters. One of the places where the paper shines
is in its accounting for heterogeneity. Much like the climate change and
power usage study that looked at ideological differences, they were able
to control for the race gender and age, of the hosts and past buyers,
along with the race and gender of the buyers. This allowed them to make
inferences differential effects such as in-group bias although they
found it had no statistical effect. They even showed the request
acceptance rate among all the names to see if any individual buyer had a
lopsided effect.

Finally, they have no direct way of measuring their mechanism, namely
racism, but they do try to have a control with sellers who have never
rented to a black person before. Thus, their results for mechanisms are
somewhat mixed. Ultimately, the things this paper did well included its
external validity, and methods of finding heterogeneity of racism on
Airbnb.

Experimental and observational studies.
---------------------------------------

When it comes to research design, there are certain things that
experiments and observational studies are optimized at but that the
other is less capable of doing. For example, when it comes to internal
and external validity, there are clear trade-offs with each. For
instance, experiments are really the only research designs capable of
internal validity because they use randomization as part of their
process and thus can clearly delineate the causal effects. However,
observational studies, by their very nature, are much better at
maximizing external validity because they are fundamentally observing
how people behave in practice without any constraints created as part of
an experiment. As an example, something like forecasting, which has very
high external validity, would be difficult to do with experiments.

These are, however, ideal types. When it came to the two studies
specifically, these differences were not optimized for (at least as far
as the 2014 paper is concerned). In theory, the observational paper
could have been much better at capturing external validity, it was
hampered by only looking at Airbnb in the New York City area.
Ultimately, observational studies are good at external validity while
expirements are better at internal validity.

Survey
------

### How I would do it

To answer this question through a survey design, I would use an enriched
asking approach similar to the Facebook personality study done by
[Kosinski et al. (2013)](http://www.pnas.org/content/110/15/5802.full).
That is, I would have thousands of participants come in for a
personality survey, indirect social questions regarding racial hostility
(ie questions of how "warmly" they feel towards groups like black
people) and Implicit Association Tests (IAT). These would require giving
their Airbnb accounts and compare their performance on the tests with
whether they rented to black people. As controls, I would also ask for
their demographic information to see if factors like where they grew up
or their income (as well as the controls in the study for things like
gender, race and sex) affected this. This would be able to control for
various confounders as well as be able to find the causal mechanism
(that is, latent racism) with the IAT and indirect race relations
questions. That is, those with a higher IAT scores and more problematic
racial answers should be less likely to have rented to black people.

### Potential problems for surveys

However, there are numerous issues in general with running survey
designs regarding racism. First, there is the issue of recruitment.
Whether it is a digitally-enriched sit-down survey, wiki survey or some
other design, it is difficult to get a representative sample of people
to take the test, largely because it is inconvenient for many people to
take long surveys. When it is more conveinent, such as a ecological
momentary assesment (EMA) there are logistical problems with developing
an app that can carry out the survey, as well as privacy concerns with
how much phone data one is allowed to observe.

In some cases there are also costs, while most digital surveys are cheap
even for thousands of people to take, when it comes to incentives to get
them to take the test, then it becomes much more expensive to compensate
thousands of survey takers. Likewise, for things like EMAs, that require
their own app or platform, it is expensive to pay to have one built.
Likewise, there are issues with having biased or improperly worded
surveys that could skew the reuslts. Finally, there are issues with the
Hawthorne effect and social desirability bias especially when it comes
to issues of racism that people would not want to divulge directly.

### Potentional solutions

However, I would have various ways of overcoming these pittfalls. First,
I would partner with Airbnb to try to get them to promote the survey for
their sellers in exchange for cash incentives the company would provide.
In exchange, I would give them the personality, indirect race questions
and IAT data to do with as they wished. Likewise, because this would be
part of their terms of service, and voluntary on the part of the
sellers, it would be much less ethically problematic. I would get around
issues of the Hawthorne effect by having them take it online (and as
sellers, they are already very likely to be real people). Finally, I
would sidestep issues of the social desriability bias by having them
take the indirect questions and IAT which would not directly ask them
these sensitive questions. Finally, since the questions and tests are
indirect, there should be few problems with the wording of the test.
Ultimately, these would solve many of the issues of doing a survey
design about racism on Airbnb.
