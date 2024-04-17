from openal import oalOpen, AL_PLAYING, oalQuit
import time

# Load songs
songs = ["music/song.wav", "music/song1.wav", "music/song2.wav", "music/song3.wav"]

# Boolean variable to control music playback
musicOn = True

# Infinite loop to continuously play songs
while musicOn:
    # Play each song sequentially
    for song_path in songs:
        song = oalOpen(song_path)
        song.play()
        # Wait until the current song finishes playing
        while song.get_state() == AL_PLAYING:
            time.sleep(1)

# Release resources (this won't be reached in an infinite loop)
oalQuit()