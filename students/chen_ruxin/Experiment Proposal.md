## Identifying the psychological effect of conformity on purchasing intention of different age groups: empirical evidence from a Chinese online retailer
### Introduction 

Conformity, as described by Cialdini and Goldstein (2004), refers to the act of changing one’s behavior to match the responses of others. As established in my previous proposal, individuals are often motivated to mimic the behavior of others through informational or normative conformity to maintain their self-concept. Also, previous literature has identified age differences in resistance to peer pressure (Steinberg and Monahan 2007), and suggest that there are possible age differences regarding tendencies ot conform.

Much like in the survey proposal, this study also wishes to examine if the psychological effect of conformity on the purchasing intention across different age groups. To be explicit, the paper intends to examine if, in the specific context of purchasing behavior regarding trending items, the effect of conformity is stronger and more pronounced for specific age groups - this time adding a control group using an experimental method to establish causality.

The study will be conducted via a digitally-enhanced experiment from the biggest Chinese online shopping website, Taobao. By manipulating the information revealed to experiment participants, the interpretation of the effect of conformity on consumers' purchasing intention is causal. The findings of this paper can help online retailers improve the efficiency of transactions. For example, modifying their item-sorting algorithm in accordance with customers in different groups: for groups that have high score of conformity, which indicates higher propensity to purchase trending items, increases the weights of trending items so that they can be observed at first; whereas for the consumer groups that are not affected by conformity, rank the trending items lower.

### Experimental Design 

We intend to implement a randomized controlled experiment via a mega online retailer in China, Taobao. By the end of August 2017, Taobao has more than 500 million of registered members as well as 369 million of monthly active users. Given the enormous amount of users, Taobao is a perfect platform to collect a large sum of data as well as identifying the heterogeneous effect on the sub-population. Since it is hard to measure the purchasing intention of consumers from observational data, we incorporate an online survey to the experiment.  

As mentioned in the introduction, it is reasonable to suspect that the effect of conformity on purchasing intention varies across different age groups. Furthermore, acquiring information on the average treatment effect does not seem to contribute to Taobao's sorting algorithm, since the current webpage has incorporated a function to allow browsers to sort by item popularity. In this case, Taobao may lack an incentive to start the partnership. Hence, we put emphasis on examining the heterogeneous effect for different age groups rather than the average treatment effect across the entire population. As the vast majority of Taobao's consumers age between 10-60, we define five age groups to be studied are 10-20, 20-30, 30-40, 40-50 and 50-60. The intended duration of the experiment is one month and we expect to collect 100000 observations. Once the specified amount is collected, we stop hiring participants. Based on the fact that more than 70% Taobao monthly active users that are in their 20s or 30s, a post-stratification is conducted to make the observations of each age group consistent with the corresponding proportion of Taobao's users.  

#### Experimental Procedure 

A survey is designed to pop-up after the users log in and enter the apparel department. Before the survey starts, the consumers are informed that: 

"the survey is designed to study the purchasing behavior of Taobao's consumers. Your completion of the survey will contribute to the optimization of Taobao's sorting algorithm in order to facilitate your future purchase. During this survey, you will be presented some images of apparel, a brief product description, and associated price, and you will need to choose from a scale that can best represent your purchasing intention." 

Consumers can choose whether or not to participate. The first question asks for their age group and gender. After this, we randomize the participants into two groups. They are presented with the same trending items and their product description except that in the first group, we inform the participants that items are trending, while no such information is revealed to the second. The trending items presented are redefined daily according to the 10 most popular items on the list of the previous day, for the associated subgroup which is explained in the next paragraph. The survey participants are shown a five-point Likert scale to indicate their willingness to buy the product, with five representing "definitely buy" and one representing "never buy". 

#### Major Experiment 

In terms of informational conformity, the individual will mimic the choice of others concerning to deviate from social norms. However, the manipulation of information may have a heterogeneous effect on different consumer subgroups, and in some cases, being informed of "trending items" does not necessarily cause a psychological effect of conformity. Reference group, a marketing term, describes a group to which an individual is compared. There are three types of reference groups: 

1. Dissociative group: the group that the individual wants to distance him or herself from; 
2. Membership group: the group that the individual currently belongs to; 
3. Aspiration group: the group which the individual would like to be associated or identified with. 

The trending items defined by the rank of the total sales heavily rely on the purchasing power of the majority consumer group. Clearly, the individual's purchasing intention is affected by his/her classification of other buyers to these groups. For example, a customer with a higher income than the median Taobao consumer will be reluctant to buy a trending item, which he/she considers as a member of his/her dissociative group. On the other hand, a frugal consumer may think wearing a trending item is a signal of being at the frontier of fashion. 

To overcome this problem, my experiment will further divide the participants into several groups according to their transaction history. A data-driven clustering technique from unsupervised learning is applied to determine how the subgroups are classified. Next, we sort the sales of items of each subgroup and collect the most popular 10 items of the associated subgroup on a daily basis. Following that, we present the graphs and product information of the trending items from the subgroup that the individual belonging to. Similar to the previous experiment design, no information is provided with the control group. However, we inform the participants in the treatment group that "these are trending items from people have bought the same items as you". The revised message takes into account of the variation of the definition of "social norms" for different individuals, therefore, it guarantees that the manipulation of information can genuinely induce conformity, not the other way around. 

The tested hypothesis is whether the means are different for the control and treatment groups. We want to test this hypothesis on a daily basis so that the result from presenting different trending items are not conflated. We can plot the mean difference between the treatment and control groups for different age groups. A positive significant mean difference suggests a higher propensity to purchase trending items driven by conformity. Moreover, if the conformity does have a heterogeneous effect on the purchasing intention of different age groups, the negative/positive difference of age groups should be persistent across the experiment period. 


### Assessment of Experimental Design

#### Internal Validity  

In order to verify that the injection of information does induce conformity, we run a parallel experiment based on the subgroup identified in the previous section. Taobao’s algorithms display a series of similar items after a transaction is completed. Consumers will be informed that the displayed items are also bought from individuals who purchased the same items in this completed transaction. According to this design, we can conduct an experiment of 1000 individuals who bought the same items. Then we randomly choose 500 individuals for which the information is omitted, ceteris paribus. We measure the magnitude of conformity by counting the number of clicks of the displayed items between the treatment and control groups. If the mean difference of the treatment group and control group is positively significant, then we can conclude that our experimental design is valid in terms of manipulating conformity. 

There is a potential threat on the internal validity of the proposed study. Even though we randomize the survey participants into two groups to manipulate the information of trending items, we cannot guarantee that the control group has no prior information regarding the trending items: individuals can know about the trending items from publications or friends, and trend-savvy individuals may sense what is trending without being explicitly informed. Although the trending items are redefined daily, which increases the difficulties of information collection to some extent, we cannot deny the possibility of the information leakage through other channels. If that is the case, the treatment effect is attenuated since we over-estimate the purchasing intention of the control group.

#### External Validity 
Admittedly, the external validity of the proposed study is questionable since our experiment conducted only in the apparel department. Generalization of the result into other consumption categories needs to be done with caution.  

#### Causal Mechanism
Since the randomization occurs after the selection of survey participation, we expect that there is no systematic bias and the experiment design leads to a good estimation of the causal effect of conformity on purchasing intention. 

#### Advantages over using observational   

As the nature of this research question, the measurement of conformity and purchasing intention is difficult using observational data. One possible way is that we can compare the spending of the trending items to the spending of some comparable items across different age groups, after controlling the characteristics including product category, price, appearance, texture, and brand. The difference can approximate of the effect of conformity. However, the actual purchase behavior is not a good reflection of purchasing intention. Furthermore, the findings of the study will heavily rely on the similarity of the trending items and non-trending items, and it may not be possible to find such comparable items. Two items with similar product characteristics may have a significant difference in sales that is caused by some unobservable factors rather than conformity. 

###References

Steinberg, Laurence, and Kathryn C. Monahan. "Age differences in resistance to peer influence." Developmental psychology 43, no. 6 (2007): 1531.

Santor, Darcy A., Deanna Messervey, and Vivek Kusumakar. "Measuring peer pressure, popularity, and conformity in adolescent boys and girls: Predicting school performance, sexual attitudes, and substance abuse." Journal of youth and adolescence 29, no. 2 (2000): 163-182.  

Cialdini, Robert B., and Noah J. Goldstein. "Social influence: Compliance and conformity." Annu. Rev. Psychol. 55 (2004): 591-621.









