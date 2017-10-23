Measuring Public Opinion in a Game Community
============================================

Introduction
============

In this paper, I will introduce an efficient digitally-enhanced method
to measure public opinion of game communities. In game communities, even
though software developers have the arbitrary power to make game
changes, public opinions are influential. To keep players in game, many
developers respond positively to players' requests, and communication
between players and developers is decisive in a game's success.

The game community studied in this paper is "Clash-Royale".
"Clash-Royale" is a mobile card game where each player forms a deck of
eight cards and compete with other players. Because some cards many be
more powered (or weaker) than others, developers constantly implement
balance changes so that no card will dominate the game for long. My job
in this paper is to measure gamers' opinions on some cards, check
whether balance changes are necessary, and decide the new changes to be
released in the next patch.

I believe the result of this study can be generalized to polarized
communities, where a small group of people have control over most public
decisions. The case of game communities will serve as a prototype to
measure public opinion in polarized communities.

Research Question
=================

i)How to measure gamers' overall opinion about a card in a timely
    manner?
ii)How to know when a balance (of a card) is necessary?
iii)If a balance (of a card) is necessary, what changes should be
    implemented?

Research Design
===============

The study design consists of four key parts: quasi-EMA, sample matching,
wiki surveys, and amplified asking.

*Quasi-EMA*

A quasi-EMA study design is applied in this study. After completing a
game, players are asked to complete a wiki survey regarding to one of
the eight cards they have used in the last game. One player will not
complete the survey multiple times, however, the survey takes in a
natural setting and asks a player's feeling about a card that they have
just used.

*Sample Matching*

This study implements a nonprobabilistic sampling and divides the target
population into subgroups based on a series of grouping factors.
Grouping assumes that different subgroups will have different opinions
on the same card. For example, top-tier players will rate highly of "Hog
Rider" but not low-level players, partly because "Hog Rider" requires a
lot of practice to achieve its best performance. A list of grouping
variables includes account level, number of trophies, number of games
played, etc. Oversample (and weighting) may be applied if there is a
small estimated number of players in a subgroup.

Note that sampling is based on accounts and their attributes, rather
than players. To execute sampling matching, I create a pool for each
subgroup, and afterwards the system actively searches for respondents
(accounts) that fall into the subgroups (and prompts them to take the
survey). If a pool is full, it will discontinue search for new
respondents for that subgroup. If all the pools are full, then the
survey data is complete and ready for analysis.

*Wiki Surveys*

Respondents selected by the sample matching can voluntarily participate
in an in-game wiki survey. The system will randomly pick a card of the
eight cards the players have played in the last game and ask their
opinions on that card (Good/ Not Good). The system will further provide
two choices following the players' previous choice. For example, if a
player chooses "Not good", then the system will provide two choices
asking the player why the card is not good (e.g. "Slow", "Squishy"). The
respondent can also add his/her own opinions. In less than a minute, the
respondent can complete the survey and receive a reward of 10 gems (game
currency). I will review the survey results and update the choices if
some of the responses are not in current choices.

A score is generated for each card and its choices. A high card score
indicates the card needs a balance (nerf/buff), and a high choice score
indicates it is favored by most respondents. Balances can be based on
the choices of a high score card.

*Amplified Asking*

Since all the available digital traces and survey answers are stored in
the game database, I can construct an estimate model that predicts
survey data with only digital traces. The estimate model enables me to
get the survey estimates of the players who did not participate in the
survey. It also helps monitor the ebbs and flows of public opinion in
the game community in a timely manner.

*Justification for the method*

The four-element design is good for measuring public opinion because,
first, nonprobabilistic method is more appropriate in digital methods,
and sample matching ensures the rigorousness of this study. By the
assignment of each pool and weighting, I can reproduce the target
population and get an accurate estimate of each subgroup. The other
advantages of this method are: Wiki surveys offer players a fast, open,
and real-time way of communicating with the developers; Quasi-EMA design
prompts player's feedback without affecting much of game experience;
amplified asking enables prediction of unknown population as well as
nowcasting. A key concern of the study is data accessibility. However,
since the "Clash-Royale" case is a prototype of polarized communities, I
can conduct this research in game communities with open sources
available or during internship (e.g. independent developers, Steam
communities). A positive relationship between researchers and game
developers is very likely to occur because the research can increase
game profits.

Digitally-enhanced characteristics of this study
================================================

This study is digitally-enhanced in several ways. First, quasi-EMA wiki
surveys are used in this study. By a quasi-EMA design, respondents can
participate in this survey right after their games. They may be
delighted at winning or angry at their lost. In either case, respondents
are very likely to yield an accurate feeling how they think about a
card. This is much more efficient than asking people on a forum because
they cannot remember every detail when playing the card. The
introduction of wiki surveys, when linked to Supercell's database,
enable players to update their own feelings about a card and share them
with other players real time. Compared with traditional survey methods,
this always-on, digitally-enhanced property enables managers to get
instant feedback at much lower costs.

More importantly, digitally-enhanced surveys enable us to build a
connection between digital traces and survey data. In the case of
"Clash-Royale", observational data alone is highly useless. Even though
it shows hot picks and cold picks in the current meta, it does not
provides useful information where we can make changes and balances.
However, after establishing a link between observational data and survey
data, we are able to construct a prediction model upon which no further
survey data is needed. This characteristic is essentially powerful
because it makes the prediction for the present and future a lot easier
and faster.

Why the survey is better than an observational study?
=====================================================

I prefer survey to observational studies in this paper because it is a
lot easier to ask people for their opinions than using data to infer
what they mean. For example, the card "Three Musketeers" has an
increasing use rate and win rate. Does it mean the card is overpowered?
Or does it mean that the card has become a popular counter-pick to an
overpowered card? The conclusion is very likely to be wrong by only
inferring from statistics.

Additionally, I believe "Clash-Royale" is just a prototype of community
decision making, and community decisions cannot be made unless the
people and the authority reaches an agreement. Supercell needs to
respect their user to release game updates, a manager has to gain
support from his/her team members to initiate a project, and a ruler
must receive the consent of its people to implement a law. When a study
touches upon intersubjectivity, it is impossible to avoid a survey.

Moreover, I believe surveys and observational studies are complements
rather than substitutes. Survey offers high quality data for analysis,
and observational research is good for timely predictions. As I have
shown in my research, it is better to combine these two methods. We can
build an estimate model with available survey data and digital traces,
and we can use the model to make a fast analysis on a target population
by imputing survey data with our model and available digital traces.

Errors and Minimization Methods
===============================

Representation Errors:
----------------------

There are two possible types of representation errors in this study.
First are the sampling errors. Tired of competitive top-tier games, some
players may create multiple lower-level accounts to beat new players and
gain enjoyment ("*Smurfing*"). *Smurfs* imply that lower-level account
owners are not necessarily new or inexperienced players. Therefore,
pooling based on account level is not robust. To minimize this error, I
suggest adding more grouping variables to dilute the effect of account
level. For example, number of gems spent is a good grouping variable,
since people with multiple accounts are unlikely to spend many gems in
their lower-level accounts. Low-level accounts with significant gem
spending are unlikely to be *smurfs*.

Other than sampling errors, coverage errors are likely to occur in this
study. The *target population* is all the players in the game. However,
the *frame population* is the people who play the game during the
survey. People in and out of frame population are likely to be
systematically different. The former subgroup likes game better than the
latter. This is the trickiest part of the study, but launching a bonus
event is a promising solution because it is a good way to bring people
back. Coverage error is reduced if more people get into the target
population.

Measurement Errors
------------------

Wording strongly influences measurement errors. Even if two choices are
similar, the choice with fewer words are more likely to be selected (as
many people want to start their next game). To minimize measurement
errors, I will try to keep each choice of equal length. For example,
when a player is asked "Why do you do not like {Musketeers}?", he/she is
likely to receive the following two choices: "Squishy" or "Weak DPS" (of
similar length).
