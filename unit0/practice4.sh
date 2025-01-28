gunzip -c ../MCB185/data/A.thaliana.gff.gz | cut -f7 | sort | uniq -c

echo "transporter"
zless ../MCB185/data/GCF_000005845.2_ASM584v2_protein.faa.gz | grep -c "transporter"
echo "reductase"
zless ../MCB185/data/GCF_000005845.2_ASM584v2_protein.faa.gz | grep -c "reductase"

zless ../MCB185/data/jaspar2024_core.transfac.gz | grep "tax_group" | cut -d":" -f2 | sort | uniq -c