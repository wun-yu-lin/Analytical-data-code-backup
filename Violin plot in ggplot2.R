##Violin plot in ggplot2
#http://www.sthda.com/english/wiki/ggplot2-violin-plot-quick-start-guide-r-software-and-data-visualization
library(ggplot2)
#SCan mode comparison

p = ggplot(RSD_table, aes(x=Mode, y=RSD, color=Mode,fill=Mode))+ 
      geom_violin()

p+scale_color_manual(values=c("sienna4", "deeppink4","green4" ))+
      ylim(c(0,200))+
      scale_fill_manual(values=c("sienna4", "deeppink4","green4" ))+
      labs(y = "RSD (%)", x = " ")+
      scale_x_discrete(limits=c("Full scan", "DIA","DDA" ))+
      theme_set(theme_bw())
      

ggsave("RSD_violin_plot.tiff",device = "tiff",dpi = 1200,width = 5, height = 3)






##Methods comparison
p = ggplot(RSD_table, aes(x=Methods, y=RSD, color=Methods,fill=Methods))+ geom_violin()
p+scale_color_manual(values=c("deeppink4","seagreen3", "green4" ,"sienna4"))+
           ylim(c(0,200))+
           scale_fill_manual(values=c("deeppink4","seagreen3", "green4" ,"sienna4"))+
           labs(y = "RSD %", x = " ")+
           scale_x_discrete(limits=c("Total","Mean","Median", "SVR"))+theme_set(theme_bw())
ggsave("Methods_RSD_violin_plot.tiff",device = "tiff",dpi = 1200,width = 6, height = 4)
