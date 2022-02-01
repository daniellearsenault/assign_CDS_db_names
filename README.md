# assign_CDS_db_names
Purpose: Add organism names to CDS databanks downloaded from NCBI nucleotide.

**1) Searching for genomes on NCBI Nucleotide:**
Example for how to return all complete genomes of certain organelles resricted to a taxonomic classification, using NCBI nucleotide:
(Chloroplast [Title] OR Plastid[Title]) AND complete[Title] AND genome[Title] AND refseq[filter] AND Chlorophyta[Organism] 
Returns all complete chloroplast and plastid genomes belonging to Chlorophyta restricting to refseq entries (you can mess around with these search criteria depending on your needs)

**2) Then obtaining raw Coding Sequences file:**
Once your search shows all the genomes that fit your criteria, use Send To>Coding Sequences>FASTA Nucleotide to get the raw CDS databank for all of these genomes (they are all downloaded together as 1 file)
<img width="1789" alt="get_raw_cds_file" src="https://user-images.githubusercontent.com/56440050/152056538-e2720075-6d9d-41ec-b8c3-7666adfe2c99.png">

**You may have noticed that, for whatever reason, the annotations on this file do not contain the organism name. Anywhere.**
<img width="1572" alt="no_names_in_raw_cds" src="https://user-images.githubusercontent.com/56440050/152056819-2df77f67-d5f7-4f96-ad57-a24b403f0c64.png">

If you'd like to remedy this you've come to the right script!

**3) Then obtaining raw file used to assign names (Complete Record FASTA):**
On that same NCBI nucleotide search results page, also use Send To>Complete Record>File>Format:FASTA>check Show GI to get the raw file we will use to assign organism names to the entries in the cds file.
<img width="1765" alt="get_raw_names_file" src="https://user-images.githubusercontent.com/56440050/152056854-1d157071-a900-4cb7-ba80-69547f5e8bdd.png">

**4) Then assigning organism names to your Coding Sequences file using the script:**
Save the 2 raw files and this Python script all in the same directory.
Set this directory as your working directory.
call with:
python assign_CDS_db_names.py

Use your CDS and Complete Record filenames when prompted by the script, and the output will be your CDS databnk with the respective organism names neatly added to the beginning of every entry. In addition, all spaces and commas will be replaced with underscores.
