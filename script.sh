#!/bin/bash

do_daemon_work() {
    while true; do
        python finance.py >> data.txt
        sleep 3600
    done
}

do_daemon_work & disown