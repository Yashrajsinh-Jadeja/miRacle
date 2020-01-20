##ID 2
##This script will trigger the mfold and VARNA applications accordingly and generate secondary RNA structures that have the miRNA motif highlighted.
##THE REMOVER.SH bash script had to be created seperately because the Linux commands run in a subshell during the execution of this script and "shopt -s extglob" option does not work in this environment.
### DO NOT RUN THIS SCRIPT ANYWHERE BUT AN EXPERIMENTAL FOLDER AS IT WILL REMOVE ALL THE FILES EXCEPT FOR FEW.
##GNU General Public License v3.0
##Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license.
##Copyright and license notices must be preserved. Contributors provide an express grant of patent rights.
## 12 January 2020 Yashrajsinh Jadeja

import os
choice = int(input("Enter the total number of files to be processed."))  ##User input for the number of files to be processed.
choicex = int(input("Enter the number from which you wish to continue. (if you wish to start from the beginning enter 1) "))

start = [] ##Lists to read and store miRNA motif start/end coordinates that were generated during the execution of "flanking_updated_v2.py" script.
end = []

for x in open("motif_start"): ##Reading and storing miRNA motif start/end coordinates.
	start.append(x.replace("\n",""))

for x in open("motif_end"):
	end.append(x.replace("\n",""))

#os.system("echo why; shopt -s extglob") ##This does not work in a python instance.
err_log = open("errorlog.txt","w")
err_log.write("Errorlog containing accessions for problematic sequences.")

for x in range(choicex,choice+1):
	print(f"******************************* ITERATION # {x} *********************************")
	n = os.system(f'mfold SEQ"=prec{x}.fasta"') ##mfold command to create folds with default options.
	os.system("bash remover.sh") ##Script executed to remove redundancy and additional files generated by mfold to save storage space.
	#os.system('rm -v !(*.py|*.fasta|*coord|*.ct|*.EPS|*.jar') ##Does not work in this python instance. These are the contents of the "remover.sh" shell script.
	if n == 0:
		try:
			flag = 0
			file = open(f"new_prec{x}.ct","w")
			for seq in open(f"prec{x}.ct"):
				if (seq.find("dG") > -1):
					flag += 1
				if flag == 1:
					file.write(seq)
			file.close()
			os.system(f'java -cp VARNAv3-93.jar fr.orsay.lri.varna.applications.VARNAcmd -i new_prec{x}.ct -o prec{x}.EPS -highlightRegion "{start[x]}-{end[x]}:fill=#FF0000"') ##Command to highlight the ".ct" extension files according to the miRNA motif start/end coordinates.
		except:
			err_log.write(f"Corrupt CT : prec{x}.fasta")
			os.system(f"bash err_ct.sh prec{x}.ct new_prec{x}.ct new_prec{x}")
			os.system(f'java -cp VARNAv3-93.jar fr.orsay.lri.varna.applications.VARNAcmd -i new_prec{x}.ct -o prec{x}.EPS -highlightRegion "{start[x]}-{end[x]}:fill=#FF0000"')				
	else:
		err_log.write(f"mfold ERROR: prec{x}.fasta")

err_log.close()
print("*" * 13)
print("All Done!")
print("*" * 13)
