The loss function of the model is written as
$$
\mathcal{L}(\boldsymbol{\beta}) = \dfrac{1}{2}\sum_{i = 1}^N w_i\Big(y_i - \boldsymbol{\beta}^\top \tilde{\mathbf{x}}_i\Big)^2 = \dfrac{1}{2}\big(\mathbf{y} - \tilde{\mathbf{X}}\boldsymbol{\beta}\big)^\top~\mathbf{W}~\big(\mathbf{y} - \tilde{\mathbf{X}}\boldsymbol{\beta}\big)
$$
where $\mathbf{W} = \text{diag}(w_1, \dots, w_N)$ and each row of $\tilde{\mathbf{X}}$ corresponds to a data point $\tilde{\mathbf{x}}_i$.

Taking the gradient of the loss function with respect to $\boldsymbol{\beta}$ yields
$$
\nabla \mathcal{L}(\boldsymbol{\beta}) = 
$$
