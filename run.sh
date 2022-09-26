export PYTHONPATH=""
# shellcheck disable=SC2068
if [ -z "$PYTHONPATH" ]; then
        export PYTHONPATH="srwc:$PYTHONPATH"
        echo "SET PYTHONPATH LIB - OK"
fi
echo "$PYTHONPATH"
# shellcheck disable=SC2068
python src/server.py $@
$SHELL