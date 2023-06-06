from Bio import Entrez
from Bio import SeqIO
Entrez.email='youremail'
# # Download a seq using GI number (id)
handle=Entrez.efetch(db='nuccore',id=34577062)
print(handle.read())
# # Download a seq (fasta) using GI number (id)
handle=Entrez.efetch(db='nuccore',id='34577062',rettype='fasta')
print(handle.read())
# # Download a seq using accession number (id)
handle=Entrez.efetch(db='nucleotide', id='NM_001126.2',rettype='gb',retmode='txt')
print(handle.read())
# Download and explore a sequence using fasta
handle=Entrez.efetch(db='nucleotide', id='NM_001126.2',rettype='fasta', retmode='txt')
record=SeqIO.read(handle,'fasta')
print(record.id)
print(record.name)
print(record.description)
seq=record.seq
print(seq[0:10])
print(len(seq))
#or
print(record)
print(seq)
# Download and explore a sequence using gene bank (gb)
handle=Entrez.efetch(db='nucleotide', id='NM_001126.2',rettype='gb', retmode='txt')
record=SeqIO.read(handle,'gb')
print(record.id)
features=record.features
print(features)
print(len(features))
seq=record.seq
print(len(seq))
# Download multiple genomes
handle=Entrez.efetch(db='nuccore',id='34577062,186972394',rettype='fasta')
print(handle.read())
# Explore multiple genomes
handle=Entrez.efetch(db='nuccore',id='34577062,186972394',rettype='fasta')
records=SeqIO.parse(handle,'fasta')
records=[i for i in records]
print(len(records))
print(records)
first_record=records[0]
second_record=records[1]
print(first_record.id)
print(second_record.id)
#Download and save genomes to an output file
handle=Entrez.efetch(db='nucleotide', id='34577062', rettype='gb')
record=SeqIO.read(handle,'gb')
outputname='D:/python/ADSS.gb'
SeqIO.write(record,outputname,'gb')
#Download and save genomes to an output fasta file
handle=Entrez.efetch(db='nucleotide', id='34577062', rettype='fasta')
record=SeqIO.read(handle,'fasta')
outputname='D:/python/ADSS.fasta'
SeqIO.write(record,outputname,'fasta')
#Output type is multi-fasta
handle=Entrez.efetch(db='nucleotide', id='34577062, 186972394', rettype='fasta')
record=SeqIO.parse(handle,'fasta')
outputname='D:/python/ADSS_matK.fasta'
SeqIO.write(record,outputname,'fasta')
