#!/bin/bash

gnome-terminal --working-directory=$(pwd) --title="Central Server" --geometry=100x24 --zoom=1.1 \
 -- bash -c "source venv/bin/activate; PORT=8001 python3 src/server.py && sleep 5"
sleep 2
gnome-terminal --working-directory=$(pwd) --title="Client" --geometry=100x24 --zoom=1.1 \
 -- bash -c "source venv/bin/activate; PORT=8001 python3 src/client.py && sleep 5"

