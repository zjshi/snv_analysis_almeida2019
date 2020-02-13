# About this repo  
This repository hosts the code for SNV analysis performed in this paper:  
[A unified sequence catalogue of over 280,000 genomes obtained from the human gut microbiome](https://www.biorxiv.org/content/10.1101/762682v1)  
  
Please consider cite this paper if you find this repository helpful:  
> A unified sequence catalogue of over 280,000 genomes obtained from the human gut microbiome  
>
> Alexandre Almeida, Stephen Nayfach, Miguel Boland, Francesco Strozzi, Martin Beracochea, Zhou Jason Shi, Katherine S. Pollard, Donovan H. Parks, Philip Hugenholtz, Nicola Segata, Nikos C. Kyrpides, Robert D. Finn  
>
> bioRxiv 762682; doi: https://doi.org/10.1101/762682  

## Running the code for SNV analysis requires the following dependencies intalled in local environment:  
* Python  
* numpy  
* MUMmer4  

## What's included:  

### Directory containing input genomes:  
* GUT_GENOME000067/  

### Direcotry hosting intermediate files for pairwise SNV analysis and creating SNV catalogue:  
* GUT_GENOME000067_ALL_PAIRS/  
* GUT_GENOME000067_CATALOG/  

### Description:  
* README  

### Genome metadata:  
* genomes_metadata.tsv  

### A Python script responsible for binning SNVs based on source information, e.g. continent origin:  
* bin_snps_by_source.py  

### A Python script for generating SNV catalogue from whole genome alignments:  
* generate_catalog.py  

### A Python script for separating reference alleles from missing sites:  
* identify_ref_allele.py  

### Two files containing genome pairs used for generating SNV catalogue and pairwise SNV analysis:  
* input_catalog_pairs.tsv  
* input_all_pairs.tsv  

### Two all-in-one scripts for pairwise SNV analysis and producing SNV catalogue:  
* run_all_pairwise_analysis.sh  
* run_all_snv_catalog.sh  

## Tutorial for using the code:  
### Generate SNV catalog:  
`bash run_all_snv_catalog.sh`  

### Output files:  
#### SNV catalog file:  
* GUT_GENOME000067.catalog.noAuto.wtRef.tsv  
#### SNV binned based on continent origin:  
* GUT_GENOME000067.continentBin.tsv  

### Generate pairwise SNV profile:  
`bash run_all_pairwise_analysis.sh`  

### Output files:  
#### Pairwise alignment summary:  
* GUT_GENOME000067.align_stats.tsv  
#### Pairwise SNP count:  
* GUT_GENOME000067.snp_count.tsv  
