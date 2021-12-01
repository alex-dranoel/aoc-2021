val <- read.csv('input.txt', header = FALSE)$V1
cat('Part 1:', sum(diff(val) > 0))
n <- length(val)
cat('Part 2:', sum(diff(val[1:(n-2)] + val[2:(n-1)] + val[3:n]) > 0))
