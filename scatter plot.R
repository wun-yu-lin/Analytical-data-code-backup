> TIC_SVR <- Nor$QC02
> SVR <- NO_nor$QC02
> plot(TIC_SVR,SVR)
> cor(TIC_SVR,SVR)
[1] 0.9917404
> cor.test(TIC_SVR,SVR)

Pearson's product-moment correlation

data:  TIC_SVR and SVR
t = 558.43, df = 5216, p-value < 2.2e-16
alternative hypothesis: true correlation is not equal to 0
95 percent confidence interval:
 0.9912817 0.9921751
sample estimates:
      cor 
0.9917404 
> plot(TIC_SVR,SVR)
> abline(lm(SVR~TIC_SVR),col(red))
>legend("topleft",legend = c("r=0.9917404","p-value=<2.2e-16","sample = QC2"))

register(bpstart(SnowParam(6)))