green=`tput setaf 2`
reset=`tput sgr0`
echo "${green}Navigating...${reset}"
rosrun turtlebot3_navigation navigator.py
