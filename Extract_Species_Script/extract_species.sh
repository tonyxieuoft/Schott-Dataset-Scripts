#! /usr/bin/sh

# ========================================= SUMMARY ===========================================
# This script takes in alignment data from the Schott datasets. It pulls data for species' of interest
# and outputs it into a another folder.
# ======================================== ARGUMENTS ==========================================
# FOLDER: the name of the folder containing the alignment data. This should be the original folder containing
# all of the data after it has just been downloaded and unzipped (the alignemnts subfolder must also be unzipped).
# SPECIES_NAMES: the name of the file containing the list of species of interest
# ========================================== USAGE ===========================================
# ./extract_species.sh FOLDER SPECIES_NAMES
# for mine, the location of my alignments folder was "2019_visual_genes/Alignments/Alignments" and the species file was 
# named "species_file.txt", so I called the script via: 
# "./extract_species.sh 2019_visual_genes/Alignments/Alignments species_file.txt"
# ================================== ADDITIONAL REQUIREMENTS =================================
# The script depends on the python files "is_sp_file.py" and "extract_species.py"
# ========================================= OUTPUT ===========================================
# A new folder containg the extracted alignments, titled "Extracted Alignments" 

folder_location=$1
species_file=$2


# creates a new folder of the alignments with reduced depth (less subfolders) if one hasn't already been created
if test -d Alignments_Schott
then
	# if Alignments_Schott already exists, no need to create a new one
	:
else
	# if not, make the Alignments_Schott folder by copying the alignments from the specified location
	cp -r $folder_location Alignments_Schott
fi

# if a folder named Extracted_Alignments already exists, delete it (to prevent duplication issues
rm -r Extracted_Alignments 2> /dev/null
# makes a new folder called Extracted_Alignments to store extracted alignments for species of interest
mkdir Extracted_Alignments

cd Alignments_Schott

# iterates through every file in Alignments_Schott
for file in *
do
	# the dataset contained two datasets for every gene. One of them included all species and was titled
	# "sp", while the other omitted snakes and was titled "no_snake". THis part of the code filters for the 
	# former. 
	if python3 ../is_sp_file.py "$file"
	then
		# extracts the species' of interest into a new folder titled Extracted_Alignments
		python3 ../extract_species.py "$file" "../${species_file}"  > ../Extracted_Alignments/$file
	fi

done
