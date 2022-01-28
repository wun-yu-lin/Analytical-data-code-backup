library(BiocParallel)
register(bpstart(SnowParam(6)))

限制單核使用
library(doParallel)
cores <- detectCores()
cores <- detectCores()
cl <- makeCluster(cores[1]-1)
registerDoParallel(cl)