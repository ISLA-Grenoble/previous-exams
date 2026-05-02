# Exam 2019-2 — Questions

## Exercise 1: Linear regression — car fuel consumption

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

---

## Exercise 2: PCA — stroke recovery assessment

Twenty subjects from two large hospitals in Brisbane, Australia were assessed after a stroke. The assessment measures motor function, balance, sensation, passive range of motion, and joint pain.

| Variable    | Description |
|-------------|-------------|
| Subject     | Subject ID (1–20) |
| Arms        | Arm and shoulder motor function (max 36) |
| Legs        | Lower limb motor function (max 30) |
| Balance     | Balance score (max 14) |
| Sensation   | Sensation score (max 24) |
| JointPain   | Freedom from joint pain (max 24) |
| JointMotion | Passive joint motion (max 24) |

```r
stroke = read.table("strokeass.txt", header=TRUE, row.names=1)
stroke = stroke[,-c(1,2,3,4,7,12,13,14)]
stroke.pca = prcomp(stroke, scale=TRUE)
```

**Q1.** Write a text with 60 to 80 words explaining the principle of PCA.

**Q2.**
- Why did we use the option `scale=TRUE`?
- What could happen if we set that option to `FALSE`? Is it desirable?

**Q3.** Considering the output of `summary(stroke.pca)`:
- What do the three lines (Standard deviation, Proportion of Variance, Cumulative Proportion) mean or represent?
- What to deduce from the output concerning the number of axes to be kept in the analysis?

**Q4.** The code below produces correlation circle figures in the planes (Axis 1, Axis 2) and (Axis 1, Axis 3). Provide a detailed comment on the figures (110 to 130 words).

```r
a <- (-100:100)/100
y <- sqrt(1-a^2)
P <- stroke.pca$rotation
lambda <- stroke.pca$sdev^2
for(i in 1:(dim(P)[2])) P[,i] <- P[,i] * sqrt(lambda[i])

par(mfcol=c(1,2))
for (j in 2:3) {
  plot(P[,1], P[,j], xlab="Axis 1", ylab=paste("Axis ", j), xlim=c(-1,1), ylim=c(-1,1))
  abline(h=0, v=0); lines(a, y); lines(a, -y)
  text(P[,1], P[,j], names(stroke))
}
```

**Q5.** Provide and execute R code to represent the 20 individuals in the first principal plane (the figure should contain 20 points).

**Q6.** Roughly speaking, what are the main features (in terms of arm/shoulder/lower limb motor functions, balance, sensation, joint pain and motion) of the individuals placed in the:
- Upper-left quadrant?
- Upper-right quadrant?
- Lower-left quadrant?
- Lower-right quadrant?

Justify your answer carefully.

**Q7.** Among the six features mentioned in Q6, which one are you the least confident in regarding your answer? Why?
