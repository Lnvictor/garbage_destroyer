#!/bin/zsh
pip3 install virtualenv
virtualenv $PWD/venv
chmod -r 777 $PWD/venv
source $PWD/venv/bin/activate    
pip install APScheduler==3.9.1 click

ln -s $PWD/garbage_destroyer/cli.py $PWD/gds
chmod +x /Users/victorpereira/Downloads/garbage_destroyer