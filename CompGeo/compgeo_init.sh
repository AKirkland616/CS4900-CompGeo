# File:         compgeo_init.sh
# Author:       Jeremy Evans (Synthabit)
#
# Description:  This uses pip3 to initialize a Python virtual environment
#               and installs required dependencies in requirements.txt
#
# Usage:        Run the following in the CompGeo directory:
#               $ bash compgeo_init.sh

#!/bin/bash

python3 -m venv venv
source venv/bin/activate
pip3 install -r ./requirements.txt
