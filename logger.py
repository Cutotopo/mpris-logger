#!/usr/bin/env python3

from time import sleep
import dbus
import json

# Type here the name of your player. To find it, run playertcl -l
# Example: playername="Lollypop"
playername = "<PLAYER NAME HERE>"


session_bus = dbus.SessionBus()

try:
    # snippet adapted from https://stackoverflow.com/questions/53362582/how-to-write-unit-tests-for-a-function-using-dbus-to-get-information-from-spotif
    mpris_bus = session_bus.get_object(f"org.mpris.MediaPlayer2.{playername}", "/org/mpris/MediaPlayer2")
    mpris_properties = dbus.Interface(mpris_bus, "org.freedesktop.DBus.Properties")
    metadata = mpris_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")
    print("MPRIS ready.")
    print("Waiting for a track to play. Press Ctrl+C to exit.")
    
    def attr(attr):
        if attr == 'artist':
            return metadata[f"xesam:{attr}"][0]
        else:
            return metadata[f"xesam:{attr}"]
    
    while True:
        prevtrackid = f"{attr('title')} ::::: {attr('artist')}".replace("'", "{CHAR.APOSTROPHE}")
        metadata = mpris_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")
        sleep(1)
        trackid = f"{attr('title')} ::::: {attr('artist')}".replace("'", "{CHAR.APOSTROPHE}")
        data = []
        
        if prevtrackid != trackid:
            trackname = f"\n=====\nTitle: {attr('title')}\nArtist: {attr('artist')}\nAlbum: {attr('album')}\n"
            try:
                current = open("history.json", "r")
                data = json.loads(current.read().replace("'", '"'))
                current.close()
            except FileNotFoundError:
                newfile = open("history.json", "w")
                newfile.write("{}")
                newfile.close()
                data = json.loads("{}")
            try:
                print(f"{trackname} Played {data[trackid] + 1} times")
                data[trackid] = int(data[trackid]) + 1
                file = open("history.json", "w")
                file.write(json.dumps(data))
                file.close()
            except:
                print(f"{trackname} It's the first time you play this!")
                data[trackid] = 1
                file = open("history.json", "w")
                file.write(json.dumps(data))
                file.close()
            print("=====\n")
except dbus.DBusException:
    print("Your player was not found. Please check the 'playername' variable at the beginning of logger.py.")
    exit(1)
