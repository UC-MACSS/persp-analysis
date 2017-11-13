R Notebook
================

Load Packages and Data
----------------------

``` r
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
library(RColorBrewer)
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
Pokemon <- read_csv("Pokemon.csv")
```

    ## Parsed with column specification:
    ## cols(
    ##   `#` = col_integer(),
    ##   Name = col_character(),
    ##   `Type 1` = col_character(),
    ##   `Type 2` = col_character(),
    ##   Total = col_integer(),
    ##   HP = col_integer(),
    ##   Attack = col_integer(),
    ##   Defense = col_integer(),
    ##   `Sp. Atk` = col_integer(),
    ##   `Sp. Def` = col_integer(),
    ##   Speed = col_integer(),
    ##   Generation = col_integer(),
    ##   Legendary = col_character()
    ## )

``` r
theme_set(theme_minimal())
```

Visual Pokemon By Distribution by Type
--------------------------------------

Color Selection was based on in game graphics via [this photo](https://vignette.wikia.nocookie.net/robloxpokemonbrickbronze/images/5/5f/Type.png/revision/latest?cb=20170426085006)

``` r
Pokemon %>% 
  group_by(`Type 1`) %>% 
  mutate(Type = `Type 1`) %>% 
  ggplot(aes(x = factor(1),fill = Type))+
  geom_bar(width = 1)+
  coord_polar(theta = "y")+
  theme(axis.text.x=element_blank())+
  labs(x = "", y="", title = "Pokemon Visualized by Primary Type")+
  scale_fill_manual(values=c(   "#89970E",  "#000000",  "#765EE1",  "#E79302"   ,"#F5B0F5"  ,"#601500", "#C72100",  "#5D73D4",  "#5D5DB2", "#0E7B00","#D3B356",  "#6DD3F5", "#7F6F65", "#47004A", "#E72062", "#9E863D", "#9B9BAB", "#0061BE"))
```

![](Kaggle3_Pokemon_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-2-1.png)
