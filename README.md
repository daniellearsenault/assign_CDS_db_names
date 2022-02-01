# assign_CDS_db_names
Add organism names to to CDS databanks downloaded from NCBI nucleotide

Example for how to return all complete genomes of certain organelles resricted to a taxonomic classification, using NCBI nucleotide:
(Chloroplast [Title] OR Plastid[Title]) AND complete[Title] AND genome[Title] AND refseq[filter] AND Chlorophyta[Organism] 
Returns all complete chloroplast and plastid genomes belonging to Chlorophyta restricting to refseq entries (you can mess around with these search criteria depending on your needs)

Once your search shows all the genomes that fit your criteria, use Send To>Coding Sequences>FASTA Nucleotide to get the raw CDS databank for all of these genomes (they are all downloaded together as 1 file)

**You may have noticed that, for whatever reason, the annotations on this file do not contain the organism name. Anywhere.**

If you'd like to remedy this you've come to the right script!

On that same NCBI nucleotide search results page, also use Send To>Complete Record>File>Format:FASTA>check Show GI to get the raw file we will use to assign organism names to the entries in the cds file.

Use these 2 files as directed in the script, and the output will be your CDS databnk with the respective organism names neatly added to the beginning of every entry. In addition, all spaces and commas will be replaced with underscores.
