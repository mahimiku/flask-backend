processId=$(ps -aef | grep -i flask | grep -v 'grep' | awk '{ printf $2 }')
kill -9 $processId
source bin/activate
export LC_ALL=en_US.utf-8
export LANG=en_US.utf-8
nohup flask run --host=0.0.0.0 &