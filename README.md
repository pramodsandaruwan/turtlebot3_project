# turtlebot3 project

#### Clone the repository
``` bash
mkdir -p ~/turtlebot3_ws/src
cd ~/turtlebot3_ws/
catkin_make
```
#### Clone the repository
``` bash
cd ~/turtlebot3_ws/src
git clone https://github.com/pramodsandaruwan/turtlebot3_project.git
```
#### Installing
``` bash
cd ~/turtlebot3_ws
rosdep install --from-paths /path/to/your/turtlebot3_project/src --ignore-src
catkin_make
```
#### Exicuting the project
``` bash
export TURTLEBOT3_MODEL=waffle_pi
cd ~/turtlebot3_ws/src/turtlebot3_project
./run
```
