import arcade
import logging
logging.basicConfig(level=logging.INFO)

DEAD_ZONE = 0.05

## Joystick Button order,  Weird!!
#
#  3 4 6 5
#  1 2 x x
#


class JoystickTest(arcade.Window):
    def __init__(self):
        super().__init__(300,200, "joystick test")
        all_joystick = arcade.get_joysticks()
        if all_joystick:
            self.joystick = all_joystick[0]
            self.joystick.open()
            self.joystick.push_handlers(self)   # need this line to handle joystick events
            
    def setup(self):
        pass

    def on_joybutton_press(self, _joystick, button):
        logging.info("Button {} down".format(button))

    def on_joyhat_motion(self, _joystick, hat_x, hat_y):
        logging.info("Hat ({}, {})".format(hat_x, hat_y))

    def on_update(self, delta_time):
        if self.joystick:
            if abs(self.joystick.x) < DEAD_ZONE and abs(self.joystick.y) < DEAD_ZONE:
                pass
            else:
                logging.info(f"x: {self.joystick.x} , y: {self.joystick.y}")

def main():
    """ Main function """
    window = JoystickTest()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
        
