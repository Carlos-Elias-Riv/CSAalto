# 1. The data set iris contains measurements of the sepal length and width and petal length and width for 50 flowers from each of 3 species of iris. We want to study the distribution of the ratio between sepal length and sepal width of an iris of the species setosa.

# a. Create a new 1-dimensional data set which contains only the ratios Sepal.Length/Sepal.Width for the irises of the species setosa.
library(iris)
ratios <- iris$Sepal.Length / iris$Sepal.Width

# b. Find a suitable way to visualize the ratio.

hist(ratios)
boxplot(ratios)

# c. Use bootstrapping to construct a 95% confidence interval for the expected value of the ratio.
# Load the necessary libraries
library(boot)

# Define the function to calculate the mean
mean_func <- function(data, indices) {
  mean(data[indices])
}

# Perform bootstrap resampling
boot_results <- boot(ratios, mean_func, R = 2000)

# Calculate the 95% confidence interval
conf_interval <- boot.ci(boot_results, type = "basic", conf = 0.95)




# d. Add the confidence interval end points to the plot of part b.

# Plot the histogram of ratios
hist(ratios, main = "Histogram of Sepal Length/Width Ratios", xlab = "Ratio", col = "lightblue")

# Add vertical lines for the confidence interval
abline(v = conf_interval$basic[4], col = "red", lty = 2)  # Lower endpoint
abline(v = conf_interval$basic[5], col = "blue", lty = 2)  # Upper endpoint

# Add a legend
legend("topright", legend = c("Lower CI", "Upper CI"), col = c("red", "blue"), lty = 2)
## alternativa para hacer boots

boots_data <- replicate(2000, mean(sample(ratios, length(ratios), replace = TRUE)))
qunatiles <- quantile(boots_data, probs = c(0.025, 0.0975))
hist(ratios)
abline(v = qunatiles, col = 2, lwd = 2)

# e. What does the confidence interval tell us about the distribution of the ratio?

# that the mean is centralized and maybe it indicates a non skewed 

# f. What assumptions did the confidence interval in part c make?

# each of the observations was independent of each other

# 2. The data set below contains the annual salaries (in dollars) of 8 American women and 8 American men. The observations are paired such that each woman is matched with a man having similar background (age, occupation, level of education, etc). We are interested in studying whether the expected values of the salaries of women and men differ.

salary <- data.frame(women = c(42600, 43600, 49300, 42300, 46200, 45900, 47500, 41300),
                     men = c(46200, 44700, 48400, 41700, 48600, 49300, 48300, 44300))

dif <- salary$men - salary$women

hist(dif)

# a. Find a suitable way to visualize the data.

# b. Which test is appropriate in studying our question of interest?

# on average does men make more money than women?
# we want to test if mu == 0 mu of the difference between men and women salary

tstatistic <- function(dif){ (mean(dif) - 0) / (sqrt(var(dif)) /  sqrt(length(dif))) }


# t.test(salary$women - salary$men, mu = 0, conf.level = 0.9)
# lo obtiene a partir de la distribución t de student

# c. State the hypotheses of your chosen test and conduct it on the significance level 10%.

# t.test(salary$women - salary$men, mu = 0, conf.level = 0.9)

# d. What is the conclusion of the test?

# on average the salary gap between men and women is not that big

# e. What assumptions did the test in part c make? Are they justifiable?



# 3. Consider again the iris data set from exercise 1. Study whether the expected values and variances of Petal.Length differ between irises of the species versicolor and virginica

versicolor <- iris[iris$Species == "versicolor", ]
virginica <- iris[iris$Species == "virginica", ]
# a. Find a suitable way to visualize the data.
boxplot(versicolor$Petal.Length)
boxplot(virginica$Petal.Length)
# b. Test whether the expected values differ using the two-sample t-test on a significance level 5%.
t_test <- t.test(versicolor$Petal.Length, virginica$Petal.Length, conf.level = .95)

# Print the test results
print(t_test)

# c. Test whether the variances differ using the variance comparison test on a significance level 5%.
v_test <- var.test(versicolor$Petal.Length, virginica$Petal.Length, conf.level = .95)
# d. What are the conclusions of the tests?

# e. What assumptions did the tests in parts b and c make? Are they justifiable?
