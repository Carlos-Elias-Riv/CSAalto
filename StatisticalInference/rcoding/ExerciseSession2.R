library(ggplot2)

carros <- cars

ggplot(carros, aes(x = speed, y = dist)) + 
  geom_point() +
  geom_line() + 
  labs(title = "correlation between speed and distance")

ggplot(carros, aes(x=speed)) +
  geom_histogram(binwidth=1, fill="blue", color="black") +
  labs(x="Speed", y="occurence", title="Distribution of Speed")

ggplot(carros, aes(x=dist)) +
  geom_histogram(binwidth=1, fill="blue", color="black") +
  labs(x="Distance", y="ocurrence", title="Distribution of Distance")

## Class exercise, podría estar chambeando puta madre

hist(rivers)
rios <- rivers
hist(rios)
breaks <- c(min(rivers), 250, 500, 750, 1000, 1250, max(rivers))
rios_cut <- cut(rios, breaks = breaks, include.lowest = TRUE)
barplot(table(rios_cut))

## segunda parte
hist(islands)

# vamos a quitar los outliers

IQR_islands <- IQR(islands)

# Calculate the lower and upper bounds
lower_bound <- quantile(islands, 0.25) - 1.5 * IQR_islands
upper_bound <- quantile(islands, 0.75) + 1.5 * IQR_islands

# Remove the outliers
islands_no_outliers <- islands[islands > lower_bound & islands < upper_bound]

IQR_islands_no_outliers <- IQR(islands_no_outliers)

lower_bound <- quantile(islands_no_outliers, 0.25) - 1.5 * IQR_islands_no_outliers
upper_bound <- quantile(islands_no_outliers, 0.75) + 1.5 * IQR_islands_no_outliers

# Remove the outliers
islands_no_outliers2 <- islands_no_outliers[islands_no_outliers > lower_bound & islands_no_outliers < upper_bound]
## lets create a function that recursively returns this 
remove_outliers_n_times <- function(data, n) {
  # Base case: if n is 0, return the data
  if (n == 0) {
    return(data)
  } else {
    # Calculate the IQR
    IQR_data <- IQR(data)
    
    # Calculate the lower and upper bounds
    lower_bound <- quantile(data, 0.25) - 1.5 * IQR_data
    upper_bound <- quantile(data, 0.75) + 1.5 * IQR_data
    
    # Remove the outliers
    data_no_outliers <- data[data > lower_bound & data < upper_bound]
    
    # Recursive call with decremented n
    return(remove_outliers_n_times(data_no_outliers, n - 1))
  }
}


testdata <- remove_outliers_n_times(islands, 8)


## metodos no robustos y robustos son clasificados con base en si son sensibles a outliers o no


## time to do the last part 

# The data set Nile contains yearly measurements of the flow of the river Nile.
#  a.Find a suitable way to visualize the data and plot it.
#  b.How has the flow of the river changed during the years 1871-1970 based on the plot?
#  c.Calculate the values of the following statistics for the flow: mean, standard deviation, variance, minimum, maximum, median, median absolute deviation, mode, skewness and kurtosis.
#  d.How are each of the statistics in part c visible in the plot of part a?

# Part a
par(mfrow = c(1, 2))

hist(Nile)

years <- seq(1871, 1970, by = 1)
plot(years, Nile, type = "o")

# Part b
# The flow of the river based on the plot has been slightly decreasing over the years

# Part c
# 
getmode <- function(v) {
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v, uniqv)))]
}

# > mean(Nile)
# [1] 919.35
# > sd(Nile)
# [1] 169.2275
# > var(Nile)
# [1] 28637.95
# > min(Nile)
# [1] 456
# > max(Nile)
# [1] 1370
# > median(Nile)
# [1] 893.5
# > mad(Nile)
# [1] 179.3946
# > getmode(Nile)
# [1] 1160
# > skewness(Nile)
# [1] 0.3223697
# > kurtosis(Nile)
# [1] 2.695093


