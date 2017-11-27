Lab\_Notebook
================
Nora Nickels
11/27/2017

``` r
# Install pacakges and import data. 
# install.packages("poliscidata")
data(gss, package = "poliscidata")

# Convert data to tibble
library(tidyverse)
```

    ## Loading tidyverse: ggplot2
    ## Loading tidyverse: tibble
    ## Loading tidyverse: tidyr
    ## Loading tidyverse: readr
    ## Loading tidyverse: purrr
    ## Loading tidyverse: dplyr

    ## Warning: package 'ggplot2' was built under R version 3.3.2

    ## Conflicts with tidy packages ----------------------------------------------

    ## filter(): dplyr, stats
    ## lag():    dplyr, stats

``` r
gss <- as_tibble(gss)
```

``` r
# looking at age distribution
gss %>% 
  ggplot(aes(age)) +
  geom_histogram()
```

    ## `stat_bin()` using `bins = 30`. Pick better value with `binwidth`.

    ## Warning: Removed 5 rows containing non-finite values (stat_bin).

![](Lab_Notebook_files/figure-markdown_github/EDA-1.png)

``` r
# adjusting binwidth
gss %>% 
  ggplot(aes(age)) +
  geom_histogram(binwidth = 1)
```

    ## Warning: Removed 5 rows containing non-finite values (stat_bin).

![](Lab_Notebook_files/figure-markdown_github/EDA-2.png)

``` r
# playing around with density plot. doesn't tell me much.
gss %>% 
  ggplot(aes(age)) +
  geom_density()
```

    ## Warning: Removed 5 rows containing non-finite values (stat_density).

![](Lab_Notebook_files/figure-markdown_github/EDA-3.png)

``` r
# looking at age and race distribution
gss %>%
  ggplot(aes(age)) +
    geom_histogram() +
    facet_wrap(~ race)
```

    ## `stat_bin()` using `bins = 30`. Pick better value with `binwidth`.

    ## Warning: Removed 5 rows containing non-finite values (stat_bin).

![](Lab_Notebook_files/figure-markdown_github/EDA-4.png)
