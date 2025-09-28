# config.sh
# Estos directorios debe estar definidos en el home
CONDA_DIR="/anaconda3/envs/networks/bin"
RESULTADOS_DIR="/Documents/POSGRADO/UEAS/TRIM_3/Proyecto/Simulador/Resultados"

# Las contantes de EXPERIMENTO y RED definen 
# los nombres de las carpetas de los resultados
#--------FORMACION-------------
ROUTING="CR"   # Algoritmo de encaminamiento: "CR", "RW", "SP"
REGLA="1"        # 1,2,3
CICLOS="5"
declare -a ARR=("D" "D2" "D4")
#--------RED-------------------
RED="malla8x8"  #anillo
#--------DEGRADACION-----------
DEGRADACION="Fallas" # "Ataques" / "Fallas"
FILE_DEGRADATION="failureDegradation.py" # "failureDegradation.py" "hubDegradation.py"
