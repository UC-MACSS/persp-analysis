sumervaid\_assignment\_8
================

### Colleges

#### Question 1

Perform PCA analysis on the college dataset and plot the first two principal components. Describe the results.

``` r
print(plot)
```

![](Assignment8_SumerVaid_files/figure-markdown_github-ascii_identifiers/print%20plot%20chunk-1.png)

``` r
print(data.pca)
```

    ## Standard deviations:
    ##  [1] 2.3331324 2.1160899 1.0831232 1.0034481 0.9659342 0.9205429 0.7778227
    ##  [8] 0.7662347 0.7279627 0.6354389 0.5595020 0.4693901 0.4093632 0.3792007
    ## [15] 0.2964985 0.1915155 0.1516517
    ## 
    ## Rotation:
    ##                     PC1         PC2         PC3         PC4         PC5
    ## Apps         0.24876560 -0.33159823  0.06309210 -0.28131053 -0.00574141
    ## Accept       0.20760150 -0.37211675  0.10124906 -0.26781735 -0.05578609
    ## Enroll       0.17630359 -0.40372425  0.08298557 -0.16182677  0.05569364
    ## Top10perc    0.35427395  0.08241182 -0.03505553  0.05154725  0.39543434
    ## Top25perc    0.34400128  0.04477866  0.02414794  0.10976654  0.42653359
    ## F.Undergrad  0.15464096 -0.41767377  0.06139298 -0.10041234  0.04345437
    ## P.Undergrad  0.02644250 -0.31508783 -0.13968172  0.15855849 -0.30238541
    ## Outstate     0.29473642  0.24964352 -0.04659887 -0.13129136 -0.22253200
    ## Room.Board   0.24903045  0.13780888 -0.14896739 -0.18499599 -0.56091947
    ## Books        0.06475752 -0.05634184 -0.67741165 -0.08708922  0.12728883
    ## Personal    -0.04252854 -0.21992922 -0.49972112  0.23071057  0.22231102
    ## PhD          0.31831287 -0.05831132  0.12702837  0.53472483 -0.14016633
    ## Terminal     0.31705602 -0.04642945  0.06603755  0.51944302 -0.20471973
    ## S.F.Ratio   -0.17695789 -0.24666528  0.28984840  0.16118949  0.07938825
    ## perc.alumni  0.20508237  0.24659527  0.14698927 -0.01731422  0.21629741
    ## Expend       0.31890875  0.13168986 -0.22674398 -0.07927349 -0.07595812
    ## Grad.Rate    0.25231565  0.16924053  0.20806465 -0.26912907  0.10926791
    ##                      PC6          PC7          PC8          PC9
    ## Apps        -0.016237442 -0.042486349  0.103090398 -0.090227080
    ## Accept       0.007534685 -0.012949720  0.056270962 -0.177864814
    ## Enroll      -0.042557980 -0.027692894 -0.058662355 -0.128560713
    ## Top10perc   -0.052692798 -0.161332069  0.122678028  0.341099863
    ## Top25perc    0.033091590 -0.118485556  0.102491967  0.403711989
    ## F.Undergrad -0.043454235 -0.025076363 -0.078889644 -0.059441918
    ## P.Undergrad -0.191198583  0.061042346 -0.570783816  0.560672902
    ## Outstate    -0.030000391  0.108528966 -0.009845998 -0.004573329
    ## Room.Board   0.162755446  0.209744235  0.221453442  0.275022548
    ## Books        0.641054950 -0.149692034 -0.213293009 -0.133663353
    ## Personal    -0.331398003  0.633790064  0.232660840 -0.094468890
    ## PhD          0.091255521 -0.001096413  0.077040000 -0.185181525
    ## Terminal     0.154927646 -0.028477011  0.012161330 -0.254938198
    ## S.F.Ratio    0.487045875  0.219259358  0.083604874  0.274544380
    ## perc.alumni -0.047340014  0.243321156 -0.678523654 -0.255334907
    ## Expend      -0.298118619 -0.226584481  0.054159377 -0.049138881
    ## Grad.Rate    0.216163313  0.559943937  0.005335539  0.041904305
    ##                    PC10         PC11        PC12         PC13        PC14
    ## Apps        -0.05250980  0.043046207 -0.02407091  0.595830975  0.08063280
    ## Accept      -0.04114008 -0.058405585  0.14510245  0.292642398  0.03346743
    ## Enroll      -0.03448791 -0.069398883 -0.01114315 -0.444638207 -0.08569672
    ## Top10perc   -0.06402578 -0.008104814 -0.03855430  0.001023036 -0.10782819
    ## Top25perc   -0.01454923 -0.273128469  0.08935156  0.021883880  0.15174211
    ## F.Undergrad -0.02084718 -0.081157818 -0.05617677 -0.523622267 -0.05637288
    ## P.Undergrad  0.22310581  0.100693324  0.06353607  0.125997650  0.01928575
    ## Outstate    -0.18667536  0.143220673  0.82344378 -0.141856014 -0.03401154
    ## Room.Board  -0.29832424 -0.359321731 -0.35455973 -0.069748585 -0.05842898
    ## Books        0.08202922  0.031940037  0.02815937  0.011437996 -0.06684946
    ## Personal    -0.13602762 -0.018578473  0.03926403  0.039454742  0.02752862
    ## PhD          0.12345220  0.040372325 -0.02322243  0.127696382 -0.69112615
    ## Terminal     0.08857846 -0.058973403 -0.01648504 -0.058313466  0.67100861
    ## S.F.Ratio   -0.47204525  0.445000727  0.01102621 -0.017715270  0.04137410
    ## perc.alumni -0.42299971 -0.130727978 -0.18266065  0.104088088 -0.02715421
    ## Expend      -0.13228633  0.692088870 -0.32598230 -0.093746450  0.07312252
    ## Grad.Rate    0.59027107  0.219839000 -0.12210670 -0.069196978  0.03647674
    ##                     PC15         PC16         PC17
    ## Apps        -0.133405806 -0.459139498 -0.358970400
    ## Accept       0.145497511  0.518568789  0.543427250
    ## Enroll      -0.029589609  0.404318439 -0.609651110
    ## Top10perc   -0.697722522  0.148738723  0.144986329
    ## Top25perc    0.617274818 -0.051868340 -0.080347844
    ## F.Undergrad -0.009916410 -0.560363054  0.414705279
    ## P.Undergrad -0.020951598  0.052731304 -0.009017890
    ## Outstate    -0.038354479 -0.101594830 -0.050899592
    ## Room.Board  -0.003401971  0.025929338 -0.001146396
    ## Books        0.009438879 -0.002882829 -0.000772632
    ## Personal     0.003090014  0.012890402  0.001114334
    ## PhD          0.112055599 -0.029807547 -0.013813337
    ## Terminal    -0.158909651  0.027075981 -0.006209327
    ## S.F.Ratio    0.020899128  0.021247629  0.002222152
    ## perc.alumni  0.008417894 -0.003334062  0.019186974
    ## Expend       0.227742017  0.043880323  0.035309822
    ## Grad.Rate    0.003394336  0.005008447  0.013071002

Describe the results: If a signifiance level is choosen (I.e -0.3&lt;r&lt;0.3), then it becmes clear that PC1 is strongly correlated with increases in Top10perc, Top25Perc, PhD, Terminal, Outstate (close to 0.3). Similarly, using this signifiance level of (-0.3&lt;r&lt;0.3), PC2 is strongly correlated with Apps, Accept, Enroll, F. Undergrad, P. Undergrad. Note that these correlations are negative. There also appear to be some outliers in the data, as evident from the plot. The plot also indicates that the S.F ratio variable is orthogonal to the F.undergrad variable, whereas the personal variabele is orthogonal to the books variable.

#### Question 2

The following table displayes the cumulative proportion of variance explained by all the principal components.

``` r
print(summary(data.pca))
```

    ## Importance of components:
    ##                           PC1    PC2     PC3     PC4     PC5     PC6
    ## Standard deviation     2.3331 2.1161 1.08312 1.00345 0.96593 0.92054
    ## Proportion of Variance 0.3202 0.2634 0.06901 0.05923 0.05488 0.04985
    ## Cumulative Proportion  0.3202 0.5836 0.65262 0.71185 0.76673 0.81658
    ##                            PC7     PC8     PC9    PC10    PC11    PC12
    ## Standard deviation     0.77782 0.76623 0.72796 0.63544 0.55950 0.46939
    ## Proportion of Variance 0.03559 0.03454 0.03117 0.02375 0.01841 0.01296
    ## Cumulative Proportion  0.85217 0.88670 0.91788 0.94163 0.96004 0.97300
    ##                           PC13    PC14    PC15    PC16    PC17
    ## Standard deviation     0.40936 0.37920 0.29650 0.19152 0.15165
    ## Proportion of Variance 0.00986 0.00846 0.00517 0.00216 0.00135
    ## Cumulative Proportion  0.98286 0.99132 0.99649 0.99865 1.00000

The cumulative portion of variance in College explained by the first two principal components is 0.5836, as evidenced by the table above. In other words, 58.36% variance in College is explained by the first two principal components.

USA Arrests
-----------

### Question 1

Plot:

``` r
print(plot_usa)
```

![](Assignment8_SumerVaid_files/figure-markdown_github-ascii_identifiers/USA-1%20print-1.png)

### Question 2

Plot:

``` r
print(plot_kmeans)
```

![](Assignment8_SumerVaid_files/figure-markdown_github-ascii_identifiers/USA-2%20print-1.png) Describe your results: We can see that the first component captures information about rape, assault and murder. We can see that most of the classication is based on the second PC, as indicated by the primary directionality of the arrows towards the y-axis. States in the first cluster typically have higher rates of crime as compared to states in the second cluster.The second cluster chiefly captures information about urban population, with states like Washington, Ohio and Pennsylvanaia all contanining similar urban populations.

### Question 3

Plot:

``` r
print(plot_k4means)
```

![](Assignment8_SumerVaid_files/figure-markdown_github-ascii_identifiers/USA-3%20print-1.png)

Describe your results: We can see that states in the first cluster are closely assosciated to crimes like murder, assault and rape. As we move towards the right, the other clusters appear to be less closely assosciated to these crimes, as they are further away from the arrows. Hence, we can conclude that states in the blue-color appear to have the highest rates of murder, assault and rape, states in the red-color cluster have medium rates of murder, assault and rape; states in the green clusters have the lower rates of these crimes and states in the black cluster have the lowest rates of these crimes. Compared to the previous graph (kmeans=2), we can also note that there are slightly greater number of outlier states in this instance too. We can eye-ball that certain clustered states appear to be distant from their clusters, implying that their distant from the centroids of those clusters and therefore are "outliers".

### Question 4

Plot:

``` r
print(plot_k3means)
```

![](Assignment8_SumerVaid_files/figure-markdown_github-ascii_identifiers/USA-4%20print-1.png)

Describe your results: Reducing the overall number of clusters does not change the pattern of results identified in Question 3: instead of classifying states by four clusters of crime-rates, combine the last two clusters into one cluster. Hence, now we have three ways of categorizing crime: high (states in red), medium (states in black) and low (states in green).

### Question 5

Plot:

``` r
print(plot_k3pcameans)
```

![](Assignment8_SumerVaid_files/figure-markdown_github-ascii_identifiers/USA-5%20print-1.png)

``` r
print(km3_pca$centers)
```

    ##         PC1        PC2
    ## 1  0.492865 -0.6027746
    ## 2 -1.645026  0.2966625
    ## 3  2.002412  0.4097244

``` r
print(km3$centers)
```

    ##      Murder  Assault UrbanPop     Rape
    ## 1  8.214286 173.2857 70.64286 22.84286
    ## 2 11.812500 272.5625 68.31250 28.37500
    ## 3  4.270000  87.5500 59.75000 14.39000

Describe your results and compare them to the clustering results with \(K=3\) based on the raw data: Visually, the clusters generated in this graph appear to be similar to those of Question 4. However, as evidenced in the R output above, their centers are very different. The nature of the clusters themselves appear to be the same.

### Question 6

Clusters:

``` r
print(cluster)
```

    ## 
    ## Call:
    ## hclust(d = dist(USArrests))
    ## 
    ## Cluster method   : complete 
    ## Distance         : euclidean 
    ## Number of objects: 50

``` r
png(filename="P2Q6.png")
plot(cluster, main="Cluster Dendrogram")
dev.off()
```

    ## quartz_off_screen 
    ##                 2

### Question 7

Which states belong to which clusters?

``` r
print(chop_cluster)
```

    ##                cutree.cluster..3.
    ## Alabama                         1
    ## Alaska                          1
    ## Arizona                         1
    ## Arkansas                        2
    ## California                      1
    ## Colorado                        2
    ## Connecticut                     3
    ## Delaware                        1
    ## Florida                         1
    ## Georgia                         2
    ## Hawaii                          3
    ## Idaho                           3
    ## Illinois                        1
    ## Indiana                         3
    ## Iowa                            3
    ## Kansas                          3
    ## Kentucky                        3
    ## Louisiana                       1
    ## Maine                           3
    ## Maryland                        1
    ## Massachusetts                   2
    ## Michigan                        1
    ## Minnesota                       3
    ## Mississippi                     1
    ## Missouri                        2
    ## Montana                         3
    ## Nebraska                        3
    ## Nevada                          1
    ## New Hampshire                   3
    ## New Jersey                      2
    ## New Mexico                      1
    ## New York                        1
    ## North Carolina                  1
    ## North Dakota                    3
    ## Ohio                            3
    ## Oklahoma                        2
    ## Oregon                          2
    ## Pennsylvania                    3
    ## Rhode Island                    2
    ## South Carolina                  1
    ## South Dakota                    3
    ## Tennessee                       2
    ## Texas                           2
    ## Utah                            3
    ## Vermont                         3
    ## Virginia                        2
    ## Washington                      2
    ## West Virginia                   3
    ## Wisconsin                       3
    ## Wyoming                         2

### Question 8

New hierarchical clustering:

``` r
print(cluster_scaled_chop)
```

    ##                cutree.cluster_scaled..3.
    ## Alabama                                1
    ## Alaska                                 1
    ## Arizona                                2
    ## Arkansas                               3
    ## California                             2
    ## Colorado                               2
    ## Connecticut                            3
    ## Delaware                               3
    ## Florida                                2
    ## Georgia                                1
    ## Hawaii                                 3
    ## Idaho                                  3
    ## Illinois                               2
    ## Indiana                                3
    ## Iowa                                   3
    ## Kansas                                 3
    ## Kentucky                               3
    ## Louisiana                              1
    ## Maine                                  3
    ## Maryland                               2
    ## Massachusetts                          3
    ## Michigan                               2
    ## Minnesota                              3
    ## Mississippi                            1
    ## Missouri                               3
    ## Montana                                3
    ## Nebraska                               3
    ## Nevada                                 2
    ## New Hampshire                          3
    ## New Jersey                             3
    ## New Mexico                             2
    ## New York                               2
    ## North Carolina                         1
    ## North Dakota                           3
    ## Ohio                                   3
    ## Oklahoma                               3
    ## Oregon                                 3
    ## Pennsylvania                           3
    ## Rhode Island                           3
    ## South Carolina                         1
    ## South Dakota                           3
    ## Tennessee                              1
    ## Texas                                  2
    ## Utah                                   3
    ## Vermont                                3
    ## Virginia                               3
    ## Washington                             3
    ## West Virginia                          3
    ## Wisconsin                              3
    ## Wyoming                                3

``` r
png(filename="P2Q8.png")
plot(cluster_scaled, main="Scaled Cluster Dendrogram")
dev.off()
```

    ## quartz_off_screen 
    ##                 2

What effect does scaling the variables have on the hierarchical clustering obtained? There appears to be some difference between the scaled cluster dendrogram and the cluster dendrogram but the overall structure does not appear to have changed drastically. In the new graph, it is easy to identify four main clusters whereas in the old graph, it is easy to identify three main clusters. Additionally, we can see that Alaska is particularly prominent in the scaled dendrogram. This is because all its values are very different from other states, but the generally high assault values mask the otherwise deviant nature of Alaskan crime statistics. Upon scaling, this effect can be removed, and we can easily identify Alaska as being different from other States in the scaled dendrogram. The scaling allows us to compare the different numeric values, some of which are per 100,000, and others of which are percentage-based values.
