## Perspective on Computational Analysis
#### Assignment 5: Journal Article Improvement
#### Name: Xiang Zhang

### Introduction to the Article
The paper I choose to improve is "_Railroads of the Raj: Estimating the impact of transportation infrastructure_" by Dave Donaldson, a forthcoming article of _American Economic Review_. In the paper, the author wants to estimate how large are the benefits of transportation infrastructure projects and find out channels through which transportation infrastructure could affect a nation's economic performance.

### Dataset Collection of the Article
In order to estimate the effects, the author construct a panel dataset on 235 Indian districts, which tracks all districts annually from 1870-1930. Data on the output and retail price of 17 principal crops are collected to compute the real income (economic performance) of the district, and the data railroad networks is also collected.

All data are collected manually by the author and the data source is the official archival sources.

### Improvement the Data Collection as a Human Computation Project
The data collection process of this paper heavily restricted the number of data points the author has. The author only has 60 years data for 235 districts, with 34 variables available per district per year. Thus, the estimation he made was only a "local effects", with quite poor external validity.

To make his estimation external valid, we could make the data collection process a human computation project. That is, use human power to extract data from official archival sources of different countries and districts.

As we can see, the definitions of the variables he needs are quite simple: simply the output and the retail price of some crops, and the data on the railroad networks. Extracting these data points is super difficult for computers, but quite simple for humans. If the author can send a list of archival resources online as ask volunteers to help, then he can easily get the data he wants.

In my design, the volunteers will first spend a few minutes for a very simple training, telling them the definitions of the variables. Then they will be directed to the online archival sources (now many archival sources are online accessible). Each volunteer will be directed to certain book chapters which have not yet been viewed and extract the data points needed. To guarantee the data quality, a single book chapter will be assigned to multiple volunteers. Furthermore, we could use weighting methods similar to methods used in “Galaxy Zoo” project to improve the quality as well.

If the author improved the data collection process, there will be two evident advantages. Firstly, in this way, the authors can have more data points and significantly increase the statistical power of his estimation. Secondly, his estimation is no longer a "local effects", but a "global effects". Currently, he can only test his hypothesis using Indian data, which means that the estimation may lack external validity. By using human computation method, he can use data from all over the world and increase the external validity of his estimation.

### Reference
Donaldson, Dave. Railroads of the Raj: Estimating the impact of transportation infrastructure. _American Economic Review_, forthcoming.
