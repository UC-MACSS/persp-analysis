Climate Change Attitude Experiment
----------------------------------

##### MACSS 30000 - Assignment 3

##### Alexander Tyan

##### 10/30/2017

### Introduction and Research Question

Climate change and whether it is a result of human activity remains a
contentious topic in the US politics. Despite the scientific consensus
on the issue (Oreskes 2004), the wider US electorate is a lot of more
divided on the issue, with a significant portion of the US population
not convinced of (human-induced) global warming (we will consider
“climate change” vs “global warming” wording later) (Street et al.
2009). One of the common approaches often cited by those who advocate
for greater awareness of climate is information dissemination. This
approach implies that the lack of information is a reason why a portion
of the US electorate is resistant to the idea of (human-induced) climate
change.

Current study will test this assumption empirically and will attempt to
identify population characteristics that may or may not be amenable to
shifting their opinion on the topic once presented with the evidence of
climate change. The research question is: is exposure to information
containing evidence of human-induced climate change effective in
changing a person’s opinion about the topic?

Computationally-Enhanced Experiment Design

As per Salganik’s (2017) typology, this is a fully-digital field
experiment, with all four steps (recruiting participants, randomizing,
and delivering treatments, and measuring outcomes) done in the digital
realm.

Participant recruitment would be done online through Amazon’s Mechanical
Turk (MTurk). Consistent with previous academic practices on recruiting
from the platform (Berinsky, Huber, and Lenz 2012), we would require our
participants to have at least 95% approval rating from their previous
participation. Also consistent with such practices, we would compensate
each individual with $1 per study completion, since we expect the
participation to last no more than 10 minutes (Berinsky, Huber, and Lenz
2012). Study participants would have to be US citizens and of voting
age, since our population of interest is potential American voters.

We would then have all participants fill out an informed consent form
and a quick demographic survey (through, say, Qualtrics) with questions
about their age, voting history and political affiliation, education and
marital status, region of residence, religious beliefs, the size of the
city/town/village they reside in, etc. As per Salganik’s (2017)
suggestion, the wording for such standard demographic questions may be
drawn from previously tested questionnaires, so as to minimize question
bias in our responses.

In addition, we would ask about their opinion about the climate change
and global warming. Again, to use pre-tested question wording, we would
adopt Pew Research Center’s questionnaire on the issue (Street et al.
2009). The questionnaire uses “warming” as opposed to “climate change,”
and we would adopt the same approach. This is important, because
previous research shows that resistance to the idea of human-induced
climate change may be linked to question wording, with “global warming”
often eliciting more resistance from conservative voters (Schuldt,
Konrath, and Schwarz 2011). Since we are interested in how our treatment
may change an attitude about human-induced climate change, which is
signaled to conservative voters by the “global warming” term, using such
wording appears justified.

Immediately after the survey, respondents will be automatically and
randomly assigned to one of the groups. These groups model Salganik’s
(2017) full factorial design assignment. First group will watch a
3-minute video which will present scientific evidence on climate change
and how such change is due to anthropogenic factors. This will be
presented in a manner accessible to the general public, so as to
minimize the intervening effect of scientific complexity on our
audience. Second group will be shown a different 3-minute video. It
would contain a human-interest story of a US person experiencing
economic and personal hardship due to climate change, such as the threat
to their personal property due to rising sea levels. However, this video
will not present any scientific evidence and will not imply that climate
change is human-induced. Third group will be exposed to both videos,
with the scientific information video presented first. Fourth group will
be exposed to the same treatment, but with the order of the two videos
reversed from group three. Videos may be built into the survey
instrument flow.

Participants would then complete a post-treatment survey. Asking them
about their attitudes toward anthropogenic climate change again. This
would measure the outcomes of the treatment in comparing pre- and post-
treatment effects for this within-group treatment assignment. As such,
the groups would be as if they are their own control (Salganik 2017).

We may then perform statistical measurements to quantify each group’s
change in attitude (or lack thereof). Because we collected demographic
data, the tests may also allow us to see whether any characteristics
such as party affiliation, age, place of residence, education, etc. made
participants more or less receptive to treatment.

Such characteristics may also allow us to observe the heterogeneity of
treatment effects along these demographic groups. For instance, we may
discover that, among those with previous reluctance to the idea of
anthropogenic climate change, the treatment effectiveness varied along
age groups, geographic location or party affiliation.

Moreover, because of our full factorial treatment design, we may also
discover the mechanisms which may make attitude shifts more or less
likely. For instance, we may discover that, for groups not inclined to
believe anthropogenic climate change pre-treatment, neither scientific
nor human-interest videos alone have much effect. But we may also
discover that such treatments, when combined, do have a significant
effect post-treatment; or that when the human-interest story is
presented first, the treatment is more effective than in the reverse
order; or that, counterfactually, human-interest story alone is
effective. Such discoveries may show the effectiveness of different
mechanisms for attitude change in the population.

We now turn to how the digital nature of the research design may aid our
study.

### Justification and Strengths of (Digital) Research Design

The most obvious advantage of using the MTurk service is its cost
efficiency (Berinsky, Huber, and Lenz 2012). Salganik (2017) classifies
research costs into fixed and variable costs, asserting that fixed costs
are high, but variable costs are low for digital experiments. At every
stage – recruitment, randomization, treatment, and outcome measurement –
we would minimize our variable costs, in so far as, once the survey and
treatment instruments are set up, there would be little need for
researchers to be involved with the administration of the study
(Salganik 2017). Recruiting service is automated through the MTurk;
randomization and treatment assignment may be automated through the flow
control of the survey instrument linked to MTurk; and outcome
measurement is also done through the online survey instrument. The only
significant source of variable cost would be the financing of research
participants. However, because all other types of variable costs would
be already minimized, all remaining funding resources can be dedicated
to inducing participation.

Moreover, even when it comes to the fixed costs, because building of the
instrument is done through existing systems, such as MTurk and a linked
survey instrument, the set-up cost-efficiency may be quite effective. As
Salganik (2017) suggests, using existing systems is less costly. This
may be especially true because many educational institutions already pay
for the licenses for services like Qualtrics and make the service
available to all researchers across the institution. Freeing up the
resources by reducing the fixed costs as well further aids our
recruitment of participants.

As a result, we would be able to recruit a greater number of
participants, which leads us to another reason for using a
digitally-enhanced experiment. Cost efficiency that results in our
ability to recruit more participants enables us to perform factorial
design, where a higher number of cases is important because of splitting
the subjects into a greater number of treatment groups (Salganik 2017).
Moreover, more participants is better because each demographic group
would also have a greater number of cases, which would give us greater
ability to reliably measure heterogeneity of treatment across different
demographic groups. Such advantages would be not be possible with
“higher costs/less participants“ analog experiments.

### Weaknesses of Research Design

One possible criticism related to the strengths above may be that it may
be still costly to recruit many participants, since our costs increase
with each additional participant. One way to make sure that the study
will have sufficient funds for this is to estimate statistically before
the study how many participants would be needed to have enough for each
treatment/demographic group to achieve statistical validity.
Consequently, we would adjust our funding search process (by, say,
seeking sufficiently large grants) and maybe the pay structure to MTurk
workers to minimize marginal costs of recruitment (for instance, by
reducing pay to $0.75 per participant, which is still comparable with
previous practices (Berinsky, Huber, and Lenz 2012)). To reduce such
financial threats to statistical validity further, we would use video
materials (for the treatment) that have been already produced, as
opposed to producing our own. That way we may license an appropriate
material that we can ensure is still affordable.

Relatedly, regarding construct validity, the content of the
video-treatment may be unrepresentative of the proper treatment, e.g.
exposure to scientific information. This is because other aspects of the
video treatment may intervene, such as its aesthetic appeal. To minimize
such effects, we would propose a pre-study that would select video
materials that are most appropriate for this setting, making sure that
the intervening effects are minimal. But why would we insist on using
video treatment in the first place as opposed to, say, exposing
participants to text material with the same content? Because exposure to
videos may be more realistic to how public engages with such messages
(e.g.TV and social media), though this would also have to be verified
through a literature review.

Internal validity risks can be minimized through the automation
processes available thanks to MTurk and the survey instrument. The
digital nature of these systems would allow us to pretest thoroughly and
amend easily prior to deployment. This would minimize risks of
technological problems for our participants and other problems that may
threaten how the study is administered once deployed (i.e. internal
validity).

The biggest issue is external validity due to uncertain persistence
effects of the treatment, desirability biases, and MTurk sample
unrepresentativeness (Berinsky, Huber, and Lenz 2012). To address the
first problem, one can adjust the experiment to repeat post-treatment
measurements at several time points; perhaps right after the treatment,
and few weeks to few months after, though this may result in additional
costs, depending on the incentives to participants. Second and third
problems can be minimized by supplementing this experiment with a series
of follow-up studies conducted in different settings and with different
sample frames. If the results hold in research settings where
desirability bias is less of an issue and with different non-MTurk
participants, this may validate the experiment externally.

### Bibliography

Berinsky, Adam J., Gregory A. Huber, and Gabriel S. Lenz. 2012.
“Evaluating Online Labor Markets for Experimental Research: Amazon.com’s
Mechanical Turk.” Political Analysis 20 (3):351–68.
<https://doi.org/10.1093/pan/mpr057>.

Oreskes, Naomi. 2004. “The Scientific Consensus on Climate Change.”
Science 306 (5702):1686–1686. <https://doi.org/10.1126/science.1103618>.

Salganik, Matthew J. 2017. Bit by Bit: Social Research in the Digital
Age. Princeton, NJ: Princeton University Press.

Schuldt, Jonathon P., Sara H. Konrath, and Norbert Schwarz. 2011.
“‘Global Warming’ or ‘climate change’?Whether the Planet Is Warming
Depends on Question Wording.” Public Opinion Quarterly 75 (1):115–24.
<https://doi.org/10.1093/poq/nfq073>.

Street, 1615 L., NW, Suite 800 Washington, and DC 20036 USA202 419 4300
| Main202 419 4349 | Fax202 419 4372 | Media Inquiries. 2009. “Fewer
Americans See Solid Evidence of Global Warming.” Pew Research Center for
the People and the Press (blog). October 22, 2009.
<http://www.people-press.org/2009/10/22/fewer-americans-see-solid-evidence-of-global-warming/>.
