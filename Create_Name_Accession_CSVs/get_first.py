import sys
import re

# ================================ SUMMARY =============================
# Very, very simple. Gets the gene name for a file through regex


gene_name = re.split(r"_|\s", sys.argv[1])[0]

print(gene_name)



