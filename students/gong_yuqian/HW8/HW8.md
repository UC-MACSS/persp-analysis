unsupervised learning
================

R Markdown
----------

This is an R Markdown document. Markdown is a simple formatting syntax for authoring HTML, PDF, and MS Word documents. For more details on using R Markdown see <http://rmarkdown.rstudio.com>.

When you click the **Knit** button a document will be generated that includes both content as well as the output of any embedded R code chunks within the document. You can embed an R code chunk like this:

``` r
summary(cars)
```

    ##      speed           dist       
    ##  Min.   : 4.0   Min.   :  2.00  
    ##  1st Qu.:12.0   1st Qu.: 26.00  
    ##  Median :15.0   Median : 36.00  
    ##  Mean   :15.4   Mean   : 42.98  
    ##  3rd Qu.:19.0   3rd Qu.: 56.00  
    ##  Max.   :25.0   Max.   :120.00

``` r
#install.packages("devtools")
library("devtools")
install_github("vqv/ggbiplot", force = TRUE)
```

    ## Downloading GitHub repo vqv/ggbiplot@master
    ## from URL https://api.github.com/repos/vqv/ggbiplot/zipball/master

    ## Installing ggbiplot

    ## '/Library/Frameworks/R.framework/Resources/bin/R' --no-site-file  \
    ##   --no-environ --no-save --no-restore --quiet CMD INSTALL  \
    ##   '/private/var/folders/29/w4_w5yl53kl330b97_fpknlm0000gn/T/RtmpO5DkGs/devtools2fae7e2686a4/vqv-ggbiplot-7325e88'  \
    ##   --library='/Library/Frameworks/R.framework/Versions/3.3/Resources/library'  \
    ##   --install-tests

    ## 

``` r
library(ggbiplot)
```

    ## Loading required package: ggplot2

    ## Loading required package: plyr

    ## Loading required package: scales

    ## Loading required package: grid

Part I problem 1 From the loadings tables, we can see that in the first component analysis, the variables Number of applications accepted, Number of applications recevied, Number of fulltime undergraduates are highly correlated and their loading values are 0.348, 0.557,0.671 respectively.

For the second component analysis, the loadings for variables decrease a lot. No variable has a loading greater than 0.3. Variables with positive laodings include Estimated personal spending, Number of applications received, Number of new students enrolled, Number of applications accepted, Number of partime undergraduates, Number of fulltime undergraduates. They are correlated with each other and contribute to the second component analysis.

``` r
College = read.csv("College.csv", header = TRUE)
college1 = subset(College, select = -c(1))
output = prcomp(college1, scale = FALSE)
ggbiplot(output)+
  scale_color_discrete(name = '') +
  theme(legend.direction = 'horizontal')
```

![](Untitled_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-3-1.png)

``` r
sort(round(output$rotation[, 1], digits = 3))
```

    ##   S.F.Ratio perc.alumni   Grad.Rate   Top10perc   Top25perc         PhD 
    ##       0.000       0.000       0.000       0.001       0.001       0.001 
    ##    Terminal       Books    Personal  Room.Board    Outstate P.Undergrad 
    ##       0.001       0.004       0.023       0.029       0.055       0.111 
    ##      Enroll      Expend      Accept        Apps F.Undergrad 
    ##       0.130       0.292       0.348       0.557       0.671

``` r
sort(round(output$rotation[, 2], digits = 3))
```

    ##      Expend    Outstate  Room.Board   Top10perc   Top25perc       Books 
    ##      -0.753      -0.569      -0.106      -0.002      -0.001      -0.001 
    ##         PhD    Terminal perc.alumni   Grad.Rate   S.F.Ratio    Personal 
    ##      -0.001      -0.001      -0.001      -0.001       0.000       0.030 
    ##        Apps      Enroll      Accept P.Undergrad F.Undergrad 
    ##       0.039       0.045       0.077       0.080       0.284

Part I problem 2 From the cumulative proportion of variance explained table, we can see that about 0.871 of all the variance can be explained by the first two principal components.

``` r
output.var = output$sdev ^ 2
pve = output.var/sum(output.var)
cum_pve = cumsum(pve)
cum_pve
```

    ##  [1] 0.4635922 0.8708235 0.9380920 0.9695296 0.9850640 0.9917575 0.9957704
    ##  [8] 0.9992940 0.9997171 0.9999898 0.9999944 0.9999967 0.9999984 0.9999992
    ## [15] 0.9999996 0.9999999 1.0000000

``` r
plot(cum_pve, xlab="Principal Component ", ylab=" Cumulative Proportion of Variance Explained ", ylim=c(0,1), main = "Cumulative PVE")
```

![](Untitled_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-4-1.png) Part II

``` r
USArrests = read.csv("USArrests.csv", header = TRUE)
usa = prcomp(USArrests[-1])
ggbiplot(usa)+
  scale_color_discrete(name = '') +
  theme(legend.direction = 'horizontal')
```

![](Untitled_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-5-1.png)

Problem 2 The groups are divided based on the observations' scores of the first component analysis. Observations whose scores are negative are in one group and observations whose scores are positive are in the other group. Assault arrests levels are the major contributing variable to the first component analysis.

``` r
#install.packages('ggfortify')
library(ggfortify)
```

    ## Warning: namespace 'DBI' is not available and has been replaced
    ## by .GlobalEnv when processing object 'quiet'

    ## Warning: namespace 'DBI' is not available and has been replaced
    ## by .GlobalEnv when processing object 'quiet'

    ## 
    ## Attaching package: 'ggfortify'

    ## The following object is masked from 'package:ggbiplot':
    ## 
    ##     ggbiplot

``` r
set.seed(4)
km.two = kmeans(USArrests[, -1], 2,nstart = 20)
km.two
```

    ## K-means clustering with 2 clusters of sizes 29, 21
    ## 
    ## Cluster means:
    ##      Murder  Assault UrbanPop     Rape
    ## 1  4.841379 109.7586 64.03448 16.24828
    ## 2 11.857143 255.0000 67.61905 28.11429
    ## 
    ## Clustering vector:
    ##  [1] 2 2 2 2 2 2 1 2 2 2 1 1 2 1 1 1 1 2 1 2 1 2 1 2 1 1 1 2 1 1 2 2 2 1 1
    ## [36] 1 1 1 1 2 1 2 2 1 1 1 1 1 1 1
    ## 
    ## Within cluster sum of squares by cluster:
    ## [1] 54762.30 41636.73
    ##  (between_SS / total_SS =  72.9 %)
    ## 
    ## Available components:
    ## 
    ## [1] "cluster"      "centers"      "totss"        "withinss"    
    ## [5] "tot.withinss" "betweenss"    "size"         "iter"        
    ## [9] "ifault"

``` r
rownames(USArrests) = USArrests[, 1]
autoplot(km.two, data = USArrests[, -1],
         label = TRUE, label.size = 3, loadings = TRUE,
         loadings.label = TRUE, loadings.label.size = 3,
         loadings.colour = "blue")+labs(title = "Clustering with k = 2")
```

![](Untitled_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-6-1.png) Problem 3: From the graph we can see that the fourt clustering groups are decided based on the score values of each state in the first principal component analysis. Since Assault is the major contributing variable in the first component analysis, we can assume that the clustering groups have different levels of assault arrests.

``` r
set.seed(5)
km.four = kmeans(USArrests[, -1], 4,nstart = 20)
km.four
```

    ## K-means clustering with 4 clusters of sizes 14, 10, 10, 16
    ## 
    ## Cluster means:
    ##      Murder  Assault UrbanPop     Rape
    ## 1  8.214286 173.2857 70.64286 22.84286
    ## 2  2.950000  62.7000 53.90000 11.51000
    ## 3  5.590000 112.4000 65.60000 17.27000
    ## 4 11.812500 272.5625 68.31250 28.37500
    ## 
    ## Clustering vector:
    ##        Alabama         Alaska        Arizona       Arkansas     California 
    ##              4              4              4              1              4 
    ##       Colorado    Connecticut       Delaware        Florida        Georgia 
    ##              1              3              4              4              1 
    ##         Hawaii          Idaho       Illinois        Indiana           Iowa 
    ##              2              3              4              3              2 
    ##         Kansas       Kentucky      Louisiana          Maine       Maryland 
    ##              3              3              4              2              4 
    ##  Massachusetts       Michigan      Minnesota    Mississippi       Missouri 
    ##              1              4              2              4              1 
    ##        Montana       Nebraska         Nevada  New Hampshire     New Jersey 
    ##              3              3              4              2              1 
    ##     New Mexico       New York North Carolina   North Dakota           Ohio 
    ##              4              4              4              2              3 
    ##       Oklahoma         Oregon   Pennsylvania   Rhode Island South Carolina 
    ##              1              1              3              1              4 
    ##   South Dakota      Tennessee          Texas           Utah        Vermont 
    ##              2              1              1              3              2 
    ##       Virginia     Washington  West Virginia      Wisconsin        Wyoming 
    ##              1              1              2              2              1 
    ## 
    ## Within cluster sum of squares by cluster:
    ## [1]  9136.643  4547.914  1480.210 19563.863
    ##  (between_SS / total_SS =  90.2 %)
    ## 
    ## Available components:
    ## 
    ## [1] "cluster"      "centers"      "totss"        "withinss"    
    ## [5] "tot.withinss" "betweenss"    "size"         "iter"        
    ## [9] "ifault"

``` r
rownames(USArrests) = USArrests[, 1]
autoplot(km.four, data = USArrests[, -1],
         label = TRUE, label.size = 3, loadings = TRUE,
         loadings.label = TRUE, loadings.label.size = 3,
         loadings.colour = "blue")+labs(title = "Clustering with k = 4")
```

![](Untitled_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-7-1.png) Problem 4: From the graph below, we can see that the groups are still divided based on their scores of the first component analysis, which is mainly dominated by their assualt arrests situation. Interestingly, we find what it differs from the graph with 4 clustering groups is that the groups with the lowest scores are merged together to be a single group in this case. The two groups with the highest scores when k is equal to 4 haven't change in this case when k is equal to 3.

``` r
set.seed(7)
km.three = kmeans(USArrests[, -1], 3 ,nstart = 20)
km.three
```

    ## K-means clustering with 3 clusters of sizes 20, 16, 14
    ## 
    ## Cluster means:
    ##      Murder  Assault UrbanPop     Rape
    ## 1  4.270000  87.5500 59.75000 14.39000
    ## 2 11.812500 272.5625 68.31250 28.37500
    ## 3  8.214286 173.2857 70.64286 22.84286
    ## 
    ## Clustering vector:
    ##        Alabama         Alaska        Arizona       Arkansas     California 
    ##              2              2              2              3              2 
    ##       Colorado    Connecticut       Delaware        Florida        Georgia 
    ##              3              1              2              2              3 
    ##         Hawaii          Idaho       Illinois        Indiana           Iowa 
    ##              1              1              2              1              1 
    ##         Kansas       Kentucky      Louisiana          Maine       Maryland 
    ##              1              1              2              1              2 
    ##  Massachusetts       Michigan      Minnesota    Mississippi       Missouri 
    ##              3              2              1              2              3 
    ##        Montana       Nebraska         Nevada  New Hampshire     New Jersey 
    ##              1              1              2              1              3 
    ##     New Mexico       New York North Carolina   North Dakota           Ohio 
    ##              2              2              2              1              1 
    ##       Oklahoma         Oregon   Pennsylvania   Rhode Island South Carolina 
    ##              3              3              1              3              2 
    ##   South Dakota      Tennessee          Texas           Utah        Vermont 
    ##              1              3              3              1              1 
    ##       Virginia     Washington  West Virginia      Wisconsin        Wyoming 
    ##              3              3              1              1              3 
    ## 
    ## Within cluster sum of squares by cluster:
    ## [1] 19263.760 19563.863  9136.643
    ##  (between_SS / total_SS =  86.5 %)
    ## 
    ## Available components:
    ## 
    ## [1] "cluster"      "centers"      "totss"        "withinss"    
    ## [5] "tot.withinss" "betweenss"    "size"         "iter"        
    ## [9] "ifault"

``` r
rownames(USArrests) = USArrests[, 1]
autoplot(km.three, data = USArrests[, -1],
         label = TRUE, label.size = 3, loadings = TRUE,
         loadings.label = TRUE, loadings.label.size = 3,
         loadings.colour = "blue")+labs(title = "Clustering with k = 3")
```

![](Untitled_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-8-1.png)

Problem 5: Interestingly, the clustering results are the same as the results when we use the raw data. This could be a great evidence that the first and second component analysis scores can explain the majority of the variances of the raw data.

``` r
set.seed(7)
prin_score = prcomp(USArrests[, -1])$x
cluster_prin_score = kmeans(prin_score,3)
df_prin_score = as.data.frame(prin_score)
rownames(df_prin_score) = USArrests[, 1]
kmscore.three = kmeans(df_prin_score, 3 ,nstart = 20)
kmscore.three
```

    ## K-means clustering with 3 clusters of sizes 16, 20, 14
    ## 
    ## Cluster means:
    ##          PC1       PC2        PC3        PC4
    ## 1 102.149155 -2.020236 -0.1554049  0.3152972
    ## 2 -83.741577 -1.982213 -0.1620741  0.1020305
    ## 3   2.888932  5.140574  0.4091400 -0.5060975
    ## 
    ## Clustering vector:
    ##        Alabama         Alaska        Arizona       Arkansas     California 
    ##              1              1              1              3              1 
    ##       Colorado    Connecticut       Delaware        Florida        Georgia 
    ##              3              2              1              1              3 
    ##         Hawaii          Idaho       Illinois        Indiana           Iowa 
    ##              2              2              1              2              2 
    ##         Kansas       Kentucky      Louisiana          Maine       Maryland 
    ##              2              2              1              2              1 
    ##  Massachusetts       Michigan      Minnesota    Mississippi       Missouri 
    ##              3              1              2              1              3 
    ##        Montana       Nebraska         Nevada  New Hampshire     New Jersey 
    ##              2              2              1              2              3 
    ##     New Mexico       New York North Carolina   North Dakota           Ohio 
    ##              1              1              1              2              2 
    ##       Oklahoma         Oregon   Pennsylvania   Rhode Island South Carolina 
    ##              3              3              2              3              1 
    ##   South Dakota      Tennessee          Texas           Utah        Vermont 
    ##              2              3              3              2              2 
    ##       Virginia     Washington  West Virginia      Wisconsin        Wyoming 
    ##              3              3              2              2              3 
    ## 
    ## Within cluster sum of squares by cluster:
    ## [1] 19563.862 19263.760  9136.643
    ##  (between_SS / total_SS =  86.5 %)
    ## 
    ## Available components:
    ## 
    ## [1] "cluster"      "centers"      "totss"        "withinss"    
    ## [5] "tot.withinss" "betweenss"    "size"         "iter"        
    ## [9] "ifault"

``` r
#rownames(USArrests) = USArrests[, 1]
autoplot(kmscore.three, data = df_prin_score,
         label = TRUE, label.size = 3, loadings = TRUE,
         loadings.label = TRUE, loadings.label.size = 3,
         loadings.colour = "blue")+labs(title = "Clustering with k = 3 on first 
         two principle scores")
```

![](Untitled_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-9-1.png)

``` r
#install.packages("ggdendro")
library(ggdendro)
#library(dendextend)
```

Problem 6

``` r
hc.complete = hclust(dist(USArrests[, -1]), method = "complete")
ggdendrogram(hc.complete) + labs(title = "Hierarchical clustering with complete
                                  and Euclidean distance")
```

![](Untitled_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-11-1.png)

Problem 7: Clustering group 1 includes states: "Alabama" "Alaska" "Arizona" "California" "Delaware"
"Florida" "Illinois" "Louisiana" "Maryland" "Michigan"
"Mississippi" "Nevada" "New Mexico" "New York" "North Carolina" "South Carolina"

Clustering group 2 includes states: "Arkansas" "Colorado" "Georgia" "Massachusetts" "Missouri"
"New Jersey" "Oklahoma" "Oregon" "Rhode Island" "Tennessee"
"Texas" "Virginia" "Washington" "Wyoming"

Clustering group 3 includes states: "Connecticut" "Hawaii" "Idaho" "Indiana" "Iowa"
"Kansas" "Kentucky" "Maine" "Minnesota" "Montana"
"Nebraska" "New Hampshire" "North Dakota" "Ohio" "Pennsylvania" "South Dakota" "Utah" "Vermont" "West Virginia" "Wisconsin"

``` r
hc.2 = hclust(dist(USArrests[, -1]), "complete")
cuttree = cutree(hc.2, k = 3)
plot(hc.2, main = '', cex = 0.6)+ title(main = list("Hierarchical clustering without scaling", cex = 1.5, font = 3))
```

    ## numeric(0)

``` r
rect.hclust(hc.2, k = 3)
```

![](Untitled_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-12-1.png)

``` r
table(cuttree)
```

    ## cuttree
    ##  1  2  3 
    ## 16 14 20

``` r
rownames(USArrests[, -1])[cuttree == 1]
```

    ##  [1] "Alabama"        "Alaska"         "Arizona"        "California"    
    ##  [5] "Delaware"       "Florida"        "Illinois"       "Louisiana"     
    ##  [9] "Maryland"       "Michigan"       "Mississippi"    "Nevada"        
    ## [13] "New Mexico"     "New York"       "North Carolina" "South Carolina"

``` r
rownames(USArrests[, -1])[cuttree == 2]
```

    ##  [1] "Arkansas"      "Colorado"      "Georgia"       "Massachusetts"
    ##  [5] "Missouri"      "New Jersey"    "Oklahoma"      "Oregon"       
    ##  [9] "Rhode Island"  "Tennessee"     "Texas"         "Virginia"     
    ## [13] "Washington"    "Wyoming"

``` r
rownames(USArrests[, -1])[cuttree == 3]
```

    ##  [1] "Connecticut"   "Hawaii"        "Idaho"         "Indiana"      
    ##  [5] "Iowa"          "Kansas"        "Kentucky"      "Maine"        
    ##  [9] "Minnesota"     "Montana"       "Nebraska"      "New Hampshire"
    ## [13] "North Dakota"  "Ohio"          "Pennsylvania"  "South Dakota" 
    ## [17] "Utah"          "Vermont"       "West Virginia" "Wisconsin"

Problem 8: After scaling the data, the observations in each clustering group are different from the case without scaling. We can see that group 3 have more observations now. Before the scaling, the variables with larger variance will be the major contributing factors in deciding which group an observation belong to. However, after the scaling, variables will mostly have equal importance in dividing the clustering groups and I think it is better if we want to compare observations by their overall differences instead of differences in a subset of variables.

``` r
hc.2 = hclust(dist(scale(USArrests[, -1])), "complete")
cuttree = cutree(hc.2, k = 3)
plot(hc.2, main = '', cex = 0.6)+ title(main = list("Hierarchical clustering without scaling", cex = 1.5, font = 3))
```

    ## numeric(0)

``` r
rect.hclust(hc.2, k = 3)
```

![](Untitled_files/figure-markdown_github-ascii_identifiers/unnamed-chunk-13-1.png)

``` r
table(cuttree)
```

    ## cuttree
    ##  1  2  3 
    ##  8 11 31

``` r
rownames(USArrests[, -1])[cuttree == 1]
```

    ## [1] "Alabama"        "Alaska"         "Georgia"        "Louisiana"     
    ## [5] "Mississippi"    "North Carolina" "South Carolina" "Tennessee"

``` r
rownames(USArrests[, -1])[cuttree == 2]
```

    ##  [1] "Arizona"    "California" "Colorado"   "Florida"    "Illinois"  
    ##  [6] "Maryland"   "Michigan"   "Nevada"     "New Mexico" "New York"  
    ## [11] "Texas"

``` r
rownames(USArrests[, -1])[cuttree == 3]
```

    ##  [1] "Arkansas"      "Connecticut"   "Delaware"      "Hawaii"       
    ##  [5] "Idaho"         "Indiana"       "Iowa"          "Kansas"       
    ##  [9] "Kentucky"      "Maine"         "Massachusetts" "Minnesota"    
    ## [13] "Missouri"      "Montana"       "Nebraska"      "New Hampshire"
    ## [17] "New Jersey"    "North Dakota"  "Ohio"          "Oklahoma"     
    ## [21] "Oregon"        "Pennsylvania"  "Rhode Island"  "South Dakota" 
    ## [25] "Utah"          "Vermont"       "Virginia"      "Washington"   
    ## [29] "West Virginia" "Wisconsin"     "Wyoming"

\`\`\`

Including Plots
---------------

You can also embed plots, for example:

![](Untitled_files/figure-markdown_github-ascii_identifiers/pressure-1.png)

Note that the `echo = FALSE` parameter was added to the code chunk to prevent printing of the R code that generated the plot.
