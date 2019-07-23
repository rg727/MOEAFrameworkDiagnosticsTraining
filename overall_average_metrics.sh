echo "$0 $@" >> history.txt
source settings.sh

for PROBLEM in ${PROBLEMS[@]}
do
  for ALGORITHM in ${ALGORITHMS[@]}
  do
    for SAMPLE in ${SAMPLES[@]}
    do
     java ${JAVA_ARGS}  org.moeaframework.analysis.sensitivity.SimpleStatistics --mode average --output ./overall_average_metrics/${ALGORITHM}_${PROBLEM}.average ./data_metrics_new/${ALGORITHM}_${PROBLEM}_*.txt

    done
  done
done

