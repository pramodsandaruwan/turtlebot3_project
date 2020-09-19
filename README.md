# turtlebot3 project

#### Create project workspace
``` bash
sudo apt update
rosdep update
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
cp -b $HOME/turtlebot3_project/src/turtlebot3_project/run.sh $HOME/turtlebot3_project/
cd ~/turtlebot3_ws/
./run
```
#### Contact / Info

**pramod sandaruwan** | [Email](mailto:pramodsandaruwan80@gmail.com) | [Github](https://www.github.com/pramodsandaruwan) |
