# Exam 2018 — Questions

## Exercise 1: High-dimensional linear regression

Consider the following R script:

```r
set.seed(0)
pt = 201       # Number of variables
p = pt - 1    # Number of predictors
n = 30 * p    # Sample size
D = matrix(rnorm(n*pt), nrow=n, ncol=pt)
D = data.frame(D)
names(D)[pt] = "Y"
reg = lm(Y~., data=D)
```

**Q1.** What does the script above do? What is the true distribution for the random variable Y given the first 200 columns of `D` (X₁, …, X₂₀₀)? Give the name and parameters of this distribution.

**Q2.** Write an equation defining the model estimated by the `lm` command. What is the difference between this model and the one defined in Q1?

**Q3.** Provide and execute some R code to compute the number of coefficients assessed as significantly non-zero at level 5%. (Hint: `summary(reg)$coefficients`)

**Q4.** Provide an explanation for the result obtained in Q3.

**Q5.** What issue is raised by the result obtained in Q3?

**Q6.** Describe a possible solution to solve this problem, explaining why you think it should work (10 lines expected, ~85 characters per line). Implement that solution and comment the results.

---

## Exercise 2: PCA on beer data

We consider 40 kinds of beers, each characterised by four variables:

| Variable   | Meaning |
|------------|---------|
| Taste      | Quantitative appreciation of taste given by experts |
| Bitter     | High values = bitter beers, low values = sweet beers |
| Thirst     | High values = thirst-quenching, low values = leaves consumers thirsty |
| DgAlcohol  | Degree of alcohol |

The aim is to use PCA to obtain a summary of the data and visualize it.

```r
load("beers.pca")
```

**Q1.** Provide and execute R code to plot individuals in the first principal plane.

**Q2.** Provide and execute R code to perform PCA on variables and plot them in the first principal plane. Three groups of variables clearly appear. What can be said about correlations:
- Between variables belonging to different groups?
- Between variables belonging to the same group?

**Q3.** In PCA computations, was the `scale` argument set to `FALSE` or `TRUE`? How can you tell? For which purpose was `scale` set to that value?

**Q4.** Do you assess that two principal components are sufficient to represent the features of the beers? Why? If not, how many principal components would be needed?

**Q5.** Return to the figure from Q1. For each of the four quadrants (upper-left, upper-right, lower-left, lower-right): what properties are shared by the beers within that quadrant? Drinking more than 50cl beer results in the legal inability to drive. You wish to drink 50cl beer and quench your thirst, but minimise the risk of exceeding the legal rate of alcohol while driving. Which beer should you avoid? Which beer would you choose to avoid bitterness, and what potential drawback should you expect? Which beer would you choose to avoid both bitterness and bad taste?
