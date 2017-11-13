R Notebook
================

Load Helpful Packages
---------------------

``` r
rm(list=ls())
set.seed(1)
library(tidyverse)
```

    ## Loading tidyverse: ggplot2
    ## Loading tidyverse: tibble
    ## Loading tidyverse: tidyr
    ## Loading tidyverse: readr
    ## Loading tidyverse: purrr
    ## Loading tidyverse: dplyr

    ## Conflicts with tidy packages ----------------------------------------------

    ## filter(): dplyr, stats
    ## lag():    dplyr, stats

``` r
library(scales)
```

    ## 
    ## Attaching package: 'scales'

    ## The following object is masked from 'package:purrr':
    ## 
    ##     discard

    ## The following object is masked from 'package:readr':
    ## 
    ##     col_factor

``` r
library(knitr)
theme_set(theme_minimal())
```

Create the Function
-------------------

``` r
income_sim <- function(p, g, SD, years, starting_income, simulations){
  
  #empty matrix to save data output
  income_data <<- as.data.frame(matrix(nrow=years, ncol= simulations))
  
  # loop for simulations
  for (j in 1:simulations){
  
  #find error terms
  Errors <<-  as.data.frame(matrix(nrow=years, ncol= 2))
  colnames(Errors) <<- c("Year", "Error")
  Errors[,1] <<- 2019:(2019+years-1)
  Errors[,2] <<- rnorm(years, mean = 0, sd = SD)

  
  #first year
  working_income <- log(starting_income) + Errors[1,2]
  income_data[1,j] <<- round(exp(working_income))
  
  #model
  for (i in (2:years)){
  working_income <- NA
  working_income<- ((1-p)*(log(starting_income)+g*(Errors[i,1]-2019))) + 
                    p*log(income_data[i-1,1]) + 
                    Errors[i,2]
  
  income_data[i,j] <<- round(exp(working_income))

  #tidy up
  rownames(income_data) <<- 2019:(2019+years-1)
  names(income_data)[j] <<- paste("Simulation", j, sep="_")
  
  }
  }
  return(income_data)
}
```

1. Simulate the Data 10,000 Times
---------------------------------

``` r
income_sim(SD=.1, p=.2, g=.03, starting_income = 80000, years = 40, simulations = 10000)
```

1. Graph An Example Graduate
----------------------------

``` r
ggplot(income_data, aes(rownames(income_data), Simulation_1))+
  geom_col()+
  scale_x_discrete(breaks=seq(2019,2058,3))+
  scale_y_continuous(breaks=seq(20000,300000,30000), label=dollar_format())+
  labs(x="Year", y="Income", title = "Expected Yearly Income of Single MACSS Graduate")
```

![](Simulation_HW_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-1-1.png)

2. Create a Histogram
---------------------

The Data Appears (approximately) Normally Distributed

``` r
income_data %>%
  slice(1) %>%
  gather() %>% 
  ggplot(aes(value))+
  geom_histogram(bins=50)+ 
  scale_x_continuous(label=dollar_format())+
  labs(x="Income Distribution", y="Frequency", title = "Distribution of MACSS Graduate Incomes")
```

![](Simulation_HW_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-2-1.png)

Percentages of Incomes
----------------------

``` r
income_data %>%
  slice(1) %>%
  gather() %>% 
  mutate(percent_under = (sum(value < 70000)/NROW(value))*100) %>% 
  mutate(percent_over = (sum(value > 100000)/NROW(value))*100) %>% 
  select(percent_under, percent_over) %>% 
  slice(1) %>%
  kable(col.names= c("Percent of Class Making Under $70,000", 
                     "        Percent of Class Making Greater than $100,000"), align = 'c')
```

| Percent of Class Making Under $70,000 | Percent of Class Making Greater than $100,000 |
|:-------------------------------------:|:---------------------------------------------:|
|                  8.97                 |                      1.18                     |

Calculate How Many Years to Pay Off Debt
----------------------------------------

``` r
  #empty data frame
  how_many_years <- as.data.frame(matrix(nrow=ncol(income_data), ncol= 1))

  #loop through columns in dataset
  for (i in 1:ncol(income_data)){
  working_column <- as.matrix(income_data[,i])
  running_sum <- 0
  number_of_years <- 1
  
  # check if data less than 95000
  while (running_sum<=95000){
    running_sum <- running_sum + working_column[number_of_years]*.1
    number_of_years <- number_of_years+1
  }
  how_many_years[i,1] <- number_of_years
  }

how_many_years %>%
mutate(`Percent of Students Paying Loan Off in 10 Years or Less` = (sum(V1<=10)/NROW(V1))*100) %>%
  slice(1) %>% 
  select(`Percent of Students Paying Loan Off in 10 Years or Less`) %>% 
  kable(align = 'c')
```

| Percent of Students Paying Loan Off in 10 Years or Less |
|:-------------------------------------------------------:|
|                            0                            |

Histogram of Years to Pay Off Debt
----------------------------------

``` r
how_many_years %>% 
ggplot(aes(V1))+
  geom_histogram()+
  scale_x_continuous(breaks=seq(10,14,1))+
  labs(x="Number of Years", y="Frequency", title = "Histogram of Years to Pay Off Debt")
```

    ## `stat_bin()` using `bins = 30`. Pick better value with `binwidth`.

![](Simulation_HW_files/figure-markdown_github-ascii_identifiers/View_Debt-1.png)

MACSS Program With New Stats
----------------------------

``` r
income_sim(SD=.15, p=.2, g=.03, starting_income = 85000, years = 40, simulations = 10000)
```

New Results for Students Paying Off Debt In Ten Years or Less
-------------------------------------------------------------

``` r
#empty data frame
  how_many_years <- as.data.frame(matrix(nrow=ncol(income_data), ncol= 1))

  #loop through columns in dataset
  for (i in 1:ncol(income_data)){
  working_column <- as.matrix(income_data[,i])
  running_sum <- 0
  number_of_years <- 1
  
  # check if data less than 95000
  while (running_sum<=95000){
    running_sum <- running_sum + working_column[number_of_years]*.1
    number_of_years <- number_of_years+1
  }
  how_many_years[i,1] <- number_of_years
  }

how_many_years %>%
mutate(`Percent of Students Paying Loan Off in 10 Years or Less` = (sum(V1<=10)/NROW(V1))*100) %>%
  slice(1) %>% 
  select(`Percent of Students Paying Loan Off in 10 Years or Less`) %>% 
  kable(align = 'c')
```

| Percent of Students Paying Loan Off in 10 Years or Less |
|:-------------------------------------------------------:|
|                           4.67                          |
