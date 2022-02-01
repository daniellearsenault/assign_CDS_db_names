if __name__ == '__main__':
    #note! script relies on the '>lcl|NC_008097.1_cds_YP....' format of the CDS annotation files downloaded from NCBI nucleotide
    # and on the '>gi|108773196|ref|NC_008097.1| Chara vulgaris chloroplast, complete genome' type format of the summary fasta files downloaded from NCBI nucleotide
    #TLDR; no pre-editing is needed to run this script: it is designed to be used with these 2 files in their raw NCBI nuc form :)
    
    #REPLACE filenames in lines 10, 13, and 16 with your filenames

    import re
    #with open('TEST_cds.txt', 'r') as cds_raw:
    with open('YOUR_raw_cds.txt', 'r') as cds_raw:
        cds = cds_raw.read()
    #with open('TEST_names.fasta', 'r') as names_raw:
    with open('YOUR_raw_names.fasta', 'r') as names_raw:
        names = names_raw.read()
   # output_file = open('TEST_cds_nuc_w_names.txt', 'w')
    output_file = open('YOUR_cds_w_names.txt', 'w')

#for each position in cds
    i = 0
    #don't write 'lcl's to output_file
    while i < len(cds):
        if i < (len(cds) - 3):
            if (cds[i:i+3])=='lcl':
                i += 3
        #replace spaces and commas w underscores
        if (cds[i]==' ') or (cds[i]==','):
            output_file.write('_')
            i+=1

        #to remove > and <'s from location coords:
        #accounts for ocassional '.>' in location coords
        #if i>0:
        #    if (cds[i-1:i]=='.>'):
        #        i+=1
        #accounts for ocassional '<' in location coords
        #if cds[i]=='<':
        #    i+=1

        if ((cds[i]) == '|'):
            #find next instance of _cds_
            cds_loc = (cds[i:].find('_cds_')) + i
            #get accession (acc)
            temp_acc = cds[(i+1):(cds_loc)]
            #find accession in names file
            names_index = names.find(temp_acc) + len(temp_acc)
            #establish name to be added
            gen_loc = (names[names_index:].find('genome')) + names_index
            temp_name = names[(names_index+1):(gen_loc)] + '_genome_'
            #replace spaces and commas in name with _
            name = ''
            j = 1
            while j<len(temp_name):
                if (temp_name[j]==' ') or (temp_name[j]==','):
                    name+='_'
                    j+=1
                else:
                    name+=(temp_name[j])
                    j+=1
            #add name to cds annotation, right before accession #
            output_file.write(name+'_')
            i += 1
        else:
            output_file.write(cds[i])
            i+=1
    output_file.close()
