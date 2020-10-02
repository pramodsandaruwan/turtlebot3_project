green=`tput setaf 2`
reset=`tput sgr0`

echo "${green}Navigating...${reset}"

WS_PATH=$HOME/turtlebot3_ws

source $WS_PATH/devel/setup.bash

 > $HOME/turtlebot3_ws/src/turtlebot3_project/myfile.txt 

echo "$1" >> $HOME/turtlebot3_ws/src/turtlebot3_project/myfile.txt

rosrun turtlebot3_navigation navigator.py
