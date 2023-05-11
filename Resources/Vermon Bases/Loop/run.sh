#!/bin/bash
python3 configure_common.py experiments/general/network.json
python3 configure_experiment_variables.py

cd experiments/general/
sudo python3 genpcaps.py

cd ..
cd ..

sudo make run
sudo make stop
