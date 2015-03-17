#!/bin/sh
# Daemon startup script
#

start(){
    export PYTHONDONTWRITEBYTECODE=True
    python main.py &
    echo " * Server started : $(date)"
}

stop(){
    PID=`ps -ef | grep '[p]ython main.py'\
                | head -1 \
                | awk '{ print $2 }'` 2>/dev/null
    kill -9 $PID 2>/dev/null
    if [ $? -eq 0 ]
        then 
            echo " * Server Killed : $(date)" 
    fi
    wait $PID 2>/dev/null
}

case "$1" in 
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        stop
        start
        ;;
    *)
        echo "Usage $0 {start|stop|restart}"
        exit 1
esac
exit 0
