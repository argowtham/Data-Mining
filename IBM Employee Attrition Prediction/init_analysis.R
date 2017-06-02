# Initial Analysis of the data set

# Setting the path of the file
path = "D:/Datasets/IBM Attrition"
filename = "WA_Fn-UseC_-HR-Employee-Attrition.csv"
ibm = read.csv(paste(path, filename, sep = "/"), header = T)

# Finding the dimensions of the data
n = nrow(ibm)
d = ncol(ibm)
feat_names = colnames(ibm)

# Testing the distribution of the numerical features
num_density_plot <- function(dat, name){
  m = mean(dat)
  s = sd(dat)
  title =  paste("Plot of", name, "vs Normal distribution", sep = " ")
  den = density(dat)
  plot(den, ylim = c(min(den$y), max(den$y)), main = title)
  lines(density(rnorm(n, m, s)), col = 2)
  legend("topright", legend = c("actual", "normal"), col = c(1, 2), lty = 1)
}

# Finding the numerical features

# Age plot
num_density_plot(ibm$ï..Age, "Age")
# From the plot, we could see that distribution of age approximately
# follows normal distribution

# Daily Rate plot
num_density_plot(ibm$DailyRate, "Daily Rate")


