# PW3 - Data, Distributions, Testing, and Causation

Data: Heart Disease (Cleveland), UCI Machine Learning Repository / Kaggle. heart.csv was made from processed.cleveland.data with prepare_heart.py (I added the column names, and target = 1 if num > 0, otherwise 0). The second dataset is chemicals_cancer.csv.

## Session 1 - Shape of the variables

age: one peak around 55-60 years, roughly bell-shaped, values from 29 to 77.

chol: one peak around 220-250, a long tail to the right, and one outlier near 560. Skewed to the right.

trestbps: one peak around 120-140, a tail to the right up to 200. Skewed to the right. The bars are jagged because blood pressure is mostly recorded as round numbers.

thalach: one peak around 160, a long tail to the left down to 70. Skewed to the left.

## Session 1 - Normality

I used the Shapiro-Wilk test, the skewness and Q-Q plots.

age: skewness -0.21, Shapiro-Wilk p = 6.1e-03. The p-value is below 0.05, but with 303 patients the test notices very small deviations. The skewness is close to 0 and the Q-Q plot follows the line, so I treat age as approximately normal.

chol: skewness 1.13, p = 5.9e-09. Strongly skewed to the right, the Q-Q plot bends away from the line at the top end. Not normal.

trestbps: skewness 0.70, p = 1.8e-06. Skewed to the right, the Q-Q plot is stepped. Not normal.

thalach: skewness -0.53, p = 7.0e-05. Skewed to the left, the Q-Q plot bends away at the lower end. Not normal, so in Session 2 I used a method that does not need normality.

## Session 2 - Is the effect real? (thalach)

Question: do patients with heart disease have a different maximum heart rate than healthy ones?

I split thalach by target (1 = disease, 0 = healthy). Because thalach is not normal, I used the Mann-Whitney U test instead of a t-test (it does not assume normality). The test was two-sided.

Disease group: 139 patients, mean 139.26, median 142.0. Healthy group: 164 patients, mean 158.38, median 161.0.

Result: U = 5806.5, p = 1.9e-13.

Conclusion: p is far below 0.05, so the two groups really differ. Patients with heart disease have a lower maximum heart rate, about 19 bpm lower on average.

Mean and uncertainty: I used the standard error of the mean (SEM = std / sqrt(n)). Disease: mean 139.26, SEM 1.92. Healthy: mean 158.38, SEM 1.50. In the plot (thalach_means.png) the error bars are small, about 2 bpm, compared to the difference between the means, and they do not overlap. So the picture agrees with the Mann-Whitney result.

## Session 2 - Age and heart rate

I used the Spearman correlation (it does not need normality, and thalach is not normal) and also the Pearson correlation for comparison. Spearman: -0.392 (p = 1.5e-12). Pearson: -0.394 (p = 1.1e-12).

The correlation is negative and moderate. Older patients tend to have a lower maximum heart rate. The effect is not by chance (p is tiny), but the scatter in the plot (age_thalach.png) is large, so age explains only part of the variation.

## Dataset 2 - Chemical mystery

Naive analysis: I computed the correlation of each chemical with malignancy. Benzene: Pearson 0.385, Spearman 0.377. Cadmium: Pearson 0.880, Spearman 0.885. Cadmium is much more strongly associated, so taken at face value cadmium looks like the cause.

Looking again: the correlation matrix showed that pollution_index is almost perfectly correlated with cadmium (0.98), strongly correlated with malignancy (0.90) and not correlated with benzene (0.05). So pollution could be a third variable that influences both cadmium and malignancy.

To test this I kept only patients with similar pollution (40 < pollution_index < 60, 199 patients) and computed the correlations again inside this group. Benzene: 0.385 for all patients, 0.702 in the restricted group. Cadmium: 0.880 for all patients, 0.316 in the restricted group (plot: controlled.png).

The association of cadmium collapses when pollution is held roughly constant. The association of benzene does not disappear, it gets even clearer. The 0.316 left for cadmium is because the band is not perfectly narrow, so pollution still varies a bit inside it and it is almost perfectly correlated with cadmium.

Conclusion: cadmium only looked guilty, because pollution raises both cadmium and malignancy. Benzene is the chemical that really causes malignancy, because its effect survives when the confounder is controlled.

## Bonus - how unpredictable is a category?

I used the Shannon entropy H = -sum(p * log2(p)). For two classes, H = 1 bit means a perfect 50/50 split (hardest to guess), and H close to 0 means almost everything is in one class (easy to guess).

target: proportions 54.1% / 45.9%, entropy 0.995 bits. It is almost perfectly balanced, always guessing the most common class is right only 54.1% of the time, about like a coin flip.

sex: proportions 68% / 32%, entropy 0.905 bits. It is more lopsided, so it is easier to guess (68.0% by always choosing the most common class).