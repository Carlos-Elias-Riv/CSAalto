datos <- sleep 
grupo1 <- sleep[sleep$group == 1, ]

## visualize the data

hist(grupo1$extra)
boxplot(grupo1$extra)

binom.test(sum(grupo1$extra > 0), length(grupo1$extra))

# if the p-value with have been lower than .05 then we reject the null hypothesis

salary <- data.frame(women = c(42600, 43600, 49300, 42300, 46200, 45900, 47500, 41300),
                     men = c(46200, 44700, 48400, 41700, 48600, 49300, 48300, 44300))

salary_diff <- salary$men - salary$women

bothsalaries <- c(salary$women, salary$men)
# W = 21, p-value = 0.269 so we reject the hypothesis

hist(salary_diff)

# we could apply, sign test or we could also apply a two-sample rank test

binom.test(sum(salary_diff > 0), length(salary_diff))

wilcox_test_result <- wilcox.test(salary$women, salary$men, paired = TRUE)
# alternativamente el hizo wilcox.test(salary_diff, mu = 0)

## suponemos que son muestras mutuamente independientes e idénticamente distribuidas

line <- c("F", "F", "M", "M", "F", "M", "F", "F", "M", "F", "M", "F", "M", "M", "M", "F", "M", "M", "M", "M")

# la hipótesis que queremos es que las medianas sean las mismas
femalerank <- c()
malerank <- c()
for (i in 1: length(line)){
  if(line[i] == "F"){
    femalerank <- c(femalerank, i)
  }
  else{
    malerank <- c(malerank, i)
  }
}
wilcox_test_result <- wilcox.test(femalerank, malerank)

female <- (1:20)[line == "F"]
male <- (1:20)[line == "M"]

wilcox.test(male, female)


