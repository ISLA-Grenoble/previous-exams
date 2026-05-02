# Exam 2024 — Questions

## Part 1: Multiple choice questions (6 points)

Each question has exactly one correct answer.

**Q1 — True or False (0.5 points each)**

For each item below, write True or False.

- (a) Unlabeled data can be used for detecting overfitting.
- (b) PCA and spectral embedding perform eigendecomposition on two different matrices. However, the dimensions of these matrices are the same.
- (c) Since classification is a special case of regression, logistic regression is a special case of linear regression.
- (d) The largest eigenvector of the covariance matrix is the direction of minimum variance in the data.
- (e) A random forest is an ensemble learning method that attempts to lower the bias error of decision trees.
- (f) As model complexity increases, bias will decrease while variance will increase.
- (g) Consider a cancer diagnosis classification problem where almost all of the people being diagnosed don't have cancer. The probability of correct classification is the most important metric to optimize.
- (h) The more features that we use to represent our data, the better the learning algorithm will generalize to new data points.

**Q2 — Ridge regularization (1 point)**
Assume N training samples (x₁, y₁), …, (xN, yN) where xᵢ ∈ Rᵖ and yᵢ ∈ R. For λ ≥ 0, consider:

L_λ(β) = (1/N) Σᵢ₌₁ᴺ (yᵢ − xᵢᵀβ)² + λ‖β‖²₂

and let C_λ = min_{β} L_λ(β). Which statement is true?
- (A) C_λ is a non-increasing function of λ.
- (B) For λ = 0, the loss L₀ is non-convex and might have several minimizers.
- (C) C_λ is a non-decreasing function of λ.
- (D) None of the above statements are true.

**Q3 — k-nearest neighbors (1 point)**
Which of the following are true for the k-nearest neighbor (k-NN) algorithm?
- (A) k-NN can be used for both classification and regression.
- (B) The decision boundary looks smoother with smaller values of k.
- (C) As k increases, the variance usually increases.
- (D) None of the above.

---

## Part 2: Multiple linear regression (5 points)

**(a)** Set `set.seed(0)`. Simulate 6000 × 201 = 1,206,000 independent random variables with the standard normal distribution. Store them into a matrix, then into a data frame with 6000 rows and 201 columns. Each column is referred to as a "variable". (Useful: `rnorm`, `matrix`, `data.frame`) **(0.5 points)**

**(b)** Define a Gaussian multiple linear regression model using the last 200 variables to predict the first one and write a mathematical equation (no R code!) to define this regression model. Write a second mathematical equation defining the true generative model associated with the data. Compare both models and discuss. **(1 point)**

**(c)** Estimate the parameters of the linear model using the last 200 variables to predict the first one. Compute the number of coefficients assessed as significantly non-zero at level 5%. Comment the result. (Useful: `summary(reg)$coefficients`) **(0.5 points)**

**(d)** Simulate a dataset of size N = 1000 of the following generating model:

X₁,ᵢ = ε₁,ᵢ  
X₂,ᵢ = 3X₁,ᵢ + ε₂,ᵢ  
Yᵢ = X₂,ᵢ + X₁,ᵢ + 2 + ε₃,ᵢ

where i ∈ {1, …, N} and the εᵢⱼ are independent N(0, 1) random variables. For a given i, what is the distribution of (X₁,ᵢ, X₂,ᵢ)? Plot the cloud of points. What is its shape? Can you write an analytical formula for it? **(1 point)**

**(e)** Consider the following two regression models:

Model A: Yᵢ = α₁X₁,ᵢ + α₀ + ε̃_{A,i}  
Model B: Yᵢ = β₂X₂,ᵢ + β₀ + ε̃_{B,i}

What should be the values of α̂₀, α̂₁, σ̂²_A, β̂₀, β̂₂, σ̂²_B when N → ∞? Consider N = 1000 and check whether estimates are close to the true values. Now do `set.seed(3)` and simulate again with n = 10. Estimate the parameters. What happens? **(1 point)**

**(f)** Consider the full model: Yᵢ = γ₂X₂,ᵢ + γ₁X₁,ᵢ + γ₀ + εᵢ. For the previously simulated data with n = 10, estimate γ̂₀, γ̂₁, γ̂₂, σ̂² and compare them with the parameters from (b). What can you say about the effects of X₁ and X₂ on Y? And about their correlation? **(1 point)**

---

## Part 3: Classification (5 points)

Generate a simulated dataset as follows:
1. `set.seed(42)`.
2. For each data point i, sample yᵢ ~ B(p): yᵢ = 1 with probability p, yᵢ = 0 with probability 1 − p. (Hint: sample U from `runif`, then B = 1(U < p).)
3. Depending on yᵢ ∈ {0, 1}, sample xᵢ ∈ R²:
   - yᵢ = 0 ⇒ xᵢ ~ N(μ₀, Σ₀)
   - yᵢ = 1 ⇒ xᵢ ~ N(μ₁, Σ₁)

where μ₀ = [0, 0]ᵀ, μ₁ = [ε, 0]ᵀ, Σ₀ = 0.5 I₂, Σ₁ = 0.4 I₂.

Use Dtrain = D(50 | 1, 0.2) and Dtest = D(1000 | 1, 0.2).

**(a)** Plot the data points in Dtrain ∪ Dtest using different colors to indicate classes and different symbols to indicate train vs. test set. **(1 point)**

**(b)** What is the mathematical expression for the optimal Bayes classifier in this setting? And for its boundary region? **(1 point)**

**(c)** Estimate the error of the Bayes classifier on the samples from Dtest. How do you expect it to change in terms of ε? **(1 point)**

**(d)** Given the structure of the model generating the datasets, which classifier (from our lectures) would you expect to be the most adequate? **(0.5 points)**

**(e)** Train a LDA, a QDA, and a Logistic Regression classifier on Dtrain and estimate their errors on Dtest. How do their errors compare to the value obtained in (b)? **(0.5 points)**

**(f)** Consider a new test set D'test = D(1000 | 1, 0.8). Use the same classifiers trained in (e) and estimate their new test errors. Do you observe any difference in the results? Can you explain what is happening? **(1 point)**

---

## Part 4: Community detection (4 points)

We consider Wayne Zachary's "karate club" network — a social network of friendships between karate club members at a US university. The club split into two parts (18 and 16 members) due to a dispute over fees. These two factions form the ground truth.

Start by loading the dataset with `load('./karate.rda')`.

**(a)** Define in your own words the notion of modularity of a network and how it can be used to split a network into communities. Your description should include whether the modularity depends solely on the structure of the network or not. **(0.5 points)**

**(b)** The true factions can be obtained via `V(karate)$Faction`. Use this information to calculate the modularity of the graph for this ground truth setup. **(1 point)**

**(c)** Calculate the modularity matrix using `modularity_matrix` and obtain its eigenvectors. Interpret the magnitude of the coordinates of the leading eigenvector (the one related to the largest eigenvalue) and explain how it relates to the importance of each vertex in the graph. How can we use this eigenvector to split the graph into two communities? **(1 point)**

**(d)** Are there any nodes for which the split in (b) looks more ambiguous than others? Which aspect of the eigenvectors of the modularity matrix could be useful to check this information? **(0.75 points)**

**(e)** What would happen if all the eigenvalues of the modularity matrix were smaller than zero? What would this indicate in terms of the structure of the network? **(0.75 points)**
