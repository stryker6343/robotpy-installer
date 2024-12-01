"""
    << Title and Description of the Robot Application >>
"""

import inspect

import wpilib


# The timed robot scheduler will call the methods of this class both periodically
# and during transitions between the four robot modes. The four robot modes are
# disabled, autonomous, teleop and test. For each mode, the class provides an
# init method, a periodic method and an exit method. Also, the class provides robot
# methods that are called regardless of robot mode.
class MyRobot(wpilib.TimedRobot):
    """
        A Timed Robot Template
    """

    def robotInit(self):
        """
        This method is called upon program startup and should be used for any
        initialization code.  The Driver Station Robot Code light will turn green
        when this method exits.
        """
        # Display the object doc string in the Driver Station console
        print(inspect.getdoc(self))

    def autonomousInit(self):
        """This method is run once each time the robot enters autonomous mode."""
        pass

    def autonomousPeriodic(self):
        """This method is called periodically during autonomous."""
        pass

    def teleopPeriodic(self):
        """This method is called periodically during operator control."""
        pass

    # This method is included here to suppress warnings on the Driver Station console
    def disabledPeriodic(self):
        """This method is called periodically while the robot is disabled."""
        pass

    # This method is included here to suppress warnings on the Driver Station console
    def robotPeriodic(self):
        """This method is called periodically regardless of robot mode."""
        pass


if __name__ == "__main__":
    wpilib.run(MyRobot)
