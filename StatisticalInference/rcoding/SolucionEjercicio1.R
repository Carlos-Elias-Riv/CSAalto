
# a 100 normal values
x <- rnorm(100)

# sample mean
xhat <- mean(x)

sd(x)

# obtener the sample variance
val <- sum((x-xhat)**2)/(100 -1)

# tres vectores con media 1 y desviacion estándar 3 uno de tamaño 10, 100 y 1000

x10 <- rnorm(10, mean = 1, sd = 3)
x100 <- rnorm(100, mean = 1, sd = 3)
x1000 <- rnorm(1000, mean = 1, sd = 3)

# observar que se cumple la ley de los grandes números o también teorema central del límite

print(mean(x10))
print(mean(x100))
print(mean(x1000))

print(sd(x10))
print(sd(x100))
print(sd(x1000))

## tercer ejercicio

alturas <- c(184, 183, 179, 160, 193, 181, 160, 170, 160, 168, 180, 181, 178, 195, 167, 177)
# 1, brown
# 2, blue 
# 3, green
eyecolor <- c(1, 2, 1, 3, 3, 1, 3, 3, 3, 1, 1, 2, 1, 2, 1, 2)

strcolor <- c()

for (i in 1:length(eyecolor)) {
  if (eyecolor[i] == 1) {
    strcolor[i] <- "brown"
  } else if (eyecolor[i] == 2) {
    strcolor[i] <- "blue"
  } else if (eyecolor[i] == 3) {
    strcolor[i] <- "green"
  }
}

hist(eyecolor)
hist(alturas)
