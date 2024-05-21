from pygame import mixer as mix

mix.init()
def play_song(path):


    mix.music.load(path)
    mix.music.play()

mix.music.set_volume(1)

def controllor(inp):

    if inp == "stop":
        mix.music.stop()
    elif inp == "pause":
        mix.music.pause()
    elif inp == "play":
        mix.music.unpause
