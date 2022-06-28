# mpris-logger
Monitor MPRIS track changes for your player and save them to a json file to see which ones are the songs you listen to the most!

## Configuration
Type the name of your player as the value for the variable "playername" at the beginning of logger.py
You can get the name of your player with the command `playerctl -l`, which lists all your available players.
Most players need to be not only running but also playing media for the application to work.

## Requirements
 - A MPRIS-compatible music player
 - A Linux installation which supports MPRIS
 - Python 3.8+

## To do
 - [ ] Count tracks played with "repeat one track" (monitor song progress)
 - [ ] Log genres for music
 - [ ] Create a way to select the current player at program startup from a list
