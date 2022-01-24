from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image

#----interface----

root = Tk()
root.title("Game Settings Rk 1.42 HD")
mainframe = ttk.Frame(root, padding="6 6 24 24")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#image

logo = tk.PhotoImage(file='logo.png')

logo_label = ttk.Label(mainframe, image=logo).grid(column=1, row=1, columnspan=4)

#user

ttk.Label(mainframe, text="  Username:").grid(column=1, row=2, sticky=W)

username = StringVar()
username_entry = ttk.Entry(mainframe, width=9, textvariable=username)
username_entry.grid(column=2, row=2, sticky=(W, E))

#res

ttk.Label(mainframe, text="  Resolution:").grid(column=1, row=3, sticky=W)

resolution = StringVar()
resolution = ttk.Combobox(mainframe, width = 9, textvariable=resolution)
resolution.grid(column=2, row=3, sticky=(W, E))
resolution['values'] = ('1024x768', '1280x720', '1360x768', '1600x900', '1920x1080')

#Fullscreen

fullscreen = StringVar()
full_check = ttk.Checkbutton(mainframe, text='Fullscreen', variable=fullscreen, onvalue='1', offvalue='0')
full_check.grid(column=2, row=4, sticky=(W,E))

#sound

ttk.Label(mainframe, text="  Sound:").grid(column=1, row=5, sticky=W)


sound = IntVar()
sound_set=ttk.Label(mainframe)
sound_set.grid(column=2, row=5, sticky=W)

def update_lbl(sound):
    sound_set['text'] =sound + "%"


s = tk.Scale(mainframe, orient='horizontal', length=101, from_=0.0, to=100.0, variable=sound, command=update_lbl, showvalue=0)
s.grid(column=2, row=6, sticky=(W,E))
s.set(50)

#music

ttk.Label(mainframe, text="  Music:").grid(column=1, row=7, sticky=W)

music = IntVar()
music_set=ttk.Label(mainframe)
music_set.grid(column=2, row=7, sticky=W)

def update_lbl(music):
    music_set['text'] = music + "%"



m = tk.Scale(mainframe, orient='horizontal', length=101, from_=0.0, to=100.0, variable=music, command=update_lbl, showvalue=0)
m.grid(column=2, row=8, sticky=(W,E))
m.set(50)

#speech

ttk.Label(mainframe, text="  Speech:").grid(column=1, row=9, sticky=W)

speech = IntVar()
speech_set=ttk.Label(mainframe)
speech_set.grid(column=2, row=9, sticky=W)

def update_lbl(speech):
    speech_set['text'] = speech + "%"



sp = tk.Scale(mainframe, orient='horizontal', length=101, from_=0.0, to=100.0, variable=speech, command=update_lbl, showvalue=0)
sp.grid(column=2, row=10, sticky=(W,E))
sp.set(50)

#ScrollSpeed

ttk.Label(mainframe, text="  Scroll Speed:").grid(column=1, row=11, sticky=W)


scroll = IntVar()
scroll_set=ttk.Label(mainframe)
scroll_set.grid(column=2, row=11, sticky=W)

def update_lbl(scroll):
    scroll_set['text'] =scroll + "%"


sc = tk.Scale(mainframe, orient='horizontal', length=101, from_=0.0, to=100.0, variable=scroll, command=update_lbl, showvalue=0)
sc.grid(column=2, row=12, sticky=(W,E))
sc.set(50)


#lang

ttk.Label(mainframe, text="  Language:").grid(column=3, row=2, sticky=W)

lang = StringVar()
lang = ttk.Combobox(mainframe, width = 9, textvariable=lang)
lang.grid(column=4, row=2, sticky=(W, E))
lang['values'] = ('English', 'Russian', 'German', 'Bulgarian', 'Chinese', 'French', 'Italian', 'Polish', 'Spanish')

#part_sys

ttk.Label(mainframe, text="  Particle System:").grid(column=3, row=3, sticky=W)

part = StringVar()
part = ttk.Combobox(mainframe, width = 9, textvariable=part)
part.grid(column=4, row=3, sticky=(W, E))
part['values'] = ('Low', 'Medium', 'High')

#OpenSpy

openspy = StringVar()
openspy_check = ttk.Checkbutton(mainframe, text='Activate OpenSpy', variable=openspy, onvalue='1', offvalue='0')
openspy_check.grid(column=2, row=13, sticky=(W,E))

#Environanim

environ = StringVar()
environ_check = ttk.Checkbutton(mainframe, text='No Environmental Animations', variable=environ, onvalue='1', offvalue='0')
environ_check.grid(column=4, row=5, sticky=(W,E))

#Allow Transparent Units

transp = StringVar()
transp_check = ttk.Checkbutton(mainframe, text='No Transparent Units', variable=transp, onvalue='1', offvalue='0')
transp_check.grid(column=4, row=6, sticky=(W,E))

#View Fog Effect

fog = StringVar()
fog_check = ttk.Checkbutton(mainframe, text='View Fog Effect (only for 1024x768)', variable=fog, onvalue='1', offvalue='0')
fog_check.grid(column=2, row=14, sticky=(W,E))

#DxWrapper

wrapper = IntVar()
wrapper_check = ttk.Checkbutton(mainframe, text='Activate DxWrapper', variable=wrapper, onvalue='1', offvalue='0')
wrapper_check.grid(column=2, row=15, sticky=(W,E))

#Hotkeys

#ttk.Label(mainframe, text="  Hotkeys:").grid(column=1, row=16, sticky=W)

#keys = StringVar()
#keys = ttk.Combobox(mainframe, width = 9, textvariable=keys)
#keys.grid(column=2, row=16, sticky=(W, E))
#keys['values'] = ('Original', 'Grid')

#Always Show Champion Healthbar

champ = StringVar()
champ_check = ttk.Checkbutton(mainframe, text='Show Champion Healthbars', variable=champ, onvalue='1', offvalue='0')
champ_check.grid(column=4, row=7, sticky=(W,E))

#Healthbars shown with Alt-Key:

ttk.Label(mainframe, text="  Healthbars shown with Alt-Key:").grid(column=3, row=8, sticky=W)

hp_alt = IntVar()
hp_alt_friendly = ttk.Radiobutton(mainframe, text='  Friendly', variable=hp_alt, value='2')
hp_alt_friendly.grid(column=4, row=9, sticky=(W,E))

hp_alt_enemy = ttk.Radiobutton(mainframe, text='  Enemy', variable=hp_alt, value='4')
hp_alt_enemy.grid(column=4, row=10, sticky=(W,E))

hp_alt_all = ttk.Radiobutton(mainframe, text='  All', variable=hp_alt, value='6')
hp_alt_all.grid(column=4, row=11, sticky=(W,E))

hp_altsw = IntVar()
hp_altsw_check = ttk.Checkbutton(mainframe, text='  Severely wounded Units only', variable=hp_altsw, onvalue='1', offvalue='0')
hp_altsw_check.grid(column=4, row=12, sticky=(W,E))

#Healthbars shown with Ctrl-Key:

ttk.Label(mainframe, text="  Healthbars shown with Ctrl-Key:").grid(column=3, row=13, sticky=W)

hp_ctrl = IntVar()
hp_ctrl_friendly = ttk.Radiobutton(mainframe, text='  Friendly', variable=hp_ctrl, value='2')
hp_ctrl_friendly.grid(column=4, row=14, sticky=(W,E))

hp_ctrl_enemy = ttk.Radiobutton(mainframe, text='  Enemy', variable=hp_ctrl, value='4')
hp_ctrl_enemy.grid(column=4, row=15, sticky=(W,E))

hp_ctrl_all = ttk.Radiobutton(mainframe, text='  All', variable=hp_ctrl, value='6')
hp_ctrl_all.grid(column=4, row=16, sticky=(W,E))

hp_ctrlsw = IntVar()
hp_ctrlsw_check = ttk.Checkbutton(mainframe, text='  Severely wounded Units only', variable=hp_ctrlsw, onvalue='1', offvalue='0')
hp_ctrlsw_check.grid(column=4, row=19, sticky=(W,E))

#-------------------------------------Read DATA------------------------------
import configparser

config = configparser.ConfigParser(allow_no_value=True, strict=False)
config.read('config.ini')

username.set(config['system']['DefaultPlayerName'])

if config['system']['windowx'] == '1920':
    resolution.set('1920x1080')
elif config['system']['windowx'] == '1600':
    resolution.set('1600x900')
elif config['system']['windowx'] == '1360':
    resolution.set('1360x768')
elif config['system']['windowx'] == '1280':
    resolution.set('1280x720')
else:
    resolution.set('1024x768')
    
openspy.set(config['system']['gamespyingame'])

fullscreen.set(config['system']['fullscreen'])


settingsconfig = configparser.ConfigParser(allow_no_value=True, strict=False)
settingsconfig.read('vxSettings.ini')

lang.set(settingsconfig['Language']['default'])

if settingsconfig['Options']['noviewfog'] == '1':
    fog.set(0)
else:
    fog.set(1)

champ.set(settingsconfig['Options']['herohealthbars'])

sound.set(settingsconfig['Options']['soundvolume'])
music.set(settingsconfig['Options']['musicvolume'])
speech.set(settingsconfig['Options']['speechvolume'])
scroll.set(settingsconfig['Options']['scrollspeed'])

if settingsconfig['Options']['particlesystemdetails'] == '2':
    part.set('High')
elif settingsconfig['Options']['particlesystemdetails'] == '1':
    part.set('Medium')
else:
    part.set('Low')
    
environ.set(settingsconfig['Options']['noobjectanimations'])
transp.set(settingsconfig['Options']['nobuildingglowanims'])

if settingsconfig['Options']['healthbaraltflags'] == '2' or settingsconfig['Options']['healthbaraltflags'] == '4' or settingsconfig['Options']['healthbaraltflags'] == '6':
    hp_alt.set(settingsconfig['Options']['healthbaraltflags'])
    hp_altsw.set('0')
else:
    read_hp_alt = int(settingsconfig['Options']['healthbaraltflags']) - 1
    hp_alt.set(read_hp_alt)
    hp_altsw.set('1')
    
if settingsconfig['Options']['healthbarctrlflags'] == '2' or settingsconfig['Options']['healthbarctrlflags'] == '4' or settingsconfig['Options']['healthbarctrlflags'] == '6':
    hp_ctrl.set(settingsconfig['Options']['healthbarctrlflags'])
    hp_ctrlsw.set('0')
else:
    read_hp_ctrl = int(settingsconfig['Options']['healthbarctrlflags']) - 1
    hp_ctrl.set(read_hp_ctrl)
    hp_ctrlsw.set('1')

    
wrapperconfig = configparser.ConfigParser()
wrapperconfig.read('dxwrapper.ini')
if wrapperconfig['General']['IncludeProcess'] == 'rk.exe':
    wrapper.set('1')
else:
    wrapper.set('0')


#-------------------------------------DATA creation--------------------------


def save():
    

    #DxWrapper
    
    if wrapper.get() == 0:
        dxwrapper1 = 'none.exe'
    else :
        dxwrapper1 = 'rk.exe'
    
    wrapperconfig = configparser.ConfigParser(allow_no_value=True, strict=False)
    wrapperconfig.read('dxwrapper.ini')
    wrapperconfig['General']['IncludeProcess'] = str(dxwrapper1)

    with open('dxwrapper.ini', 'w') as wrapperfile:
        wrapperconfig.write(wrapperfile)

    #-config.ini-
    config = configparser.ConfigParser()
    config.read('config.ini')
    
        #username
    username1 = username.get()
    config['system']['DefaultPlayerName'] = str(username1)

        #openspy
    if openspy.get() == '0':
        openspy1 = '0'
    else :
        openspy1 = '1'
    config['system']['gamespyingame'] = str(openspy1)

        #fullscreen
    if fullscreen.get() == '0':
        fullscreen1 = '0'
    else :
        fullscreen1 = '1'
    config['system']['fullscreen'] = str(fullscreen1)

        #res_x
    if resolution.get() == '1920x1080':
        res_x = '1920'
    elif resolution.get() == '1360x768' :
        res_x = '1360'
    elif resolution.get() == '1280x720' :
        res_x = '1280'
    elif resolution.get() == '1600x900' :
        res_x = '1600'
    else:
        res_x = '1024'
    config['system']['windowx'] = str(res_x)

        #res_y
    if resolution.get() == '1920x1080':
        res_y = '1080'
    elif resolution.get() == '1360x768' :
        res_y = '768'
    elif resolution.get() == '1280x720' :
        res_y = '720'
    elif resolution.get() == '1600x900' :
        res_y = '900'
    else:
        res_y = '768'
    config['system']['windowy'] = str(res_y)


    
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

    #-vxSettings.ini-
    settingsconfig = configparser.ConfigParser(allow_no_value=True, strict=False)
    settingsconfig.read('vxSettings.ini')

                #language
    if lang.get() == "":
        lang1 = 'english'
    else:
        lang1 = lang.get()
    settingsconfig['Language']['default'] = str(lang1)

    

                #fog
    if fog.get() == '0':
        fog1 = '1'
    else :
        fog1 = '0'
    settingsconfig['Options']['noviewfog'] = str(fog1)

                #champ_healthbar
    if champ.get() == '0':
        champ1 = '0'
    else :
        champ1 = '1'
    settingsconfig['Options']['herohealthbars'] = str(champ1)

                #Scrollspeed
    settingsconfig['Options']['scrollspeed'] = str(scroll.get())
    
                #Sound
    settingsconfig['Options']['soundvolume'] = str(sound.get())
    
                #Music
    settingsconfig['Options']['musicvolume'] = str(music.get())
    
                #Speech
    settingsconfig['Options']['speechvolume'] = str(speech.get())
    
                #Alt-Healthbars
    hp_alt_value = hp_alt.get() + hp_altsw.get()
    settingsconfig['Options']['healthbaraltflags'] = str(hp_alt_value)
    
                #Strg-Healthbars
    hp_ctrl_value = hp_ctrl.get() + hp_ctrlsw.get()
    settingsconfig['Options']['healthbarctrlflags'] = str(hp_ctrl_value)
    
                #online Username
    settingsconfig['OnlineBattle']['lastusername'] = str(username1)
    
                #obj_anim/env_anim
    if environ.get() == '0':
        environ1 = '0'
    else :
        environ1 = '1'
    settingsconfig['Options']['noobjectanimations'] = str(environ1)
    
                #Building_glow/transparency
    if transp.get() == '0':
        transp1 = '0'
    else :
        transp1 = '1'
    settingsconfig['Options']['nobuildingglowanims'] = str(transp1)
    
                #part_sys
    if part.get() == 'High':
        part1 = '2'
    elif part.get() == 'Medium' :
        part1 = '1'
    else:
        part1 = '0'
    settingsconfig['Options']['particlesystemdetails'] = str(part1)

    
    with open('vxSettings.ini', 'w') as settingsfile:
        settingsconfig.write(settingsfile)

        
    #--DATA\VXCONST.ini--
    constconfig = configparser.ConfigParser(allow_no_value=True, strict=False)
    constconfig.read('DATA\VXCONST.ini')
    
    #Frame
    if res_y == '1080':
        
            #Darklings 1080
        constconfig['FrameDarklings']['Texture'] = 'assets/interface/darkling/interface_top_hd.tga'
        constconfig['FrameDarklings']['dest1'] = '0, 766'
        constconfig['FrameDarklings']['dest2'] = '992, 754'
        constconfig['FrameDarklings']['dest3'] = '227, 811'
        constconfig['FrameDarklings']['dest4'] = '453, 846'
        constconfig['FrameDarklings']['dest5'] = '483, 833'
        constconfig['FrameDarklings']['dest6'] = '738, 771'
        constconfig['FrameDarklings']['src6'] = '0, 172, 511, 255'

            #Foresters 1080 309 260,301 309 309 309
        constconfig['FrameForesters']['Texture'] = 'assets/interface/forester/interface_top_hd.tga'
        constconfig['FrameForesters']['dest1'] = '0, 782'
        constconfig['FrameForesters']['dest2'] = '226, 839'
        constconfig['FrameForesters']['dest3'] = '483, 857'
        constconfig['FrameForesters']['dest4'] = '739, 819'
        constconfig['FrameForesters']['dest5'] = '995, 848'
        constconfig['FrameForesters']['dest6'] = '223, 878'
        constconfig['FrameForesters']['src4'] = '0, 163, 512, 212'
        
            #Humans 1080
        constconfig['FrameHumans']['Texture'] = 'assets/interface/human/interface_top_hd.tga'
        constconfig['FrameHumans']['dest1'] = '0, 799'
        constconfig['FrameHumans']['dest2'] = '799, 834'
        constconfig['FrameHumans']['dest3'] = '223, 868'
        constconfig['FrameHumans']['dest4'] = '479, 874'
        constconfig['FrameHumans']['dest5'] = '735, 868'
        constconfig['FrameHumans']['src2'] = '32, 72, 512, 106'
        
            #Common 1080
        constconfig['Frame']['Texture'] = 'assets/interface/human/interface_top_hd.tga'
        constconfig['Frame']['dest1'] = '0, 799'
        constconfig['Frame']['dest2'] = '799, 834'
        constconfig['Frame']['dest3'] = '223, 868'
        constconfig['Frame']['dest4'] = '479, 874'
        constconfig['Frame']['dest5'] = '735, 868'
        constconfig['Frame']['src2'] = '32, 72, 512, 106'
        

        constconfig['IndRaceIcons']['x'] = '1866' #Independent Special Button positions
        constconfig['GamePlay']['HintYPosLeft'] = '812' #Info Pop-Up Position
        constconfig['GamePlay']['HintYPosRight'] = '812'
        
    elif res_y == '720':
        
            #Darklings 1280 ---Done----
        constconfig['FrameDarklings']['Texture'] = 'assets/interface/darkling/interface_top_hd.tga'
        constconfig['FrameDarklings']['dest1'] = '0, 426'
        constconfig['FrameDarklings']['dest2'] = '992, 415'
        constconfig['FrameDarklings']['dest3'] = '227, 471'
        constconfig['FrameDarklings']['dest4'] = '453, 506'
        constconfig['FrameDarklings']['dest5'] = '483, 493'
        constconfig['FrameDarklings']['dest6'] = '739, 431'
        constconfig['FrameDarklings']['src6'] = '0, 172, 511, 255'

            #Foresters 1280 -----FINISH----- -71 -71 483,-79 -71 -71 -71
        constconfig['FrameForesters']['Texture'] = 'assets/interface/forester/interface_top_hd.tga'
        constconfig['FrameForesters']['dest1'] = '0, 422'
        constconfig['FrameForesters']['dest2'] = '226, 479'
        constconfig['FrameForesters']['dest3'] = '483, 497'
        constconfig['FrameForesters']['dest4'] = '739, 459'
        constconfig['FrameForesters']['dest5'] = '995, 488'
        constconfig['FrameForesters']['dest6'] = '223, 518'
        constconfig['FrameForesters']['src4'] = '0, 163, 512, 212'
        
            #Humans 1280
        constconfig['FrameHumans']['Texture'] = 'assets/interface/human/interface_top_hd.tga'
        constconfig['FrameHumans']['dest1'] = '0, 439'
        constconfig['FrameHumans']['dest2'] = '799, 474'
        constconfig['FrameHumans']['dest3'] = '223, 508'
        constconfig['FrameHumans']['dest4'] = '479, 514'
        constconfig['FrameHumans']['dest5'] = '735, 508'
        constconfig['FrameHumans']['src2'] = '32, 72, 512, 106'
        
            #Common 1280
        constconfig['Frame']['Texture'] = 'assets/interface/human/interface_top_hd.tga'
        constconfig['Frame']['dest1'] = '0, 439'
        constconfig['Frame']['dest2'] = '799, 474'
        constconfig['Frame']['dest3'] = '223, 508'
        constconfig['Frame']['dest4'] = '479, 514'
        constconfig['Frame']['dest5'] = '735, 508'
        constconfig['Frame']['src2'] = '32, 72, 512, 106'

        constconfig['IndRaceIcons']['x'] = '1226'
        constconfig['GamePlay']['HintYPosLeft'] = '452'
        constconfig['GamePlay']['HintYPosRight'] = '452'
        
    elif res_y =='900':
        
            #Darklings 1600 --Done--
        constconfig['FrameDarklings']['Texture'] = 'assets/interface/darkling/interface_top_hd.tga'
        constconfig['FrameDarklings']['dest1'] = '0, 586'
        constconfig['FrameDarklings']['dest2'] = '992, 575'
        constconfig['FrameDarklings']['dest3'] = '227, 631'
        constconfig['FrameDarklings']['dest4'] = '453, 666'
        constconfig['FrameDarklings']['dest5'] = '483, 653'
        constconfig['FrameDarklings']['dest6'] = '738, 591'
        constconfig['FrameDarklings']['src6'] = '0, 172, 511, 255'

            #Foresters 1600 --FINISH-- 129 129 483,121 129 129 129
        constconfig['FrameForesters']['Texture'] = 'assets/interface/forester/interface_top_hd.tga'
        constconfig['FrameForesters']['dest1'] = '0, 602'
        constconfig['FrameForesters']['dest2'] = '226, 659'
        constconfig['FrameForesters']['dest3'] = '483, 677'
        constconfig['FrameForesters']['dest4'] = '739, 639'
        constconfig['FrameForesters']['dest5'] = '995, 668'
        constconfig['FrameForesters']['dest6'] = '223, 698'
        constconfig['FrameForesters']['src4'] = '0, 163, 512, 212'
        
            #Humans 1600 132
        constconfig['FrameHumans']['Texture'] = 'assets/interface/human/interface_top_hd.tga'
        constconfig['FrameHumans']['dest1'] = '0, 619'
        constconfig['FrameHumans']['dest2'] = '799, 654'
        constconfig['FrameHumans']['dest3'] = '223, 688'
        constconfig['FrameHumans']['dest4'] = '479, 694'
        constconfig['FrameHumans']['dest5'] = '735, 688'
        constconfig['FrameHumans']['src2'] = '32, 72, 512, 106'
        
            #Common 1600
        constconfig['Frame']['Texture'] = 'assets/interface/human/interface_top_hd.tga'
        constconfig['Frame']['dest1'] = '0, 619'
        constconfig['Frame']['dest2'] = '799, 654'
        constconfig['Frame']['dest3'] = '223, 688'
        constconfig['Frame']['dest4'] = '479, 694'
        constconfig['Frame']['dest5'] = '735, 688'
        constconfig['Frame']['src2'] = '32, 72, 512, 106'

        constconfig['IndRaceIcons']['x'] = '1546'
        constconfig['GamePlay']['HintYPosLeft'] = '632'
        constconfig['GamePlay']['HintYPosRight'] = '632'
        
        
    else:
            #Darklings 1024
        constconfig['FrameDarklings']['Texture'] = 'assets/interface/darkling/interface_top.tga'
        constconfig['FrameDarklings']['dest1'] = '0, 474'
        constconfig['FrameDarklings']['dest2'] = '994, 463'
        constconfig['FrameDarklings']['dest3'] = '227, 519'
        constconfig['FrameDarklings']['dest4'] = '453, 554'
        constconfig['FrameDarklings']['dest5'] = '483, 541'
        constconfig['FrameDarklings']['dest6'] = '739, 479'
        constconfig['FrameDarklings']['src6'] = '0, 172, 255, 255'

            #Foresters 1024
        constconfig['FrameForesters']['Texture'] = 'assets/interface/forester/interface_top.tga'
        constconfig['FrameForesters']['dest1'] = '0, 473'
        constconfig['FrameForesters']['dest2'] = '226, 530'
        constconfig['FrameForesters']['dest3'] = '483, 548'
        constconfig['FrameForesters']['dest4'] = '739, 510'
        constconfig['FrameForesters']['dest5'] = '995, 539'
        constconfig['FrameForesters']['dest6'] = '223, 569'
        constconfig['FrameForesters']['src4'] = '0, 163, 256, 212'
        
            #Humans 1024
        constconfig['FrameHumans']['Texture'] = 'assets/interface/human/interface_top.tga'
        constconfig['FrameHumans']['dest1'] = '0, 487'
        constconfig['FrameHumans']['dest2'] = '799, 522'
        constconfig['FrameHumans']['dest3'] = '223, 556'
        constconfig['FrameHumans']['dest4'] = '479, 562'
        constconfig['FrameHumans']['dest5'] = '735, 556'
        constconfig['FrameHumans']['src2'] = '32, 72, 256, 106'
        
            #Common 1024
        constconfig['Frame']['Texture'] = 'assets/interface/human/interface_top.tga'
        constconfig['Frame']['dest1'] = '0, 487'
        constconfig['Frame']['dest2'] = '799, 522'
        constconfig['Frame']['dest3'] = '223, 556'
        constconfig['Frame']['dest4'] = '479, 562'
        constconfig['Frame']['dest5'] = '735, 556'
        constconfig['Frame']['src2'] = '32, 72, 256, 106'

        if res_x== '1360':
            constconfig['IndRaceIcons']['x'] = '1312'
            constconfig['GamePlay']['HintYPosLeft'] = '500'
            constconfig['GamePlay']['HintYPosRight'] = '520'
        else:
            constconfig['IndRaceIcons']['x'] = '950'
            constconfig['GamePlay']['HintYPosLeft'] = '500'
            constconfig['GamePlay']['HintYPosRight'] = '520'
        
    with open('DATA\VXCONST.ini', 'w') as constfile:
        constconfig.write(constfile)

    #profiles\noname
    profileconfig = configparser.ConfigParser(allow_no_value=True, strict=False)
    profileconfig.read('PROFILES\\NONAME\\PLAYER.ini')
    
    profileconfig['Player']['name'] = str(username1)
    profileconfig['Player 0']['plrname'] = str(username1)

    with open('PROFILES\\NONAME\\PLAYER.ini', 'w') as profilefile:
        profileconfig.write(profilefile)
        
    #DATA\INTERFACE\MENU\MainMenu.ini
    mainconfig = configparser.ConfigParser(allow_no_value=True, strict=False)
    mainconfig.read('DATA\INTERFACE\MENU\MAINMENU.ini')     

    if res_y == '1080':
        mainconfig['MainMenu']['RectWH'] = '0, 0, 1920, 1080'
        mainconfig['Sheath']['RectWH'] = '726, 595, 276, 489'
        mainconfig['Sheath']['Image'] = 'menures/sheath_hd.bmp, 0, 0'
        
    elif res_y == '720':

        mainconfig['MainMenu']['RectWH'] = '0, 0, 1280, 720'
        mainconfig['Sheath']['RectWH'] = '734, 595, 264, 177' #<--768 value
        mainconfig['Sheath']['Image'] = 'menures/sheath.bmp, 0, 0'

    elif res_x == '1360':

        mainconfig['MainMenu']['RectWH'] = '0, 0, 1360, 768'
        mainconfig['Sheath']['RectWH'] = '734, 595, 264, 177' #<--768 value
        mainconfig['Sheath']['Image'] = 'menures/sheath.bmp, 0, 0'
    
    elif res_y =='900':

        mainconfig['MainMenu']['RectWH'] = '0, 0, 1600, 900'
        mainconfig['Sheath']['RectWH'] = '726, 595, 276, 489' #<--wrong value
        mainconfig['Sheath']['Image'] = 'menures/sheath_hd.bmp, 0, 0'
        
    else:
        mainconfig['MainMenu']['RectWH'] = '0, 0, 1024, 768'
        mainconfig['Sheath']['RectWH'] = '734, 595, 264, 177'
        mainconfig['Sheath']['Image'] = 'menures/sheath.bmp, 0, 0'

    with open('DATA\INTERFACE\MENU\MAINMENU.ini', 'w') as mainfile:
        mainconfig.write(mainfile)

    #DATA\INTERFACE\MENU\MenuBack.ini
    backconfig = configparser.ConfigParser(allow_no_value=True, strict=False)
    backconfig.read('DATA\INTERFACE\MENU\MENUBACK.ini')     

    if res_y == '1080':
        backconfig['MenuBack']['rectwh'] = '0, 0, 1920, 1080'
        backconfig['Back']['Image'] = 'menures/main_background_hd.bmp, 400, 300'
        backconfig['Back']['RectWH'] = '0, 0, 1920, 1080'
        backconfig['BlackBkg']['rectwh'] = '0, 0, 1920, 1080'
        
    elif res_y == '720':
        backconfig['MenuBack']['rectwh'] = '0, 0, 1280, 720'
        backconfig['Back']['Image'] = 'menures/main_background_1280.bmp, 400, 300'
        backconfig['Back']['RectWH'] = '0, 0, 1280, 720'
        backconfig['BlackBkg']['rectwh'] = '0, 0, 1280, 720'

    elif res_x == '1360':
        backconfig['MenuBack']['rectwh'] = '0, 0, 1360, 768'
        backconfig['Back']['Image'] = 'menures/main_background_1360.bmp, 400, 300'
        backconfig['Back']['RectWH'] = '0, 0, 1360, 768'
        backconfig['BlackBkg']['rectwh'] = '0, 0, 1360, 768'
        
    elif res_y =='900':
        backconfig['MenuBack']['rectwh'] = '0, 0, 1600, 900'
        backconfig['Back']['Image'] = 'menures/main_background_1600.bmp, 400, 300'
        backconfig['Back']['RectWH'] = '0, 0, 1600, 900'
        backconfig['BlackBkg']['rectwh'] = '0, 0, 1600, 900'
        
    else:
        backconfig['MenuBack']['rectwh'] = '0, 0, 1024, 768'
        backconfig['Back']['Image'] = 'menures/main_background.bmp, 400, 300'
        backconfig['Back']['RectWH'] = '0, 0, 1024, 768'
        backconfig['BlackBkg']['rectwh'] = '0, 0, 1024, 768'

    with open('DATA\INTERFACE\MENU\MENUBACK.ini', 'w') as backfile:
        backconfig.write(backfile)

    #DATA\INTERFACE\MENU\OB_LOBBY.ini
    oblobbyconfig = configparser.ConfigParser(allow_no_value=True, strict=False)
    oblobbyconfig.read('DATA\INTERFACE\MENU\OB_LOBBY.ini')     

    if res_y == '1080':
        oblobbyconfig['Ob_lobby']['RectWH'] = '0, 0, 1920, 1080'
        oblobbyconfig['Ob_lobby Params']['DialogRect'] = '0, 0, 1920, 1080'
        
    elif res_y == '720':
        oblobbyconfig['Ob_lobby']['RectWH'] = '0, 0, 1280, 720'
        oblobbyconfig['Ob_lobby Params']['DialogRect'] = '0, 0, 1280, 720'

    elif res_x == '1360':
        oblobbyconfig['Ob_lobby']['RectWH'] = '0, 0, 1360, 768'
        oblobbyconfig['Ob_lobby Params']['DialogRect'] = '0, 0, 1360, 768'
        
    elif res_y =='900':
        oblobbyconfig['Ob_lobby']['RectWH'] = '0, 0, 1600, 900'
        oblobbyconfig['Ob_lobby Params']['DialogRect'] = '0, 0, 1600, 900'
        
    else:
        oblobbyconfig['Ob_lobby']['RectWH'] = '0, 0, 1024, 768'
        oblobbyconfig['Ob_lobby Params']['DialogRect'] = '0, 0, 1024, 768'

    with open('DATA\INTERFACE\MENU\OB_LOBBY.ini', 'w') as oblobbyfile:
        oblobbyconfig.write(oblobbyfile)

    #DATA\INTERFACE\MENU\OB_PROFILE.ini
    obprofileconfig = configparser.ConfigParser(allow_no_value=True, strict=False)
    obprofileconfig.read('DATA\INTERFACE\MENU\OB_PROFILE.ini')     

    if res_y == '1080':
        obprofileconfig['Ob_profile']['RectWH'] = '0, 0, 1920, 1080'
        obprofileconfig['Ob_profile Params']['DialogRect'] = '0, 0, 1920, 1080'
        
    elif res_y == '720':
        obprofileconfig['Ob_profile']['RectWH'] = '0, 0, 1280, 720'
        obprofileconfig['Ob_profile Params']['DialogRect'] = '0, 0, 1280, 720'
        
    elif res_x == '1360':
        obprofileconfig['Ob_profile']['RectWH'] = '0, 0, 1360, 768'
        obprofileconfig['Ob_profile Params']['DialogRect'] = '0, 0, 1360, 768'
        
    elif res_y =='900':
        obprofileconfig['Ob_profile']['RectWH'] = '0, 0, 1600, 900'
        obprofileconfig['Ob_profile Params']['DialogRect'] = '0, 0, 1600, 900'
        
    else:
        obprofileconfig['Ob_profile']['RectWH'] = '0, 0, 1024, 768'
        obprofileconfig['Ob_profile Params']['DialogRect'] = '0, 0, 1024, 768'

    with open('DATA\INTERFACE\MENU\OB_PROFILE.ini', 'w') as obprofilefile:
        obprofileconfig.write(obprofilefile)

    #DATA\INTERFACE\MENU\OB_LOGIN.ini
    obloginconfig = configparser.ConfigParser(allow_no_value=True, strict=False)
    obloginconfig.read('DATA\INTERFACE\MENU\OB_LOGIN.ini')     

    if res_y == '1080':
        obloginconfig['Ob_login']['RectWH'] = '0, 0, 1920, 1080'
        obloginconfig['Ob_login Params']['DialogRect'] = '0, 0, 1920, 1080'
        
    elif res_y == '720':
        obloginconfig['Ob_login']['RectWH'] = '0, 0, 1280, 720'
        obloginconfig['Ob_login Params']['DialogRect'] = '0, 0, 1280, 720'

    elif res_x == '1360':
        obloginconfig['Ob_login']['RectWH'] = '0, 0, 1360, 768'
        obloginconfig['Ob_login Params']['DialogRect'] = '0, 0, 1360, 768'
        
    elif res_y =='900':
        obloginconfig['Ob_login']['RectWH'] = '0, 0, 1600, 900'
        obloginconfig['Ob_login Params']['DialogRect'] = '0, 0, 1600, 900'
        
    else:
        obloginconfig['Ob_login']['RectWH'] = '0, 0, 1024, 768'
        obloginconfig['Ob_login Params']['DialogRect'] = '0, 0, 1024, 768'

    with open('DATA\INTERFACE\MENU\OB_LOGIN.ini', 'w') as obloginfile:
        obloginconfig.write(obloginfile)

    #DATA\INTERFACE\MENU\OB_REGISTER.ini
    obregisterconfig = configparser.ConfigParser(allow_no_value=True, strict=False)
    obregisterconfig.read('DATA\INTERFACE\MENU\OB_REGISTER.ini')     

    if res_y == '1080':
        obregisterconfig['Ob_register']['RectWH'] = '0, 0, 1920, 1080'
        obregisterconfig['Ob_register Params']['DialogRect'] = '0, 0, 1920, 1080'
        
    elif res_y == '720':
        obregisterconfig['Ob_register']['RectWH'] = '0, 0, 1280, 720'
        obregisterconfig['Ob_register Params']['DialogRect'] = '0, 0, 1280, 720'

    elif res_x == '1360':
        obregisterconfig['Ob_register']['RectWH'] = '0, 0, 1360, 768'
        obregisterconfig['Ob_register Params']['DialogRect'] = '0, 0, 1360, 768'
        
    elif res_y =='900':
        obregisterconfig['Ob_register']['RectWH'] = '0, 0, 1600, 900'
        obregisterconfig['Ob_register Params']['DialogRect'] = '0, 0, 1600, 900'
        
    else:
        obregisterconfig['Ob_register']['RectWH'] = '0, 0, 1024, 768'
        obregisterconfig['Ob_register Params']['DialogRect'] = '0, 0, 1024, 768'

    with open('DATA\INTERFACE\MENU\OB_REGISTER.ini', 'w') as obregisterfile:
        obregisterconfig.write(obregisterfile)

    #DATA\INTERFACE\MENU\OB_HALLOFFAME.ini
    obhofconfig = configparser.ConfigParser(allow_no_value=True, strict=False)
    obhofconfig.read('DATA\INTERFACE\MENU\OB_HALLOFFAME.ini')     

    if res_y == '1080':
        obhofconfig['Ob_halloffame']['RectWH'] = '0, 0, 1920, 1080'
        obhofconfig['Ob_halloffame Params']['DialogRect'] = '0, 0, 1920, 1080'
        
    elif res_y == '720':
        obhofconfig['Ob_halloffame']['RectWH'] = '0, 0, 1280, 720'
        obhofconfig['Ob_halloffame Params']['DialogRect'] = '0, 0, 1280, 720'

    elif res_x == '1360':
        obhofconfig['Ob_halloffame']['RectWH'] = '0, 0, 1360, 768'
        obhofconfig['Ob_halloffame Params']['DialogRect'] = '0, 0, 1360, 768'
        
    elif res_y =='900':
        obhofconfig['Ob_halloffame']['RectWH'] = '0, 0, 1600, 900'
        obhofconfig['Ob_halloffame Params']['DialogRect'] = '0, 0, 1600, 900'
        
    else:
        obhofconfig['Ob_halloffame']['RectWH'] = '0, 0, 1024, 768'
        obhofconfig['Ob_halloffame Params']['DialogRect'] = '0, 0, 1024, 768'

    with open('DATA\INTERFACE\MENU\OB_HALLOFFAME.ini', 'w') as obhoffile:
        obhofconfig.write(obhoffile)                

    #DATA\INTERFACE\MENU\OB_AUTOMATCH.ini
    obautoconfig = configparser.ConfigParser(allow_no_value=True, strict=False)
    obautoconfig.read('DATA\INTERFACE\MENU\OB_AUTOMATCH.ini')     

    if res_y == '1080':
        obautoconfig['Ob_automatch']['RectWH'] = '0, 0, 1920, 1080'
        obautoconfig['Ob_automatch Params']['DialogRect'] = '0, 0, 1920, 1080'
        
    elif res_y == '720':
        obautoconfig['Ob_automatch']['RectWH'] = '0, 0, 1280, 720'
        obautoconfig['Ob_automatch Params']['DialogRect'] = '0, 0, 1280, 720'

    elif res_x == '1360':
        obautoconfig['Ob_automatch']['RectWH'] = '0, 0, 1360, 768'
        obautoconfig['Ob_automatch Params']['DialogRect'] = '0, 0, 1360, 768'
        
    elif res_y =='900':
        obautoconfig['Ob_automatch']['RectWH'] = '0, 0, 1600, 900'
        obautoconfig['Ob_automatch Params']['DialogRect'] = '0, 0, 1600, 900'
        
    else:
        obautoconfig['Ob_automatch']['RectWH'] = '0, 0, 1024, 768'
        obautoconfig['Ob_automatch Params']['DialogRect'] = '0, 0, 1024, 768'

    with open('DATA\INTERFACE\MENU\OB_AUTOMATCH.ini', 'w') as obautofile:
        obautoconfig.write(obautofile)                

    #DATA\INTERFACE\MENU\GAMEMENU.ini
    gmconfig = configparser.ConfigParser(allow_no_value=True, strict=False)
    gmconfig.read('DATA\INTERFACE\MENU\GAMEMENU.ini')     

    if res_y == '1080':
        gmconfig['gamemenu']['RectWH'] = '0, 0, 1920, 1080'
        
    elif res_y == '720':
        gmconfig['gamemenu']['RectWH'] = '0, 0, 1280, 720'

    elif res_x == '1360':
        gmconfig['gamemenu']['RectWH'] = '0, 0, 1360, 768'
        
    elif res_y =='900':
        gmconfig['gamemenu']['RectWH'] = '0, 0, 1600, 900'
        
    else:
        gmconfig['gamemenu']['RectWH'] = '0, 0, 1024, 768'

    with open('DATA\INTERFACE\MENU\GAMEMENU.ini', 'w') as gmfile:
        gmconfig.write(gmfile)                

    #DATA\INTERFACE\MENU\GAMEOPTIONS.ini
    goconfig = configparser.ConfigParser(allow_no_value=True, strict=False)
    goconfig.read('DATA\INTERFACE\MENU\GAMEOPTIONS.ini')     

    if res_y == '1080':
        goconfig['GameOptions']['RectWH'] = '0, 0, 1920, 1080'
        
    elif res_y == '720':
        goconfig['GameOptions']['RectWH'] = '0, 0, 1280, 720'

    elif res_x == '1360':
        goconfig['GameOptions']['RectWH'] = '0, 0, 1360, 768'
        
    elif res_y =='900':
        goconfig['GameOptions']['RectWH'] = '0, 0, 1600, 900'
        
    else:
        goconfig['GameOptions']['RectWH'] = '0, 0, 1024, 768'

    with open('DATA\INTERFACE\MENU\GAMEOPTIONS.ini', 'w') as gofile:
        goconfig.write(gofile)                

        
    #-Darklings\CMDBAR.INI-
    darklingsconfig = configparser.ConfigParser(allow_no_value=True, strict=False)
    darklingsconfig.read('DATA\INTERFACE\Darklings\CMDBAR.ini')

    if res_y == '1080':
        darklingsconfig['Cmdbar']['RectWH'] = '0, 0, 1024, 247'
        darklingsconfig['Bottom']['Image'] = 'assets/interface/darkling/interface_BOTTOM_hd.bmp, 100, 100'
        
    elif res_y == '720':
        darklingsconfig['Cmdbar']['RectWH'] = '0, 0, 1024, 247'
        darklingsconfig['Bottom']['Image'] = 'assets/interface/darkling/interface_BOTTOM_1280.bmp, 100, 100'

    elif res_x == '1360':
        darklingsconfig['Cmdbar']['RectWH'] = '0, 0, 1024, 247'
        darklingsconfig['Bottom']['Image'] = 'assets/interface/darkling/interface_BOTTOM_1360.bmp, 100, 100'
        
    elif res_y =='900':
        darklingsconfig['Cmdbar']['RectWH'] = '0, 0, 1024, 247'
        darklingsconfig['Bottom']['Image'] = 'assets/interface/darkling/interface_BOTTOM_1600.bmp, 100, 100'
        
    else:
        darklingsconfig['Cmdbar']['RectWH'] = '0, 0, 1024, 227'
        darklingsconfig['Bottom']['Image'] = 'assets/interface/darkling/interface_BOTTOM.bmp, 100, 100'
        
    with open('DATA\INTERFACE\Darklings\CMDBAR.ini', 'w') as darklingsfile:
        darklingsconfig.write(darklingsfile)

    #-Foresters\CMDBAR.INI-
    forestersconfig = configparser.ConfigParser(allow_no_value=True, strict=False)
    forestersconfig.read('DATA\INTERFACE\Foresters\CMDBAR.ini')

    if res_y == '1080':
        forestersconfig['Cmdbar']['RectWH'] = '0, 0, 1024, 227'
        forestersconfig['Bottom']['Image'] = 'assets/interface/forester/interface_BOTTOM_hd.bmp, 100, 100'
            
    elif res_y == '720':
        forestersconfig['Cmdbar']['RectWH'] = '0, 0, 1024, 227'
        forestersconfig['Bottom']['Image'] = 'assets/interface/forester/interface_BOTTOM_1280.bmp, 100, 100'

    elif res_x == '1360':
        forestersconfig['Cmdbar']['RectWH'] = '0, 0, 1024, 227'
        forestersconfig['Bottom']['Image'] = 'assets/interface/forester/interface_BOTTOM_1360.bmp, 100, 100'
        
    elif res_y =='900':
        forestersconfig['Cmdbar']['RectWH'] = '0, 0, 1024, 227'
        forestersconfig['Bottom']['Image'] = 'assets/interface/forester/interface_BOTTOM_1600.bmp, 100, 100'
            
    else:
        forestersconfig['Cmdbar']['RectWH'] = '0, 0, 1024, 227'
        forestersconfig['Bottom']['Image'] = 'assets/interface/forester/interface_BOTTOM.bmp, 100, 100'
        

    with open('DATA\INTERFACE\Foresters\CMDBAR.ini', 'w') as forestersfile:
        forestersconfig.write(forestersfile)
        
    #-Humans\CMDBAR.INI-
    humansconfig = configparser.ConfigParser(allow_no_value=True, strict=False)
    humansconfig.read('DATA\INTERFACE\Humans\CMDBAR.ini')

    if res_y == '1080':
        humansconfig['Cmdbar']['RectWH'] = '0, 0, 1024, 227'
        humansconfig['Bottom']['Image'] = 'assets/interface/human/interface_BOTTOM_hd.bmp, 100, 100, 100, 100'
            
    elif res_y == '720':
        humansconfig['Cmdbar']['RectWH'] = '0, 0, 1024, 227'
        humansconfig['Bottom']['Image'] = 'assets/interface/human/interface_BOTTOM_1280.bmp, 100, 100, 100, 100'

    elif res_x == '1360':
        humansconfig['Cmdbar']['RectWH'] = '0, 0, 1024, 227'
        humansconfig['Bottom']['Image'] = 'assets/interface/human/interface_BOTTOM_1360.bmp, 100, 100, 100, 100'
        
    elif res_y =='900':
        humansconfig['Cmdbar']['RectWH'] = '0, 0, 1024, 227'
        humansconfig['Bottom']['Image'] = 'assets/interface/human/interface_BOTTOM_1600.bmp, 100, 100, 100, 100'
            
    else:
        humansconfig['Cmdbar']['RectWH'] = '0, 0, 1024, 227'
        humansconfig['Bottom']['Image'] = 'assets/interface/human/interface_BOTTOM.bmp, 100, 100, 100, 100'

    with open('DATA\INTERFACE\Humans\CMDBAR.ini', 'w') as humansfile:
        humansconfig.write(humansfile)
      
    #-COMMON-
    commonconfig = configparser.ConfigParser(allow_no_value=True, strict=False)
    commonconfig.read('DATA\INTERFACE\CMDBAR.ini')

    if res_y == '1080':
        commonconfig['Cmdbar']['RectWH'] = '0, 0, 1024, 227'
        commonconfig['Bottom']['Image'] = 'assets/interface/human/interface_BOTTOM_hd.bmp, 100, 100, 100, 100'
            
    elif res_y == '720':
        commonconfig['Cmdbar']['RectWH'] = '0, 0, 1024, 227'
        commonconfig['Bottom']['Image'] = 'assets/interface/human/interface_BOTTOM_1280.bmp, 100, 100, 100, 100'
    
    elif res_x == '1360':
        commonconfig['Cmdbar']['RectWH'] = '0, 0, 1024, 227'
        commonconfig['Bottom']['Image'] = 'assets/interface/human/interface_BOTTOM_1360.bmp, 100, 100, 100, 100'
        
    elif res_y =='900':
        commonconfig['Cmdbar']['RectWH'] = '0, 0, 1024, 227'
        commonconfig['Bottom']['Image'] = 'assets/interface/human/interface_BOTTOM_1600.bmp, 100, 100, 100, 100'
            
    else:
        commonconfig['Cmdbar']['RectWH'] = '0, 0, 1024, 227'
        commonconfig['Bottom']['Image'] = 'assets/interface/human/interface_BOTTOM.bmp, 100, 100, 100, 100'

    with open('DATA\INTERFACE\CMDBAR.ini', 'w') as commonfile:
        commonconfig.write(commonfile)

    #EDITOR\infobar.ini
        
    infoconfig = configparser.ConfigParser(allow_no_value=True, strict=False)
    infoconfig.read('DATA\INTERFACE\EDITOR\INFOBAREDITOR.ini')

    if res_y == '1080':
        infoconfig['InfobarEditor']['RectWH'] = '0, 0, 1920, 80'
        infoconfig['Background']['RectWH'] = '0, 0, 1920, 80'
        infoconfig['Background']['Image'] = 'assets/interface/editor/cmdbar_hd.bmp'

    elif res_y == '720':
        infoconfig['InfobarEditor']['RectWH'] = '0, 0, 1280, 80'
        infoconfig['Background']['RectWH'] = '0, 0, 1280, 80'
        infoconfig['Background']['Image'] = 'assets/interface/editor/cmdbar.bmp'

    elif res_x == '1360':
        infoconfig['InfobarEditor']['RectWH'] = '0, 0, 1360, 80'
        infoconfig['Background']['RectWH'] = '0, 0, 1360, 80'
        infoconfig['Background']['Image'] = 'assets/interface/editor/cmdbar.bmp'

    elif res_y == '900':
        infoconfig['InfobarEditor']['RectWH'] = '0, 0, 1600, 80'
        infoconfig['Background']['RectWH'] = '0, 0, 1600, 80'
        infoconfig['Background']['Image'] = 'assets/interface/editor/cmdbar_hd.bmp'

    else:
        infoconfig['InfobarEditor']['RectWH'] = '0, 0, 1280, 80'
        infoconfig['Background']['RectWH'] = '0, 0, 1280, 80'
        infoconfig['Background']['Image'] = 'assets/interface/editor/cmdbar.bmp'

    with open('DATA\INTERFACE\EDITOR\INFOBAREDITOR.ini', 'w') as infofile:
        infoconfig.write(infofile)


    #EDITOR\cmdbar.ini
        
    editcmdconfig = configparser.ConfigParser(allow_no_value=True, strict=False)
    editcmdconfig.read('DATA\INTERFACE\EDITOR\CMDBAREDITOR.ini')

    if res_y == '1080':
        editcmdconfig['CmdbarEditor']['RectWH'] = '0, 0, 1920, 80'
        editcmdconfig['Background']['RectWH'] = '0, 0, 1920, 80'
        editcmdconfig['Background']['Image'] = 'assets/interface/editor/cmdbar_hd.bmp'

    elif res_y == '720':
        editcmdconfig['CmdbarEditor']['RectWH'] = '0, 0, 1280, 80'
        editcmdconfig['Background']['RectWH'] = '0, 0, 1280, 80'
        editcmdconfig['Background']['Image'] = 'assets/interface/editor/cmdbar.bmp'

    elif res_x == '1360':
        editcmdconfig['CmdbarEditor']['RectWH'] = '0, 0, 1360, 80'
        editcmdconfig['Background']['RectWH'] = '0, 0, 1360, 80'
        editcmdconfig['Background']['Image'] = 'assets/interface/editor/cmdbar.bmp'

    elif res_y == '900':
        editcmdconfig['CmdbarEditor']['RectWH'] = '0, 0, 1600, 80'
        editcmdconfig['Background']['RectWH'] = '0, 0, 1600, 80'
        editcmdconfig['Background']['Image'] = 'assets/interface/editor/cmdbar_hd.bmp'

    else:
        editcmdconfig['CmdbarEditor']['RectWH'] = '0, 0, 1280, 80'
        editcmdconfig['Background']['RectWH'] = '0, 0, 1280, 80'
        editcmdconfig['Background']['Image'] = 'assets/interface/editor/cmdbar.bmp'

    with open('DATA\INTERFACE\EDITOR\CMDBAREDITOR.ini', 'w') as editcmdfile:
        editcmdconfig.write(infofile)

        
blankspace_z = tk.Label(mainframe, width=2, height=2)
blankspace_z.grid(column=1, row=34)

#Default Settings

def default():
    username.set('Player')
    resolution.set('1024x768')
    sound.set('50')
    music.set('50')
    speech.set('50')
    scroll.set('50')
    fullscreen.set('1')
    lang.set('English')
    part.set('High')
    openspy.set('1')
    environ.set('0')
    transp.set('0')
    fog.set('0')
    wrapper.set('1')
    champ.set('1')
    hp_alt.set('2')
    hp_altsw.set('0')
    hp_ctrl.set('6')
    hp_ctrlsw.set('0')
    #keys.set('Original')
    
    

ttk.Button(mainframe, text="Reset to Default", command=default).grid(column=1, row=36, sticky=(W))

#Save
ttk.Button(mainframe, text="Save", command=save).grid(column=2, row=36, sticky=(E))

#Start
def start(): 
    save()
    import os
    os.system('"rk.exe"')
    root.destroy()

ttk.Button(mainframe, text="Start", command = start).grid(column=3, row=36, sticky=(W))

#Exit
ttk.Button(mainframe, text="Exit", command=lambda: root.destroy()).grid(column=4, row=36, sticky=(E))
root.mainloop()



