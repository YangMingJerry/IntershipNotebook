# Pyenv instruction
This note is an instruction for how to install pyenv for a Ubuntu OS

## Pyenv install

###1. install git:

    sudo apt install git

###2. install pyenv to ~/.pyenv

    git clone https://github.com/yyuu/pyenv.git ~/.pyenv

###3. configuration for bash

copy and paste the following lines to the bottom of .bashrc

    export PATH=~/.pyenv/bin:$PATH
    export PYENV_ROOT=~/.pyenv
    eval "$(pyenv init -)"

###4. source the bash profile and initialize the pyenv

    source .bashrc

## Python install

###1. install python dependency

    sudo apt-get install make build-essential libssl-dev zlib1g-dev
    sudo apt-get install libbz2-dev libreadline-dev libsqlite3-dev wget curl
    sudo apt-get install llvm libncurses5-dev libncursesw5-dev
    sudo apt-get update

###2. install python through pyenv

    pyenv install 3.7.0
    
refresh pyenv:

    pyenv rehash

###3. switch python versions by pyenv:

    　　1. pyenv global 3.7.0 #to change the global version
    　　2. pyenv local 3.7.0 #change local environment, rollback to global version after reboot
    　　3. pyenv shell 3.7.0 #change env for current terminal, rollback to global if you turn it off.

warning: be aware of using the pyenv global command might fuck up your entire ubuntu OS. Thats why venv is highly recommended.

###4. uninstall specific version

    pyenv uninstall 3.7.0

###5. commands to check python:

    which python

    python -V
    
    pyenv versions


## virtualenv (VENV)

###1. install venv if not 

    git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv

###2. bash configuration

add

    echo 'eval "$(pyenv virtualenv-init -)"'

to .bashrc

and 

    source ~/.bashrc


###3. create virtualenv named venv

    pyenv virtualenv 3.7.0 venv

###4. activate venv created

    pyenv activate venv

###5. deactivate venv

    pyenv deactivate 


