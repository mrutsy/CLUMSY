# shellcheck disable=SC2034
python_path=$(which python)
# shellcheck disable=SC1009
if [ $? -eq 0 ]
then
  # shellcheck disable=SC2068
  python src/server.py $@
  $SHELL
else
  echo "Устанавливаю питон"
fi

#echo python_version
# shellcheck disable=SC2068

#echo $?
#python src/server.py $@
#$SHELL




##echo "[RU] Очищаю PYTHONPATH."
##export PYTHONPATH=""
## shellcheck disable=SC2068
#echo "[RU] Проверка Pythonpath на наличие пути к библиотеке."
##[BY] Праверка Pythonpath на наяўнасць шляху да бібліятэкі.
##[CN] 检查Pythonpath的库路径。
##[EN] Checking Pythonpath for the library path."
#if [ -z "$PYTHONPATH" ]; then
#  # shellcheck disable=SC2140
#  echo "[RU] Переменная PYTHONPATH не обнаружена или пустая. Добавляю путь к библиотеке ("src:"$PYTHONPATH"")."
#  export PYTHONPATH="src:$PYTHONPATH"
##        export PYTHONPATH="src/libs:$PYTHONPATH"
##        export PYTHONPATH="src\libs:$PYTHONPATH"
#  echo "[RU] Путь к библиотеке добавлен."
##  echo "$PYTHONPATH"
#fi
## shellcheck disable=SC2034
##version=$(awk -F "=" '/database_version/ {print $2}' parameters.ini)
#echo "[RU] Запускаю программу."
## shellcheck disable=SC2068
#python src/server.py $@
#$SHELL