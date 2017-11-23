Lab Notebook (Part 1)
================

### Get Data, Load Packages

``` r
rm(list=ls())
data(gss, package = "poliscidata")

# convert to tibble
library(tidyverse)
gss <- as_tibble(gss)
theme_set(theme_minimal())
```

Exploring Income
================

``` r
gss %>% 
  ggplot(aes(income06))+
  geom_bar()
```

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-2-1.png)

### Relationship between family income, and education

``` r
gss %>% 
  ggplot(aes(educ, income06))+
  geom_count()
```

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-3-1.png)

``` r
gss %>% 
  ggplot(aes(income06))+
  geom_bar()+
  facet_wrap(~happy)
```

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-4-1.png)

### It's looks like wealthier people tend to be working fill time , but the most wealthy people may be retired. Low income people tend not to be employed full time as much

``` r
gss %>% 
  ggplot(aes(as.factor(income06), fill=wrkstat))+
  geom_bar(position = "fill")
```

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-5-1.png)

### Employment for someone else is similar accross the spectrum

``` r
gss %>% 
  ggplot(aes(as.factor(income06), fill=wrkslf))+
  geom_bar(position = "fill")
```

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-6-1.png)

### The most wealthy families seem to be mixed of all ages. No clear pattern between age and wealth

``` r
gss %>% 
  ggplot(aes(income06, age))+
  geom_jitter()
```

    ## Warning: Removed 5 rows containing missing values (geom_point).

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-7-1.png)

``` r
gss %>% 
  ggplot(aes(income06))+
  geom_bar()+
  facet_wrap(~workhard)+
  labs(title = "Importance of Hard Work")
```

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-8-1.png)

``` r
gss %>% 
  ggplot(aes(income06))+
  geom_bar()+
  facet_wrap(~getahead)+
  labs(title = "How to Get Ahead")
```

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-9-1.png)

### No one seems to think being popular is important

``` r
gss %>% 
  ggplot(aes(income06))+
  geom_bar()+
  facet_wrap(~popular)+
  labs(title = "How Important is Being Popular")
```

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-10-1.png)

graph 10

### The most wealthy families rate religion as strongly important

``` r
gss %>% 
  ggplot(aes(income06))+
  geom_bar()+
  facet_wrap(~reliten)+
  labs(title = "Religion")
```

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-11-1.png)

### A lot of really wealthy families didn't want to answer who they voted for

``` r
gss %>% 
  ggplot(aes(income06))+
  geom_bar()+
  facet_wrap(~pres08)
```

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-12-1.png)

``` r
gss %>% 
  ggplot(aes(abpoor, income06))+
  geom_count()
```

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-13-1.png)

Exploring Presidential Votes and Other Views
============================================

``` r
gss %>% 
  ggplot(aes(pres08))+
  geom_bar()
```

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-14-1.png)

Librerals rarely expressed voting for McCain
--------------------------------------------

``` r
gss %>% 
  ggplot(aes(pres08, polviews))+
  geom_jitter()
```

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-15-1.png)

### No clear relation between opinion for space exploration and presidential vote

``` r
gss %>% 
  ggplot(aes(as.factor(pres08), fill=natspac))+
  geom_bar(position = "fill")
```

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-16-1.png)

Not much of a relationship between who they voted for and halting natural crime
-------------------------------------------------------------------------------

``` r
gss %>% 
  ggplot(aes(as.factor(pres08), fill=natcrime))+
  geom_bar(position = "fill")
```

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-17-1.png)

### People who votes for McCain seem to think there was too little on Defense being spent more than other votes. This is intuitive.

``` r
gss %>% 
  ggplot(aes(as.factor(pres08), fill=natarms))+
  geom_bar(position = "fill")
```

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-18-1.png)

### Not clear relationship for supporting sciencetific research

``` r
gss %>% 
  ggplot(aes(as.factor(pres08), fill=natsci))+
  geom_bar(position = "fill")
```

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-19-1.png)

### Obama voters look less religious than McCain voters

``` r
gss %>% 
  ggplot(aes(as.factor(pres08), fill=bible))+
  geom_bar(position = "fill")
```

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-20-1.png)

Who are these people with a lot of siblings?
============================================

20

``` r
gss %>% 
  ggplot(aes(childs, sibs, group=childs))+
  geom_boxplot()
```

    ## Warning: Removed 5 rows containing non-finite values (stat_boxplot).

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-21-1.png)

### Baseline for education

``` r
gss %>% 
  ggplot(aes(educ))+
  geom_bar()
```

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-22-1.png)

### People with &gt;20 siblings seem lower educated than normal

``` r
gss %>% 
  filter(sibs > 20) %>% 
  ggplot(aes(educ))+
  geom_bar()
```

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-23-1.png)

### About normal in regards to opinions in childcare

``` r
gss %>% 
  filter(sibs > 20) %>% 
  ggplot(aes(natchld))+
  geom_bar()
```

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-24-1.png)

Looking into Racial Preferences
===============================

### Most people seem to feel equally close to white and black people. Seems to be more who feel close to whites than blacks though

``` r
gss %>% 
  ggplot(aes(closewht, closeblk, color=race))+
  geom_jitter()
```

    ## Warning: Removed 680 rows containing missing values (geom_point).

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-25-1.png)

### People who feel closer to blacks seem to be more supporitive of legalizing marijuana

``` r
gss %>%
  ggplot(aes(grass, closeblk, group=grass))+
  geom_boxplot()
```

    ## Warning: Removed 680 rows containing non-finite values (stat_boxplot).

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-26-1.png)

### No clear relationship between feeling close to blacks and opinions about the bible

``` r
gss %>%
  ggplot(aes(closeblk, bible))+
  geom_count()
```

    ## Warning: Removed 680 rows containing non-finite values (stat_sum).

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-27-1.png)

### Most people prefer not to answer whether they think if blacks get ahead without favors... but of the people who do answer, they seem to strongly agree that blacks get ahead without favors

``` r
gss %>%
  ggplot(aes(closeblk, wrkwayup, color=race))+
  geom_jitter()
```

    ## Warning: Removed 680 rows containing missing values (geom_point).

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-28-1.png)

### People who felt close to blacks didnt comment on removing racist books. However, the only other thing we can see is that people who were closer and less closer to blacks both agreed on removing racist books

``` r
gss %>%
  ggplot(aes(librac, closeblk))+
  geom_boxplot()
```

    ## Warning: Removed 680 rows containing non-finite values (stat_boxplot).

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-29-1.png)

### People who were less close to blacks were less likely to vote for Obama

``` r
gss %>% 
  filter(closeblk <2.5) %>% 
  ggplot(aes(pres08))+
  geom_bar()
```

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-30-1.png)

30

### Basline for allowing homosexual speech

``` r
gss %>% 
  ggplot(aes(spkhomo))+
  geom_bar()
```

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-31-1.png)

### People less close to blacks seem like they are more apt to saying "not allowed" than bigger population. Relationship could be compromised because of y axis however

``` r
gss %>% 
  filter(closeblk <2.5) %>% 
  ggplot(aes(spkhomo))+
  geom_bar()
```

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-32-1.png)

### Baseline for religious

``` r
gss %>% 
  ggplot(aes(reliten))+
  geom_bar()
```

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-33-1.png)

### Not close to blacks is not radically associated with strength of religion

``` r
gss %>% 
  filter(closeblk <2.5) %>% 
  ggplot(aes(reliten))+
  geom_bar()
```

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-34-1.png)

### Favor Preference in Hiring Blacks

``` r
gss %>% 
  ggplot(aes(affrmact))+
  geom_bar()
```

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-35-1.png)

### Preference for hiring blacks for people who don't feel close to blacks

``` r
gss %>% 
  filter(closeblk <2.5) %>% 
  ggplot(aes(affrmact))+
  geom_bar()
```

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-36-1.png)

### Of the people who have an "oppose" preference in hiring blacks, most of them feel equally close to whites and blacks, or just more close to whites. The "support" group tends to be equal or favorable to hiring blacks

``` r
gss %>% 
  ggplot(aes(closewht, closeblk, color = race))+
  geom_jitter() +
  facet_wrap(~affrmact)
```

    ## Warning: Removed 680 rows containing missing values (geom_point).

![](Lab_Notebook_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-37-1.png)
