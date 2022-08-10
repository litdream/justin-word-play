import arcade
import logging
logging.basicConfig(level=logging.INFO)

DEAD_ZONE = 0.9

class JustinWordPad(arcade.Window):
    def __init__(self):
        super().__init__(300, 200, "Justin Words!")
        self.mpset1: list = None
        self.mpset2: list = None
        self.curset: list = None

        all_joystick = arcade.get_joysticks()
        logging.info(f"All Joysticks: {all_joystick}")
        if all_joystick:
            self.joystick = all_joystick[0]
            self.joystick.open()
            self.joystick.push_handlers(self)   # need this line to handle joystick events

        self.change_set = 0
        
    def setup(self):
        prv1 = arcade.load_sound("../sound/preview-1-eat.wav")
        eat      = arcade.load_sound("../sound/eat.wav")
        music    = arcade.load_sound("../sound/music.wav")
        bathroom = arcade.load_sound("../sound/bathroom.wav")
        car      = arcade.load_sound("../sound/car.wav")
        more     = arcade.load_sound("../sound/more.wav")
        alldone  = arcade.load_sound("../sound/all-done.wav")

        prv2 = arcade.load_sound("../sound/preview-2-top.wav")
        top    = arcade.load_sound("../sound/top.wav")
        middle = arcade.load_sound("../sound/middle.wav")        
        bottom = arcade.load_sound("../sound/bottom.wav")
        play   = arcade.load_sound("../sound/play.wav")        
        go     = arcade.load_sound("../sound/go.wav")
        stop   = arcade.load_sound("../sound/stop.wav")

        self.mpset1 = [ prv1, more, alldone,  eat, music, car,  bathroom ]
        self.mpset2 = [ prv2, go, stop, top, middle, play, bottom ]
        self.curset = self.mpset1
        
    def on_joybutton_press(self, _joystick, button):
        logging.info("Button {} down".format(button))
        arcade.play_sound( self.curset[ button ] )

    def on_joyhat_motion(self, _joystick, hat_x, hat_y):
        logging.info("Hat ({}, {})".format(hat_x, hat_y))

    def on_update(self, delta_time):
        if self.joystick:
            if self.joystick.x > DEAD_ZONE:
                if self.change_set == 0:
                    logging.info("Changing to new set +")
                    self.curset = self.mpset1
                    arcade.play_sound( self.curset[0] )
                self.change_set = 1
            elif self.joystick.x < -DEAD_ZONE:
                if self.change_set == 0:
                    logging.info("Changing to new set -")
                    self.curset = self.mpset2
                    arcade.play_sound( self.curset[0] )
                self.change_set = -1
            else:
                self.change_set = 0

                
def main():
    """ Main function """
    window = JustinWordPad()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
