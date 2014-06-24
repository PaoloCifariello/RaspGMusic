#!/bin/bash

echo "Checking Python"
case "$(python --version 2>&1)" in
    *" 3."*)
        ;;
    *" 2.7"*)
        ;;
    *)
		echo "Installing Python"
		sudo apt-get install python
		;;	
esac

echo "Checking pip"
pip_path=`which pip`
if [ "$pip_path" == "" ]; then
	echo "Installing pip"
	sudo apt-get install python-pip
fi

echo "Installing required packages"
sudo pip install dataset gmusicapi Jinja2 > /dev/null
