# Schott Dataset Scripts

## The first script ("Extract_Species_Script")

### Purpose

The first script ("extract_species") extracts, for select species, alignment data from the Schott 2018 and 2019 visual transduction gene supplementary datasets. The script pulls for these eight species by default: 
- Taenopgyia guttata
- Struthio camelus australis
- Alligator mississippiensis
- Chrysemys picta
- Gekko gecko
- Anolis carolinensis
- Python molurus
- Thamnophis sirtalis
but allows for greater (or fewer) species to be pulled through user input.

### What each file does

`extract_species.sh` is the main script. It calls upon the scripts `is_sp_file.py` and `extract_species.py`. For each visual transduction gene, the Schott dataset contains two alignments, one containing all species investigated (denoted "sp") and the other omitting snakes (denoted "nosnake"). `is_sp_file.py` does the simple job of determining whether a given file is an "sp" file, while `extract_species.py` does the bulk of the work by extracting sequences for the species' of interest from a single alignment file. 

`species_file.txt` is the file specifying all species of interest to pull for. The file, by default contains the original 8 species, and can be expanded or reduced. As Gekko gecko was often referred to as only "Gekko" (with similar cases for Python molurus and Thamnophis sirtalis), `extract_species.py` contains additional code pulling specifically for these exceptions. If you do not wish for these to be pulled, omit lines from `extract_species.py`.

### Usage

Before calling the main scripts, make sure that all of the f











