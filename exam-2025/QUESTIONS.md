# Exam 2025 — Questions

## Part 1: Multiple choice questions (0.5 point each, 6 points total)

Each question has exactly one correct answer.

**Q1.** Given $d$-dimensional data $x_{i=1}^N$, you run PCA and pick $P$ principal components. Can you always reconstruct any data point $x_i$ from the $P$ principal components with zero reconstruction error?
- (A) Yes, if $P < d$.
- (B) Yes, if $P = d$.
- (C) Yes, if $P < N$.
- (D) No, always.

**Q2.** Which of the following transformations to a data matrix $X$ will affect the principal components obtained through PCA?
- (A) Adding a constant value to all elements of $X$.
- (B) Multiplying one of the features of $X$ by a constant.
- (C) Adding an extra feature to $X$ (an extra column) that is constant across all data points.
- (D) None of the above answers.

**Q3.** In linear regression, we model $p(y \mid x) \sim \mathcal{N}(\beta^\top x + \beta_0, \sigma^2)$. The irreducible error in this model is:
- (A) $\sigma^2$
- (B) $E[y \mid x]$
- (C) $E[(y - E[y \mid x])^2 \mid x]$
- (D) None of the above.

**Q4.** The decision boundaries of a logistic regression model:
- (A) Split classes using only one of the input features.
- (B) Split classes using a combination of the input features.
- (C) Often have curved shapes.
- (D) None of the above.

**Q5.** How does the bias-variance decomposition of a ridge regression estimator compare with that of ordinary least squares regression?
- (A) Ridge has larger bias, larger variance.
- (B) Ridge has larger bias, smaller variance.
- (C) Ridge has smaller bias, larger variance.
- (D) Ridge has smaller bias, smaller variance.

**Q6.** Suppose you want to split a graph $G$ into two subgraphs. Let $L$ be $G$'s Laplacian matrix. Which of the following could help you find a good split?
- (A) The eigenvector corresponding to the second-largest eigenvalue of $L$.
- (B) The eigenvector corresponding to the second-smallest eigenvalue of $L$.
- (C) The left singular vector corresponding to the second-largest singular value of $L$.
- (D) None of the above.

**Q7.** We define a 2-dimensional dataset and process it using `StandardScaler` from `sklearn` with its default parameters. The dataset has feature $X_1$ centered around $4$ with unit variance and feature $X_2$ uniformly spread around $0$ with larger variance. Which of the four presented preprocessings (A, B, C, D — shown in the figure in the exam PDF) results from applying `StandardScaler`?
- (A) Preprocessing A
- (B) Preprocessing B
- (C) Preprocessing C
- (D) Preprocessing D

**Q8.** Why does random forests select a random subset of predictors when building each of its decision trees?
- (A) To facilitate the cross-validation procedure afterwards.
- (B) To reduce bias of the final ensemble estimator.
- (C) To maximize the entropy of the decision trees.
- (D) To reduce the correlation between the decision trees in the ensemble.

**Q9.** Which of the following statements is true about nearest neighbor classifiers?
- (A) Nearest neighbors can be slow to find in high-dimensional spaces.
- (B) Nearest neighbor classifiers can only work with the Euclidean distance.
- (C) Nearest neighbor classifiers do not need to store the training data.
- (D) None of the above.

**Q10.** Suppose you have data with lots of outliers. Everything else being equal, and assuming that you do not do any pre-processing, what cost function will be less affected by these outliers?
- (A) $(y - f(x))^2$
- (B) $|y - f(x)|$
- (C) $\frac{1}{y} \times (y - f(x))^2$
- (D) $(\log(y) - f(x))^2$

**Q11.** The figure below shows three different datasets (A, B, C) and the predictions of the same linear model (the line $y = x$) used to predict each of them. Choose the correct ordering with respect to the MSE (Mean Squared Error) loss on each dataset:
- (A) $\text{MSE}_B > \text{MSE}_A > \text{MSE}_C$
- (B) $\text{MSE}_B > \text{MSE}_C > \text{MSE}_A$
- (C) At least two of the MSE losses are equal.
- (D) $\text{MSE}_A > \text{MSE}_B > \text{MSE}_C$

**Q12.** Considering the same figure from Q11, choose the correct ordering with respect to the MAE (Mean Absolute Error) loss on each dataset:
- (A) $\text{MAE}_A > \text{MAE}_C > \text{MAE}_B$
- (B) $\text{MAE}_C > \text{MAE}_B > \text{MAE}_A$
- (C) At least two of MAE losses are equal.
- (D) $\text{MAE}_B > \text{MAE}_C > \text{MAE}_A$

---

## Part 2: Multiple linear regression (5 points)

Set `numpy.random.seed(0)` at the beginning.

**(a)** Simulate a dataset of size $N = 1000$ of the following generating model:

$$X_{1,i} = \varepsilon_{1,i}$$
$$X_{2,i} = 4X_{1,i} + \varepsilon_{2,i}$$
$$Y_i = X_{2,i} + X_{1,i} - 5 + \varepsilon_{3,i}$$

where $i \in \{1, \ldots, N\}$ and the $\varepsilon_{j,i}$ are independent $\mathcal{N}(0, 1)$ random variables. For a given $i$, what is the distribution of $(X_{1,i}, X_{2,i})$? Plot the cloud of points of the simulated values. What is its shape? Can you write a closed-form expression for it? **(2 points)**

**(b)** Consider the following two regression models:

$$\text{Model A:} \quad Y_i = \alpha_1 X_{1,i} + \alpha_0 + \tilde{\varepsilon}_{A,i}$$
$$\text{Model B:} \quad Y_i = \beta_2 X_{2,i} + \beta_0 + \tilde{\varepsilon}_{B,i}$$

What should be the values of $\hat{\alpha}_0$, $\hat{\alpha}_1$, $\hat{\sigma}^2_A$, $\hat{\beta}_0$, $\hat{\beta}_2$, $\hat{\sigma}^2_B$ when $N \to \infty$? Consider $N = 1000$ and check whether estimates are close to the true values. Now do `np.random.seed(3)` and simulate again with $n = 10$. Estimate the parameters. What happens? **(2 points)**

**(c)** Consider the full model: $Y_i = \gamma_2 X_{2,i} + \gamma_1 X_{1,i} + \gamma_0 + \varepsilon_i$. For the previously simulated data with $n = 10$, estimate $\hat{\gamma}_0$, $\hat{\gamma}_1$, $\hat{\gamma}_2$, $\hat{\sigma}^2$ and compare them with the parameters from (b). What can you say about the effects of $X_1$ and $X_2$ on $Y$? And about their correlation? **(1 point)**

---

## Part 3: AdaBoost (5 points)

Recall the AdaBoost algorithm with decision stumps. The algorithm iteratively trains weak classifiers $h_t$, choosing step-sizes $\alpha_t = \frac{1}{2} \log\frac{1 - \varepsilon_t}{\varepsilon_t}$ and updating sample weights $D_{t+1}$. The final hypothesis is $H(x) = \text{sign}\!\left(\sum_t \alpha_t h_t(x)\right)$.

The figure in the exam PDF shows three iterations of AdaBoost using a depth-1 decision tree (decision stump) on a given dataset. Each dashed line represents the decision boundary of $h_t$ at iteration $t \in \{1, 2, 3\}$, and the shaded regions represent the predictions.

**(a)** For each iteration in the figure, find the weighted training error $\varepsilon_t$ and importance $\alpha_t$ of $h_t$. For $t = 2$ and $t = 3$, find the weight normalization $Z_t$ and record the updated weight for each point. **(1 point)**

**(b)** Load the `datasets/dataset_ex3.csv` file into a dataframe and make a scatter plot of the data points using the same markers and colors as in the figure (hint: `marker='+'` for positive class, `marker='_'` for negative class in matplotlib). **(1 point)**

**(c)** With the help of `DecisionTreeClassifier` from sklearn, fit a decision stump $h_1$ on the dataset corresponding to the first iteration of AdaBoost. Remember to set a uniform weight $w_1$ over all data points and ensure labels $y_i \in \{-1, +1\}$. Show that your predictions match those from the first iteration in the figure. **(1 point)**

**(d)** Calculate the new weights $w_2$ of the data points based on predictions from iteration $t = 1$. Use them to fit a new decision stump $h_2$ on the weighted dataset (hint: use the optional argument `sample_weight` in sklearn's `fit` method). Show that your predictions match those from the second iteration in the figure. **(0.5 points)**

**(e)** Calculate the new weights $w_3$ of the data points based on predictions from iteration $t = 2$. Use them to fit a new decision stump $h_3$ on the weighted dataset. Show that your predictions match those from the third iteration in the figure. **(0.5 points)**

**(f)** Calculate the training error of the final ensemble classifier, i.e. the classifier that for each datapoint $x$ outputs $H(x) = \text{sign}(\alpha_1 h_1(x) + \alpha_2 h_2(x) + \alpha_3 h_3(x))$. **(1 point)**

---

## Part 4: Community detection (4 points)

We consider Wayne Zachary's "karate club" network — a social network of friendships between karate club members at a US university. The club split into two equal parts of 17 members each due to a dispute over fees. These two factions form the ground truth.

Load the data as follows:
```python
A = np.loadtxt('datasets/karate_adjacency.csv')  # adjacency matrix
F = np.loadtxt('datasets/karate_factions.csv')   # ground truth factions
```

**(a)** Define in your own words the notion of modularity of a network and how it can be used to split a network into communities. Your description should include whether the modularity depends solely on the structure of the network or not. **(0.5 points)**

**(b)** Using the equations seen in class, calculate the modularity matrix of the graph. **(0.5 points)**

**(c)** Using the equations seen in class, calculate the modularity $Q$ of the graph when fixing the classes of each node according to their ground truth factions as given in array $F$. (Hint: encode the factions with $-1$ and $+1$ as discussed in class.) **(1 point)**

**(d)** Based on the eigenvalue and eigenvector decomposition of the modularity matrix, split the graph into two communities. Interpret the magnitude of the coordinates of the leading eigenvector (the one related to the largest eigenvalue) and explain how it can be related to the "faction ambiguity" of each vertex in the graph. Are there any nodes for which the split looks more ambiguous than others? Relate your answer with the figure of the graph. **(1.5 points)**

**(e)** What would happen if all the eigenvalues of the modularity matrix were smaller than zero? What would this indicate in terms of the structure of the network? **(0.5 points)**
