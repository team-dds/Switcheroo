# Definitions.rpy

# This section defines stuff for DDLC and your mod!

# Use this as a starting point if you would like to override with your own.

define persistent.demo = False
define persistent.steam = ("steamapps" in config.basedir.lower())
# Change this to True to enable Developer Mode
define config.developer = False

python early:
    import singleton
    me = singleton.SingleInstance()

init python:
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []
    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    
    # Get's position of Music
    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0

    # Delete's All Saves
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)

    # Delete's Characters
    def delete_character(name):
        import os
        try: os.remove(config.basedir + "/characters/" + name + ".chr")
        except: pass

    # Restores Character's CHR
    def restore_all_characters():
        try: renpy.file("../characters/monika.chr")
        except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
        try: renpy.file("../characters/natsuki.chr")
        except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
        try: renpy.file("../characters/yuri.chr")
        except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
        try: renpy.file("../characters/sayori.chr")
        except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())
    
    # Restores Characters if their playthough matches current run.
    def restore_relevant_characters():
        restore_all_characters()
        if persistent.playthrough == 1 or persistent.playthrough == 2:
            delete_character("sayori")
        elif persistent.playthrough == 3:
            delete_character("sayori")
            delete_character("natsuki")
            delete_character("yuri")
        elif persistent.playthrough == 4:
            delete_character("monika")

    # Controls time.
    def pause(time=None):
        #global _windows_hidden
        if not time:
            #_windows_hidden = True
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            #_windows_hidden = False
            return
        if time <= 0: return
        #_windows_hidden = True
        renpy.pause(time)
        #_windows_hidden = False

# Music

# This section is where you can reference DDLC audio and add your own!
# audio. - tells Ren'Py this is sound
# t1 - tells Ren'Py the label of the music/sound file
# <loop 22.073> - tells Ren'Py to loop the song at that time interval
# "bgm/1.ogg" - location of your music
define audio.t1 = "<loop 7.613>mod_assets/audio/main_theme.mp3" #Title theme
define audio.t2 = "<loop 0.026 to 156.290>mod_assets/audio/ohayou_satori.mp3" #Ohayou Satori!
define audio.t2g = "bgm/2g.ogg" #Ohayou Satori! Wobbly Section
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg" #Ohayou Satori! Rapid Glitch
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg" #Ohayou Satori! Gradual Pitch Increase
define audio.t3 = "<loop 0.027 to 56.024>mod_assets/audio/in_game_main_theme.mp3"   #Main theme (in-game theme)
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg" 
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define audio.t4 = "<loop 57.630>mod_assets/audio/poem_game.mp3"  #Poemgame
define audio.t4g = "<loop 1.000>bgm/4g.ogg" #Static and Error
define audio.t5 = "<loop 7.444>mod_assets/audio/okay_everyone.mp3"   #Okay Everyone!

# Doki Poem Theme
define audio.tmateo = "<loop 4.444>bgm/5_monika.ogg" #Okay Everyone! (Mateo)
define audio.tsatori = "<loop 4.444>bgm/5_sayori.ogg" #Okay Everyone! (Satori)
define audio.tnatsuko = "<loop 4.444>bgm/5_natsuki.ogg" #Okay Everyone! (Natsuko)
define audio.tyuuri = "<loop 4.444>bgm/5_yuri.ogg" #Okay Everyone! (Yuuri)

define audio.t5b = "<loop 4.444>bgm/5.ogg"
define audio.t5c = "<loop 4.444>bgm/5.ogg"
define audio.t6 = "<loop 4.414>mod_assets/audio/play_with_me.mp3" #Play With Me
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<loop 3.898>mod_assets/audio/poem_panic.mp3" #Poem Panic!
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg"
define audio.t7g = "<loop 31.880>bgm/7g.ogg"
define audio.t8 = "<loop 8.324>mod_assets/audio/daijoubu.mp3" #Daijoubu
define audio.t9 = "<loop 3.172>bgm/9.ogg"   #My Feelings
define audio.t9g = "<loop 1.532>bgm/9g.ogg" #207% speed (My Feelings)
define audio.t10 = "<loop 5.861>bgm/10.ogg"   #Confession
define audio.t10y = "<loop 0>bgm/10-yuuri.ogg" #Yuri Confession
define audio.td = "<loop 36.782>bgm/d.ogg"

define audio.m1 = "<loop 0>bgm/m1.ogg" # Just Monika. - Just Monika.
define audio.mend = "<loop 6.424>bgm/monika-end.ogg" # I Still Love You - Monika Post-Delete Theme

define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"
define audio.hb = "<loop 0>bgm/heartbeat.ogg"

define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "mod_assets/audio/fall3.wav"
define audio.door_knock = "mod_assets/audio/door_knock.wav"


# Backgrounds
image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image splash = "bg/splash.png"
image end:
    truecenter
    "gui/end.png"
image bg residential_day = "bg/residential.png" # Start of DDLC BG
image bg class_day = "bg/class.png" # The classroom BG
image bg corridor = "bg/corridor.png" # The hallway BG
image bg club_day = "bg/club.png" # The club BG
image bg club_day2: # Glitched Club BG
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg/club-skill.png"
image bg closet = "bg/closet.png" # The closet BG
image bg bedroom = "bg/bedroom.png" # MC's Room BG
image bg sayori_bedroom = "bg/sayori_bedroom.png" # Sayori's Room BG
image bg house = "bg/house.png" # Sayori's House BG
image bg kitchen = "bg/kitchen.png" # MC's Kitchen BG

image bg notebook = "bg/notebook.png" # Poem Game Notebook Scene
image bg notebook-glitch = "bg/notebook-glitch.png" # Glitched Poem Game BG

image bg glitch = LiveTile("bg/glitch.jpg")

image bg club_desks = "mod_assets/images/bg/club_desks.png"
image bg Fmbedroom = "mod_assets/images/bg/femc_bedroom.png"

image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0



image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0

# Character Definitions

# This is where the characters bodies and faces are defined.
# They are defined by left half, right half and their head.

# Sayori's Definitions
image satori 1 = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/a.png")
image satori 1a = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/a.png")
image satori 1b = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/b.png")
image satori 1c = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/c.png")
image satori 1d = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/d.png")
image satori 1e = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/e.png")
image satori 1f = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/f.png")
image satori 1g = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/g.png")
image satori 1h = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/h.png")
image satori 1i = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/i.png")
image satori 1j = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/j.png")
image satori 1k = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/k.png")
image satori 1l = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/l.png")
image satori 1m = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/m.png")
image satori 1n = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/n.png")
image satori 1o = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/o.png")
image satori 1p = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/p.png")
image satori 1q = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/q.png")
image satori 1r = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/r.png")
image satori 1s = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/s.png")
image satori 1t = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/t.png")
image satori 1u = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/u.png")
image satori 1v = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/v.png")
image satori 1w = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/w.png")
image satori 1x = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/x.png")
image satori 1y = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/y.png")
image satori 1z = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/z.png")
image satori 1aa = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/aa.png")
image satori 1ab = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ab.png")
image satori 1ac = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ac.png")
image satori 1ad = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ad.png")
image satori 1ae = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ae.png")
image satori 1af = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/af.png")
image satori 1ag = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ag.png")
image satori 1ah = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ah.png")
image satori 1ai = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ai.png")
image satori 1aj = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/aj.png")
image satori 1ak = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ak.png")
image satori 1al = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/al.png")
image satori 1am = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/am.png")
image satori 1an = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/an.png")
image satori 1ao = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ao.png")
image satori 1ap = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ap.png")
image satori 1aq = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/aq.png")
image satori 1ar = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ar.png")

image satori 2 = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/a.png")
image satori 2a = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/a.png")
image satori 2b = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/b.png")
image satori 2c = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/c.png")
image satori 2d = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/d.png")
image satori 2e = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/e.png")
image satori 2f = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/f.png")
image satori 2g = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/g.png")
image satori 2h = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/h.png")
image satori 2i = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/i.png")
image satori 2j = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/j.png")
image satori 2k = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/k.png")
image satori 2l = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/l.png")
image satori 2m = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/m.png")
image satori 2n = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/n.png")
image satori 2o = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/o.png")
image satori 2p = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/p.png")
image satori 2q = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/q.png")
image satori 2r = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/r.png")
image satori 2s = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/s.png")
image satori 2t = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/t.png")
image satori 2u = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/u.png")
image satori 2v = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/v.png")
image satori 2w = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/w.png")
image satori 2x = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/x.png")
image satori 2y = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/y.png")
image satori 2z = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/z.png")
image satori 2aa = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/aa.png")
image satori 2ab = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ab.png")
image satori 2ac = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ac.png")
image satori 2ad = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ad.png")
image satori 2ae = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ae.png")
image satori 2af = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/af.png")
image satori 2ag = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ag.png")
image satori 2ah = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ah.png")
image satori 2ai = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ai.png")
image satori 2aj = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/aj.png")
image satori 2ak = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ak.png")
image satori 2al = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/al.png")
image satori 2am = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/am.png")
image satori 2an = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/an.png")
image satori 2ao = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ao.png")
image satori 2ap = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ap.png")
image satori 2aq = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/aq.png")
image satori 2ar = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ar.png")

image satori 3 = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/a.png")
image satori 3a = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/a.png")
image satori 3b = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/b.png")
image satori 3c = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/c.png")
image satori 3d = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/d.png")
image satori 3e = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/e.png")
image satori 3f = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/f.png")
image satori 3g = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/g.png")
image satori 3h = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/h.png")
image satori 3i = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/i.png")
image satori 3j = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/j.png")
image satori 3k = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/k.png")
image satori 3l = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/l.png")
image satori 3m = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/m.png")
image satori 3n = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/n.png")
image satori 3o = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/o.png")
image satori 3p = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/p.png")
image satori 3q = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/q.png")
image satori 3r = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/r.png")
image satori 3s = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/s.png")
image satori 3t = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/t.png")
image satori 3u = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/u.png")
image satori 3v = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/v.png")
image satori 3w = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/w.png")
image satori 3x = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/x.png")
image satori 3y = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/y.png")
image satori 3z = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/z.png")
image satori 3aa = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/aa.png")
image satori 3ab = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ab.png")
image satori 3ac = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ac.png")
image satori 3ad = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ad.png")
image satori 3ae = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ae.png")
image satori 3af = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/af.png")
image satori 3ag = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ag.png")
image satori 3ah = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ah.png")
image satori 3ai = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ai.png")
image satori 3aj = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/aj.png")
image satori 3ak = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ak.png")
image satori 3al = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/al.png")
image satori 3am = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/am.png")
image satori 3an = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/an.png")
image satori 3ao = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ao.png")
image satori 3ap = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ap.png")
image satori 3aq = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/aq.png")
image satori 3ar = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/1l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ar.png")

image satori 4 = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/a.png")
image satori 4a = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/a.png")
image satori 4b = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/b.png")
image satori 4c = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/c.png")
image satori 4d = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/d.png")
image satori 4e = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/e.png")
image satori 4f = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/f.png")
image satori 4g = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/g.png")
image satori 4h = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/h.png")
image satori 4i = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/i.png")
image satori 4j = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/j.png")
image satori 4k = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/k.png")
image satori 4l = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/l.png")
image satori 4m = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/m.png")
image satori 4n = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/n.png")
image satori 4o = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/o.png")
image satori 4p = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/p.png")
image satori 4q = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/q.png")
image satori 4r = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/r.png")
image satori 4s = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/s.png")
image satori 4t = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/t.png")
image satori 4u = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/u.png")
image satori 4v = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/v.png")
image satori 4w = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/w.png")
image satori 4x = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/x.png")
image satori 4y = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/y.png")
image satori 4z = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/z.png")
image satori 4aa = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/aa.png")
image satori 4ab = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ab.png")
image satori 4ac = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ac.png")
image satori 4ad = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ad.png")
image satori 4ae = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ae.png")
image satori 4af = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/af.png")
image satori 4ag = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ag.png")
image satori 4ah = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ah.png")
image satori 4ai = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ai.png")
image satori 4aj = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/aj.png")
image satori 4ak = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ak.png")
image satori 4al = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/al.png")
image satori 4am = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/am.png")
image satori 4an = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/an.png")
image satori 4ao = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ao.png")
image satori 4ap = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ap.png")
image satori 4aq = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/aq.png")
image satori 4ar = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ar.png")

image satori 5 = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/a.png")
image satori 5a = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/a.png")
image satori 5b = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/b.png")
image satori 5c = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/c.png")
image satori 5d = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/d.png")
image satori 5e = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/e.png")
image satori 5f = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/f.png")
image satori 5g = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/g.png")
image satori 5h = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/h.png")
image satori 5i = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/i.png")
image satori 5j = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/j.png")
image satori 5k = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/k.png")
image satori 5l = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/l.png")
image satori 5m = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/m.png")
image satori 5n = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/n.png")
image satori 5o = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/o.png")
image satori 5p = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/p.png")
image satori 5q = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/q.png")
image satori 5r = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/r.png")
image satori 5s = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/s.png")
image satori 5t = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/t.png")
image satori 5u = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/u.png")
image satori 5v = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/v.png")
image satori 5w = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/w.png")
image satori 5x = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/x.png")
image satori 5y = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/y.png")
image satori 5z = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/z.png")
image satori 5aa = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/aa.png")
image satori 5ab = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ab.png")
image satori 5ac = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ac.png")
image satori 5ad = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ad.png")
image satori 5ae = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ae.png")
image satori 5af = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/af.png")
image satori 5ag = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ag.png")
image satori 5ah = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ah.png")
image satori 5ai = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ai.png")
image satori 5aj = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/aj.png")
image satori 5ak = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ak.png")
image satori 5al = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/al.png")
image satori 5am = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/am.png")
image satori 5an = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/an.png")
image satori 5ao = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ao.png")
image satori 5ap = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ap.png")
image satori 5aq = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/aq.png")
image satori 5ar = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ar.png")

image satori 6 = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/a.png")
image satori 6a = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/a.png")
image satori 6b = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/b.png")
image satori 6c = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/c.png")
image satori 6d = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/d.png")
image satori 6e = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/e.png")
image satori 6f = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/f.png")
image satori 6g = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/g.png")
image satori 6h = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/h.png")
image satori 6i = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/i.png")
image satori 6j = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/j.png")
image satori 6k = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/k.png")
image satori 6l = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/l.png")
image satori 6m = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/m.png")
image satori 6n = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/n.png")
image satori 6o = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/o.png")
image satori 6p = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/p.png")
image satori 6q = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/q.png")
image satori 6r = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/r.png")
image satori 6s = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/s.png")
image satori 6t = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/t.png")
image satori 6u = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/u.png")
image satori 6v = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/v.png")
image satori 6w = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/w.png")
image satori 6x = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/x.png")
image satori 6y = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/y.png")
image satori 6z = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/z.png")
image satori 6aa = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/aa.png")
image satori 6ab = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ab.png")
image satori 6ac = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ac.png")
image satori 6ad = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ad.png")
image satori 6ae = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ae.png")
image satori 6af = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/af.png")
image satori 6ag = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ag.png")
image satori 6ah = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ah.png")
image satori 6ai = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ai.png")
image satori 6aj = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/aj.png")
image satori 6ak = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ak.png")
image satori 6al = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/al.png")
image satori 6am = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/am.png")
image satori 6an = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/an.png")
image satori 6ao = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ao.png")
image satori 6ap = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ap.png")
image satori 6aq = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/aq.png")
image satori 6ar = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/2l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ar.png")

image satori 7 = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/a.png")
image satori 7a = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/a.png")
image satori 7b = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/b.png")
image satori 7c = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/c.png")
image satori 7d = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/d.png")
image satori 7e = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/e.png")
image satori 7f = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/f.png")
image satori 7g = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/g.png")
image satori 7h = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/h.png")
image satori 7i = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/i.png")
image satori 7j = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/j.png")
image satori 7k = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/k.png")
image satori 7l = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/l.png")
image satori 7m = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/m.png")
image satori 7n = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/n.png")
image satori 7o = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/o.png")
image satori 7p = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/p.png")
image satori 7q = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/q.png")
image satori 7r = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/r.png")
image satori 7s = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/s.png")
image satori 7t = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/t.png")
image satori 7u = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/u.png")
image satori 7v = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/v.png")
image satori 7w = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/w.png")
image satori 7x = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/x.png")
image satori 7y = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/y.png")
image satori 7z = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/z.png")
image satori 7aa = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/aa.png")
image satori 7ab = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ab.png")
image satori 7ac = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ac.png")
image satori 7ad = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ad.png")
image satori 7ae = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ae.png")
image satori 7af = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/af.png")
image satori 7ag = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ag.png")
image satori 7ah = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ah.png")
image satori 7ai = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ai.png")
image satori 7aj = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/aj.png")
image satori 7ak = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ak.png")
image satori 7al = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/al.png")
image satori 7am = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/am.png")
image satori 7an = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/an.png")
image satori 7ao = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ao.png")
image satori 7ap = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ap.png")
image satori 7aq = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/aq.png")
image satori 7ar = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/1r.png", (0, 0), "mod_assets/images/satori/ar.png")

image satori 8 = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/a.png")
image satori 8a = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/a.png")
image satori 8b = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/b.png")
image satori 8c = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/c.png")
image satori 8d = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/d.png")
image satori 8e = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/e.png")
image satori 8f = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/f.png")
image satori 8g = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/g.png")
image satori 8h = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/h.png")
image satori 8i = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/i.png")
image satori 8j = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/j.png")
image satori 8k = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/k.png")
image satori 8l = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/l.png")
image satori 8m = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/m.png")
image satori 8n = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/n.png")
image satori 8o = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/o.png")
image satori 8p = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/p.png")
image satori 8q = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/q.png")
image satori 8r = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/r.png")
image satori 8s = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/s.png")
image satori 8t = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/t.png")
image satori 8u = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/u.png")
image satori 8v = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/v.png")
image satori 8w = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/w.png")
image satori 8x = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/x.png")
image satori 8y = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/y.png")
image satori 8z = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/z.png")
image satori 8aa = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/aa.png")
image satori 8ab = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ab.png")
image satori 8ac = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ac.png")
image satori 8ad = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ad.png")
image satori 8ae = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ae.png")
image satori 8af = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/af.png")
image satori 8ag = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ag.png")
image satori 8ah = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ah.png")
image satori 8ai = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ai.png")
image satori 8aj = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/aj.png")
image satori 8ak = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ak.png")
image satori 8al = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/al.png")
image satori 8am = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/am.png")
image satori 8an = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/an.png")
image satori 8ao = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ao.png")
image satori 8ap = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ap.png")
image satori 8aq = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/aq.png")
image satori 8ar = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/2r.png", (0, 0), "mod_assets/images/satori/ar.png")

image satori 9 = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/a.png")
image satori 9a = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/a.png")
image satori 9b = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/b.png")
image satori 9c = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/c.png")
image satori 9d = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/d.png")
image satori 9e = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/e.png")
image satori 9f = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/f.png")
image satori 9g = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/g.png")
image satori 9h = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/h.png")
image satori 9i = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/i.png")
image satori 9j = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/j.png")
image satori 9k = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/k.png")
image satori 9l = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/l.png")
image satori 9m = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/m.png")
image satori 9n = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/n.png")
image satori 9o = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/o.png")
image satori 9p = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/p.png")
image satori 9q = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/q.png")
image satori 9r = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/r.png")
image satori 9s = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/s.png")
image satori 9t = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/t.png")
image satori 9u = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/u.png")
image satori 9v = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/v.png")
image satori 9w = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/w.png")
image satori 9x = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/x.png")
image satori 9y = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/y.png")
image satori 9z = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/z.png")
image satori 9aa = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/aa.png")
image satori 9ab = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ab.png")
image satori 9ac = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ac.png")
image satori 9ad = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ad.png")
image satori 9ae = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ae.png")
image satori 9af = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/af.png")
image satori 9ag = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ag.png")
image satori 9ah = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ah.png")
image satori 9ai = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ai.png")
image satori 9aj = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/aj.png")
image satori 9ak = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ak.png")
image satori 9al = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/al.png")
image satori 9am = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/am.png")
image satori 9an = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/an.png")
image satori 9ao = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ao.png")
image satori 9ap = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ap.png")
image satori 9aq = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/aq.png")
image satori 9ar = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/3l.png", (0, 0), "mod_assets/images/satori/3r.png", (0, 0), "mod_assets/images/satori/ar.png")

image satori 10aq = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/4aq.png")
image satori 10ar = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/4ar.png")
image satori 10d = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/4d.png")
image satori 10l = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/4l.png")
image satori 10q = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/4q.png")
image satori 10r = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/4r.png")
image satori 10s = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/4s.png")
#ADD THE NEW EXPRESION
image satori 10y = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/4y.png")
image satori 10z = im.Composite((960, 960), (0, 0), "mod_assets/images/satori/4z.png")


image satori glitch:
    "mod_assets/images/satori/glitch1.png"
    pause 0.01666
    "mod_assets/images/satori/glitch2.png"
    pause 0.01666
    "mod_assets/images/satori/glitch3.png"
    pause 0.01666
    repeat

# natsuko
image natsuko 1 = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/a.png")
image natsuko 1a = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/a.png")
image natsuko 1b = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/b.png")
image natsuko 1c = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/c.png")
image natsuko 1d = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/d.png")
image natsuko 1e = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/e.png")
image natsuko 1f = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/f.png")
image natsuko 1g = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/g.png")
image natsuko 1h = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/h.png")
image natsuko 1i = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/i.png")
image natsuko 1j = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/j.png")
image natsuko 1k = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/k.png")
image natsuko 1l = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/l.png")
image natsuko 1m = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/m.png")
image natsuko 1n = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/n.png")
image natsuko 1o = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/o.png")
image natsuko 1p = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/p.png")
image natsuko 1q = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/q.png")
image natsuko 1r = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/r.png")
image natsuko 1s = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/s.png")
image natsuko 1t = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/t.png")
image natsuko 1u = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/u.png")
image natsuko 1v = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/v.png")
image natsuko 1w = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/w.png")
image natsuko 1x = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/x.png")
image natsuko 1y = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/y.png")
image natsuko 1z = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/z.png")
image natsuko 1aa = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/aa.png")
image natsuko 1ab = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/ab.png")
image natsuko 1ac = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/ac.png")
image natsuko 1ad = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/ad.png")
image natsuko 1ae = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/ae.png")
image natsuko 1af = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/af.png")
image natsuko 1ag = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/ag.png")
image natsuko 1ah = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/ah.png")
image natsuko 1ai = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/ai.png")
image natsuko 1aj = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/aj.png")
image natsuko 1ak = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/ak.png")
image natsuko 1al = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/al.png")
image natsuko 1am = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/am.png")
image natsuko 1an = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/an.png")
image natsuko 1ao = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/ao.png")

image natsuko 2 = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/a.png")
image natsuko 2a = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/a.png")
image natsuko 2b = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/b.png")
image natsuko 2c = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/c.png")
image natsuko 2d = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/d.png")
image natsuko 2e = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/e.png")
image natsuko 2f = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/f.png")
image natsuko 2g = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/g.png")
image natsuko 2h = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/h.png")
image natsuko 2i = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/i.png")
image natsuko 2j = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/j.png")
image natsuko 2k = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/k.png")
image natsuko 2l = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/l.png")
image natsuko 2m = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/m.png")
image natsuko 2n = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/n.png")
image natsuko 2o = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/o.png")
image natsuko 2p = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/p.png")
image natsuko 2q = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/q.png")
image natsuko 2r = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/r.png")
image natsuko 2s = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/s.png")
image natsuko 2t = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/t.png")
image natsuko 2u = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/u.png")
image natsuko 2v = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/v.png")
image natsuko 2w = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/w.png")
image natsuko 2x = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/x.png")
image natsuko 2y = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/y.png")
image natsuko 2z = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/z.png")
image natsuko 2aa = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/aa.png")
image natsuko 2ab = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/ab.png")
image natsuko 2ac = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/ac.png")
image natsuko 2ad = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/ad.png")
image natsuko 2ae = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/ae.png")
image natsuko 2af = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/af.png")
image natsuko 2ag = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/ag.png")
image natsuko 2ah = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/ah.png")
image natsuko 2ai = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/ai.png")
image natsuko 2aj = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/aj.png")
image natsuko 2ak = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/ak.png")
image natsuko 2al = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/al.png")
image natsuko 2am = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/am.png")
image natsuko 2an = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/an.png")
image natsuko 2ao = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/ao.png")

image natsuko 3 = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/a.png")
image natsuko 3a = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/a.png")
image natsuko 3b = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/b.png")
image natsuko 3c = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/c.png")
image natsuko 3d = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/d.png")
image natsuko 3e = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/e.png")
image natsuko 3f = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/f.png")
image natsuko 3g = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/g.png")
image natsuko 3h = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/h.png")
image natsuko 3i = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/i.png")
image natsuko 3j = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/j.png")
image natsuko 3k = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/k.png")
image natsuko 3l = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/l.png")
image natsuko 3m = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/m.png")
image natsuko 3n = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/n.png")
image natsuko 3o = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/o.png")
image natsuko 3p = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/p.png")
image natsuko 3q = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/q.png")
image natsuko 3r = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/r.png")
image natsuko 3s = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/s.png")
image natsuko 3t = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/t.png")
image natsuko 3u = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/u.png")
image natsuko 3v = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/v.png")
image natsuko 3w = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/w.png")
image natsuko 3x = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/x.png")
image natsuko 3y = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/y.png")
image natsuko 3z = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/z.png")
image natsuko 3aa = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/aa.png")
image natsuko 3ab = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/ab.png")
image natsuko 3ac = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/ac.png")
image natsuko 3ad = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/ad.png")
image natsuko 3ae = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/ae.png")
image natsuko 3af = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/af.png")
image natsuko 3ag = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/ag.png")
image natsuko 3ah = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/ah.png")
image natsuko 3ai = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/ai.png")
image natsuko 3aj = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/aj.png")
image natsuko 3ak = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/ak.png")
image natsuko 3al = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/al.png")
image natsuko 3am = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/am.png")
image natsuko 3an = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/an.png")
image natsuko 3ao = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/ao.png")

image natsuko 4 = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/a.png")
image natsuko 4a = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/a.png")
image natsuko 4b = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/b.png")
image natsuko 4c = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/c.png")
image natsuko 4d = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/d.png")
image natsuko 4e = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/e.png")
image natsuko 4f = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/f.png")
image natsuko 4g = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/g.png")
image natsuko 4h = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/h.png")
image natsuko 4i = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/i.png")
image natsuko 4j = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/j.png")
image natsuko 4k = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/k.png")
image natsuko 4l = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/l.png")
image natsuko 4m = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/m.png")
image natsuko 4n = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/n.png")
image natsuko 4o = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/o.png")
image natsuko 4p = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/p.png")
image natsuko 4q = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/q.png")
image natsuko 4r = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/r.png")
image natsuko 4s = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/s.png")
image natsuko 4t = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/t.png")
image natsuko 4u = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/u.png")
image natsuko 4v = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/v.png")
image natsuko 4w = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/w.png")
image natsuko 4x = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/x.png")
image natsuko 4y = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/y.png")
image natsuko 4z = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/z.png")
image natsuko 4aa = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/aa.png")
image natsuko 4ab = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/ab.png")
image natsuko 4ac = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/ac.png")
image natsuko 4ad = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/ad.png")
image natsuko 4ae = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/ae.png")
image natsuko 4af = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/af.png")
image natsuko 4ag = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/ag.png")
image natsuko 4ah = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/ah.png")
image natsuko 4ai = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/ai.png")
image natsuko 4aj = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/aj.png")
image natsuko 4ak = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/ak.png")
image natsuko 4al = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/al.png")
image natsuko 4am = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/am.png")
image natsuko 4an = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/an.png")
image natsuko 4ao = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/2l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/ao.png")

image natsuko 5 = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/a.png")
image natsuko 5a = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/a.png")
image natsuko 5b = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/b.png")
image natsuko 5c = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/c.png")
image natsuko 5d = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/d.png")
image natsuko 5e = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/e.png")
image natsuko 5f = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/f.png")
image natsuko 5g = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/g.png")
image natsuko 5h = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/h.png")
image natsuko 5i = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/i.png")
image natsuko 5j = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/j.png")
image natsuko 5k = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/k.png")
image natsuko 5l = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/l.png")
image natsuko 5m = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/m.png")
image natsuko 5n = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/n.png")
image natsuko 5o = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/o.png")
image natsuko 5p = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/p.png")
image natsuko 5q = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/q.png")
image natsuko 5r = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/r.png")
image natsuko 5s = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/s.png")
image natsuko 5t = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/t.png")
image natsuko 5u = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/u.png")
image natsuko 5v = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/v.png")
image natsuko 5w = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/w.png")
image natsuko 5x = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/x.png")
image natsuko 5y = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/y.png")
image natsuko 5z = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/z.png")
image natsuko 5aa = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/aa.png")
image natsuko 5ab = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/ab.png")
image natsuko 5ac = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/ac.png")
image natsuko 5ad = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/ad.png")
image natsuko 5ae = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/ae.png")
image natsuko 5af = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/af.png")
image natsuko 5ag = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/ag.png")
image natsuko 5ah = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/ah.png")
image natsuko 5ai = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/ai.png")
image natsuko 5aj = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/aj.png")
image natsuko 5ak = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/ak.png")
image natsuko 5al = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/al.png")
image natsuko 5am = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/am.png")
image natsuko 5an = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/an.png")
image natsuko 5ao = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/ao.png")

image natsuko 6 = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/a.png")
image natsuko 6a = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/a.png")
image natsuko 6b = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/b.png")
image natsuko 6c = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/c.png")
image natsuko 6d = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/d.png")
image natsuko 6e = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/e.png")
image natsuko 6f = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/f.png")
image natsuko 6g = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/g.png")
image natsuko 6h = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/h.png")
image natsuko 6i = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/i.png")
image natsuko 6j = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/j.png")
image natsuko 6k = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/k.png")
image natsuko 6l = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/l.png")
image natsuko 6m = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/m.png")
image natsuko 6n = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/n.png")
image natsuko 6o = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/o.png")
image natsuko 6p = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/p.png")
image natsuko 6q = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/q.png")
image natsuko 6r = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/r.png")
image natsuko 6s = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/s.png")
image natsuko 6t = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/t.png")
image natsuko 6u = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/u.png")
image natsuko 6v = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/v.png")
image natsuko 6w = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/w.png")
image natsuko 6x = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/x.png")
image natsuko 6y = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/y.png")
image natsuko 6z = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/z.png")
image natsuko 6aa = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/aa.png")
image natsuko 6ab = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/ab.png")
image natsuko 6ac = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/ac.png")
image natsuko 6ad = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/ad.png")
image natsuko 6ae = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/ae.png")
image natsuko 6af = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/af.png")
image natsuko 6ag = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/ag.png")
image natsuko 6ah = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/ah.png")
image natsuko 6ai = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/ai.png")
image natsuko 6aj = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/aj.png")
image natsuko 6ak = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/ak.png")
image natsuko 6al = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/al.png")
image natsuko 6am = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/am.png")
image natsuko 6an = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/an.png")
image natsuko 6ao = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/3l.png", (0, 0), "mod_assets/images/natsuko/2r.png", (0, 0), "mod_assets/images/natsuko/ao.png")

image natsuko 7 = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/a.png")
image natsuko 7a = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/a.png")
image natsuko 7b = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/b.png")
image natsuko 7c = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/c.png")
image natsuko 7d = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/d.png")
image natsuko 7e = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/e.png")
image natsuko 7f = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/f.png")
image natsuko 7g = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/g.png")
image natsuko 7h = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/h.png")
image natsuko 7i = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/i.png")
image natsuko 7j = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/j.png")
image natsuko 7k = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/k.png")
image natsuko 7l = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/l.png")
image natsuko 7m = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/m.png")
image natsuko 7n = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/n.png")
image natsuko 7o = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/o.png")
image natsuko 7p = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/p.png")
image natsuko 7q = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/q.png")
image natsuko 7r = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/r.png")
image natsuko 7s = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/s.png")
image natsuko 7t = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/t.png")
image natsuko 7u = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/u.png")
image natsuko 7v = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/v.png")
image natsuko 7w = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/w.png")
image natsuko 7x = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/x.png")
image natsuko 7y = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/y.png")
image natsuko 7z = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/z.png")
image natsuko 7aa = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/aa.png")
image natsuko 7ab = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/ab.png")
image natsuko 7ac = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/ac.png")
image natsuko 7ad = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/ad.png")
image natsuko 7ae = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/ae.png")
image natsuko 7af = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/af.png")
image natsuko 7ag = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/ag.png")
image natsuko 7ah = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/ah.png")
image natsuko 7ai = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/ai.png")
image natsuko 7aj = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/aj.png")
image natsuko 7ak = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/ak.png")
image natsuko 7al = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/al.png")
image natsuko 7am = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/am.png")
image natsuko 7an = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/an.png")
image natsuko 7ao = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/4.png", (0, 0), "mod_assets/images/natsuko/ao.png")

image natsuko scream = im.Composite((960, 960), (0, 0), "mod_assets/images/natsuko/1l.png", (0, 0), "mod_assets/images/natsuko/1r.png", (0, 0), "mod_assets/images/natsuko/scream.png")

image natsuko glitch:
    "mod_assets/images/natsuko/glitch1.png"
    pause 0.1
    "mod_assets/images/natsuko/glitch2.png"
    pause 0.1
    "mod_assets/images/natsuko/glitch3.png"
    repeat

# yuuri
image yuuri 1 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/a.png")
image yuuri 1a = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/a.png")
image yuuri 1b = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/b.png")
image yuuri 1c = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/c.png")
image yuuri 1d = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/d.png")
image yuuri 1e = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/e.png")
image yuuri 1f = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/f.png")
image yuuri 1g = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/g.png")
image yuuri 1h = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/h.png")
image yuuri 1i = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/i.png")
image yuuri 1j = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/j.png")
image yuuri 1k = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/k.png")
image yuuri 1l = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/l.png")
image yuuri 1m = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/m.png")
image yuuri 1n = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/n.png")
image yuuri 1o = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/o.png")
image yuuri 1p = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/p.png")
image yuuri 1q = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/q.png")
image yuuri 1r = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/r.png")
image yuuri 1s = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/s.png")
image yuuri 1t = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/t.png")
image yuuri 1u = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/u.png")
image yuuri 1v = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/v.png")
image yuuri 1w = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/w.png")
image yuuri 1x = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/x.png")
image yuuri 1y = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/y.png")
image yuuri 1y1 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/y1.png")
image yuuri 1y2 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/y2.png")
image yuuri 1y3 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/y3.png")
image yuuri 1y4 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/y4.png")
image yuuri 1y5 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/y5.png")
image yuuri 1y6 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/y6.png")
image yuuri 1y7 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/y7.png")
image yuuri 1y8 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/y8.png")

image yuuri 2 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/a.png")
image yuuri 2a = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/a.png")
image yuuri 2b = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/b.png")
image yuuri 2c = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/c.png")
image yuuri 2d = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/d.png")
image yuuri 2e = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/e.png")
image yuuri 2f = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/f.png")
image yuuri 2g = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/g.png")
image yuuri 2h = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/h.png")
image yuuri 2i = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/i.png")
image yuuri 2j = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/j.png")
image yuuri 2k = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/k.png")
image yuuri 2l = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/l.png")
image yuuri 2m = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/m.png")
image yuuri 2n = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/n.png")
image yuuri 2o = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/o.png")
image yuuri 2p = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/p.png")
image yuuri 2q = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/q.png")
image yuuri 2r = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/r.png")
image yuuri 2s = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/s.png")
image yuuri 2t = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/t.png")
image yuuri 2u = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/u.png")
image yuuri 2v = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/v.png")
image yuuri 2w = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/w.png")
image yuuri 2x = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/x.png")
image yuuri 2y = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/y.png")
image yuuri 2y1 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/y1.png")
image yuuri 2y2 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/y2.png")
image yuuri 2y3 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/y3.png")
image yuuri 2y4 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/y4.png")
image yuuri 2y5 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/y5.png")
image yuuri 2y6 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/y6.png")
image yuuri 2y7 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/y7.png")
image yuuri 2y8 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/1l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/y8.png")

image yuuri 3 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/a.png")
image yuuri 3a = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/a.png")
image yuuri 3b = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/b.png")
image yuuri 3c = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/c.png")
image yuuri 3d = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/d.png")
image yuuri 3e = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/e.png")
image yuuri 3f = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/f.png")
image yuuri 3g = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/g.png")
image yuuri 3h = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/h.png")
image yuuri 3i = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/i.png")
image yuuri 3j = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/j.png")
image yuuri 3k = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/k.png")
image yuuri 3l = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/l.png")
image yuuri 3m = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/m.png")
image yuuri 3n = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/n.png")
image yuuri 3o = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/o.png")
image yuuri 3p = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/p.png")
image yuuri 3q = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/q.png")
image yuuri 3r = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/r.png")
image yuuri 3s = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/s.png")
image yuuri 3t = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/t.png")
image yuuri 3u = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/u.png")
image yuuri 3v = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/v.png")
image yuuri 3w = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/w.png")
image yuuri 3x = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/x.png")
image yuuri 3y = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/y.png")
image yuuri 3y1 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/y1.png")
image yuuri 3y2 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/y2.png")
image yuuri 3y3 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/y3.png")
image yuuri 3y4 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/y4.png")
image yuuri 3y5 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/y5.png")
image yuuri 3y6 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/y6.png")
image yuuri 3y7 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/y7.png")
image yuuri 3y8 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/y8.png")

image yuuri 4 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/a.png")
image yuuri 4a = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/a.png")
image yuuri 4b = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/b.png")
image yuuri 4c = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/c.png")
image yuuri 4d = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/d.png")
image yuuri 4e = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/e.png")
image yuuri 4f = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/f.png")
image yuuri 4g = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/g.png")
image yuuri 4h = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/h.png")
image yuuri 4i = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/i.png")
image yuuri 4j = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/j.png")
image yuuri 4k = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/k.png")
image yuuri 4l = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/l.png")
image yuuri 4m = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/m.png")
image yuuri 4n = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/n.png")
image yuuri 4o = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/o.png")
image yuuri 4p = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/p.png")
image yuuri 4q = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/q.png")
image yuuri 4r = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/r.png")
image yuuri 4s = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/s.png")
image yuuri 4t = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/t.png")
image yuuri 4u = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/u.png")
image yuuri 4v = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/v.png")
image yuuri 4w = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/w.png")
image yuuri 4x = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/x.png")
image yuuri 4y = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/y.png")
image yuuri 4y1 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/y1.png")
image yuuri 4y2 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/y2.png")
image yuuri 4y3 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/y3.png")
image yuuri 4y4 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/y4.png")
image yuuri 4y5 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/y5.png")
image yuuri 4y6 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/y6.png")
image yuuri 4y7 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/y7.png")
image yuuri 4y8 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/2l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/y8.png")

image yuuri 5 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/a.png")
image yuuri 5a = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/a.png")
image yuuri 5b = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/b.png")
image yuuri 5c = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/c.png")
image yuuri 5d = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/d.png")
image yuuri 5e = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/e.png")
image yuuri 5f = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/f.png")
image yuuri 5g = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/g.png")
image yuuri 5h = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/h.png")
image yuuri 5i = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/i.png")
image yuuri 5j = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/j.png")
image yuuri 5k = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/k.png")
image yuuri 5l = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/l.png")
image yuuri 5m = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/m.png")
image yuuri 5n = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/n.png")
image yuuri 5o = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/o.png")
image yuuri 5p = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/p.png")
image yuuri 5q = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/q.png")
image yuuri 5r = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/r.png")
image yuuri 5s = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/s.png")
image yuuri 5t = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/t.png")
image yuuri 5u = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/u.png")
image yuuri 5v = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/v.png")
image yuuri 5w = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/w.png")
image yuuri 5x = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/x.png")
image yuuri 5y = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/y.png")
image yuuri 5y1 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/y1.png")
image yuuri 5y2 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/y2.png")
image yuuri 5y3 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/y3.png")
image yuuri 5y4 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/y4.png")
image yuuri 5y5 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/y5.png")
image yuuri 5y6 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/y6.png")
image yuuri 5y7 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/y7.png")
image yuuri 5y8 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/1r.png", (0, 0), "mod_assets/images/yuuri/y8.png")

image yuuri 6 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/a.png")
image yuuri 6a = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/a.png")
image yuuri 6b = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/b.png")
image yuuri 6c = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/c.png")
image yuuri 6d = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/d.png")
image yuuri 6e = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/e.png")
image yuuri 6f = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/f.png")
image yuuri 6g = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/g.png")
image yuuri 6h = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/h.png")
image yuuri 6i = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/i.png")
image yuuri 6j = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/j.png")
image yuuri 6k = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/k.png")
image yuuri 6l = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/l.png")
image yuuri 6m = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/m.png")
image yuuri 6n = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/n.png")
image yuuri 6o = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/o.png")
image yuuri 6p = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/p.png")
image yuuri 6q = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/q.png")
image yuuri 6r = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/r.png")
image yuuri 6s = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/s.png")
image yuuri 6t = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/t.png")
image yuuri 6u = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/u.png")
image yuuri 6v = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/v.png")
image yuuri 6w = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/w.png")
image yuuri 6x = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/x.png")
image yuuri 6y = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/y.png")
image yuuri 6y1 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/y1.png")
image yuuri 6y2 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/y2.png")
image yuuri 6y3 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/y3.png")
image yuuri 6y4 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/y4.png")
image yuuri 6y5 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/y5.png")
image yuuri 6y6 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/y6.png")
image yuuri 6y7 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/y7.png")
image yuuri 6y8 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/3l.png", (0, 0), "mod_assets/images/yuuri/2r.png", (0, 0), "mod_assets/images/yuuri/y8.png")

image yuuri 7 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/a.png")
image yuuri 7a = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/a.png")
image yuuri 7b = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/b.png")
image yuuri 7c = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/c.png")
image yuuri 7d = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/d.png")
image yuuri 7e = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/e.png")
image yuuri 7f = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/f.png")
image yuuri 7g = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/g.png")
image yuuri 7h = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/h.png")
image yuuri 7i = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/i.png")
image yuuri 7j = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/j.png")
image yuuri 7k = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/k.png")
image yuuri 7l = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/l.png")
image yuuri 7m = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/m.png")
image yuuri 7n = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/n.png")
image yuuri 7o = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/o.png")
image yuuri 7p = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/p.png")
image yuuri 7q = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/q.png")
image yuuri 7r = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/r.png")
image yuuri 7s = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/s.png")
image yuuri 7t = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/t.png")
image yuuri 7u = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/u.png")
image yuuri 7v = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/v.png")
image yuuri 7w = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/w.png")
image yuuri 7x = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/x.png")
image yuuri 7y = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/y.png")
image yuuri 7y1 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/y1.png")
image yuuri 7y2 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/y2.png")
image yuuri 7y3 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/y3.png")
image yuuri 7y4 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/y4.png")
image yuuri 7y5 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/y5.png")
image yuuri 7y6 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/y6.png")
image yuuri 7y7 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/y7.png")
image yuuri 7y8 = im.Composite((960, 960), (0, 0), "mod_assets/images/yuuri/4.png", (0, 0), "mod_assets/images/yuuri/y8.png")

image yuuri glitch:
    "mod_assets/images/yuuri/glitch1.png"
    pause 0.1
    "mod_assets/images/yuuri/glitch2.png"
    pause 0.1
    "mod_assets/images/yuuri/glitch3.png"
    repeat

# Mateo the Douchebag
image mateo 1 = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/a.png")
image mateo 1a = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/a.png")
image mateo 1b = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/b.png")
image mateo 1c = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/c.png")
image mateo 1d = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/d.png")
image mateo 1e = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/e.png")
image mateo 1f = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/f.png")
image mateo 1g = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/g.png")
image mateo 1h = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/h.png")
image mateo 1i = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/i.png")
image mateo 1j = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/j.png")
image mateo 1k = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/k.png")
image mateo 1l = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/l.png")
image mateo 1m = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/m.png")
image mateo 1n = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/n.png")
image mateo 1o = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/o.png")
image mateo 1p = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/p.png")
image mateo 1q = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/q.png")
image mateo 1r = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/r.png")
image mateo 1s = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/s.png")
image mateo 1t = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/t.png")
image mateo 1u = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/u.png")
image mateo 1v = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/v.png")
image mateo 1w = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/w.png")
image mateo 1x = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/x.png")
image mateo 1y = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/y.png")
image mateo 1z = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/z.png")
image mateo 1aa = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/aa.png")
image mateo 1ab = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/ab.png")
image mateo 1ac = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/ac.png")
image mateo 1ad = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/ad.png")
image mateo 1ae = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/ae.png")
image mateo 1af = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/af.png")
image mateo 1ag = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/ag.png")
image mateo 1ah = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/ah.png")

image mateo 2 = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/a.png")
image mateo 2a = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/a.png")
image mateo 2b = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/b.png")
image mateo 2c = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/c.png")
image mateo 2d = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/d.png")
image mateo 2e = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/e.png")
image mateo 2f = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/f.png")
image mateo 2g = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/g.png")
image mateo 2h = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/h.png")
image mateo 2i = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/i.png")
image mateo 2j = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/j.png")
image mateo 2k = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/k.png")
image mateo 2l = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/l.png")
image mateo 2m = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/m.png")
image mateo 2n = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/n.png")
image mateo 2o = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/o.png")
image mateo 2p = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/p.png")
image mateo 2q = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/q.png")
image mateo 2r = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/r.png")
image mateo 2s = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/s.png")
image mateo 2t = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/t.png")
image mateo 2u = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/u.png")
image mateo 2v = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/v.png")
image mateo 2w = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/w.png")
image mateo 2x = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/x.png")
image mateo 2y = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/y.png")
image mateo 2z = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/z.png")
image mateo 2aa = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/aa.png")
image mateo 2ab = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/ab.png")
image mateo 2ac = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/ac.png")
image mateo 2ad = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/ad.png")
image mateo 2ae = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/ae.png")
image mateo 2af = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/af.png")
image mateo 2ag = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/ag.png")
image mateo 2ah = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/1l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/ah.png")

image mateo 3 = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/a.png")
image mateo 3a = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/a.png")
image mateo 3b = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/b.png")
image mateo 3c = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/c.png")
image mateo 3d = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/d.png")
image mateo 3e = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/e.png")
image mateo 3f = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/f.png")
image mateo 3g = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/g.png")
image mateo 3h = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/h.png")
image mateo 3i = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/i.png")
image mateo 3j = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/j.png")
image mateo 3k = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/k.png")
image mateo 3l = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/l.png")
image mateo 3m = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/m.png")
image mateo 3n = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/n.png")
image mateo 3o = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/o.png")
image mateo 3p = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/p.png")
image mateo 3q = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/q.png")
image mateo 3r = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/r.png")
image mateo 3s = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/s.png")
image mateo 3t = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/t.png")
image mateo 3u = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/u.png")
image mateo 3v = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/v.png")
image mateo 3w = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/w.png")
image mateo 3x = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/x.png")
image mateo 3y = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/y.png")
image mateo 3z = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/z.png")
image mateo 3aa = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/aa.png")
image mateo 3ab = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/ab.png")
image mateo 3ac = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/ac.png")
image mateo 3ad = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/ad.png")
image mateo 3ae = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/ae.png")
image mateo 3af = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/af.png")
image mateo 3ag = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/ag.png")
image mateo 3ah = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/ah.png")

image mateo 4 = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/a.png")
image mateo 4a = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/a.png")
image mateo 4b = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/b.png")
image mateo 4c = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/c.png")
image mateo 4d = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/d.png")
image mateo 4e = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/e.png")
image mateo 4f = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/f.png")
image mateo 4g = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/g.png")
image mateo 4h = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/h.png")
image mateo 4i = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/i.png")
image mateo 4j = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/j.png")
image mateo 4k = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/k.png")
image mateo 4l = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/l.png")
image mateo 4m = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/m.png")
image mateo 4n = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/n.png")
image mateo 4o = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/o.png")
image mateo 4p = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/p.png")
image mateo 4q = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/q.png")
image mateo 4r = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/r.png")
image mateo 4s = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/s.png")
image mateo 4t = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/t.png")
image mateo 4u = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/u.png")
image mateo 4v = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/v.png")
image mateo 4w = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/w.png")
image mateo 4x = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/x.png")
image mateo 4y = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/y.png")
image mateo 4z = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/z.png")
image mateo 4aa = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/aa.png")
image mateo 4ab = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/ab.png")
image mateo 4ac = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/ac.png")
image mateo 4ad = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/ad.png")
image mateo 4ae = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/ae.png")
image mateo 4af = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/af.png")
image mateo 4ag = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/ag.png")
image mateo 4ah = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/2l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/ah.png")

image mateo 5 = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/a.png")
image mateo 5a = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/a.png")
image mateo 5b = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/b.png")
image mateo 5c = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/c.png")
image mateo 5d = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/d.png")
image mateo 5e = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/e.png")
image mateo 5f = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/f.png")
image mateo 5g = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/g.png")
image mateo 5h = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/h.png")
image mateo 5i = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/i.png")
image mateo 5j = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/j.png")
image mateo 5k = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/k.png")
image mateo 5l = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/l.png")
image mateo 5m = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/m.png")
image mateo 5n = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/n.png")
image mateo 5o = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/o.png")
image mateo 5p = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/p.png")
image mateo 5q = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/q.png")
image mateo 5r = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/r.png")
image mateo 5s = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/s.png")
image mateo 5t = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/t.png")
image mateo 5u = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/u.png")
image mateo 5v = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/v.png")
image mateo 5w = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/w.png")
image mateo 5x = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/x.png")
image mateo 5y = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/y.png")
image mateo 5z = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/z.png")
image mateo 5aa = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/aa.png")
image mateo 5ab = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/ab.png")
image mateo 5ac = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/ac.png")
image mateo 5ad = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/ad.png")
image mateo 5ae = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/ae.png")
image mateo 5af = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/af.png")
image mateo 5ag = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/ag.png")
image mateo 5ah = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/1r.png", (0, 0), "mod_assets/images/mateo/ah.png")

image mateo 6 = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/a.png")
image mateo 6a = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/a.png")
image mateo 6b = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/b.png")
image mateo 6c = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/c.png")
image mateo 6d = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/d.png")
image mateo 6e = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/e.png")
image mateo 6f = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/f.png")
image mateo 6g = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/g.png")
image mateo 6h = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/h.png")
image mateo 6i = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/i.png")
image mateo 6j = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/j.png")
image mateo 6k = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/k.png")
image mateo 6l = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/l.png")
image mateo 6m = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/m.png")
image mateo 6n = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/n.png")
image mateo 6o = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/o.png")
image mateo 6p = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/p.png")
image mateo 6q = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/q.png")
image mateo 6r = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/r.png")
image mateo 6s = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/s.png")
image mateo 6t = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/t.png")
image mateo 6u = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/u.png")
image mateo 6v = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/v.png")
image mateo 6w = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/w.png")
image mateo 6x = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/x.png")
image mateo 6y = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/y.png")
image mateo 6z = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/z.png")
image mateo 6aa = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/aa.png")
image mateo 6ab = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/ab.png")
image mateo 6ac = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/ac.png")
image mateo 6ad = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/ad.png")
image mateo 6ae = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/ae.png")
image mateo 6af = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/af.png")
image mateo 6ag = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/ag.png")
image mateo 6ah = im.Composite((960, 960), (0, 0), "mod_assets/images/mateo/3l.png", (0, 0), "mod_assets/images/mateo/2r.png", (0, 0), "mod_assets/images/mateo/ah.png")

image mateo glitch:
    "mod_assets/images/mateo/glitch1.png"
    pause 0.1
    "mod_assets/images/mateo/glitch2.png"
    pause 0.1
    "mod_assets/images/mateo/glitch3.png"
    repeat

image femc femc1 = "mod_assets/images/femc/femc_sprite.png"

###### Character Variables ######
# These configure the shortcuts for writing dialog for each character.
define narrator = Character(ctc="ctc", ctc_position="fixed")
define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', image='satori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define m = DynamicCharacter('m_name', image='mateo', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', image='natsuko', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define y = DynamicCharacter('y_name', image='yuuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ny = Character('Nat & Yuuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

define _dismiss_pause = config.developer

# Persistent Variables

# These variables are load at game startup and exist on all saves.
default persistent.playername = ""
default player = persistent.playername
default persistent.playthrough = 0
default persistent.yuri_kill = 0
default persistent.seen_eyes = None
default persistent.seen_sticker = None
default persistent.ghost_menu = None
default persistent.seen_ghost_menu = None
default seen_eyes_this_chapter = False
default persistent.anticheat = 0
default persistent.clear = [False, False, False, False, False, False, False, False, False, False]
default persistent.special_poems = None
default persistent.clearall = None
default persistent.menu_bg_m = None
default persistent.first_load = None
default persistent.first_poem = None
default persistent.seen_colors_poem = None
default persistent.monika_back = None

# Other Persistent Variables
default in_sayori_kill = None
default in_yuri_kill = None
default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0
default currentpos = 0
default faint_effect = None

default s_name = "Sayori"
default m_name = "Monika"
default n_name = "Natsuki"
default y_name = "Yuri"

# Poem Variables
# This is how much each character likes your poem day by day
# -1 - Bad, 0 - Neutral, 1 - Good
default n_poemappeal = [0, 0, 0]
default s_poemappeal = [0, 0, 0]
default y_poemappeal = [0, 0, 0]
default m_poemappeal = [0, 0, 0]

# The last winner of the poem game
default poemwinner = ['sayori', 'sayori', 'sayori']

# This keeps track on who already read your poem
default s_readpoem = False
default n_readpoem = False
default y_readpoem = False
default m_readpoem = False

# This stores how many poems you read so far.
default poemsread = 0

# This stores who likes your poem the most.
# This controls which exclusive scene you will get each chapter.
default n_appeal = 0
default s_appeal = 0
default y_appeal = 0
default m_appeal = 0

# Tracks whether we watched Natsuki's and Yuri's exclusive scenes
default n_exclusivewatched = False
default y_exclusivewatched = False

# Tracks whether Yuri runs away after the first exclusive scene of Act 2
default y_gave = False
default y_ranaway = False

# Tracks if we get to Natsuki's and Yuri's third poem
default n_read3 = False
default y_read3 = False

# Tracks who we chose to side with in Chapter 1
default ch1_choice = "sayori"

default n_poemearly = False

# Tracks whether we wanted to help Sayori and/or Monika
default help_sayori = None
default help_monika = None

# Tracks who we chose to spend time with in Chapter 4
default ch4_scene = "yuri"
default ch4_name = "Yuri"

# Tracks if we accepted Sayori's Confession
default sayori_confess = True

# We read Natsuki's third poem in Chapter 23
default natsuki_23 = None

