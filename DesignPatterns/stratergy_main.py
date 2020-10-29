from strategy import LoudQuackStratergy
from strategy import GentleQuackStratergy
from strategy import OnForTenSecondStratergy

loud_quack = LoudQuackStratergy()
gentle_quack = GentleQuackStratergy()
ten_seconds = OnForTenSecondStratergy()

class Duck(object):
    def __init__(self, quack_stratergy, light_stratergy):
        self._quack_stratergy = quack_stratergy
        self._light_stratergy = light_stratergy
    def quack(self):
        self._quack_stratergy.quack()
    def lights_on(self):
        self._light_stratergy.lights_on()

class VillageDuck(Duck):
    def __init__(self):
        super(VillageDuck, self).__init__(loud_quack, None)

class RobotDuck(Duck):
    def __init__(self):
        super(RobotDuck, self).__init__(loud_quack, ten_seconds) # here learning is how to call parent __init__ from child

robo = RobotDuck()
robo.lights_on()
robo.quack()