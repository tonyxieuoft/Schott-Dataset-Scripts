import sys

# ================================= SUMMARY ===================================
# The shell script calls on this python file to filter for species of interest 
# within a given alignment. Don't call this script alone, unless you are 
# extracting from a single alignment. 
# ============================= USAGE/ARGUMENTS ===============================
# python3 extract_species.py ALIGNMENT_FILENAME SPECIES_OF_INTEREST_FILENAME
# ================================= OUTPUT ====================================
# Prints out the name and sequences for the species of interest in fasta format. 
# The shell script redirects the output into other files.

# the position (by words) of the scientific name in the fasta heading. CAN BE MODIFIED TO ACCOMODATE OTHER FORMATS
NAME_POSITION = 0 # the "0th" position (the first "word" in the fasta heading)


# opens the file containing the alignments
f = open(sys.argv[1], "r")

# opens the file containing the list of species to extract
species_file = open(sys.argv[2], "r")

# stores the names of the species to extract in a list. Time complexity to find a species in a list of size n is O(n) 
# which isn't great, and if many more species need to be extracted, I can implement a hashmap for this instead. 
species_of_interest = []
species = species_file.readline()
while (species != ""):
	species_of_interest.append(species.strip().upper())
	species = species_file.readline()

# starts reading through the file
line = f.readline()
found = 0

# iterates until the end of the file is reached
while (line != ""):

	line = line.strip()

	# "even" line numbers (if the first line is the 0th line) are names, whereas odd line numbers correspond to
	# nucleotide sequences
	if line[0] == ">":

		# identifies the name of the current species
		# THIS PART OF THE CODE CAN BE MODIFIED TO ACCOMODATE THE NAME FORMATTING OF OTHER DATASETS
		split_line = line.split("_")
		likely_species_name = (split_line[NAME_POSITION][1:] + " " + split_line[NAME_POSITION + 1]).upper()

		# if the current species is in the list of "species' of interest"
		if likely_species_name in species_of_interest:
			print(line)
			found = 1

		# these statements account for exceptions, such as the fact that Gekko gecko is sometimes referred to as just "Gekko", etc. 
		# from the dataset itself, it's a little difficult to tell when a name ends (since accessions can mimick their format)
		elif likely_species_name.split()[NAME_POSITION] == "GEKKO" and likely_species_name.split()[NAME_POSITION + 1] != "JAPONICUS":
			print(line)
			found = 1

		elif likely_species_name.split()[NAME_POSITION] == "THAMNOPHIS" and likely_species_name.split()[NAME_POSITION + 1] != "PROXIMUS":
			print(line)
			found = 1

		elif likely_species_name.split()[NAME_POSITION] == "PYTHON" and likely_species_name.split()[NAME_POSITION + 1] != "REGIUS":
			print(line)
			found = 1

		else:
			found = 0


	# prints out the alignment if it's for a "species of interest"
	else:
		if found == 1:
			print(line)

	line = f.readline()




