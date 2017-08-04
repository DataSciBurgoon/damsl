echo "Remember that you need to run the SplitSMI runner.runner Scala script first"
echo "That script takes a tab-delimited file with SMILES\tchemical names"
echo "And here we go!"
echo $PATH
python3 parse_smi.py
obabel *.smi -opdb --gen3d -h -m
for i in *.pdb; do
	/Library/MGLTools/1.5.6/bin/pythonsh ~/Documents/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_ligand4.py -l "$i" -A 'hydrogens' -B 'amide' -F
done
for f in *.pdbqt; do
    b=`basename $f .pdbqt`
    echo Processing ligand $b
    vina --config vina_conf.txt --ligand $f --out ${b}_docked.pdbqt --log ${b}_log.txt
done
