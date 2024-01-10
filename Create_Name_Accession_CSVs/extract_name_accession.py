

# ============================================ SUMMARY ==========================================
# For a given file, extracts the species names and accessions from the fasta headings of one
# alignment file and formats it in CSV. Assumes a fairly specific format following the Schott 
# dataset. Output is print statements, and requires the script to create the CSV files. 
# ============================================= USAGE ===========================================
# "python3 extract_name_accession.py file_name", where:
# file_name is the name of the alignment file


import sys
import re

# the column headings of each csv file
print("Name,Accession (or Comment)")

# opens the alignment file for reading
file = open(sys.argv[1], "r")

# the gene name is obtained by using regex to split the filename
gene = re.split(r"_|\s", sys.argv[1].strip())[0]


# reading the file
line = file.readline()
while line != "":

	if line[0] == ">": # if fasta heading, pull out name/accession

		# splits the fasta heading into "words", which are stored in the list split_line
		split_line = line.strip().split("_")

		# finds the position of the gene name (ex. finding that "ARR3" is the 3rd "word" in the heading)
		# position starts at 0
		gene_name_position = 0
		while gene_name_position < len(split_line) and split_line[gene_name_position] != gene:
			gene_name_position += 1

		# assuming that the species name is at the beginning of the heading (generalizable?), find the 
		# length of the name (range between 1 to 3)
		# relies on the fact that species is lowercase, while accessions aren't
		name_length = 1
		while split_line[name_length][0].islower():
			name_length += 1

		# creates a string corresponding to the species name. 
		# remember that the 0th index of the fasta heading is ">"; this is removed
		name = split_line[0][1:]
		for i in range(1,name_length):
			name = name + " " + split_line[i]


		# determines the accession
		accession = ""
		if gene_name_position == len(split_line) - 1: # if the gene name is at the end of the fasta heading


			if name_length == gene_name_position: # if the species name covers the rest of the heading, there is no accession
				accession = "N/A"

			else: # otherwise, the accession is sandwiched between the species name and gene name
				accession = split_line[name_length]
				for n in range(name_length+1, gene_name_position):
					accession = accession + " " + split_line[n]


		elif gene_name_position == len(split_line): # if the gene name doesn't exist, base the accession position on the name length

			if name_length == len(split_line):
				accession = "N/A"
			else:
				accession = split_line[name_length]
				for n in range(name_length + 1, len(split_line)):
					accession = accession + " " + split_line[n]

		else: # if the gene name is not at the end of the fasta heading (and instead in the middle somewhere, then accession will be after the gene name
			accession = split_line[gene_name_position + 1]
			for a in range(gene_name_position + 2,len(split_line)):
				accession = accession + " " + split_line[a]


		# for csv formatting
		print(name + "," + accession)

	# moves to the next line
	line = file.readline()
