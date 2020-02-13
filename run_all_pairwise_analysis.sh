SPECIES=GUT_GENOME000067

GENOMES_DIR=$SPECIES
PAIRS_IN=input_all_pairs.tsv

OUTPUT_DIR=$SPECIES"_ALL_PAIRS"

while IFS= read -r pair
do
    genome1=$(echo $pair | cut -d' ' -f1)
    genome2=$(echo $pair | cut -d' ' -f2)

    GB_PATH_1=$GENOMES_DIR/$genome1.fna
    GB_PATH_2=$GENOMES_DIR/$genome2.fna


    nucmer $GENOMES_DIR/$genome1.fna $GENOMES_DIR/$genome2.fna --prefix $OUTPUT_DIR/$genome1-$genome2 --threads 1
    delta-filter -q -r $OUTPUT_DIR/$genome1-$genome2.delta > $OUTPUT_DIR/$genome1-$genome2.filter.delta
    show-coords $OUTPUT_DIR/$genome1-$genome2.filter.delta > $OUTPUT_DIR/$genome1-$genome2.coords
    show-snps $OUTPUT_DIR/$genome1-$genome2.filter.delta > $OUTPUT_DIR/$genome1-$genome2.snps
    show-diff $OUTPUT_DIR/$genome1-$genome2.filter.delta > $OUTPUT_DIR/$genome1-$genome2.diff

	echo "done whole genome alignment for $genome1 and $genome2"
done < $PAIRS_IN

find $OUTPUT_DIR/ -name '*.snps' | xargs -I[] bash -c 'sed "1,5d" [] | awk "$0" | wc -l | awk "$1" OFS="\t"' '$2 != "." && $3 != "." {printf "%s\t%s||%s||%s||%s\n", "[]", $14, $1, $2, $3}' '{print "[]", $1}' | cut -d'/' -f2 > $SPECIES.snp_count.tsv

find $OUTPUT_DIR/ -name '*.coords' | xargs -I[] bash -c 'awk "$0" "$1"' 'BEGIN{OFS="\t";total_len=0;total_sim=0}; NR > 5 {total_len = total_len + $7; total_sim=total_sim+$7*$10}; END {split(FILENAME,a,"/");pair_name=a[2];print pair_name, total_len, total_sim, total_sim/total_len};' '[]' > $SPECIES.align_stats.tsv
