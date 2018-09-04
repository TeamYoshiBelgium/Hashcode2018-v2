#!/bin/bash
finish() {
    pkill python3 >/dev/null
    echo "test $i"
    if [ $init == 0 ] 
    then
        echo "test"
        # bash watch.sh $1
    fi
}
trap finish EXIT

if command -v inotifywait >/dev/null 2>&1 ; then
    i=1
    base=`basename "$PWD"`
    inotifywait -m -e CLOSE_WRITE ./*.py | while read line
    do
        pkill python3 >/dev/null
        sleep 0.01
        echo -n -e '\0033\0143'
        echo "CODE ITERATION $i"
        echo "================="
        echo ""

        rm "../$base.zip"
        zip "../$base.zip" ./* &>/dev/null
        python3 main.py $1 &
        i=$((i+1))
    done

else 

    echo ""
    tput setaf 1;
    echo "inotifywait not found, trying to install inotify-tools"
    tput sgr0;
    echo ""


    if command -v pacman >/dev/null 2>&1 ; then
        sudo pacman -S inotify-tools
    fi

    if command -v apt-get >/dev/null 2>&1 ; then
        sudo apt-get install inotify-tools
    fi

fi