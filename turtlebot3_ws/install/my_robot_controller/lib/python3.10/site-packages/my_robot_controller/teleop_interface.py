import curses
import sys
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TeleopInterface(Node):
    def __init__(self, stdscr):
        super().__init__('teleop_interface')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.stdscr = stdscr
        self.init_screen()

    def init_screen(self):
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(True)
        self.stdscr.clear()
        self.stdscr.refresh()

    def run(self):
        while rclpy.ok():
            key = self.stdscr.getkey()
            if key == 'q':
                break
            elif key == 'w':
                self.send_velocity_command(0.5, 0.0)  # Forward
            elif key == 's':
                self.send_velocity_command(-0.5, 0.0)  # Backward
            elif key == 'a':
                self.send_velocity_command(0.0, 0.5)  # Left
            elif key == 'd':
                self.send_velocity_command(0.0, -0.5)  # Right
            self.stdscr.addstr(0, 0, f"Tecla pressionada: {key}   ")
            self.stdscr.refresh()

    def send_velocity_command(self, linear, angular):
        msg = Twist()
        msg.linear.x = linear
        msg.angular.z = angular
        self.publisher_.publish(msg)

def main():
    rclpy.init()
    stdscr = curses.initscr()
    teleop_interface = TeleopInterface(stdscr)
    teleop_interface.run()
    curses.endwin()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
