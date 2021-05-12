Name:Rakshitaa Geetha Mohan

Move.py

This python script makes the turtle (simulator) move in a circle. The linear and angular velocities used are 2 and 1.5 respectively. 
Screenshot: /home/rakshitaagm/git_ws/AuE893Spring20_RakshitaaGM/catkin_ws/move.png

Square.py

This python script makes the turtle (simulator) move in a square. It basically moves in a straight line and makes a turn 4 times.
The straightline and turn function were called four times to achieve this. It first checks whether the distance is less than 2 and if 
it so, it moves in a straightline with a linear velocity of 0.2 for sometime until the while condition (which checks whether the 
distance travelled is less than 2) is satisfied and then it takes a turn of 90 degrees which has another while loop to give it a limit.

Screenshot:/home/rakshitaagm/git_ws/AuE893Spring20_RakshitaaGM/catkin_ws/square.png

Square_closedloop.py

This python script makes the turtle (simulator) move in a square but it keeps on checking whether the control is able to achieve this target
using a PID controller. This was implemented using two while loops which checks separately whether the displacement and angular orientation is within
the required limits. Inside the while loop (for both angular orientation and dsiplacement) a velocity is assigned with a gain multiplied to it. The  current angle difference as well as the 
displacement gets updated before the end of the loop. If the while condition is satisfied the control moves to the next task.

Screenshot:/home/rakshitaagm/git_ws/AuE893Spring20_RakshitaaGM/catkin_ws/square_Closedloop.png


