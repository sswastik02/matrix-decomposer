#!/bin/bash

gnome-terminal --working-directory=$(pwd) --title="DNS" --geometry=100x24 --zoom=1.1 \
 -- bash -c "source env/bin/activate; python3 src/dns.py && sleep 5"
sleep 1
gnome-terminal --working-directory=$(pwd) --title="L_Worker" --geometry=100x24 --zoom=1.1 \
 -- bash -c "source env/bin/activate; PORT=8001 python3 src/l_worker.py && sleep 5"
sleep 1
gnome-terminal --working-directory=$(pwd) --title="U_Worker" --geometry=100x24 --zoom=1.1 \
 -- bash -c "source env/bin/activate; PORT=8002 python3 src/u_worker.py && sleep 5"
sleep 1
gnome-terminal --working-directory=$(pwd) --title="Central Server" --geometry=100x24 --zoom=1.1 \
 -- bash -c "source env/bin/activate; PORT=8003 python3 src/server.py && sleep 5"
sleep 1
gnome-terminal --working-directory=$(pwd) --title="Client" --geometry=100x24 --zoom=1.1 \
 -- bash -c "source env/bin/activate; PORT=8003 python3 src/client.py && sleep 2"

