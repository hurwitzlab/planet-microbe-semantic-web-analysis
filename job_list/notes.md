# Background

Generally filter fractionation is as follows:

```
viruses < 0.22 um

bacteria 0.22 - 2 um

eukaryotes > 2 um
```

# Datasets taken

## Amazon Plume Metagenomes

Has filter sizes 2 - 156 um, and 0.2 - 2 um, taking the latter as the prokaryotic fraction.


Applied `Aquatic Sample Minimum Filter Fractionation Size Threshold ` from `0.2 - max` and `Aquatic Sample Maximum Filter Fractionation Size Threshold` from `min - 2` to get 24 samples with 40 files.

## Amazon River Metagenomes

Has filter sizes 2 - 297 um, and 0.2 - 2 um, taking the latter as the prokaryotic fraction.

Applied `Aquatic Sample Minimum Filter Fractionation Size Threshold ` from `0.2 - max` and `Aquatic Sample Maximum Filter Fractionation Size Threshold` from `min - 2` to get 24 samples with 38 files.


## BATS Chisholm

https://www.ncbi.nlm.nih.gov/bioproject/385855 unclear if these samples are from the prokaryotic fraction. Add them for now but this needs to be double checked, removed if we can't determine it.  

## GOS

Has filter sizes 0.1 - 0.8, 0.8 - 3, and 3 - 20 um, taking the 0.1 - 0.8um and 0.8 - 3um fractions

Applied `Aquatic Sample Minimum Filter Fractionation Size Threshold ` from `min - 3` and `Aquatic Sample Maximum Filter Fractionation Size Threshold` from `min - 3` to get 51 samples with 53 files.


## HOT ALOHA time/depth series

Has filter sizes 0.02 - 0.2um (274 samples) and 0.2 - 1.6um (272 samples), taking the latter. Many samples are missing maxium filter values, but only taking those with a Minimum filter value we have 274 samples. My understanding is that there are only those two filter fractions (0.02 - 0.2 and 0.2 - 1.6um) thus taking only min 0.2 will get the prokaryotic fraction.

Applied `Aquatic Sample Minimum Filter Fractionation Size Threshold ` from `0.2 - max` to get 274 samples with 559 files.

Retrieving from the Planet Microbe database, sample `SAMN05991650` was listed twice with the same file `SRR5002342.fastq.gz` so the duplicate was removed.


## HOT Chisholm

Samples don't have maximum filter values, but it has minimum filter values.

Applied `Aquatic Sample Minimum Filter Fractionation Size Threshold ` from `0.2 - max` to get 68 samples with 135 files.


## HOT DeLong

all 42 samples are 0.22 - 1.6um.

Applied `Aquatic Sample Minimum Filter Fractionation Size Threshold ` from `min - 0.22` and `Aquatic Sample Maximum Filter Fractionation Size Threshold` from `1.6 - max` to get 42 samples with 44 files.

## HOT DeLong Metatranscriptomes

only 8 samples, all have filter min 0.22 and the rest are split half and half with filter max between 1.6 and 125um. Taking only the 0.22 - 1.6um fraction and only the metagenomic samples.

Applied `Aquatic Sample Minimum Filter Fractionation Size Threshold ` from `min - 0.22` and `Aquatic Sample Maximum Filter Fractionation Size Threshold` from `min - 2` to get 4 samples with 20 files.

Furthur refined this down to only 7 WGS METAGENOMIC files


## OSD

OSD's minimum filtration was conducted through a 0.22um filter by default, (there was no viral fraction), all 162 samples have minimum filter values of 0.22um. Only four OSD samples have maximum filter values, two of which are 3um and the others are 100um.

In order to filter the few samples with the larger filter fraction, we applied `Aquatic Sample Maximum Filter Fractionation Size Threshold` from `4 - max` to get the 2 samples with 12 files, which need to be removed from the list of files derived from the selection of all OSD files. There are a total of 162 samples and 934 files.

Removing the WGS METAGENOMIC files: ERR770974_1.fastq.gz, ERR770974_2.fastq.gz, ERR770973_1.fastq.gz, ERR770973_2.fastq.gz, as well as all files of `strategy` `AMPLICON`, a total of 295 files remained.  

## Tara Oceans

From the Tara paper they describe their filter fraction sizes as:

```
1) girus/prokaryote-enriched fractions (0.1 to 0.22 μm, 0.22 to 0.45 μm, 0.45 to 0.8 μm)

2) prokaryote-enriched fractions (0.22 to 1.6 μm, 0.22 to 3 μm)
```

Confirming in planet microbe database by filter min 0.2-3 and filter max 0.02 -3 gives 327 samples. with fractions:

```
0.1-0.22, 0.22-0.45, 0.22-1.6, 0.22-3, 0.45-0.8, 0.8-3, 0.8-(0.8,200) (need to remove these), and 0.8-0.8 (need to remove these too)
```

### Taking filter fractions one at a time:

**0.1-0.22**

Applied `Aquatic Sample Minimum Filter Fractionation Size Threshold ` from `0.1 - max` and `Aquatic Sample Maximum Filter Fractionation Size Threshold` from `min - 0.22` to get 26 samples with 59 files.

**0.22-0.45**

Applied `Aquatic Sample Minimum Filter Fractionation Size Threshold ` from `0.2 - 0.22` and `Aquatic Sample Maximum Filter Fractionation Size Threshold` from `min - 0.5` to get 18 samples with 52 files.

**0.22-1.6**

Applied `Aquatic Sample Minimum Filter Fractionation Size Threshold ` from `0 - 0.23` and `Aquatic Sample Maximum Filter Fractionation Size Threshold` from `1 - 2` to get 52 samples with 188 files.

**0.22-3**

Applied `Aquatic Sample Minimum Filter Fractionation Size Threshold ` from `0 - 0.23` and `Aquatic Sample Maximum Filter Fractionation Size Threshold` from `2 - 4` to get 104 samples with 440 files.

**0.45-0.8**

Applied `Aquatic Sample Minimum Filter Fractionation Size Threshold ` from `0.4 - 0.5` and `Aquatic Sample Maximum Filter Fractionation Size Threshold` from `0.7 - 0.9` to get 21 samples with 53 files.

**0.8-3**

Applied `Aquatic Sample Minimum Filter Fractionation Size Threshold ` from `0.7 - 0.9` and `Aquatic Sample Maximum Filter Fractionation Size Threshold` from `2 - 4` to get 31 samples with 202 files.

Finally we removed all `METAGENOMIC	AMPLICON` and `METATRANSCRIPTOMIC	RNA-Seq` files, 708 files remained.

## Stats

In total there are `937` unique WGS METAGENOMIC samples corresponding to `2002` files. Most are paired end sequencing, although some have three corresponding read files, the rest have layout single.
