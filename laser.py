import time
import random
from enum import Enum

class Laser:
    class Status(Enum):
        OFF = 0
        ON = 1       

    def __init__(self):
        self._status : Laser.Status = Laser.Status.OFF

    def setBiasVoltage(self, voltage : float) -> bool:
        """
        sets the bias voltage of the laser (that's not actually a thing, this is just a simulation)
        """
        if self._status != Laser.Status.ON:
            print("cannot set bias voltage when laser is off")
            return False

        print(f"setting bias voltage to: {voltage:.2f} V")
        return True

    def getStatus(self) -> "Laser.Status":
        return self._status

    def enableLaser(self) -> bool:
        """
        enable the laser (simulated) - this command may fail randomly
        enabling is only possible when the laser is not on already
        """
        print(f"enabling laser...")
        if self._status == Laser.Status.ON:
            print("laser already on")
            return False

        time.sleep(1)
        success = random.randint(0, 10) != 6
        if not success:
            print("enabling laser failed!")

        else:
            self._status = Laser.Status.ON
            print("enabling laser succeeded")

        return success

    def disableLaser(self) -> None:
        self._status = Laser.Status.OFF
        print("disabling laser")
        time.sleep(0.1)