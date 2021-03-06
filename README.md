
# miRacle
### A repository for some scripts and tools that I wrote during my M.S thesis/dissertation work in the genomics domain.
#### **EDIT : CNN-based image classifier for further automation coming soon with substantially large pre-trained Keras model (trained on 5 plant datasets) along with the source code.  

---
### Table of Contents

1. [What is this about and will it suit my workflow?](#what-is-this-about-and-will-it-suit-my-workflow)
2. [Prerequisites](#prerequisites)
3. [Instructions](#instructions)
---
#### What is this about and will it suit my workflow?
 This is a script that sort of automates the process of fetching BLAST hits along with their flanking region for creating precursor microRNA sequences. 

Furthermore, it will fold the precursor sequences into secondary RNA structures using mfold and allow the users to highlight the bases to their own liking using the VARNA applet. (intended for highlighting miRNA and miRNA* in the 2<sup>o</sup> structure.

This script can be a workaround for batch-processing highlighting mfold structures as the standalone mfold does not have a highlight feature similar to it's web-server.

Due to the batch-process nature of this program, it offers little to no interaction and the files that have to be supplied need to be in a very particular format that is required by the program. However, if you need to tweak the program, you most certainly can due to it's relatively small length and not-so-complex nature.

> *Note : This workflow has been designed for short microRNA sequences. If you wish to use this script to fetch other nucleotide sequences just for the flanking regions, you most certainly can.* 

---
#### Prerequisites

1. A Linux system.
2. Python version 3.x.x.
3. [pyfaidx](https://pythonhosted.org/pyfaidx/#installation)
4. BLAST results.
5. [mfold](http://unafold.rna.albany.edu/?q=mfold/download-mfold) (preferably v. 3.6)
6. [VARNA binaries.](http://varna.lri.fr/index.php?lang=en&page=downloads&css=varna) (Visualization Applet for RNA)
7. Tons of patience and a lot of sleep.

> *Note : This program has been tested on Ubuntu 16.x and 18.04 with 64-bit architecture. You __will__ need to install the 'pyfaidx' package for Python 3 and **not** Python 2.* 

---
#### Instructions
#### Part One
1. Take a deep breath.

2. After installing the appropriate prerequisites, move the "**flanking_updated_vx.py**" Python script to your work folder.

3. Create **3 files separately** with each containing your **sequence accession** (subject or reference), **start coordinates** and **end coordinates** respectively from your BLAST results spreadsheet/table.

4. Name the files accordingly as mentioned in the script. (Note: Files as command line parameters will be added soon)
> **The file containing the Gene Accession list from the BLAST results (Subject/Genome) has to be named 'gene.txt'.**

> **The file containing the Start Coordinates list from the BLAST results (Subject/Genome) has to be named 'start.txt'.** 

>**The file containing the End Coordinates list from the BLAST results (Subject/Genome) has to be named 'end.txt'.** 

>*(if you have errors with the naming due to Windows/Linux encoding/line-ending you can name the file according to your own choice and change the filename from the code)*  

5. Run the script with 
`python3 flanking_updated_v2.py`
6. Set the appropriate flank length for your sequences.
7. *Don't* grab a coffee because this is *not* going to take a while. It's rather quick.
#### Part Two
_Now that we have a gazillion ".fasta" files, we will process them for fold and highlight._
1. Move all the ".fasta" precursors to a new folder to avoid the clutter.

2. Move the "**fold_and_highlight.py**" Python script to the aforementioned new folder along with the "**remover.sh**" and the "**motif_start**", "**motif_end**" files. (The 'motif_start' and 'motif_end' files contain the start and end coordinates of the miRNA motifs that have to be highlighted.

3. Now move the VARNAx.jar applet binary to the folder.

4. Execute the script using `python3 fold_and_highlight_v2.py`.

5. This is **definitely** going to take a while. Go grab that coffee.
---
##### TLDR
> **(What goes in)** 3 files containing gene accessions, start coordinates and end coordinates respectively and a ".fasta" reference file.

> **(What comes out)** _Multiple_ ".fasta" files containing precursors (as mfold does NOT allow multi-fasta files) + file containing motif start coordinates + file containing motif end coordinates. (relevant for further folding and highlighting)

#### TODO
**Learn to write better documentation, update the terrible documentation, tweak the code for better performance, fix terrible variable names.**


> Written with [StackEdit](https://stackedit.io/).
