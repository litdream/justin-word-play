import arcade


class Mp3Driver(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "mp3 test")
        self.mpset1: list = list()
        self.mpset2: list = list()

    def setup(self):
        pass


def main():
    mp3test = Mp3Driver()
    mp3test.setup()


    arcade.run()


if __name__ == '__main__':
    main()
