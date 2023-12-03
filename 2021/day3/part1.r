dataset <- do.call(rbind, lapply(
    strsplit(scan("day3\\input.txt", what = ""), ""), as.numeric
))

data_size <- length(dataset[1, ])

gamma_rate <- 0

for (i in 1:data_size) {
    col <- dataset[, i]

    count_0 <- length(col[col == 0])
    count_1 <- length(col[col == 1])

    if (count_0 > count_1) {
        cat("higher rate: 0\n")
        gamma_rate <- gamma_rate * 2
    } else {
        cat("higher rate: 1\n")
        gamma_rate <- gamma_rate * 2 + 1
    }
}

epsilon_rate <- bitwXor(gamma_rate, ((2**data_size) - 1))

cat(paste(
    "gamma rate: ", gamma_rate, "\n",
    "epsilon rate: ", epsilon_rate, "\n",
    sep = ""))
cat(paste("final answer: ", gamma_rate * epsilon_rate, sep = ""))
