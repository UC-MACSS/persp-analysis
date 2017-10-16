# Entry Regulation and Entrepreneurial Activities: Evidence from China’s Business Regulation Reform

**Zhiyu Fu**

## Introduction

Entrepreneurial activities are the main engine of innovation and economic growth (Schumpeter, 1911). However, entrepreneurship, especially small start-ups, is commonly hindered by entry regulations set by governments. Entry regulations are highly common, though in varied forms, across counties. An intuitive question is that if free market can achieve efficient outcomes as predicted by most economists, why do governments set entry regulations? What is the economic outcome of entry regulations?

In economic literature, there are two polar views explaining the motive of governments. According to public choice theory, illustrated by Stigler (1971), entry barrier raises the rent of government officials and insiders, and thus leads to the inefficient economic outcome; on the contrary, as public interest theory argues, entry barrier acts as screening mechanism by keeping low-quality firms out and thus corrects the potential market failure (Pigou, 1938). We propose to use China's business regulation reform to empirically evaluate the effect of entry regulation. 

China's business regulation reform, taking place nationwide in 2014, greatly changed the business environment. Previously, opening a new business in China requires tedious procedures, several months' waiting, and a deposit of registered capital, which were all simplified or canceled after the reform. Before the nationwide deregulation, the government piloted the reform in several, but not all, prefectures in Guangdong province, which can be exploited as an approximating experiment to estimate the treatment effect.

Utilizing this reform, we investigate the impact of entry regulations (more accurately, deregulations) on firm extensive margin, firm size, profitability, as well as the entrepreneurial characteristics. More specifically, we hope to answer the following questions in this paper: 
- Will the deregulation encourage more entry of firms? 
- Are those marginal entrants (those who would not have entered without deregulation) less productive than others?

## Data

The primary data we will use in this paper is a whole-sample firm registry database from the State Administration of Industry and Commerce (referred as SAIC in the following). Officially, all firms are required to register at SAIC, so all formal business activities are recorded in this database. As a whole-sample data, it has a large size: The number of new entrants in Guangdong Province during 2010 to 2015 is at the magnitude of 10^5 every year. This database also contains comprehensive information on registered firms including location, registry date, as well as the characteristics of the firm owner, such as age, gender, and education background.

Besides, SAIC also requires firms to report management information annually. Its annual report database includes their gross assets, sales, taxes, and profits. However, due to confidentiality of the data, the data we can access were processed. That is, all raw numbers are categorized into several intervals. For example, if a firm's gross asset is 25,000, it is recorded as 20,000~50,000 in the public database. We will discuss our solution to it in the following section.

## Method

The main feature of the pilot reform in Guangdong is that different prefectures started at the different time, ranging from May 2012 to March 2014. A matching strategy can fully exploit this situation. 

To answer the first question that whether the deregulation encourages more entry, we aggregate our data to prefecture level. We use **synthetic control** approach to estimate the treatment effect. Synthetic control is a method to evaluate the effect of an intervention in comparative case studies. It constructs a weighted combination of observations from control groups to approximate the treatment group based on target variables, and then compare the synthesized unit with treatment group to obtain the treatment effect (Abadie et al., 2010). One of the advantages of synthetic control is that it can be implemented even the treatment group is small, which just fits the situation of the prefecture-level analysis. We use the monthly entry at prefectures as the target variable, construct synthesized unit based on monthly entry and other economic variables of prefectures, and then compare the difference of post-reform monthly entry to estimate the treatment effect. In our hypothesis, the treatment effect should be positive. That is, after the reform, the monthly entry increases.

To answer the second question, we run a series of firm-level regressions from different aspects. Due to the large sample of firms, synthetic control is too computationally expensive; traditional difference-in-difference method fits this task well. The key x variable in these regressions is a binary variable denoting whether the firm entered after the reform at that prefecture. An ideal approach is to directly compare the marginal entrants with others. However, it is practically impossible to identify marginal entrants. Fortunately, if the statistical power is sufficiently large, we are still able to detect the difference with our model specification. The y variable includes the size of the firm, gross assets, profitability (sales/asset ratio, revenue/asset ratio), and the characteristics of the owner (age, education background), etc. Fixed effects are controlled. According to our hypothesis, the size and gross assets of the marginal entrants are presumably lower. For profitability, two theories diverge: Public choice theory predicts that profitability of marginal entrants is not different from others, while public interest theory predicts that marginal entrants are not as profitable as others.

## Discussion

The data we use for this study is a typical **Big Data** collected by the government for administrative purpose. One of the most striking characteristics is its bigness. Being so big, it provides sufficient statistical power so that as long as there is an economically significant difference between the marginal entrants and others, it will be detected by our model.

As a whole-sample dataset, it also avoids two issues that commonly plague social science research: Incompleteness and non-representativeness. Since all formal business are registered at SAIC, this dataset covers almost all operations of interest.

Nevertheless, our study still suffers from several problems of big data.

The most serious problem is the dirtiness of the data. Due to the imperfect administration system, though spending resources collecting annual report data, neither the SAIC nor local AICs attach importance to it previously. This data will not be used as policy guidance or valid statistics. There was even no standardized procedure for local AICs to collect annual reports from firms. Thus, the quality of annual reports data is poor. Fortunately, it will not be a too concerning issue for our research: It is plausible to assume the measurement error is random, so our estimates are still unbiased, and the variance generated by the measurement error converges to 0 due to our large sample size; even if it has a systematic bias, since we are estimating the treatment effect and there is no reason to assume the bias varies across the treatment group and control group, the systematical biases offset each other when we make a deduction.

Another issue is that due to the sensitivity of the data, we cannot access the original dataset but only a categorized version. There are several strategies to deal with this situation. First, we can use the median of the interval as an estimate and calculate the revenue/asset ratio based on it. The obvious problem with such approach is that it distorts the distribution of the y variables. A feasible remedy is using imputation method to manually add some randomness to the variable to recover its distribution. Second, we can also directly use the categorical variable with logistic regression. Thanks to the bigness of the dataset, the random error derived from categorization will not be a huge problem to our estimation.

In conclusion, this rich dataset provides us with a great opportunity to investigate into our questions. It does have some defects, but we can minimize the impact with statistical methods.


## Reference

- Abadie, A., Diamond, A., & Hainmueller, J. (2010). Synthetic control methods for comparative case studies: Estimating the effect of California’s tobacco control program. Journal of the American statistical Association, 105(490), 493-505.
- Pigou, Arthur C. (1938). The Economics of Welfare, London.
- Schumpeter, J. A. (1911). 1934. The theory of economic development.
- Stigler, G. J. (1971). The theory of economic regulation. The Bell Journal of Economics and Management Science, 3-21.