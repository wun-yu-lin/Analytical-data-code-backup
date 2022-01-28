if (!requireNamespace("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

BiocManager::install("xcms")
library(xcms)
library(RColorBrewer)
library(pander)
library(magrittr)
library(pheatmap)
library(SummarizedExperiment)
setwd("/Users/frankliu/Desktop/microsclerotia_metabolomic")
nCores <- parallel::detectCores()
file <- dir("convert",full.name = TRUE, pattern = "mzXML$")
pd <- data.frame(sample_name = sub(basename(file), pattern = ".mzXML",
                                   replacement = "", fixed = TRUE),
                 sample_group = c(rep("blank", 3), rep("MS1", 3)),
                 class=c(rep("blank", 3), rep("MS1", 3)),stringsAsFactors
                 = FALSE)
raw_data <- readMSData(files = file, pdata = new("NAnnotatedDataFrame", pd),
                       mode = "onDisk")
head(raw_data)
phenoData(raw_data)
head(rtime(raw_data))
mzs <- mz(raw_data)
mzs_by_file <- split(mzs, f = fromFile(raw_data))
length(mzs_by_file)
bpis <- chromatogram(raw_data, aggregationFun = "max")
group_colors <- paste0(brewer.pal(3, "Set1")[1:2], "60")
names(group_colors) <- c("blank", "MS1")
plot(bpis,col=group_colors[raw_data$sample_group])
tc <- split(tic(raw_data), f = fromFile(raw_data))
boxplot(tc, col = group_colors[raw_data$sample_group],
        ylab = "intensity", main = "Total ion current")
bpis_bin <- bin(bpis, binSize = 4)
cormat <- cor(log2(do.call(cbind, lapply(bpis_bin, intensity))))
colnames(cormat) <- rownames(cormat) <- raw_data$sample_name
ann <- data.frame(group = raw_data$sample_group)
rownames(ann) <- raw_data$sample_name
pheatmap(cormat, annotation = ann,
         annotation_color = list(group = group_colors))
cwp <- CentWaveParam(ppm = 20, snthresh = 5,verboseColumns=FALSE,peakwidth = c(10,60),noise=500,mzdiff = 0.05)
xdata<-findChromPeaks(raw_data,param = cwp)
head(chromPeaks(xdata))
chromPeakData(xdata)
mpp <- MergeNeighboringPeaksParam(expandRt = 30, expandMz = 0.05, ppm=20)
xdata_pp <- refineChromPeaks(xdata,param=mpp)
processedData <- adjustRtime(xdata_pp, param = ObiwarpParam())
bpis_adj <- chromatogram(processedData, aggregationFun = "max", include = "none")
plot(bpis_adj, col = group_colors[bpis_adj$sample_group])
plotAdjustedRtime(processedData, col = group_colors[xdata$sample_group])
pdp <- PeakDensityParam(sampleGroups = processedData$sample_group, minFraction = 0.1)
processedData <- groupChromPeaks(processedData, param = pdp) 
medWidth <- median(chromPeaks(processedData)[, "rtmax"] -
                     chromPeaks(processedData)[, "rtmin"])
processed_Data <- fillChromPeaks(
  processedData, param = FillChromPeaksParam(fixedRt = medWidth))

##用differreport只吃ms1data##
xset<-as(processed_Data,"xcmsSet")
getpeaktable<-peakTable(xset)
reporttab<-diffreport(xset,"blank","MS1")
###
source("https://raw.githubusercontent.com/jorainer/xcms-gnps-tools/master/customFunctions.R")
filteredMs2Spectra <- featureSpectra(processed_Data, return.type = "MSpectra")
filteredMs2Spectra <- clean(filteredMs2Spectra, all = TRUE)
filteredMs2Spectra <- formatSpectraForGNPS(filteredMs2Spectra)
writeMgfData(filteredMs2Spectra, "ms2spectra_all.mgf")
## get feature definitions and intensities
featuresDef <- featureDefinitions(processed_Data)
featuresIntensities <- featureValues(processed_Data, value = "into")
## generate data table
dataTable <- merge(featuresDef, featuresIntensities, by = 0, all = TRUE)
dataTable <- dataTable[, !(colnames(dataTable) %in% c("peakidx"))]
write.table(dataTable, "xcms_all.txt", sep = "\t", quote = FALSE, 
            row.names = FALSE)
###filtermaxtic
filteredMs2Spectra_maxTic <- combineSpectra(filteredMs2Spectra,
                                            fcol = "feature_id",
                                            method = maxTic)
writeMgfData(filteredMs2Spectra_maxTic, "ms2spectra_maxTic.mgf")
##
filteredDataTable <- dataTable[which(
  dataTable$Row.names %in% filteredMs2Spectra@elementMetadata$feature_id),]
write.table(filteredDataTable, "xcms_onlyMS2.txt", sep = "\t", quote = FALSE, row.names = FALSE)
