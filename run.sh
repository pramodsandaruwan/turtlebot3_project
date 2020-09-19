
green=`tput setaf 2`
reset=`tput sgr0`

echo "${green}Turtlebot simulation...${reset}"

WS_PATH=$HOME/turtlebot3_project

source $WS_PATH/devel/setup.bash

export TURTLEBOT3_MODEL=waffle_pi

roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$WS_PATH/src/turtlebot3_project/map1.yaml
