ALGORITHMS=( NSGAII NSGAIII Borg MOEAD RVEA  )
NSAMPLES=20
NSEEDS=5
PROBLEMS=( lake )

USEPBS=true
SAMPLES=( $(seq 1 ${NSAMPLES}) )
SEEDS=( $(seq 1 ${NSEEDS}) )
JAVA_ARGS="-cp \"$(echo lib/*.jar | tr ' ' ':'):.\" -Xmx512m"
WALLTIME=256:00:00

while [[ $# > 0 ]]
do
  key="$1"

  case $key in
    -s|--seed)
      if [[ $2 =~ .*\-.* ]]
      then
        SEEDS=$(eval echo {${2//-/..}})
      else
        SEEDS=( $2 )
      fi
      shift
      ;;
    -a|--algorithm)
      ALGORITHMS=( $2 )
      shift
      ;;
    -b|--problem)
      PROBLEMS=( $2 )
      shift
      ;;
    -t|--test)
      TEST=echo
      ;;
    *)
      echo "Unknown option $1"
      ;;
  esac
  shift
done

declare -A EPSILON_MAP
EPSILON_MAP["lake"]=0.01,0.01,0.0001,0.0001


declare -A MAXNFE_MAP

MAXNFE_MAP["lake"]=100000
