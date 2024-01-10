#! /usr/bin/sh

# ======================================== SUMMARY ========================================
# Creates a CSV file containing species names and accessions for each alignment file in a 
# folder. Relies upon the python scripts "get_first.py" and "extract_name_accession.py".
# Outputs the results to a folder titled "Name_Accession_CSVs".
# ========================================= USAGE =========================================
# "./extract_name_accession.sh ALIGNMENT_FOLDER_NAME", where ALIGNMENT_FOLDER_NAME is the 
# name of the folder containing the alignment files, ie. "Extracted_Alignments".


folder_name=$1

# deletes the folder "Name_Accession_CSVs" if it already exists. prevents duplication when the new folder is created
rm -r Name_Accession_CSVs 2> /dev/null
# creates the new folder
mkdir Name_Accession_CSVs

cd $folder_name

# iterates through eery alignment file in the folder
for file in *
do
	# gets the gene name with "get_first.py"
	name=$(python3 ../get_first.py "$file")
	# "extract_name_accession.py" pulls out the species name and accession", and the output is redirected to the
	# Name_accession_CSVs folder after a CSV file is created for it
	python3 ../extract_name_accession.py "$file" 2> /dev/null > ../Name_Accession_CSVs/${name}.csv
done

