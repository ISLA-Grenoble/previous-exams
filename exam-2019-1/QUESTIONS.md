# Exam 2019-1 — Questions

## Exercise 1: Graph analysis — student migrations

To analyse student flows from 10 countries, 206,796 students are considered. For each student, the country of origin (O) and arrival (A) are recorded. The data is stored in `migrations.csv` as a matrix A where A[a,o] contains the number of students moving from country o to country a.

```r
A <- read.csv("migrations.csv", sep=";")
library(igraph)
```

**Q1.** Consider the code below. In the literature, how is matrix A referred to? Comment and justify the values of parameters `mode`, `weighted`, and `diag`.

```r
G <- graph.adjacency(as.matrix(A), mode="directed", weighted=TRUE, diag=FALSE)
```

**Q2.** Propose and run R code to plot the graph, using one vertex per country. Use arc widths proportional to their weights, the `layout.auto` layout, and scale the weights by a 1/3,000 factor.

**Q3.** Using visual information from the graph obtained in Q2 only, what are the most striking features of student flows?

**Q4.** Propose a formula for the order of directed graphs, defined as the ratio of the actual number of arcs on the maximal number of arcs (forbidding self-loops). Provide R commands to compute the graph order, size, density, and diameter (ignoring weights) and provide those values.

**Q5.** The graph is displayed as an undirected, weighted bipartite graph B (as shown with the code below). Perform graph clustering on B and justify your choice of algorithm. Clusters may contain both countries of departure and arrival. Plot the yielded graph partition using different vertex colors for clusters.

```r
B <- graph.incidence(A, weighted = TRUE)
V(B)$color <- V(B)$type
V(B)$label.cex <- 0.8
V(B)$color=gsub("FALSE","red",V(B)$color)
V(B)$color=gsub("TRUE","green",V(B)$color)
plot(B, edge.color="gray30", edge.width=E(B)$weight/3000, layout=layout_as_bipartite)
```

**Q6.** Provide an interpretation of the clusters.

---

## Exercise 2: Linear regression — car fuel consumption

Car consumptions are measured in MPGs (miles per gallon): higher MPG values mean more miles with one gallon of fuel. To determine which car features affect consumption, we use the following linear regression model:

```r
M <- lm(mpg~., data=mtcars)
summary(M)
```

**Q1.** Which predictors seem to have an effect on mpg? Make your criterion explicit.

**Q2.** Provide a 95% confidence interval for the `carb` parameter. What can you deduce from the fact that 0 is in the confidence interval? Provide descriptions and formulas to explain what the quantity in column `Pr(>|t|)` represents.

**Q3.** Provide descriptions and formulas to explain what `p-value: 3.793e-07` represents. What to conclude from this value? Does it seem in discordance with your answer in Q1? What could explain such discordance?

**Q4.** What strategy could be used to obtain a linear regression model with a maximal number of predictors, all of which have significant effect at level 5%? Can you run it in practice? If yes, provide the estimates. If not, provide the reason.

**Q5.** Describe and run some algorithm to find the best model in some sense.
