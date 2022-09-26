export PYTHONPATH=""
# shellcheck disable=SC2068
if [ -z "$PYTHONPATH" ]; then
        export PYTHONPATH="src:$PYTHONPATH"
        export PYTHONPATH="src/libs:$PYTHONPATH"
        export PYTHONPATH="src\libs:$PYTHONPATH"
        echo "SET PYTHONPATH LIB - OK"
        echo "$PYTHONPATH"
fi
# shellcheck disable=SC2068
python src/server.py $@
$SHELL