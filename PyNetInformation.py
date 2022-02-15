import sys
import time
from networktables import NetworkTables

# To see messages from networktables, you must setup logging
class NetTable:
    def __init__(self):
        NetworkTables.initialize(server="10.35.02.2")
        self.robo_state = NetworkTables.getTable("State")
        time.sleep(3)
        self.x_pos = self.robo_state.getAutoUpdateValue("x_pos", 0)
        self.y_pos = self.robo_state.getAutoUpdateValue("y_pos", 0)
        self.heading = self.robo_state.getAutoUpdateValue("heading", 0)

    def getPosVal(self):
        return [self.x_pos, self.y_pos]

    def getHeadingVal(self):
        return self.heading
