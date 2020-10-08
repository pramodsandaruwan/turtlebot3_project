green=`tput setaf 2`
red=`tput setaf 1`
reset=`tput sgr0`

# Should not run this script as sudo.
if [ "$EUID" = 0 ]; then
    echo "${red}Please run this script as a non-root user.${reset}"
    exit
fi

echo "${red}Turtlebot3 project by pramod sandaruwan${reset}"
echo "${green}Please type 'yes' and press enter to continue...${reset}"

while true; do
    read -p "Do you accept the license terms of all of the components which are going to be installed? " yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done

echo "${green}Updating system ...${reset}"

sudo apt update
rosdep update

# Environment setup - optional. Do not run if multiple versions of ROS are present.
source /opt/ros/$ROS_DISTRO/setup.bash
echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> $HOME/.bashrc
source ~/.bashrc

echo "${green}Creating workspace ...${reset}"
# Create catkin workspace directory.
CATKIN_WS=$HOME/turtlebot3_ws
if [ ! -d "$CATKIN_WS" ]; then
    echo "${green}Creating catkin workspace in $CATKIN_WS...${reset}"
    mkdir -p $CATKIN_WS/src
    cd $CATKIN_WS
fi

echo "${green}Starting installation of turtlebot3 ROS packages...${reset}"
cd $CATKIN_WS/src
if [ ! -d "$CATKIN_WS/src/turtlebot3_project" ]; then
    echo "Cloning turtlebot3_project sources..."
    git clone https://github.com/pramodsandaruwan/turtlebot3_project.git
else
    echo "Updating turtlebot3_project sources..."
    cd turtlebot3_ws
    git checkout master
    git pull
fi

cd $CATKIN_WS
echo "Building turtlebot3_project packages..."
rosdep install --from-paths $CATKIN_WS/src --ignore-src
catkin_make

# Environment setup.
echo "source $CATKIN_WS/devel/setup.bash" >> $HOME/.bashrc
source $CATKIN_WS/devel/setup.bash
cp -b $CATKIN_WS/src/turtlebot3_project/run.sh $CATKIN_WS/
cp -b $CATKIN_WS/src/turtlebot3_project/move.sh $CATKIN_WS/

echo "${green}All done.${reset}"



