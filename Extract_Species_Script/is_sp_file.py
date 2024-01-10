import sys
import re

# ============================== SUMMARY =================================
# Called on by the extract_species shell script. Not useful when called by itself.
# Helps filter out "nosnake" files


filename = sys.argv[1].strip()

# splits the name of the alignment file into chunks delimited by "_", "." or whitespace
split_name = re.split(r"[_.\s]", filename)

# returns 0 iff the file is not a "nosnake" file
if split_name[2] != "nosnake":
	sys.exit(0)
else:
	sys.exit(1)

