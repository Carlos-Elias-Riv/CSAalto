# vamos a generar un vector de 100 valores con distribución normal

# quiero cambiar este vector de por 1: brown, 2: blue, 3: green

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