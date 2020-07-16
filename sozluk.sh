menu() {
printf '\e[8;35;120t'

case $SHELL in
	*bash)
		ECHO='echo -e'
		;;
	*)
		ECHO='echo'
		;;
esac

purple="\033[0;35m"
pink="\033[38;5;198m"
green="\033[1;32m"
white="\033[97m"
blue="\033[1;34m"

clear; ${ECHO} ""
${ECHO} "$purple "
${ECHO} "   		     ████████ ██   ██ ██████  ██   ██  ██████ ██████    "
${ECHO} "   			██            ██   ██ ██  ██  ██      ██            "
${ECHO} "   			██    ██   ██ ██████  █████   ██      █████         "
${ECHO} "   			██    ██   ██ ██   ██ ██  ██   ██████ ██            "
${ECHO} "   			██    ███████ ██   ██ ██   ██    ██   ██████        "

${ECHO} ""
${ECHO} "	               ██████  ██  ██  ██████ ██    ██   ██ ██   ██                "
${ECHO} "	               ██                  █  ██            ██  ██                 "
${ECHO} "	               ██████ ████████   ██   ██    ██   ██ ████                   "
${ECHO} "	                   ██ ██    ██  █     ██    ██   ██ ██  ██                 "
${ECHO} "	               ██████ ████████ ██████ █████ ███████ ██   ██                "

${ECHO} ""
${ECHO} $green"                                                             Versiyon: "$pink"1.1\n"
sleep 0.1
${ECHO} $green"              Bilgiler, TDK'nin sitesinden alınmaktadır. ("$pink"https://sozluk.gov.tr"$green")"
sleep 0.1
${ECHO} $white "           	Eren "$blue"("$pink"erenbasulas"$blue")"$white" tarafından yapıldı ve geliştirildi"
sleep 0.1

${ECHO} ""

python_baslat
}

python_baslat() {
	printf "\n\n"
	python3 python/sozluk.py
}
menu