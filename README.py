You Tube Search Client.

Essentially this will search for X pages of resaults.  Using the image previes name as a key it then downloads the icons, embedding the track info into the image while in ram using python pil library.  You then have the choice to download or stream using youtube-dl mpv or vlc.  The image downloading and batch conversion is multithreaded. Should be cross platform.

ToDo: make coin-noise on dl-complete


Example:  python tubless.py justin beiber
