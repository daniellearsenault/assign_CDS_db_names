# assign_CDS_db_names
Add organism names to CDS databanks downloaded from NCBI nucleotide

**1) Searching for genomes on NCBI Nucleotide:**
Example for how to return all complete genomes of certain organelles resricted to a taxonomic classification, using NCBI nucleotide:
(Chloroplast [Title] OR Plastid[Title]) AND complete[Title] AND genome[Title] AND refseq[filter] AND Chlorophyta[Organism] 
Returns all complete chloroplast and plastid genomes belonging to Chlorophyta restricting to refseq entries (you can mess around with these search criteria depending on your needs)

**2) Then obtaining raw Coding Sequences file:**
Once your search shows all the genomes that fit your criteria, use Send To>Coding Sequences>FASTA Nucleotide to get the raw CDS databank for all of these genomes (they are all downloaded together as 1 file)

**You may have noticed that, for whatever reason, the annotations on this file do not contain the organism name. Anywhere.**

If you'd like to remedy this you've come to the right script!

**3) Then obtaining raw file used to assign names (Complete Record FASTA):**
On that same NCBI nucleotide search results page, also use Send To>Complete Record>File>Format:FASTA>check Show GI to get the raw file we will use to assign organism names to the entries in the cds file.

**4) Then assigning organism names to your Coding Sequences file using the script:**
Save the 2 raw files and this Python script all in the same directory.
Set this directory as your working directory.
call with:
python assign_CDS_db_names.py

Use your CDS and Complete Record filenames when prompted by the script, and the output will be your CDS databnk with the respective organism names neatly added to the beginning of every entry. In addition, all spaces and commas will be replaced with underscores.
