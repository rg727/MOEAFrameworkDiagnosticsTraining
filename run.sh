echo "$0 $@" >> history.txt
source settings.sh
set -e
mkdir -p data_raw

for PROBLEM in ${PROBLEMS[@]}
do
  EPSILON=${EPSILON_MAP[$PROBLEM]}
  MAXNFE=${MAXNFE_MAP[$PROBLEM]}

  for ALGORITHM in ${ALGORITHMS[@]}
  do
    if [ "${ALGORITHM}" == "Borg" ]
    then
      PARAMETERS="-e ${EPSILON}"
# -x \"restartMode=3;probabilityMode=2\""
    elif [ "${ALGORITHM}" == "NSGAIII" ]
    then
      PARAMETERS="-x \"sbx.swap=false\""
    else
      PARAMETERS=""
    fi

    if [ "${ALGORITHM}" == "NSGAIII" ] || [ "${ALGORITHM}" == "RVEA" ]
    then
      PARAM_FILE="${ALGORITHM}_${PROBLEM}_Params.txt"
      SAMPLES_FILE="${ALGORITHM}_${PROBLEM}_Samples.txt"
    else
      PARAM_FILE="${ALGORITHM}_Params.txt"
      SAMPLES_FILE="${ALGORITHM}_Samples.txt"
    fi

    for SEED in ${SEEDS[@]}
    do
      if [ -z "$USEPBS" ]
      then
        ${TEST} rm -f data_raw/${ALGORITHM}_${PROBLEM}_S${SEED}_P*.data
        ${TEST} java ${JAVA_ARGS} org.moeaframework.analysis.sensitivity.DetailedEvaluator -p ${PARAM_FILE} -i ${SAMPLES_FILE} -b ${PROBLEM} -a ${ALGORITHM} -s ${SEED} -f 100 -x maxEvaluations=${MAXNFE} ${PARAMETERS} -o data_raw/${ALGORITHM}_${PROBLEM}_S${SEED}_P%d.data
      else
        if [ ! -t 1 ] && [ -z "${TEST}" ]
        then
          >&2 echo "Error: Use -t when piping output in USEPBS mode"
          exit -1
        fi

        NAME=RUN_${ALGORITHM}_${PROBLEM}_S${SEED}
        SCRIPT="\
#PBS -N ${NAME}\n\
#PBS -l nodes=1\n\
#PBS -l walltime=${WALLTIME}\n\
#PBS -o data_mpi/${NAME}.out\n\
#PBS -e data_mpi/${NAME}.err\n\
cd \$PBS_O_WORKDIR\n\
rm -f data_raw/${ALGORITHM}_${PROBLEM}_S${SEED}_P*.data\n\
java ${JAVA_ARGS} org.moeaframework.analysis.sensitivity.DetailedEvaluator -p ${PARAM_FILE} -i ${SAMPLES_FILE} -b ${PROBLEM} -a ${ALGORITHM} -f 100 -s ${SEED} -x maxEvaluations=${MAXNFE} ${PARAMETERS} -o data_raw/${ALGORITHM}_${PROBLEM}_S${SEED}_P%d.data"

        echo -e "$SCRIPT" > data_mpi/${NAME}.pbs
        ${TEST} qsub data_mpi/${NAME}.pbs
      fi
    done
  done
done

