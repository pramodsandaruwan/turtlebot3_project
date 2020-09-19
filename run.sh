echo "Turtlebot simulation"
#source $HOME/pramod/turtlebot_ws/devil/setup.bash
export TURTLEBOT3_MODEL=waffle_pi
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map1.yaml
