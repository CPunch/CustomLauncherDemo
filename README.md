# FFR-ReLauncher
A custom launcher for FusionFall Universe's Retro client. Based on version 1.0.5 of their launcher, this will send a fake MAC address getting past MAC bans (although i'm sure they also 
IP ban you so please don't be stupid with this.) This launcher can also exploit an oversight in the client's URL verification and launch a custom client if you're motivated to create one.

# Why?
Well, originally I was going to release this post without specifics, just the technical details, leaving out FFU and their Retro client. Then they banned me after I reached out about the issues with the client :(.

# Will this send my MAC?
Nope! As a side effect of this, if you were MAC banned you should be able to create a new account and use this launcher to launch the game.

# Why doesn't it update anything!!!!
I didn't bother adding support for that because I had already been banned, and this is still more of a POC than an actual usable script. If you want to add it, make a merge request!

# How do I make it launch a custom URL?
with the -client (URL)
e.g
'''bash
python3 main.py -client https://google.com/
'''

# I have an import error!!!
Make sure you pip install colorama and requests