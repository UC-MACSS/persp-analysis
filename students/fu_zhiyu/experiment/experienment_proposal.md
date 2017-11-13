# Self-Deletion and Decision-Making for Low Probability

**Zhiyu Fu** 

## Introduction

Decision making under risks is highly common for everyone. Traditionally, economists rely on the rational expectation model to predict one's behavior under risks, while more and more evidence showed that human's behavior under risks is far from being rational. For example, Kahneman(1979) found that the very low probabilities are generally over-weighted in people's decision weight function. That is, people tend to over-react to the very unlikely events.

In this paper, we are going to explore one of the factors influencing people's rationality when making the decision under risks. Specifically, we focus on the case where people deal with low probabilities when they are **self-depleted**. We argue that when depleted, people are more likely to overweight the low probabilities. 

Self-depletion refers to the phenomenon that after making self-control efforts, people tend to fail in the subsequent self-control tasks. i.e., people's self-control resources are limited and can be depleted (Baumeister, 1998). Though self-depletion is a concept in personality psychology or social psychology, it has a deep cognitive foundation. Studies have shown that in the state of self-depletion, people's analytic system is also impaired. According to the competing dual system model, once the analytic system is impaired, the experiential system will prevail in people's thinking, knowing and information-processing (Epstein, 1994).

In the mode of experiential thinking, people rely more heavily on *affect heuristic* (Slovic, 2004). Affect means the specific quality of "goodness" or "badness" toward a certain stimulus (target). Affect is influenced by many characteristics of the stimulus, such as memorability, imaginability, and availability. For example, being bitten by a snake is more effectively salient than an electric shock and thus weighs more in decision-making.

The disproportionally high weight for the very low probability can also be explained by affect heuristic theory. When probability increases from 0 to a small value, such event begins to trigger people's affect and thus have a huge effect on people's decision-making, while the same increase in probability from 0.49 to 0.50 has little effect on people's affect and therefore won't influence decision too much. Support for these arguments comes from Rottenstreich and Hsee (2001), who showed that if the potential outcome is emotionally powerful, people are more irrational when making decisions.

Therefore, the potential mechanism for our hypothesis is as follows: after self-depletion, people rely more on their experiential system and thereby affect heuristic, and subsequently stronger affect heuristic lead to over-reaction to small probability. According to this mechanism, the effect of self-depletion depends on the affectiveness of the stimulus: self-depletion will have little effect in the decision-making toward an affect-poor target, but has a large effect in the decision-making toward an affect-rich target. We designed an online experiment to test our hypothesis.

## Method

### Design and Participants

This experiment is based on a 2 x 2 between-subject factorial design. One factor is depletion or non-depletion, the other is the affectiveness of the stimulus (affect-rich vs. affect-poor). The main dependent variable is whether participants will buy the provided lottery with a low probability of winning. We aim to detect the main effect of self-depletion, as well as the interaction of two factors to explain the mechanism.

The participants are recruited from Amazon Mechanical Turk. Since the experiment is conducted online, we could expect a large sample size of 400 (100 for each condition). Participants are randomly allocated to four conditions. To avoid participants' guess of the aim of the experiment, the task is labeled on MTurk as a text recognition task to build a training set for machine learning model. After the completion the main self-depletion task, they are paid $2 and offered a chance to buy a lottery, which is our dependent measure. After making the decision, they are told the real aim for this task and they can exit. The whole experiment can be completed in 5 minutes.


### Procedures

First, participants are asked to complete a text recognition task, which is actually the manipulation of participants' self-depletion status. Participants are presented with a two-page English passage. The control group are asked to highlight all instances of letter e in the text. People can learn to do this task easily and quickly, and they can become accustomed to scanning for every e and highlight them. To raise the cognitive difficulty and deplete their self-control resources for the treatment group, we ask them not to highlight the e if some certain criteria are met. Those criteria are designed to be complicated and hard to follow. For example, they should not highlight the e if there is another vowel adjacent to it. These participants will at first scan all e and want to highlight it at the first glance, but have to overcome such simple response if any criterion is met. This process involves heavy regulation, and thus generates self-depletion. According to the meta-analysis, this technique is the most efficient one for manipulation of self-depletion (Hagger, Wood, Stiff, & Chatzisarantis, 2010).

After the manipulation, all participants are required to complete a short questionnaire to test the validity of manipulation. The questionnaire consists of items like "I feel exhausted after the task". Participants response on a Likert 5-level scale.

Afterwards, participants are told the task is over, and they can get $2  as the reward. However, they are also offered a chance to get a lottery instead of money. All participants are randomly and equally divided into two groups. For the affect-rich group, they have the probability of 0.1% to win a $1000 coupon for a European vacation; for the affect-poor group, they have the same probability to win a $1000 coupon which can be used for tax payment. A European vacation is more imaginable and more vivid than tax coupon, so the European coupon will arouse stronger affect in participants. This manipulation is modified based on the Rottenstreich and Hsee's (2001). Whether the participants choose the lottery is the main dependent variable. Note that the exception of the lottery is $1, less than the riskless fee they can get. Therefore, choosing the lottery violates the classical rational expectation model. In addition, the lottery is not hypothesized: We will use a random number generator to determine who (if any, given the small chance) win the coupon, and send him the money.

### Statistical Method

We use two-way ANOVA to analyze the data. According to our hypothesis, the main effect for self-depletion should be significant: Depleted participants are more likely to choose the lottery, i.e., overweight the small probability.

The interaction between depletion and affectiveness should also be significant. According to our hypothesis of the mechanism, facing an affect-rich stimulus, depleted participants are more likely to over-react; while when facing an affect-poor stimulus, since it cannot invoke strong affect heuristic, depleted participants behave similarly with non-depleted participants do. The figure below summarizes our expected results.

![Expected Result](interaction.png)

## Discussion

### Validity

Our experiment has strong validities. For internal validity, since the experiment is conducted online without experimenters, all participants are randomly assigned to four conditions and received standardized procedures and instructions. We choose the manipulations that has been well-tested by previous studies to achieve the best construct validity. With respect to statistical validity, we use two-way ANOVA to analyze the data, the canonical approach to deal with the 2 by 2 x 2 between-subject factorial design.

External validity is always relatively weak for this kind of experiments. The potential problems for external validity may arise from two aspects: the representativeness of the participants and the generalizability of the scenario in the experiment. For representativeness, as we recruit participants on MTurk, admittedly, there is a selection bias to some extent. However, compared to the traditional in-lab sample which mainly consists of students on a campus, participants on MTurk have significantly and desirably more diverse background (Casler etc., 2013). Second, our variables of interest, self-depletion, and affectiveness, are relatively fundamental in one's cognition so that the variation among people is relatively smaller, compared to the variation of other socio-economic variables. For generalizability,  instead of an imaginary lottery, we use a real lottery and real decision-making to obtain the true reaction when people making risky decisions. According to Hsee (2001), real decision-making situation can reveal individual's true preference for risks and are more correlated with real-life decisions. 

### Mechanism

As discussed above, our experiment is able to test the potential mechanism of the effect of self-depletion on decision-making under risks. We did not incorporate the measure of heterogeneity of treatment effects for two reasons: First, the heterogeneity of treatment effects is not the main interest of our study. Second, in order to test the heterogeneity, we have to apply a three-factor design,  which requires a larger sample size and the result could also be hard to interpret. To focus on our research question, we stick to the 2x2 design.

## Reference 

- Baumeister, R. F., Bratslavsky, E., Muraven, M., & Tice, D. M. (1998). Ego depletion: is the active self a limited resource? Journal of Personality and Social Psychology, 74(5), 1252.
- Epstein, S. (1994). Integration of the cognitive and the psychodynamic unconscious. American Psychologist, 49(8), 709.
- Rottenstreich, Y., & Hsee, C. K. (2001). Money, Kisses, and Electric Shocks: On the Affective Psychology of Risk. Psychological Science, 12(3), 185–190. doi:10.1111/1467-9280.00334 
- Slovic, P., Finucane, M. L., Peters, E., & MacGregor, D. G. (2004). Risk as Analysis and Risk as Feelings: Some Thoughts about Affect, Reason, Risk, and Rationality. Risk Analysis, 24(2), 311–322. doi:10.1111/j.0272-4332.2004.00433.x
- Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. Econometrica: Journal of the Econometric Society, 263–291.
- Casler, K., Bickel, L., & Hackett, E. (2013). Separate but equal? A comparison of participants and data gathered via Amazon’s MTurk, social media, and face-to-face behavioral testing. Computers in Human Behavior, 29(6), 2156-2160.