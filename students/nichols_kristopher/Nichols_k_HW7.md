Homework 07: Notebook
================
Kristopher Nichols
November 27, 2017

``` r
library(knitr)
library(dplyr)
library(rmarkdown)
library(tidyr)
library(foreign)
library(ggplot2)
library(tidyverse)
library(data.table)
library(scales)
```

``` r
data(gss, package = "poliscidata")
gss <- as_tibble(gss)
View(gss)
```

``` r
#1
gss %>%
  ggplot(aes(vote08_coded)) +
    geom_bar(aes(fill = pres08))
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-1.png)

``` r
#2
gss %>%
  ggplot(aes(pres08)) +
    geom_bar()
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-2.png)

``` r
#3  Who did and didnt vote by age?
gss %>%
  ggplot(aes(vote08_coded, age)) +
    geom_count()
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-3.png)

``` r
#4 Better graph
gss %>%
  ggplot(aes(vote08_coded, age)) +
    geom_violin()
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-4.png)

``` r
#5 Voting by age
gss %>%
  ggplot(aes(pres08, age)) +
    geom_violin()
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-5.png)

``` r
#6 Density of age 
gss %>%
  ggplot(aes(age)) +
    geom_density()
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-6.png)

``` r
#7 More info about who voted
gss %>%
  ggplot(aes(vote08_coded, race)) +
    geom_count()
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-7.png)

``` r
#8 Pres voting by race
gss %>%
  ggplot(aes(pres08, race)) +
    geom_count()
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-8.png)

``` r
#9 Show discrepancy between number of whites in sample *important*
gss %>%
  ggplot(aes(race)) +
    geom_bar()
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-9.png)

``` r
#10 Many more older whites than older blacks/others
gss %>%
  ggplot(aes(race, age)) +
    geom_violin()
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-10.png)

``` r
#11
gss %>%
  ggplot(aes(vote08_coded, age)) +
    geom_violin()
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-11.png)

``` r
#12 Strong and Weak Dems had best showing
gss %>%
  ggplot(aes(partyid, pres08)) +
    geom_count()
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-12.png)

``` r
#13 As shown in #5 younger populations came out for Obama
gss %>%
  ggplot(aes(partyid, age)) +
    geom_violin()
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-13.png)

``` r
#14 #Graph data altered by large number of whites *important*
gss %>%
  ggplot(aes(partyid, race)) +
    geom_count()
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-14.png)

``` r
gss %>%
  ggplot(aes(partyid, race)) +
    geom_count(aes(size = ..prop.., group = race))
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-15.png)

``` r
gss %>%
  ggplot(aes(polviews, race)) +
    geom_count(aes(size = ..prop.., group = race))
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-16.png)

``` r
#15
gss %>%
  ggplot(aes(polviews, partyid)) +
    geom_count()
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-17.png)

``` r
#16
gss %>%
  ggplot(aes(polviews, pres08)) +
    geom_count()
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-18.png)

``` r
#17
gss %>%
  ggplot(aes(polviews, degree)) +
    geom_count()
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-19.png)

``` r
#18
gss %>%
  ggplot(aes(degree, pres08)) +
    geom_count()
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-20.png)

``` r
#19
gss %>%
  ggplot(aes(degree, partyid)) +
    geom_count()
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-21.png)

``` r
#20
gss %>%
  ggplot(aes(degree)) +
    geom_bar(aes(fill = race))
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-22.png)

``` r
gss %>%
  ggplot(aes(relig)) +
    geom_bar() +
    theme(axis.text.x = element_text(angle = 90))
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-23.png)

``` r
#21 Relig & Party
gss %>%
  ggplot(aes(relig, partyid)) +
    geom_count(aes(size = ..prop.., group = relig)) +
    theme(axis.text.x = element_text(angle = 90))
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-24.png)

``` r
#22 Fundamentalism and PArty
gss %>%
  ggplot(aes(fund, partyid)) +
    geom_count(aes(size = ..prop.., group = fund)) +
    theme(axis.text.x = element_text(angle = 90)) +
    scale_size_area(max_size = 12)
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-25.png)

``` r
#23 Atheism keys
gss %>%
  ggplot(aes(attend, partyid)) +
    geom_count() +
    theme(axis.text.x = element_text(angle = 90)) +
    scale_size_area(max_size = 10)
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-26.png)

``` r
#24
gss %>%
  ggplot(aes(reliten, partyid)) +
    geom_count(aes(size = ..prop.., group = reliten)) +
    theme(axis.text.x = element_text(angle = 90)) +
    scale_size_area(max_size = 10)
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-27.png)

``` r
#26
gss %>%
  ggplot(aes(pray, partyid)) +
    geom_count(aes(size = ..prop.., group = pray)) +
    theme(axis.text.x = element_text(angle = 90)) +
    scale_size_area(max_size = 12)
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-28.png)

``` r
#27 Check back on how partyid relates to voting behavior
gss %>%
  ggplot(aes(partyid, vote08_coded)) +
    geom_count() +
    scale_size_area(max_size = 12)
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-29.png)

``` r
gss %>%
  ggplot(aes(relig, vote08_coded)) +
  geom_count(aes(size = ..prop.., group = relig)) +
  theme(axis.text.x = element_text(angle = 90)) +
  scale_size_area(max_size = 12)
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-30.png)

``` r
#28 Connections between religious behaviors and voting
gss %>%
  ggplot(aes(pray, vote08_coded)) +
    geom_count(aes(size = ..prop.., group = vote08_coded)) +
    theme(axis.text.x = element_text(angle = 90)) +
    scale_size_area(max_size = 12)
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-31.png)

``` r
#29
gss %>%
  ggplot(aes(attend, vote08_coded)) +
    geom_count(aes(size = ..prop.., group = vote08_coded)) +
    theme(axis.text.x = element_text(angle = 90)) +
    scale_size_area(max_size = 12)
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-32.png)

``` r
#30
gss %>%
  ggplot(aes(pray, partyid)) +
    geom_count(aes(size = ..prop.., group = pray)) +
    theme(axis.text.x = element_text(angle = 90)) +
    scale_size_area(max_size = 12)
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-33.png)

``` r
#31
gss %>%
  ggplot(aes(pray, obey)) +
    geom_count(aes(size = ..prop.., group = pray)) +
    theme(axis.text.x = element_text(angle = 90)) +
    scale_size_area(max_size = 12)
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-34.png)

``` r
#32
gss %>%
  ggplot(aes(attend, obey)) +
    geom_count(aes(size = ..prop.., group = attend)) +
    theme(axis.text.x = element_text(angle = 90)) +
    scale_size_area(max_size = 12)
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-35.png)

``` r
#33
gss %>%
  ggplot(aes(obey, vote08_coded)) +
    geom_count(aes(size = ..prop.., group = vote08_coded)) +
    theme(axis.text.x = element_text(angle = 90)) +
    scale_size_area(max_size = 12)
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-36.png)

``` r
#34
gss %>%
  ggplot(aes(obey, thnkself)) +
    geom_count(aes(size = ..prop.., group = obey)) +
    theme(axis.text.x = element_text(angle = 90)) +
    scale_size_area(max_size = 12)
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-37.png)

``` r
#35
gss %>%
  ggplot(aes(vote08_coded, thnkself)) +
    geom_count(aes(size = ..prop.., group = vote08_coded)) +
    theme(axis.text.x = element_text(angle = 90)) +
    scale_size_area(max_size = 12)
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-38.png)

``` r
#36
gss %>%
  ggplot(aes(pray, thnkself)) +
    geom_count(aes(size = ..prop.., group = pray)) +
    theme(axis.text.x = element_text(angle = 90)) +
    scale_size_area(max_size = 12)
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-39.png)

``` r
#37
gss %>%
  ggplot(aes(consci, vote08_coded)) +
    geom_count(aes(size = ..prop.., group = consci)) +
    theme(axis.text.x = element_text(angle = 90)) +
    scale_size_area(max_size = 20)
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-40.png)

``` r
#38
gss %>%
  ggplot(aes(bible, vote08_coded)) +
    geom_count(aes(size = ..prop.., group = bible)) +
    theme(axis.text.x = element_text(angle = 90)) +
    scale_size_area(max_size = 20)
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-41.png)

``` r
#39
gss %>%
  ggplot(aes(postlife, vote08_coded)) +
    geom_count(aes(size = ..prop.., group = postlife)) +
    theme(axis.text.x = element_text(angle = 90)) +
    scale_size_area(max_size = 20)
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-42.png)

``` r
#40 Important* 
gss %>%
  ggplot(aes(spkath, vote08_coded)) +
    geom_count(aes(size = ..prop.., group = vote08_coded)) +
    theme(axis.text.x = element_text(angle = 90)) +
    scale_size_area(max_size = 20)
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-43.png)

``` r
#41
gss %>%
  ggplot(aes(colath, vote08_coded)) +
    geom_count(aes(size = ..prop.., group = bible)) +
    theme(axis.text.x = element_text(angle = 90)) +
    scale_size_area(max_size = 20)
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-44.png)

``` r
#42
gss %>%
  ggplot(aes(natsci, vote08_coded)) +
    geom_count(aes(size = ..prop.., group = bible)) +
    theme(axis.text.x = element_text(angle = 90)) +
    scale_size_area(max_size = 20)
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-45.png)

``` r
#43
gss %>%
  ggplot(aes(income06)) +
    geom_bar(aes(fill = race)) +
    theme(axis.text.x = element_text(angle = 90))
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-46.png)

``` r
#44
gss %>%
  ggplot(aes(income06)) +
    geom_bar(aes(fill = relig)) +
    theme(axis.text.x = element_text(angle = 90))
```

![](Nichols_k_HW7_files/figure-markdown_github-ascii_identifiers/Graphs-47.png)
