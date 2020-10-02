green=`tput setaf 2`
reset=`tput sgr0`
echo "${green}Navigating...${reset}"

WS_PATH=$HOME/turtlebot3_ws

source $WS_PATH/devel/setup.bash

 > myfile.txt 

echo "$1" >> myfile.txt

rosrun turtlebot3_navigation navigator.py
