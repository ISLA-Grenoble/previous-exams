# Exam 2022 — Questions

## Part 1: Multiple regression (7 points)

The dataset contains data on test performance, school characteristics, and student demographic backgrounds from Californian districts (1998–1999). The objective is to predict test scores (combining math and reading tests) based on sociodemographic variables.

Variables:
- `enrltot`: number of kids at school
- `teachers`: number of full-time teachers
- `calwpct`: percentage of students in a public assistance program
- `mealpct`: percentage of students qualifying for reduced price lunch
- `computer`: number of computers per classroom
- `testscr`: test score
- `compstu`: number of computers per student
- `expnstu`: expenditure per student
- `str`: student–teacher ratio
- `avginc`: district average income (×1000)
- `elpct`: percentage of students for whom English is a second language

```r
data <- read.csv("Caschool.csv", sep=";")
library(MASS)
```

**Q1.** How many Californian districts are represented in the dataset?

**Q2.** Using multiple regression, find which variables are significantly associated with test scores. Are the effects significant in the expected directions? (`testscr`)

**Q3.** Is the variable `calwpct` significant when using a simple linear regression (one predictive variable only)? Explain the difference with the result of multiple regression.

**Q4.** Using model selection based on an information criterion (e.g. with the `aic` command in R), find a parsimonious regression model that explains the test score. Explain the computational procedure and provide the parsimonious model.

**Q5.** Train the complete model (all variables) on all districts except the first 100 districts and evaluate the mean square prediction error on the first 100 districts.

**Q6.** Plot the first 100 fitted values as a function of the true value of the test score and evaluate if the model over- or underestimates test scores. Confirm your results using numerical computations.

**Q7.** Compute the mean square prediction error using the parsimonious model found in Q4. Compare prediction accuracies and evaluate if the reduced model under- or overestimates test score.

---

## Part 2: Classification (7 points)

Consider a simulated dataset generated as follows:
1. Set the seed: `set.seed(42)`.
2. For each data point i, sample its label from a Bernoulli distribution yᵢ ~ B(p): yᵢ = 1 with probability p, yᵢ = 0 with probability 1 − p.
3. Depending on the label yᵢ ∈ {0,1}, sample the data point xᵢ as follows:
   - yᵢ = 0 ⇒ xᵢ ~ 0.5 N(μ₀⁽ᵃ⁾, C₀⁽ᵃ⁾) + 0.5 N(μ₀⁽ᵇ⁾, C₀⁽ᵇ⁾)
   - yᵢ = 1 ⇒ xᵢ ~ N(μ₁, C₁)

where μ₀⁽ᵃ⁾ = [0, 1]ᵀ, μ₀⁽ᵇ⁾ = [0, −1]ᵀ, μ₁ = [ε, 0]ᵀ, and C₀⁽ᵃ⁾ = C₀⁽ᵇ⁾ = 0.5 I₂, C₁ = I₂.

Denote a set of n data points simulated with ε and p as D(n | ε, p).

**Q1.** Consider p = 0.5, ε = 2. Simulate Dtrain = D(200 | 2, 0.5) and Dtest = D(1000 | 2, 0.5).
- (a) What is the mathematical expression for the optimal Bayes classifier in this setting? And for its boundary region?
- (b) Plot the boundary region for the Bayes classifier overlaid with the scattered data points of Dtrain. Use different colors for each class and use `contour` for plotting the boundary region.
- (c) Estimate the error of the Bayes classifier on the samples from Dtest.
- (d) Train a LDA and a Logistic Regression classifier on Dtrain and estimate their errors on Dtest. How do these errors compare to (c)? Comment your results.

**Q2.** Consider p = 0.5 fixed and ε varying. Simulate 51 datasets D⁽ⁱ⁾train = D(200 | εᵢ, 0.5) and D⁽ⁱ⁾test = D(1000 | εᵢ, 0.5) with εᵢ = 1 + i/10 and i = 0, …, 50.
- (a) Calculate the test error for the Bayes classifier, LDA, and Logistic Regression for each dataset (train on D⁽ⁱ⁾train, test on D⁽ⁱ⁾test).
- (b) Plot a curve showing the error with each classifier as a function of ε. Comment your results. You should notice that for large ε the logistic regression throws an error — can you explain what is happening? What would be a good approach for limiting this problem?

---

## Part 3: Community detection (6 points)

We consider Wayne Zachary's "karate club" network — a social network representing friendships between members of a karate club at a US university. During the observation period, a dispute arose over fees and the club split into two parts (18 and 16 members). These two factions serve as the ground truth for community detection.

```r
library(igraph)
load('./karate.rda')
```

**Q1.** What does the following command do?
```r
plot(karate, vertex.size=degree(karate))
```
Can you interpret the result and explain why it might be useful for better understanding this graph of relations?

**Q2.** The true factions can be obtained via `V(karate)$Faction`. Use this information to calculate the modularity of the graph with this ground truth setup.

**Q3.** Calculate the modularity matrix using `modularity_matrix` and obtain its eigenvectors. Interpret the magnitude of the coordinates of the leading eigenvector (the one related to the largest eigenvalue) and explain how it can be related to the importance of each vertex in the graph. How can we use this eigenvector to split the graph into two communities?

**Q4.** Run algorithms `cluster_louvain` and `cluster_edge_betweenness` and comment the results (e.g. plot the graphs with detected communities, compare to the ground truth, check the modularity of each split).
