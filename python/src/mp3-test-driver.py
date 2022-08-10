import arcade


class Mp3Driver(arcade.Window):
    def __init__(self):
        super().__init__(300, 200, "mp3 test")
        self.mpset1: list = None
        self.mpset2: list = None
        self.curset: list = None

    def setup(self):
        #self.laser_sound = arcade.load_sound("laser.wav")
        eat      = arcade.load_sound("../sound/eat.wav")
        music    = arcade.load_sound("../sound/music.wav")
        bathroom = arcade.load_sound("../sound/bathroom.wav")
        car      = arcade.load_sound("../sound/car.wav")
        more     = arcade.load_sound("../sound/more.wav")
        alldone  = arcade.load_sound("../sound/all-done.wav")

        top    = arcade.load_sound("../sound/top.wav")
        middle = arcade.load_sound("../sound/middle.wav")        
        bottom = arcade.load_sound("../sound/bottom.wav")
        play   = arcade.load_sound("../sound/play.wav")        
        go     = arcade.load_sound("../sound/go.wav")
        stop   = arcade.load_sound("../sound/stop.wav")

        self.mpset1 = [ eat, music, bathroom, car, more, alldone ]
        self.mpset2 = [ top, middle, bottom, play, go, stop ]
        self.curset = self.mpset1
        
    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            if self.curset == self.mpset1:
                self.curset = self.mpset2
            else:
                self.curset = self.mpset1
                
        elif key == arcade.key.A:
            arcade.play_sound( self.curset[0] )
        elif key == arcade.key.S:
            arcade.play_sound( self.curset[1] )
        elif key == arcade.key.D:
            arcade.play_sound( self.curset[2] )
        elif key == arcade.key.F:
            arcade.play_sound( self.curset[3] )
        elif key == arcade.key.G:
            arcade.play_sound( self.curset[4] )
        elif key == arcade.key.H:
            arcade.play_sound( self.curset[5] )
            

        
        
def main():
    mp3test = Mp3Driver()
    mp3test.setup()


    arcade.run()


if __name__ == '__main__':
    main()
