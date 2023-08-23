#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.2),
    on August 18, 2023, at 23:20
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.2'
expName = 'Dashboard'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\William Chen\\Desktop\\ResearchStudyDashboard\\Dashboard.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=True,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Start" ---
Start_Button = visual.ButtonStim(win, 
    text='Start', font='Open Sans',
    pos=(0, 0),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='Start_Button',
    depth=0
)
Start_Button.buttonClock = core.Clock()

# --- Initialize components for Routine "Cond" ---
ConditionTextBox = visual.TextBox2(
     win, text=None, placeholder='What robot condition is being used for this block?', font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(0.5, 0.5), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0, speechPoint=None,
     padding=0.0, alignment='center',
     anchor='center', overflow='visible',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='ConditionTextBox',
     depth=0, autoLog=True,
)
ConditionDone = visual.ButtonStim(win, 
    text='Done', font='Open Sans',
    pos=(0.0, -0.4),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='ConditionDone',
    depth=-1
)
ConditionDone.buttonClock = core.Clock()

# --- Initialize components for Routine "GR" ---
GetReady_Text = visual.TextStim(win=win, name='GetReady_Text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
GetRead_Cross = visual.ShapeStim(
    win=win, name='GetRead_Cross', vertices='cross',
    size=(0.2, 0.2),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "SS" ---
StorySentence_Text = visual.TextStim(win=win, name='StorySentence_Text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Rat" ---
Rating_Text = visual.TextStim(win=win, name='Rating_Text',
    text='How negative are you feeling?',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Rating_Response = visual.Slider(win=win, name='Rating_Response',
    startValue=None, size=(1.5, 0.15), pos=(0, -0.2), units=win.units,
    labels=("Not at all", "Slightly", "Moderately", "Very", "Extremely"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, ori=0.0, depth=-1, readOnly=False)
Rating_Done = visual.ButtonStim(win, 
    text='Done', font='Open Sans',
    pos=(0.5, -0.4),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='Rating_Done',
    depth=-2
)
Rating_Done.buttonClock = core.Clock()

# --- Initialize components for Routine "Trial" ---
Trial_NSB = visual.TextStim(win=win, name='Trial_NSB',
    text=NSBs,
    font='Open Sans',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Trial_Cue = visual.TextStim(win=win, name='Trial_Cue',
    text=Cue,
    font='Open Sans',
    pos=(0, -0.1), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Trial_RatingText = visual.TextStim(win=win, name='Trial_RatingText',
    text='How negative are you feeling?',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Trial_RatingResponse = visual.Slider(win=win, name='Trial_RatingResponse',
    startValue=None, size=(1.5, 0.15), pos=(0, -0.2), units=win.units,
    labels=("Not at all", "Slightly", "Moderately", "Very", "Extremely"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, ori=0.0, depth=-3, readOnly=False)
Trial_ResponseDone = visual.ButtonStim(win, 
    text='Done', font='Open Sans',
    pos=(0.5, -0.4),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='Trial_ResponseDone',
    depth=-4
)
Trial_ResponseDone.buttonClock = core.Clock()

# --- Initialize components for Routine "GR" ---
GetReady_Text = visual.TextStim(win=win, name='GetReady_Text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
GetRead_Cross = visual.ShapeStim(
    win=win, name='GetRead_Cross', vertices='cross',
    size=(0.2, 0.2),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "SS" ---
StorySentence_Text = visual.TextStim(win=win, name='StorySentence_Text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "NS" ---
NeutralStatement_Text = visual.TextStim(win=win, name='NeutralStatement_Text',
    text=NeutralStatement,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Rat" ---
Rating_Text = visual.TextStim(win=win, name='Rating_Text',
    text='How negative are you feeling?',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Rating_Response = visual.Slider(win=win, name='Rating_Response',
    startValue=None, size=(1.5, 0.15), pos=(0, -0.2), units=win.units,
    labels=("Not at all", "Slightly", "Moderately", "Very", "Extremely"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, ori=0.0, depth=-1, readOnly=False)
Rating_Done = visual.ButtonStim(win, 
    text='Done', font='Open Sans',
    pos=(0.5, -0.4),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='Rating_Done',
    depth=-2
)
Rating_Done.buttonClock = core.Clock()

# --- Initialize components for Routine "RegRat" ---
RegulationRating_Text = visual.TextStim(win=win, name='RegulationRating_Text',
    text='Emotion regulation helped me regulate my negativity compared to react.',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
RegulationRating_Response = visual.Slider(win=win, name='RegulationRating_Response',
    startValue=None, size=(1.5, 0.15), pos=(0, -0.2), units=win.units,
    labels=("strongly disagree", "disagree", "undecided", "agree", "strongly agree"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, ori=0.0, depth=-1, readOnly=False)
RegulationRating_Done = visual.ButtonStim(win, 
    text='Done', font='Open Sans',
    pos=(0.5, -0.4),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='RegulationRating_Done',
    depth=-2
)
RegulationRating_Done.buttonClock = core.Clock()

# --- Initialize components for Routine "BC" ---
BContinue_Button = visual.ButtonStim(win, 
    text='Continue', font='Open Sans',
    pos=(0, -0.1),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='BContinue_Button',
    depth=0
)
BContinue_Button.buttonClock = core.Clock()
BContinue_Text = visual.TextStim(win=win, name='BContinue_Text',
    text='Press CONTINUE when ready to move on to the next block.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Cond" ---
ConditionTextBox = visual.TextBox2(
     win, text=None, placeholder='What robot condition is being used for this block?', font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(0.5, 0.5), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0, speechPoint=None,
     padding=0.0, alignment='center',
     anchor='center', overflow='visible',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='ConditionTextBox',
     depth=0, autoLog=True,
)
ConditionDone = visual.ButtonStim(win, 
    text='Done', font='Open Sans',
    pos=(0.0, -0.4),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='ConditionDone',
    depth=-1
)
ConditionDone.buttonClock = core.Clock()

# --- Initialize components for Routine "GR" ---
GetReady_Text = visual.TextStim(win=win, name='GetReady_Text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
GetRead_Cross = visual.ShapeStim(
    win=win, name='GetRead_Cross', vertices='cross',
    size=(0.2, 0.2),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "SS" ---
StorySentence_Text = visual.TextStim(win=win, name='StorySentence_Text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Rat" ---
Rating_Text = visual.TextStim(win=win, name='Rating_Text',
    text='How negative are you feeling?',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Rating_Response = visual.Slider(win=win, name='Rating_Response',
    startValue=None, size=(1.5, 0.15), pos=(0, -0.2), units=win.units,
    labels=("Not at all", "Slightly", "Moderately", "Very", "Extremely"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, ori=0.0, depth=-1, readOnly=False)
Rating_Done = visual.ButtonStim(win, 
    text='Done', font='Open Sans',
    pos=(0.5, -0.4),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='Rating_Done',
    depth=-2
)
Rating_Done.buttonClock = core.Clock()

# --- Initialize components for Routine "Trial" ---
Trial_NSB = visual.TextStim(win=win, name='Trial_NSB',
    text=NSBs,
    font='Open Sans',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Trial_Cue = visual.TextStim(win=win, name='Trial_Cue',
    text=Cue,
    font='Open Sans',
    pos=(0, -0.1), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Trial_RatingText = visual.TextStim(win=win, name='Trial_RatingText',
    text='How negative are you feeling?',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Trial_RatingResponse = visual.Slider(win=win, name='Trial_RatingResponse',
    startValue=None, size=(1.5, 0.15), pos=(0, -0.2), units=win.units,
    labels=("Not at all", "Slightly", "Moderately", "Very", "Extremely"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, ori=0.0, depth=-3, readOnly=False)
Trial_ResponseDone = visual.ButtonStim(win, 
    text='Done', font='Open Sans',
    pos=(0.5, -0.4),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='Trial_ResponseDone',
    depth=-4
)
Trial_ResponseDone.buttonClock = core.Clock()

# --- Initialize components for Routine "GR" ---
GetReady_Text = visual.TextStim(win=win, name='GetReady_Text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
GetRead_Cross = visual.ShapeStim(
    win=win, name='GetRead_Cross', vertices='cross',
    size=(0.2, 0.2),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "SS" ---
StorySentence_Text = visual.TextStim(win=win, name='StorySentence_Text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "NS" ---
NeutralStatement_Text = visual.TextStim(win=win, name='NeutralStatement_Text',
    text=NeutralStatement,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Rat" ---
Rating_Text = visual.TextStim(win=win, name='Rating_Text',
    text='How negative are you feeling?',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Rating_Response = visual.Slider(win=win, name='Rating_Response',
    startValue=None, size=(1.5, 0.15), pos=(0, -0.2), units=win.units,
    labels=("Not at all", "Slightly", "Moderately", "Very", "Extremely"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, ori=0.0, depth=-1, readOnly=False)
Rating_Done = visual.ButtonStim(win, 
    text='Done', font='Open Sans',
    pos=(0.5, -0.4),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='Rating_Done',
    depth=-2
)
Rating_Done.buttonClock = core.Clock()

# --- Initialize components for Routine "RegRat" ---
RegulationRating_Text = visual.TextStim(win=win, name='RegulationRating_Text',
    text='Emotion regulation helped me regulate my negativity compared to react.',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
RegulationRating_Response = visual.Slider(win=win, name='RegulationRating_Response',
    startValue=None, size=(1.5, 0.15), pos=(0, -0.2), units=win.units,
    labels=("strongly disagree", "disagree", "undecided", "agree", "strongly agree"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, ori=0.0, depth=-1, readOnly=False)
RegulationRating_Done = visual.ButtonStim(win, 
    text='Done', font='Open Sans',
    pos=(0.5, -0.4),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='RegulationRating_Done',
    depth=-2
)
RegulationRating_Done.buttonClock = core.Clock()

# --- Initialize components for Routine "BC" ---
BContinue_Button = visual.ButtonStim(win, 
    text='Continue', font='Open Sans',
    pos=(0, -0.1),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='BContinue_Button',
    depth=0
)
BContinue_Button.buttonClock = core.Clock()
BContinue_Text = visual.TextStim(win=win, name='BContinue_Text',
    text='Press CONTINUE when ready to move on to the next block.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Cond" ---
ConditionTextBox = visual.TextBox2(
     win, text=None, placeholder='What robot condition is being used for this block?', font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(0.5, 0.5), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0, speechPoint=None,
     padding=0.0, alignment='center',
     anchor='center', overflow='visible',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='ConditionTextBox',
     depth=0, autoLog=True,
)
ConditionDone = visual.ButtonStim(win, 
    text='Done', font='Open Sans',
    pos=(0.0, -0.4),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='ConditionDone',
    depth=-1
)
ConditionDone.buttonClock = core.Clock()

# --- Initialize components for Routine "GR" ---
GetReady_Text = visual.TextStim(win=win, name='GetReady_Text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
GetRead_Cross = visual.ShapeStim(
    win=win, name='GetRead_Cross', vertices='cross',
    size=(0.2, 0.2),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "SS" ---
StorySentence_Text = visual.TextStim(win=win, name='StorySentence_Text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Rat" ---
Rating_Text = visual.TextStim(win=win, name='Rating_Text',
    text='How negative are you feeling?',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Rating_Response = visual.Slider(win=win, name='Rating_Response',
    startValue=None, size=(1.5, 0.15), pos=(0, -0.2), units=win.units,
    labels=("Not at all", "Slightly", "Moderately", "Very", "Extremely"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, ori=0.0, depth=-1, readOnly=False)
Rating_Done = visual.ButtonStim(win, 
    text='Done', font='Open Sans',
    pos=(0.5, -0.4),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='Rating_Done',
    depth=-2
)
Rating_Done.buttonClock = core.Clock()

# --- Initialize components for Routine "Trial" ---
Trial_NSB = visual.TextStim(win=win, name='Trial_NSB',
    text=NSBs,
    font='Open Sans',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Trial_Cue = visual.TextStim(win=win, name='Trial_Cue',
    text=Cue,
    font='Open Sans',
    pos=(0, -0.1), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Trial_RatingText = visual.TextStim(win=win, name='Trial_RatingText',
    text='How negative are you feeling?',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Trial_RatingResponse = visual.Slider(win=win, name='Trial_RatingResponse',
    startValue=None, size=(1.5, 0.15), pos=(0, -0.2), units=win.units,
    labels=("Not at all", "Slightly", "Moderately", "Very", "Extremely"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, ori=0.0, depth=-3, readOnly=False)
Trial_ResponseDone = visual.ButtonStim(win, 
    text='Done', font='Open Sans',
    pos=(0.5, -0.4),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='Trial_ResponseDone',
    depth=-4
)
Trial_ResponseDone.buttonClock = core.Clock()

# --- Initialize components for Routine "GR" ---
GetReady_Text = visual.TextStim(win=win, name='GetReady_Text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
GetRead_Cross = visual.ShapeStim(
    win=win, name='GetRead_Cross', vertices='cross',
    size=(0.2, 0.2),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "SS" ---
StorySentence_Text = visual.TextStim(win=win, name='StorySentence_Text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "NS" ---
NeutralStatement_Text = visual.TextStim(win=win, name='NeutralStatement_Text',
    text=NeutralStatement,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Rat" ---
Rating_Text = visual.TextStim(win=win, name='Rating_Text',
    text='How negative are you feeling?',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Rating_Response = visual.Slider(win=win, name='Rating_Response',
    startValue=None, size=(1.5, 0.15), pos=(0, -0.2), units=win.units,
    labels=("Not at all", "Slightly", "Moderately", "Very", "Extremely"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, ori=0.0, depth=-1, readOnly=False)
Rating_Done = visual.ButtonStim(win, 
    text='Done', font='Open Sans',
    pos=(0.5, -0.4),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='Rating_Done',
    depth=-2
)
Rating_Done.buttonClock = core.Clock()

# --- Initialize components for Routine "RegRat" ---
RegulationRating_Text = visual.TextStim(win=win, name='RegulationRating_Text',
    text='Emotion regulation helped me regulate my negativity compared to react.',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
RegulationRating_Response = visual.Slider(win=win, name='RegulationRating_Response',
    startValue=None, size=(1.5, 0.15), pos=(0, -0.2), units=win.units,
    labels=("strongly disagree", "disagree", "undecided", "agree", "strongly agree"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, ori=0.0, depth=-1, readOnly=False)
RegulationRating_Done = visual.ButtonStim(win, 
    text='Done', font='Open Sans',
    pos=(0.5, -0.4),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='RegulationRating_Done',
    depth=-2
)
RegulationRating_Done.buttonClock = core.Clock()

# --- Initialize components for Routine "BC" ---
BContinue_Button = visual.ButtonStim(win, 
    text='Continue', font='Open Sans',
    pos=(0, -0.1),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='BContinue_Button',
    depth=0
)
BContinue_Button.buttonClock = core.Clock()
BContinue_Text = visual.TextStim(win=win, name='BContinue_Text',
    text='Press CONTINUE when ready to move on to the next block.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Cond" ---
ConditionTextBox = visual.TextBox2(
     win, text=None, placeholder='What robot condition is being used for this block?', font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(0.5, 0.5), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0, speechPoint=None,
     padding=0.0, alignment='center',
     anchor='center', overflow='visible',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='ConditionTextBox',
     depth=0, autoLog=True,
)
ConditionDone = visual.ButtonStim(win, 
    text='Done', font='Open Sans',
    pos=(0.0, -0.4),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='ConditionDone',
    depth=-1
)
ConditionDone.buttonClock = core.Clock()

# --- Initialize components for Routine "GR" ---
GetReady_Text = visual.TextStim(win=win, name='GetReady_Text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
GetRead_Cross = visual.ShapeStim(
    win=win, name='GetRead_Cross', vertices='cross',
    size=(0.2, 0.2),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "SS" ---
StorySentence_Text = visual.TextStim(win=win, name='StorySentence_Text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Rat" ---
Rating_Text = visual.TextStim(win=win, name='Rating_Text',
    text='How negative are you feeling?',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Rating_Response = visual.Slider(win=win, name='Rating_Response',
    startValue=None, size=(1.5, 0.15), pos=(0, -0.2), units=win.units,
    labels=("Not at all", "Slightly", "Moderately", "Very", "Extremely"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, ori=0.0, depth=-1, readOnly=False)
Rating_Done = visual.ButtonStim(win, 
    text='Done', font='Open Sans',
    pos=(0.5, -0.4),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='Rating_Done',
    depth=-2
)
Rating_Done.buttonClock = core.Clock()

# --- Initialize components for Routine "Trial" ---
Trial_NSB = visual.TextStim(win=win, name='Trial_NSB',
    text=NSBs,
    font='Open Sans',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Trial_Cue = visual.TextStim(win=win, name='Trial_Cue',
    text=Cue,
    font='Open Sans',
    pos=(0, -0.1), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Trial_RatingText = visual.TextStim(win=win, name='Trial_RatingText',
    text='How negative are you feeling?',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Trial_RatingResponse = visual.Slider(win=win, name='Trial_RatingResponse',
    startValue=None, size=(1.5, 0.15), pos=(0, -0.2), units=win.units,
    labels=("Not at all", "Slightly", "Moderately", "Very", "Extremely"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, ori=0.0, depth=-3, readOnly=False)
Trial_ResponseDone = visual.ButtonStim(win, 
    text='Done', font='Open Sans',
    pos=(0.5, -0.4),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='Trial_ResponseDone',
    depth=-4
)
Trial_ResponseDone.buttonClock = core.Clock()

# --- Initialize components for Routine "GR" ---
GetReady_Text = visual.TextStim(win=win, name='GetReady_Text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
GetRead_Cross = visual.ShapeStim(
    win=win, name='GetRead_Cross', vertices='cross',
    size=(0.2, 0.2),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "SS" ---
StorySentence_Text = visual.TextStim(win=win, name='StorySentence_Text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "NS" ---
NeutralStatement_Text = visual.TextStim(win=win, name='NeutralStatement_Text',
    text=NeutralStatement,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Rat" ---
Rating_Text = visual.TextStim(win=win, name='Rating_Text',
    text='How negative are you feeling?',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Rating_Response = visual.Slider(win=win, name='Rating_Response',
    startValue=None, size=(1.5, 0.15), pos=(0, -0.2), units=win.units,
    labels=("Not at all", "Slightly", "Moderately", "Very", "Extremely"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, ori=0.0, depth=-1, readOnly=False)
Rating_Done = visual.ButtonStim(win, 
    text='Done', font='Open Sans',
    pos=(0.5, -0.4),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='Rating_Done',
    depth=-2
)
Rating_Done.buttonClock = core.Clock()

# --- Initialize components for Routine "RegRat" ---
RegulationRating_Text = visual.TextStim(win=win, name='RegulationRating_Text',
    text='Emotion regulation helped me regulate my negativity compared to react.',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
RegulationRating_Response = visual.Slider(win=win, name='RegulationRating_Response',
    startValue=None, size=(1.5, 0.15), pos=(0, -0.2), units=win.units,
    labels=("strongly disagree", "disagree", "undecided", "agree", "strongly agree"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, ori=0.0, depth=-1, readOnly=False)
RegulationRating_Done = visual.ButtonStim(win, 
    text='Done', font='Open Sans',
    pos=(0.5, -0.4),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='RegulationRating_Done',
    depth=-2
)
RegulationRating_Done.buttonClock = core.Clock()

# --- Initialize components for Routine "BC" ---
BContinue_Button = visual.ButtonStim(win, 
    text='Continue', font='Open Sans',
    pos=(0, -0.1),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='BContinue_Button',
    depth=0
)
BContinue_Button.buttonClock = core.Clock()
BContinue_Text = visual.TextStim(win=win, name='BContinue_Text',
    text='Press CONTINUE when ready to move on to the next block.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Cond" ---
ConditionTextBox = visual.TextBox2(
     win, text=None, placeholder='What robot condition is being used for this block?', font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(0.5, 0.5), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0, speechPoint=None,
     padding=0.0, alignment='center',
     anchor='center', overflow='visible',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='ConditionTextBox',
     depth=0, autoLog=True,
)
ConditionDone = visual.ButtonStim(win, 
    text='Done', font='Open Sans',
    pos=(0.0, -0.4),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='ConditionDone',
    depth=-1
)
ConditionDone.buttonClock = core.Clock()

# --- Initialize components for Routine "GR" ---
GetReady_Text = visual.TextStim(win=win, name='GetReady_Text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
GetRead_Cross = visual.ShapeStim(
    win=win, name='GetRead_Cross', vertices='cross',
    size=(0.2, 0.2),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "SS" ---
StorySentence_Text = visual.TextStim(win=win, name='StorySentence_Text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Rat" ---
Rating_Text = visual.TextStim(win=win, name='Rating_Text',
    text='How negative are you feeling?',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Rating_Response = visual.Slider(win=win, name='Rating_Response',
    startValue=None, size=(1.5, 0.15), pos=(0, -0.2), units=win.units,
    labels=("Not at all", "Slightly", "Moderately", "Very", "Extremely"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, ori=0.0, depth=-1, readOnly=False)
Rating_Done = visual.ButtonStim(win, 
    text='Done', font='Open Sans',
    pos=(0.5, -0.4),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='Rating_Done',
    depth=-2
)
Rating_Done.buttonClock = core.Clock()

# --- Initialize components for Routine "Trial" ---
Trial_NSB = visual.TextStim(win=win, name='Trial_NSB',
    text=NSBs,
    font='Open Sans',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Trial_Cue = visual.TextStim(win=win, name='Trial_Cue',
    text=Cue,
    font='Open Sans',
    pos=(0, -0.1), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Trial_RatingText = visual.TextStim(win=win, name='Trial_RatingText',
    text='How negative are you feeling?',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Trial_RatingResponse = visual.Slider(win=win, name='Trial_RatingResponse',
    startValue=None, size=(1.5, 0.15), pos=(0, -0.2), units=win.units,
    labels=("Not at all", "Slightly", "Moderately", "Very", "Extremely"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, ori=0.0, depth=-3, readOnly=False)
Trial_ResponseDone = visual.ButtonStim(win, 
    text='Done', font='Open Sans',
    pos=(0.5, -0.4),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='Trial_ResponseDone',
    depth=-4
)
Trial_ResponseDone.buttonClock = core.Clock()

# --- Initialize components for Routine "GR" ---
GetReady_Text = visual.TextStim(win=win, name='GetReady_Text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
GetRead_Cross = visual.ShapeStim(
    win=win, name='GetRead_Cross', vertices='cross',
    size=(0.2, 0.2),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "SS" ---
StorySentence_Text = visual.TextStim(win=win, name='StorySentence_Text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "NS" ---
NeutralStatement_Text = visual.TextStim(win=win, name='NeutralStatement_Text',
    text=NeutralStatement,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Rat" ---
Rating_Text = visual.TextStim(win=win, name='Rating_Text',
    text='How negative are you feeling?',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Rating_Response = visual.Slider(win=win, name='Rating_Response',
    startValue=None, size=(1.5, 0.15), pos=(0, -0.2), units=win.units,
    labels=("Not at all", "Slightly", "Moderately", "Very", "Extremely"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, ori=0.0, depth=-1, readOnly=False)
Rating_Done = visual.ButtonStim(win, 
    text='Done', font='Open Sans',
    pos=(0.5, -0.4),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='Rating_Done',
    depth=-2
)
Rating_Done.buttonClock = core.Clock()

# --- Initialize components for Routine "RegRat" ---
RegulationRating_Text = visual.TextStim(win=win, name='RegulationRating_Text',
    text='Emotion regulation helped me regulate my negativity compared to react.',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
RegulationRating_Response = visual.Slider(win=win, name='RegulationRating_Response',
    startValue=None, size=(1.5, 0.15), pos=(0, -0.2), units=win.units,
    labels=("strongly disagree", "disagree", "undecided", "agree", "strongly agree"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, ori=0.0, depth=-1, readOnly=False)
RegulationRating_Done = visual.ButtonStim(win, 
    text='Done', font='Open Sans',
    pos=(0.5, -0.4),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='RegulationRating_Done',
    depth=-2
)
RegulationRating_Done.buttonClock = core.Clock()

# --- Initialize components for Routine "BC" ---
BContinue_Button = visual.ButtonStim(win, 
    text='Continue', font='Open Sans',
    pos=(0, -0.1),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='BContinue_Button',
    depth=0
)
BContinue_Button.buttonClock = core.Clock()
BContinue_Text = visual.TextStim(win=win, name='BContinue_Text',
    text='Press CONTINUE when ready to move on to the next block.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Cond" ---
ConditionTextBox = visual.TextBox2(
     win, text=None, placeholder='What robot condition is being used for this block?', font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(0.5, 0.5), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0, speechPoint=None,
     padding=0.0, alignment='center',
     anchor='center', overflow='visible',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='ConditionTextBox',
     depth=0, autoLog=True,
)
ConditionDone = visual.ButtonStim(win, 
    text='Done', font='Open Sans',
    pos=(0.0, -0.4),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='ConditionDone',
    depth=-1
)
ConditionDone.buttonClock = core.Clock()

# --- Initialize components for Routine "GR" ---
GetReady_Text = visual.TextStim(win=win, name='GetReady_Text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
GetRead_Cross = visual.ShapeStim(
    win=win, name='GetRead_Cross', vertices='cross',
    size=(0.2, 0.2),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "SS" ---
StorySentence_Text = visual.TextStim(win=win, name='StorySentence_Text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Rat" ---
Rating_Text = visual.TextStim(win=win, name='Rating_Text',
    text='How negative are you feeling?',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Rating_Response = visual.Slider(win=win, name='Rating_Response',
    startValue=None, size=(1.5, 0.15), pos=(0, -0.2), units=win.units,
    labels=("Not at all", "Slightly", "Moderately", "Very", "Extremely"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, ori=0.0, depth=-1, readOnly=False)
Rating_Done = visual.ButtonStim(win, 
    text='Done', font='Open Sans',
    pos=(0.5, -0.4),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='Rating_Done',
    depth=-2
)
Rating_Done.buttonClock = core.Clock()

# --- Initialize components for Routine "Trial" ---
Trial_NSB = visual.TextStim(win=win, name='Trial_NSB',
    text=NSBs,
    font='Open Sans',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Trial_Cue = visual.TextStim(win=win, name='Trial_Cue',
    text=Cue,
    font='Open Sans',
    pos=(0, -0.1), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Trial_RatingText = visual.TextStim(win=win, name='Trial_RatingText',
    text='How negative are you feeling?',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Trial_RatingResponse = visual.Slider(win=win, name='Trial_RatingResponse',
    startValue=None, size=(1.5, 0.15), pos=(0, -0.2), units=win.units,
    labels=("Not at all", "Slightly", "Moderately", "Very", "Extremely"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, ori=0.0, depth=-3, readOnly=False)
Trial_ResponseDone = visual.ButtonStim(win, 
    text='Done', font='Open Sans',
    pos=(0.5, -0.4),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='Trial_ResponseDone',
    depth=-4
)
Trial_ResponseDone.buttonClock = core.Clock()

# --- Initialize components for Routine "GR" ---
GetReady_Text = visual.TextStim(win=win, name='GetReady_Text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
GetRead_Cross = visual.ShapeStim(
    win=win, name='GetRead_Cross', vertices='cross',
    size=(0.2, 0.2),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "SS" ---
StorySentence_Text = visual.TextStim(win=win, name='StorySentence_Text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "NS" ---
NeutralStatement_Text = visual.TextStim(win=win, name='NeutralStatement_Text',
    text=NeutralStatement,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Rat" ---
Rating_Text = visual.TextStim(win=win, name='Rating_Text',
    text='How negative are you feeling?',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Rating_Response = visual.Slider(win=win, name='Rating_Response',
    startValue=None, size=(1.5, 0.15), pos=(0, -0.2), units=win.units,
    labels=("Not at all", "Slightly", "Moderately", "Very", "Extremely"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, ori=0.0, depth=-1, readOnly=False)
Rating_Done = visual.ButtonStim(win, 
    text='Done', font='Open Sans',
    pos=(0.5, -0.4),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='Rating_Done',
    depth=-2
)
Rating_Done.buttonClock = core.Clock()

# --- Initialize components for Routine "RegRat" ---
RegulationRating_Text = visual.TextStim(win=win, name='RegulationRating_Text',
    text='Emotion regulation helped me regulate my negativity compared to react.',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
RegulationRating_Response = visual.Slider(win=win, name='RegulationRating_Response',
    startValue=None, size=(1.5, 0.15), pos=(0, -0.2), units=win.units,
    labels=("strongly disagree", "disagree", "undecided", "agree", "strongly agree"), ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.04,
    flip=False, ori=0.0, depth=-1, readOnly=False)
RegulationRating_Done = visual.ButtonStim(win, 
    text='Done', font='Open Sans',
    pos=(0.5, -0.4),
    letterHeight=0.05,
    size=(0.2, 0.1), borderWidth=0.0,
    fillColor=[-0.3333, -0.1608, -0.6314], borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='RegulationRating_Done',
    depth=-2
)
RegulationRating_Done.buttonClock = core.Clock()

# --- Initialize components for Routine "End" ---
text = visual.TextStim(win=win, name='text',
    text='End of the experiment. \n\nThank you for participating!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Start" ---
continueRoutine = True
# update component parameters for each repeat
# reset Start_Button to account for continued clicks & clear times on/off
Start_Button.reset()
# keep track of which components have finished
StartComponents = [Start_Button]
for thisComponent in StartComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Start" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *Start_Button* updates
    
    # if Start_Button is starting this frame...
    if Start_Button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Start_Button.frameNStart = frameN  # exact frame index
        Start_Button.tStart = t  # local t and not account for scr refresh
        Start_Button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Start_Button, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Start_Button.started')
        # update status
        Start_Button.status = STARTED
        Start_Button.setAutoDraw(True)
    
    # if Start_Button is active this frame...
    if Start_Button.status == STARTED:
        # update params
        pass
        # check whether Start_Button has been pressed
        if Start_Button.isClicked:
            if not Start_Button.wasClicked:
                # if this is a new click, store time of first click and clicked until
                Start_Button.timesOn.append(Start_Button.buttonClock.getTime())
                Start_Button.timesOff.append(Start_Button.buttonClock.getTime())
            elif len(Start_Button.timesOff):
                # if click is continuing from last frame, update time of clicked until
                Start_Button.timesOff[-1] = Start_Button.buttonClock.getTime()
            if not Start_Button.wasClicked:
                # end routine when Start_Button is clicked
                continueRoutine = False
            if not Start_Button.wasClicked:
                # run callback code when Start_Button is clicked
                pass
    # take note of whether Start_Button was clicked, so that next frame we know if clicks are new
    Start_Button.wasClicked = Start_Button.isClicked and Start_Button.status == STARTED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Start" ---
for thisComponent in StartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Start_Button.numClicks', Start_Button.numClicks)
if Start_Button.numClicks:
   thisExp.addData('Start_Button.timesOn', Start_Button.timesOn)
   thisExp.addData('Start_Button.timesOff', Start_Button.timesOff)
else:
   thisExp.addData('Start_Button.timesOn', "")
   thisExp.addData('Start_Button.timesOff', "")
# the Routine "Start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Cond" ---
continueRoutine = True
# update component parameters for each repeat
ConditionTextBox.reset()
# reset ConditionDone to account for continued clicks & clear times on/off
ConditionDone.reset()
# keep track of which components have finished
CondComponents = [ConditionTextBox, ConditionDone]
for thisComponent in CondComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Cond" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ConditionTextBox* updates
    
    # if ConditionTextBox is starting this frame...
    if ConditionTextBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ConditionTextBox.frameNStart = frameN  # exact frame index
        ConditionTextBox.tStart = t  # local t and not account for scr refresh
        ConditionTextBox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ConditionTextBox, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ConditionTextBox.started')
        # update status
        ConditionTextBox.status = STARTED
        ConditionTextBox.setAutoDraw(True)
    
    # if ConditionTextBox is active this frame...
    if ConditionTextBox.status == STARTED:
        # update params
        pass
    # *ConditionDone* updates
    
    # if ConditionDone is starting this frame...
    if ConditionDone.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        ConditionDone.frameNStart = frameN  # exact frame index
        ConditionDone.tStart = t  # local t and not account for scr refresh
        ConditionDone.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ConditionDone, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ConditionDone.started')
        # update status
        ConditionDone.status = STARTED
        ConditionDone.setAutoDraw(True)
    
    # if ConditionDone is active this frame...
    if ConditionDone.status == STARTED:
        # update params
        pass
        # check whether ConditionDone has been pressed
        if ConditionDone.isClicked:
            if not ConditionDone.wasClicked:
                # if this is a new click, store time of first click and clicked until
                ConditionDone.timesOn.append(ConditionDone.buttonClock.getTime())
                ConditionDone.timesOff.append(ConditionDone.buttonClock.getTime())
            elif len(ConditionDone.timesOff):
                # if click is continuing from last frame, update time of clicked until
                ConditionDone.timesOff[-1] = ConditionDone.buttonClock.getTime()
            if not ConditionDone.wasClicked:
                # end routine when ConditionDone is clicked
                continueRoutine = False
            if not ConditionDone.wasClicked:
                # run callback code when ConditionDone is clicked
                pass
    # take note of whether ConditionDone was clicked, so that next frame we know if clicks are new
    ConditionDone.wasClicked = ConditionDone.isClicked and ConditionDone.status == STARTED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CondComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Cond" ---
for thisComponent in CondComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ConditionTextBox.text',ConditionTextBox.text)
thisExp.addData('ConditionDone.numClicks', ConditionDone.numClicks)
if ConditionDone.numClicks:
   thisExp.addData('ConditionDone.timesOn', ConditionDone.timesOn)
   thisExp.addData('ConditionDone.timesOff', ConditionDone.timesOff)
else:
   thisExp.addData('ConditionDone.timesOn', "")
   thisExp.addData('ConditionDone.timesOff', "")
# the Routine "Cond" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "GR" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
GRComponents = [GetReady_Text, GetRead_Cross]
for thisComponent in GRComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "GR" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *GetReady_Text* updates
    
    # if GetReady_Text is starting this frame...
    if GetReady_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GetReady_Text.frameNStart = frameN  # exact frame index
        GetReady_Text.tStart = t  # local t and not account for scr refresh
        GetReady_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GetReady_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'GetReady_Text.started')
        # update status
        GetReady_Text.status = STARTED
        GetReady_Text.setAutoDraw(True)
    
    # if GetReady_Text is active this frame...
    if GetReady_Text.status == STARTED:
        # update params
        GetReady_Text.setText('', log=False)
    
    # if GetReady_Text is stopping this frame...
    if GetReady_Text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > GetReady_Text.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            GetReady_Text.tStop = t  # not accounting for scr refresh
            GetReady_Text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'GetReady_Text.stopped')
            # update status
            GetReady_Text.status = FINISHED
            GetReady_Text.setAutoDraw(False)
    
    # *GetRead_Cross* updates
    
    # if GetRead_Cross is starting this frame...
    if GetRead_Cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GetRead_Cross.frameNStart = frameN  # exact frame index
        GetRead_Cross.tStart = t  # local t and not account for scr refresh
        GetRead_Cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GetRead_Cross, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'GetRead_Cross.started')
        # update status
        GetRead_Cross.status = STARTED
        GetRead_Cross.setAutoDraw(True)
    
    # if GetRead_Cross is active this frame...
    if GetRead_Cross.status == STARTED:
        # update params
        pass
    
    # if GetRead_Cross is stopping this frame...
    if GetRead_Cross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > GetRead_Cross.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            GetRead_Cross.tStop = t  # not accounting for scr refresh
            GetRead_Cross.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'GetRead_Cross.stopped')
            # update status
            GetRead_Cross.status = FINISHED
            GetRead_Cross.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GRComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "GR" ---
for thisComponent in GRComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# set up handler to look after randomisation of conditions etc
Neg1 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PsychopyIntegrationSheets/Negative1.xlsx'),
    seed=None, name='Neg1')
thisExp.addLoop(Neg1)  # add the loop to the experiment
thisNeg1 = Neg1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNeg1.rgb)
if thisNeg1 != None:
    for paramName in thisNeg1:
        exec('{} = thisNeg1[paramName]'.format(paramName))

for thisNeg1 in Neg1:
    currentLoop = Neg1
    # abbreviate parameter names if possible (e.g. rgb = thisNeg1.rgb)
    if thisNeg1 != None:
        for paramName in thisNeg1:
            exec('{} = thisNeg1[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "SS" ---
    continueRoutine = True
    # update component parameters for each repeat
    StorySentence_Text.setText(StorySentences)
    # keep track of which components have finished
    SSComponents = [StorySentence_Text]
    for thisComponent in SSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "SS" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *StorySentence_Text* updates
        
        # if StorySentence_Text is starting this frame...
        if StorySentence_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StorySentence_Text.frameNStart = frameN  # exact frame index
            StorySentence_Text.tStart = t  # local t and not account for scr refresh
            StorySentence_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StorySentence_Text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'StorySentence_Text.started')
            # update status
            StorySentence_Text.status = STARTED
            StorySentence_Text.setAutoDraw(True)
        
        # if StorySentence_Text is active this frame...
        if StorySentence_Text.status == STARTED:
            # update params
            pass
        
        # if StorySentence_Text is stopping this frame...
        if StorySentence_Text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StorySentence_Text.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                StorySentence_Text.tStop = t  # not accounting for scr refresh
                StorySentence_Text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'StorySentence_Text.stopped')
                # update status
                StorySentence_Text.status = FINISHED
                StorySentence_Text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "SS" ---
    for thisComponent in SSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Neg1'


# --- Prepare to start Routine "Rat" ---
continueRoutine = True
# update component parameters for each repeat
Rating_Response.reset()
# reset Rating_Done to account for continued clicks & clear times on/off
Rating_Done.reset()
# keep track of which components have finished
RatComponents = [Rating_Text, Rating_Response, Rating_Done]
for thisComponent in RatComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Rat" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Rating_Text* updates
    
    # if Rating_Text is starting this frame...
    if Rating_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rating_Text.frameNStart = frameN  # exact frame index
        Rating_Text.tStart = t  # local t and not account for scr refresh
        Rating_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Text.started')
        # update status
        Rating_Text.status = STARTED
        Rating_Text.setAutoDraw(True)
    
    # if Rating_Text is active this frame...
    if Rating_Text.status == STARTED:
        # update params
        pass
    
    # *Rating_Response* updates
    
    # if Rating_Response is starting this frame...
    if Rating_Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rating_Response.frameNStart = frameN  # exact frame index
        Rating_Response.tStart = t  # local t and not account for scr refresh
        Rating_Response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Response, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Response.started')
        # update status
        Rating_Response.status = STARTED
        Rating_Response.setAutoDraw(True)
    
    # if Rating_Response is active this frame...
    if Rating_Response.status == STARTED:
        # update params
        pass
    # *Rating_Done* updates
    
    # if Rating_Done is starting this frame...
    if Rating_Done.status == NOT_STARTED and Rating_Response.getRating() != None:
        # keep track of start time/frame for later
        Rating_Done.frameNStart = frameN  # exact frame index
        Rating_Done.tStart = t  # local t and not account for scr refresh
        Rating_Done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Done, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Done.started')
        # update status
        Rating_Done.status = STARTED
        Rating_Done.setAutoDraw(True)
    
    # if Rating_Done is active this frame...
    if Rating_Done.status == STARTED:
        # update params
        pass
        # check whether Rating_Done has been pressed
        if Rating_Done.isClicked:
            if not Rating_Done.wasClicked:
                # if this is a new click, store time of first click and clicked until
                Rating_Done.timesOn.append(Rating_Done.buttonClock.getTime())
                Rating_Done.timesOff.append(Rating_Done.buttonClock.getTime())
            elif len(Rating_Done.timesOff):
                # if click is continuing from last frame, update time of clicked until
                Rating_Done.timesOff[-1] = Rating_Done.buttonClock.getTime()
            if not Rating_Done.wasClicked:
                # end routine when Rating_Done is clicked
                continueRoutine = False
            if not Rating_Done.wasClicked:
                # run callback code when Rating_Done is clicked
                pass
    # take note of whether Rating_Done was clicked, so that next frame we know if clicks are new
    Rating_Done.wasClicked = Rating_Done.isClicked and Rating_Done.status == STARTED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RatComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Rat" ---
for thisComponent in RatComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Rating_Response.response', Rating_Response.getRating())
thisExp.addData('Rating_Response.rt', Rating_Response.getRT())
thisExp.addData('Rating_Done.numClicks', Rating_Done.numClicks)
if Rating_Done.numClicks:
   thisExp.addData('Rating_Done.timesOn', Rating_Done.timesOn)
   thisExp.addData('Rating_Done.timesOff', Rating_Done.timesOff)
else:
   thisExp.addData('Rating_Done.timesOn', "")
   thisExp.addData('Rating_Done.timesOff', "")
# the Routine "Rat" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
NSB1 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PsychopyIntegrationSheets/NSB1.xlsx'),
    seed=None, name='NSB1')
thisExp.addLoop(NSB1)  # add the loop to the experiment
thisNSB1 = NSB1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNSB1.rgb)
if thisNSB1 != None:
    for paramName in thisNSB1:
        exec('{} = thisNSB1[paramName]'.format(paramName))

for thisNSB1 in NSB1:
    currentLoop = NSB1
    # abbreviate parameter names if possible (e.g. rgb = thisNSB1.rgb)
    if thisNSB1 != None:
        for paramName in thisNSB1:
            exec('{} = thisNSB1[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    Trial_RatingResponse.reset()
    # reset Trial_ResponseDone to account for continued clicks & clear times on/off
    Trial_ResponseDone.reset()
    # keep track of which components have finished
    TrialComponents = [Trial_NSB, Trial_Cue, Trial_RatingText, Trial_RatingResponse, Trial_ResponseDone]
    for thisComponent in TrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Trial" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Trial_NSB* updates
        
        # if Trial_NSB is starting this frame...
        if Trial_NSB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Trial_NSB.frameNStart = frameN  # exact frame index
            Trial_NSB.tStart = t  # local t and not account for scr refresh
            Trial_NSB.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_NSB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_NSB.started')
            # update status
            Trial_NSB.status = STARTED
            Trial_NSB.setAutoDraw(True)
        
        # if Trial_NSB is active this frame...
        if Trial_NSB.status == STARTED:
            # update params
            pass
        
        # if Trial_NSB is stopping this frame...
        if Trial_NSB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Trial_NSB.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                Trial_NSB.tStop = t  # not accounting for scr refresh
                Trial_NSB.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Trial_NSB.stopped')
                # update status
                Trial_NSB.status = FINISHED
                Trial_NSB.setAutoDraw(False)
        
        # *Trial_Cue* updates
        
        # if Trial_Cue is starting this frame...
        if Trial_Cue.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            Trial_Cue.frameNStart = frameN  # exact frame index
            Trial_Cue.tStart = t  # local t and not account for scr refresh
            Trial_Cue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_Cue, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_Cue.started')
            # update status
            Trial_Cue.status = STARTED
            Trial_Cue.setAutoDraw(True)
        
        # if Trial_Cue is active this frame...
        if Trial_Cue.status == STARTED:
            # update params
            pass
        
        # if Trial_Cue is stopping this frame...
        if Trial_Cue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Trial_Cue.tStartRefresh + 12-frameTolerance:
                # keep track of stop time/frame for later
                Trial_Cue.tStop = t  # not accounting for scr refresh
                Trial_Cue.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Trial_Cue.stopped')
                # update status
                Trial_Cue.status = FINISHED
                Trial_Cue.setAutoDraw(False)
        
        # *Trial_RatingText* updates
        
        # if Trial_RatingText is starting this frame...
        if Trial_RatingText.status == NOT_STARTED and tThisFlip >= 15-frameTolerance:
            # keep track of start time/frame for later
            Trial_RatingText.frameNStart = frameN  # exact frame index
            Trial_RatingText.tStart = t  # local t and not account for scr refresh
            Trial_RatingText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_RatingText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_RatingText.started')
            # update status
            Trial_RatingText.status = STARTED
            Trial_RatingText.setAutoDraw(True)
        
        # if Trial_RatingText is active this frame...
        if Trial_RatingText.status == STARTED:
            # update params
            pass
        
        # *Trial_RatingResponse* updates
        
        # if Trial_RatingResponse is starting this frame...
        if Trial_RatingResponse.status == NOT_STARTED and tThisFlip >= 15-frameTolerance:
            # keep track of start time/frame for later
            Trial_RatingResponse.frameNStart = frameN  # exact frame index
            Trial_RatingResponse.tStart = t  # local t and not account for scr refresh
            Trial_RatingResponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_RatingResponse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_RatingResponse.started')
            # update status
            Trial_RatingResponse.status = STARTED
            Trial_RatingResponse.setAutoDraw(True)
        
        # if Trial_RatingResponse is active this frame...
        if Trial_RatingResponse.status == STARTED:
            # update params
            pass
        # *Trial_ResponseDone* updates
        
        # if Trial_ResponseDone is starting this frame...
        if Trial_ResponseDone.status == NOT_STARTED and Trial_RatingResponse.getRating() != None:
            # keep track of start time/frame for later
            Trial_ResponseDone.frameNStart = frameN  # exact frame index
            Trial_ResponseDone.tStart = t  # local t and not account for scr refresh
            Trial_ResponseDone.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_ResponseDone, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_ResponseDone.started')
            # update status
            Trial_ResponseDone.status = STARTED
            Trial_ResponseDone.setAutoDraw(True)
        
        # if Trial_ResponseDone is active this frame...
        if Trial_ResponseDone.status == STARTED:
            # update params
            pass
            # check whether Trial_ResponseDone has been pressed
            if Trial_ResponseDone.isClicked:
                if not Trial_ResponseDone.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    Trial_ResponseDone.timesOn.append(Trial_ResponseDone.buttonClock.getTime())
                    Trial_ResponseDone.timesOff.append(Trial_ResponseDone.buttonClock.getTime())
                elif len(Trial_ResponseDone.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    Trial_ResponseDone.timesOff[-1] = Trial_ResponseDone.buttonClock.getTime()
                if not Trial_ResponseDone.wasClicked:
                    # end routine when Trial_ResponseDone is clicked
                    continueRoutine = False
                if not Trial_ResponseDone.wasClicked:
                    # run callback code when Trial_ResponseDone is clicked
                    pass
        # take note of whether Trial_ResponseDone was clicked, so that next frame we know if clicks are new
        Trial_ResponseDone.wasClicked = Trial_ResponseDone.isClicked and Trial_ResponseDone.status == STARTED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Trial" ---
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    NSB1.addData('Trial_RatingResponse.response', Trial_RatingResponse.getRating())
    NSB1.addData('Trial_RatingResponse.rt', Trial_RatingResponse.getRT())
    NSB1.addData('Trial_ResponseDone.numClicks', Trial_ResponseDone.numClicks)
    if Trial_ResponseDone.numClicks:
       NSB1.addData('Trial_ResponseDone.timesOn', Trial_ResponseDone.timesOn)
       NSB1.addData('Trial_ResponseDone.timesOff', Trial_ResponseDone.timesOff)
    else:
       NSB1.addData('Trial_ResponseDone.timesOn', "")
       NSB1.addData('Trial_ResponseDone.timesOff', "")
    # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'NSB1'


# --- Prepare to start Routine "GR" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
GRComponents = [GetReady_Text, GetRead_Cross]
for thisComponent in GRComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "GR" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *GetReady_Text* updates
    
    # if GetReady_Text is starting this frame...
    if GetReady_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GetReady_Text.frameNStart = frameN  # exact frame index
        GetReady_Text.tStart = t  # local t and not account for scr refresh
        GetReady_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GetReady_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'GetReady_Text.started')
        # update status
        GetReady_Text.status = STARTED
        GetReady_Text.setAutoDraw(True)
    
    # if GetReady_Text is active this frame...
    if GetReady_Text.status == STARTED:
        # update params
        GetReady_Text.setText('', log=False)
    
    # if GetReady_Text is stopping this frame...
    if GetReady_Text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > GetReady_Text.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            GetReady_Text.tStop = t  # not accounting for scr refresh
            GetReady_Text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'GetReady_Text.stopped')
            # update status
            GetReady_Text.status = FINISHED
            GetReady_Text.setAutoDraw(False)
    
    # *GetRead_Cross* updates
    
    # if GetRead_Cross is starting this frame...
    if GetRead_Cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GetRead_Cross.frameNStart = frameN  # exact frame index
        GetRead_Cross.tStart = t  # local t and not account for scr refresh
        GetRead_Cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GetRead_Cross, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'GetRead_Cross.started')
        # update status
        GetRead_Cross.status = STARTED
        GetRead_Cross.setAutoDraw(True)
    
    # if GetRead_Cross is active this frame...
    if GetRead_Cross.status == STARTED:
        # update params
        pass
    
    # if GetRead_Cross is stopping this frame...
    if GetRead_Cross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > GetRead_Cross.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            GetRead_Cross.tStop = t  # not accounting for scr refresh
            GetRead_Cross.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'GetRead_Cross.stopped')
            # update status
            GetRead_Cross.status = FINISHED
            GetRead_Cross.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GRComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "GR" ---
for thisComponent in GRComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# set up handler to look after randomisation of conditions etc
Neu1 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PsychopyIntegrationSheets/Neutral1.xlsx'),
    seed=None, name='Neu1')
thisExp.addLoop(Neu1)  # add the loop to the experiment
thisNeu1 = Neu1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNeu1.rgb)
if thisNeu1 != None:
    for paramName in thisNeu1:
        exec('{} = thisNeu1[paramName]'.format(paramName))

for thisNeu1 in Neu1:
    currentLoop = Neu1
    # abbreviate parameter names if possible (e.g. rgb = thisNeu1.rgb)
    if thisNeu1 != None:
        for paramName in thisNeu1:
            exec('{} = thisNeu1[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "SS" ---
    continueRoutine = True
    # update component parameters for each repeat
    StorySentence_Text.setText(StorySentences)
    # keep track of which components have finished
    SSComponents = [StorySentence_Text]
    for thisComponent in SSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "SS" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *StorySentence_Text* updates
        
        # if StorySentence_Text is starting this frame...
        if StorySentence_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StorySentence_Text.frameNStart = frameN  # exact frame index
            StorySentence_Text.tStart = t  # local t and not account for scr refresh
            StorySentence_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StorySentence_Text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'StorySentence_Text.started')
            # update status
            StorySentence_Text.status = STARTED
            StorySentence_Text.setAutoDraw(True)
        
        # if StorySentence_Text is active this frame...
        if StorySentence_Text.status == STARTED:
            # update params
            pass
        
        # if StorySentence_Text is stopping this frame...
        if StorySentence_Text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StorySentence_Text.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                StorySentence_Text.tStop = t  # not accounting for scr refresh
                StorySentence_Text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'StorySentence_Text.stopped')
                # update status
                StorySentence_Text.status = FINISHED
                StorySentence_Text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "SS" ---
    for thisComponent in SSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Neu1'


# set up handler to look after randomisation of conditions etc
NeuSta1 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PsychopyIntegrationSheets/NeutralStatements1.xlsx'),
    seed=None, name='NeuSta1')
thisExp.addLoop(NeuSta1)  # add the loop to the experiment
thisNeuSta1 = NeuSta1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNeuSta1.rgb)
if thisNeuSta1 != None:
    for paramName in thisNeuSta1:
        exec('{} = thisNeuSta1[paramName]'.format(paramName))

for thisNeuSta1 in NeuSta1:
    currentLoop = NeuSta1
    # abbreviate parameter names if possible (e.g. rgb = thisNeuSta1.rgb)
    if thisNeuSta1 != None:
        for paramName in thisNeuSta1:
            exec('{} = thisNeuSta1[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "NS" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    NSComponents = [NeutralStatement_Text]
    for thisComponent in NSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "NS" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 12.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NeutralStatement_Text* updates
        
        # if NeutralStatement_Text is starting this frame...
        if NeutralStatement_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NeutralStatement_Text.frameNStart = frameN  # exact frame index
            NeutralStatement_Text.tStart = t  # local t and not account for scr refresh
            NeutralStatement_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NeutralStatement_Text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NeutralStatement_Text.started')
            # update status
            NeutralStatement_Text.status = STARTED
            NeutralStatement_Text.setAutoDraw(True)
        
        # if NeutralStatement_Text is active this frame...
        if NeutralStatement_Text.status == STARTED:
            # update params
            pass
        
        # if NeutralStatement_Text is stopping this frame...
        if NeutralStatement_Text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > NeutralStatement_Text.tStartRefresh + 12-frameTolerance:
                # keep track of stop time/frame for later
                NeutralStatement_Text.tStop = t  # not accounting for scr refresh
                NeutralStatement_Text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'NeutralStatement_Text.stopped')
                # update status
                NeutralStatement_Text.status = FINISHED
                NeutralStatement_Text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "NS" ---
    for thisComponent in NSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-12.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'NeuSta1'


# --- Prepare to start Routine "Rat" ---
continueRoutine = True
# update component parameters for each repeat
Rating_Response.reset()
# reset Rating_Done to account for continued clicks & clear times on/off
Rating_Done.reset()
# keep track of which components have finished
RatComponents = [Rating_Text, Rating_Response, Rating_Done]
for thisComponent in RatComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Rat" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Rating_Text* updates
    
    # if Rating_Text is starting this frame...
    if Rating_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rating_Text.frameNStart = frameN  # exact frame index
        Rating_Text.tStart = t  # local t and not account for scr refresh
        Rating_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Text.started')
        # update status
        Rating_Text.status = STARTED
        Rating_Text.setAutoDraw(True)
    
    # if Rating_Text is active this frame...
    if Rating_Text.status == STARTED:
        # update params
        pass
    
    # *Rating_Response* updates
    
    # if Rating_Response is starting this frame...
    if Rating_Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rating_Response.frameNStart = frameN  # exact frame index
        Rating_Response.tStart = t  # local t and not account for scr refresh
        Rating_Response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Response, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Response.started')
        # update status
        Rating_Response.status = STARTED
        Rating_Response.setAutoDraw(True)
    
    # if Rating_Response is active this frame...
    if Rating_Response.status == STARTED:
        # update params
        pass
    # *Rating_Done* updates
    
    # if Rating_Done is starting this frame...
    if Rating_Done.status == NOT_STARTED and Rating_Response.getRating() != None:
        # keep track of start time/frame for later
        Rating_Done.frameNStart = frameN  # exact frame index
        Rating_Done.tStart = t  # local t and not account for scr refresh
        Rating_Done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Done, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Done.started')
        # update status
        Rating_Done.status = STARTED
        Rating_Done.setAutoDraw(True)
    
    # if Rating_Done is active this frame...
    if Rating_Done.status == STARTED:
        # update params
        pass
        # check whether Rating_Done has been pressed
        if Rating_Done.isClicked:
            if not Rating_Done.wasClicked:
                # if this is a new click, store time of first click and clicked until
                Rating_Done.timesOn.append(Rating_Done.buttonClock.getTime())
                Rating_Done.timesOff.append(Rating_Done.buttonClock.getTime())
            elif len(Rating_Done.timesOff):
                # if click is continuing from last frame, update time of clicked until
                Rating_Done.timesOff[-1] = Rating_Done.buttonClock.getTime()
            if not Rating_Done.wasClicked:
                # end routine when Rating_Done is clicked
                continueRoutine = False
            if not Rating_Done.wasClicked:
                # run callback code when Rating_Done is clicked
                pass
    # take note of whether Rating_Done was clicked, so that next frame we know if clicks are new
    Rating_Done.wasClicked = Rating_Done.isClicked and Rating_Done.status == STARTED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RatComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Rat" ---
for thisComponent in RatComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Rating_Response.response', Rating_Response.getRating())
thisExp.addData('Rating_Response.rt', Rating_Response.getRT())
thisExp.addData('Rating_Done.numClicks', Rating_Done.numClicks)
if Rating_Done.numClicks:
   thisExp.addData('Rating_Done.timesOn', Rating_Done.timesOn)
   thisExp.addData('Rating_Done.timesOff', Rating_Done.timesOff)
else:
   thisExp.addData('Rating_Done.timesOn', "")
   thisExp.addData('Rating_Done.timesOff', "")
# the Routine "Rat" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "RegRat" ---
continueRoutine = True
# update component parameters for each repeat
RegulationRating_Response.reset()
# reset RegulationRating_Done to account for continued clicks & clear times on/off
RegulationRating_Done.reset()
# keep track of which components have finished
RegRatComponents = [RegulationRating_Text, RegulationRating_Response, RegulationRating_Done]
for thisComponent in RegRatComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "RegRat" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *RegulationRating_Text* updates
    
    # if RegulationRating_Text is starting this frame...
    if RegulationRating_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RegulationRating_Text.frameNStart = frameN  # exact frame index
        RegulationRating_Text.tStart = t  # local t and not account for scr refresh
        RegulationRating_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RegulationRating_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RegulationRating_Text.started')
        # update status
        RegulationRating_Text.status = STARTED
        RegulationRating_Text.setAutoDraw(True)
    
    # if RegulationRating_Text is active this frame...
    if RegulationRating_Text.status == STARTED:
        # update params
        pass
    
    # *RegulationRating_Response* updates
    
    # if RegulationRating_Response is starting this frame...
    if RegulationRating_Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RegulationRating_Response.frameNStart = frameN  # exact frame index
        RegulationRating_Response.tStart = t  # local t and not account for scr refresh
        RegulationRating_Response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RegulationRating_Response, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RegulationRating_Response.started')
        # update status
        RegulationRating_Response.status = STARTED
        RegulationRating_Response.setAutoDraw(True)
    
    # if RegulationRating_Response is active this frame...
    if RegulationRating_Response.status == STARTED:
        # update params
        pass
    # *RegulationRating_Done* updates
    
    # if RegulationRating_Done is starting this frame...
    if RegulationRating_Done.status == NOT_STARTED and RegulationRating_Response.getRating() != None:
        # keep track of start time/frame for later
        RegulationRating_Done.frameNStart = frameN  # exact frame index
        RegulationRating_Done.tStart = t  # local t and not account for scr refresh
        RegulationRating_Done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RegulationRating_Done, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RegulationRating_Done.started')
        # update status
        RegulationRating_Done.status = STARTED
        RegulationRating_Done.setAutoDraw(True)
    
    # if RegulationRating_Done is active this frame...
    if RegulationRating_Done.status == STARTED:
        # update params
        pass
        # check whether RegulationRating_Done has been pressed
        if RegulationRating_Done.isClicked:
            if not RegulationRating_Done.wasClicked:
                # if this is a new click, store time of first click and clicked until
                RegulationRating_Done.timesOn.append(RegulationRating_Done.buttonClock.getTime())
                RegulationRating_Done.timesOff.append(RegulationRating_Done.buttonClock.getTime())
            elif len(RegulationRating_Done.timesOff):
                # if click is continuing from last frame, update time of clicked until
                RegulationRating_Done.timesOff[-1] = RegulationRating_Done.buttonClock.getTime()
            if not RegulationRating_Done.wasClicked:
                # end routine when RegulationRating_Done is clicked
                continueRoutine = False
            if not RegulationRating_Done.wasClicked:
                # run callback code when RegulationRating_Done is clicked
                pass
    # take note of whether RegulationRating_Done was clicked, so that next frame we know if clicks are new
    RegulationRating_Done.wasClicked = RegulationRating_Done.isClicked and RegulationRating_Done.status == STARTED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RegRatComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "RegRat" ---
for thisComponent in RegRatComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('RegulationRating_Response.response', RegulationRating_Response.getRating())
thisExp.addData('RegulationRating_Response.rt', RegulationRating_Response.getRT())
thisExp.addData('RegulationRating_Done.numClicks', RegulationRating_Done.numClicks)
if RegulationRating_Done.numClicks:
   thisExp.addData('RegulationRating_Done.timesOn', RegulationRating_Done.timesOn)
   thisExp.addData('RegulationRating_Done.timesOff', RegulationRating_Done.timesOff)
else:
   thisExp.addData('RegulationRating_Done.timesOn', "")
   thisExp.addData('RegulationRating_Done.timesOff', "")
# the Routine "RegRat" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "BC" ---
continueRoutine = True
# update component parameters for each repeat
# reset BContinue_Button to account for continued clicks & clear times on/off
BContinue_Button.reset()
# keep track of which components have finished
BCComponents = [BContinue_Button, BContinue_Text]
for thisComponent in BCComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "BC" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *BContinue_Button* updates
    
    # if BContinue_Button is starting this frame...
    if BContinue_Button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        BContinue_Button.frameNStart = frameN  # exact frame index
        BContinue_Button.tStart = t  # local t and not account for scr refresh
        BContinue_Button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BContinue_Button, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'BContinue_Button.started')
        # update status
        BContinue_Button.status = STARTED
        BContinue_Button.setAutoDraw(True)
    
    # if BContinue_Button is active this frame...
    if BContinue_Button.status == STARTED:
        # update params
        pass
        # check whether BContinue_Button has been pressed
        if BContinue_Button.isClicked:
            if not BContinue_Button.wasClicked:
                # if this is a new click, store time of first click and clicked until
                BContinue_Button.timesOn.append(BContinue_Button.buttonClock.getTime())
                BContinue_Button.timesOff.append(BContinue_Button.buttonClock.getTime())
            elif len(BContinue_Button.timesOff):
                # if click is continuing from last frame, update time of clicked until
                BContinue_Button.timesOff[-1] = BContinue_Button.buttonClock.getTime()
            if not BContinue_Button.wasClicked:
                # end routine when BContinue_Button is clicked
                continueRoutine = False
            if not BContinue_Button.wasClicked:
                # run callback code when BContinue_Button is clicked
                pass
    # take note of whether BContinue_Button was clicked, so that next frame we know if clicks are new
    BContinue_Button.wasClicked = BContinue_Button.isClicked and BContinue_Button.status == STARTED
    
    # *BContinue_Text* updates
    
    # if BContinue_Text is starting this frame...
    if BContinue_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BContinue_Text.frameNStart = frameN  # exact frame index
        BContinue_Text.tStart = t  # local t and not account for scr refresh
        BContinue_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BContinue_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'BContinue_Text.started')
        # update status
        BContinue_Text.status = STARTED
        BContinue_Text.setAutoDraw(True)
    
    # if BContinue_Text is active this frame...
    if BContinue_Text.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BCComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "BC" ---
for thisComponent in BCComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('BContinue_Button.numClicks', BContinue_Button.numClicks)
if BContinue_Button.numClicks:
   thisExp.addData('BContinue_Button.timesOn', BContinue_Button.timesOn)
   thisExp.addData('BContinue_Button.timesOff', BContinue_Button.timesOff)
else:
   thisExp.addData('BContinue_Button.timesOn', "")
   thisExp.addData('BContinue_Button.timesOff', "")
# the Routine "BC" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Cond" ---
continueRoutine = True
# update component parameters for each repeat
ConditionTextBox.reset()
# reset ConditionDone to account for continued clicks & clear times on/off
ConditionDone.reset()
# keep track of which components have finished
CondComponents = [ConditionTextBox, ConditionDone]
for thisComponent in CondComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Cond" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ConditionTextBox* updates
    
    # if ConditionTextBox is starting this frame...
    if ConditionTextBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ConditionTextBox.frameNStart = frameN  # exact frame index
        ConditionTextBox.tStart = t  # local t and not account for scr refresh
        ConditionTextBox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ConditionTextBox, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ConditionTextBox.started')
        # update status
        ConditionTextBox.status = STARTED
        ConditionTextBox.setAutoDraw(True)
    
    # if ConditionTextBox is active this frame...
    if ConditionTextBox.status == STARTED:
        # update params
        pass
    # *ConditionDone* updates
    
    # if ConditionDone is starting this frame...
    if ConditionDone.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        ConditionDone.frameNStart = frameN  # exact frame index
        ConditionDone.tStart = t  # local t and not account for scr refresh
        ConditionDone.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ConditionDone, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ConditionDone.started')
        # update status
        ConditionDone.status = STARTED
        ConditionDone.setAutoDraw(True)
    
    # if ConditionDone is active this frame...
    if ConditionDone.status == STARTED:
        # update params
        pass
        # check whether ConditionDone has been pressed
        if ConditionDone.isClicked:
            if not ConditionDone.wasClicked:
                # if this is a new click, store time of first click and clicked until
                ConditionDone.timesOn.append(ConditionDone.buttonClock.getTime())
                ConditionDone.timesOff.append(ConditionDone.buttonClock.getTime())
            elif len(ConditionDone.timesOff):
                # if click is continuing from last frame, update time of clicked until
                ConditionDone.timesOff[-1] = ConditionDone.buttonClock.getTime()
            if not ConditionDone.wasClicked:
                # end routine when ConditionDone is clicked
                continueRoutine = False
            if not ConditionDone.wasClicked:
                # run callback code when ConditionDone is clicked
                pass
    # take note of whether ConditionDone was clicked, so that next frame we know if clicks are new
    ConditionDone.wasClicked = ConditionDone.isClicked and ConditionDone.status == STARTED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CondComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Cond" ---
for thisComponent in CondComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ConditionTextBox.text',ConditionTextBox.text)
thisExp.addData('ConditionDone.numClicks', ConditionDone.numClicks)
if ConditionDone.numClicks:
   thisExp.addData('ConditionDone.timesOn', ConditionDone.timesOn)
   thisExp.addData('ConditionDone.timesOff', ConditionDone.timesOff)
else:
   thisExp.addData('ConditionDone.timesOn', "")
   thisExp.addData('ConditionDone.timesOff', "")
# the Routine "Cond" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "GR" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
GRComponents = [GetReady_Text, GetRead_Cross]
for thisComponent in GRComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "GR" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *GetReady_Text* updates
    
    # if GetReady_Text is starting this frame...
    if GetReady_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GetReady_Text.frameNStart = frameN  # exact frame index
        GetReady_Text.tStart = t  # local t and not account for scr refresh
        GetReady_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GetReady_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'GetReady_Text.started')
        # update status
        GetReady_Text.status = STARTED
        GetReady_Text.setAutoDraw(True)
    
    # if GetReady_Text is active this frame...
    if GetReady_Text.status == STARTED:
        # update params
        GetReady_Text.setText('', log=False)
    
    # if GetReady_Text is stopping this frame...
    if GetReady_Text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > GetReady_Text.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            GetReady_Text.tStop = t  # not accounting for scr refresh
            GetReady_Text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'GetReady_Text.stopped')
            # update status
            GetReady_Text.status = FINISHED
            GetReady_Text.setAutoDraw(False)
    
    # *GetRead_Cross* updates
    
    # if GetRead_Cross is starting this frame...
    if GetRead_Cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GetRead_Cross.frameNStart = frameN  # exact frame index
        GetRead_Cross.tStart = t  # local t and not account for scr refresh
        GetRead_Cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GetRead_Cross, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'GetRead_Cross.started')
        # update status
        GetRead_Cross.status = STARTED
        GetRead_Cross.setAutoDraw(True)
    
    # if GetRead_Cross is active this frame...
    if GetRead_Cross.status == STARTED:
        # update params
        pass
    
    # if GetRead_Cross is stopping this frame...
    if GetRead_Cross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > GetRead_Cross.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            GetRead_Cross.tStop = t  # not accounting for scr refresh
            GetRead_Cross.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'GetRead_Cross.stopped')
            # update status
            GetRead_Cross.status = FINISHED
            GetRead_Cross.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GRComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "GR" ---
for thisComponent in GRComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# set up handler to look after randomisation of conditions etc
Neg2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PsychopyIntegrationSheets/Negative2.xlsx'),
    seed=None, name='Neg2')
thisExp.addLoop(Neg2)  # add the loop to the experiment
thisNeg2 = Neg2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNeg2.rgb)
if thisNeg2 != None:
    for paramName in thisNeg2:
        exec('{} = thisNeg2[paramName]'.format(paramName))

for thisNeg2 in Neg2:
    currentLoop = Neg2
    # abbreviate parameter names if possible (e.g. rgb = thisNeg2.rgb)
    if thisNeg2 != None:
        for paramName in thisNeg2:
            exec('{} = thisNeg2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "SS" ---
    continueRoutine = True
    # update component parameters for each repeat
    StorySentence_Text.setText(StorySentences)
    # keep track of which components have finished
    SSComponents = [StorySentence_Text]
    for thisComponent in SSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "SS" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *StorySentence_Text* updates
        
        # if StorySentence_Text is starting this frame...
        if StorySentence_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StorySentence_Text.frameNStart = frameN  # exact frame index
            StorySentence_Text.tStart = t  # local t and not account for scr refresh
            StorySentence_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StorySentence_Text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'StorySentence_Text.started')
            # update status
            StorySentence_Text.status = STARTED
            StorySentence_Text.setAutoDraw(True)
        
        # if StorySentence_Text is active this frame...
        if StorySentence_Text.status == STARTED:
            # update params
            pass
        
        # if StorySentence_Text is stopping this frame...
        if StorySentence_Text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StorySentence_Text.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                StorySentence_Text.tStop = t  # not accounting for scr refresh
                StorySentence_Text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'StorySentence_Text.stopped')
                # update status
                StorySentence_Text.status = FINISHED
                StorySentence_Text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "SS" ---
    for thisComponent in SSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Neg2'


# --- Prepare to start Routine "Rat" ---
continueRoutine = True
# update component parameters for each repeat
Rating_Response.reset()
# reset Rating_Done to account for continued clicks & clear times on/off
Rating_Done.reset()
# keep track of which components have finished
RatComponents = [Rating_Text, Rating_Response, Rating_Done]
for thisComponent in RatComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Rat" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Rating_Text* updates
    
    # if Rating_Text is starting this frame...
    if Rating_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rating_Text.frameNStart = frameN  # exact frame index
        Rating_Text.tStart = t  # local t and not account for scr refresh
        Rating_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Text.started')
        # update status
        Rating_Text.status = STARTED
        Rating_Text.setAutoDraw(True)
    
    # if Rating_Text is active this frame...
    if Rating_Text.status == STARTED:
        # update params
        pass
    
    # *Rating_Response* updates
    
    # if Rating_Response is starting this frame...
    if Rating_Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rating_Response.frameNStart = frameN  # exact frame index
        Rating_Response.tStart = t  # local t and not account for scr refresh
        Rating_Response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Response, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Response.started')
        # update status
        Rating_Response.status = STARTED
        Rating_Response.setAutoDraw(True)
    
    # if Rating_Response is active this frame...
    if Rating_Response.status == STARTED:
        # update params
        pass
    # *Rating_Done* updates
    
    # if Rating_Done is starting this frame...
    if Rating_Done.status == NOT_STARTED and Rating_Response.getRating() != None:
        # keep track of start time/frame for later
        Rating_Done.frameNStart = frameN  # exact frame index
        Rating_Done.tStart = t  # local t and not account for scr refresh
        Rating_Done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Done, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Done.started')
        # update status
        Rating_Done.status = STARTED
        Rating_Done.setAutoDraw(True)
    
    # if Rating_Done is active this frame...
    if Rating_Done.status == STARTED:
        # update params
        pass
        # check whether Rating_Done has been pressed
        if Rating_Done.isClicked:
            if not Rating_Done.wasClicked:
                # if this is a new click, store time of first click and clicked until
                Rating_Done.timesOn.append(Rating_Done.buttonClock.getTime())
                Rating_Done.timesOff.append(Rating_Done.buttonClock.getTime())
            elif len(Rating_Done.timesOff):
                # if click is continuing from last frame, update time of clicked until
                Rating_Done.timesOff[-1] = Rating_Done.buttonClock.getTime()
            if not Rating_Done.wasClicked:
                # end routine when Rating_Done is clicked
                continueRoutine = False
            if not Rating_Done.wasClicked:
                # run callback code when Rating_Done is clicked
                pass
    # take note of whether Rating_Done was clicked, so that next frame we know if clicks are new
    Rating_Done.wasClicked = Rating_Done.isClicked and Rating_Done.status == STARTED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RatComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Rat" ---
for thisComponent in RatComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Rating_Response.response', Rating_Response.getRating())
thisExp.addData('Rating_Response.rt', Rating_Response.getRT())
thisExp.addData('Rating_Done.numClicks', Rating_Done.numClicks)
if Rating_Done.numClicks:
   thisExp.addData('Rating_Done.timesOn', Rating_Done.timesOn)
   thisExp.addData('Rating_Done.timesOff', Rating_Done.timesOff)
else:
   thisExp.addData('Rating_Done.timesOn', "")
   thisExp.addData('Rating_Done.timesOff', "")
# the Routine "Rat" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
NSB2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PsychopyIntegrationSheets/NSB2.xlsx'),
    seed=None, name='NSB2')
thisExp.addLoop(NSB2)  # add the loop to the experiment
thisNSB2 = NSB2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNSB2.rgb)
if thisNSB2 != None:
    for paramName in thisNSB2:
        exec('{} = thisNSB2[paramName]'.format(paramName))

for thisNSB2 in NSB2:
    currentLoop = NSB2
    # abbreviate parameter names if possible (e.g. rgb = thisNSB2.rgb)
    if thisNSB2 != None:
        for paramName in thisNSB2:
            exec('{} = thisNSB2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    Trial_RatingResponse.reset()
    # reset Trial_ResponseDone to account for continued clicks & clear times on/off
    Trial_ResponseDone.reset()
    # keep track of which components have finished
    TrialComponents = [Trial_NSB, Trial_Cue, Trial_RatingText, Trial_RatingResponse, Trial_ResponseDone]
    for thisComponent in TrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Trial" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Trial_NSB* updates
        
        # if Trial_NSB is starting this frame...
        if Trial_NSB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Trial_NSB.frameNStart = frameN  # exact frame index
            Trial_NSB.tStart = t  # local t and not account for scr refresh
            Trial_NSB.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_NSB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_NSB.started')
            # update status
            Trial_NSB.status = STARTED
            Trial_NSB.setAutoDraw(True)
        
        # if Trial_NSB is active this frame...
        if Trial_NSB.status == STARTED:
            # update params
            pass
        
        # if Trial_NSB is stopping this frame...
        if Trial_NSB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Trial_NSB.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                Trial_NSB.tStop = t  # not accounting for scr refresh
                Trial_NSB.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Trial_NSB.stopped')
                # update status
                Trial_NSB.status = FINISHED
                Trial_NSB.setAutoDraw(False)
        
        # *Trial_Cue* updates
        
        # if Trial_Cue is starting this frame...
        if Trial_Cue.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            Trial_Cue.frameNStart = frameN  # exact frame index
            Trial_Cue.tStart = t  # local t and not account for scr refresh
            Trial_Cue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_Cue, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_Cue.started')
            # update status
            Trial_Cue.status = STARTED
            Trial_Cue.setAutoDraw(True)
        
        # if Trial_Cue is active this frame...
        if Trial_Cue.status == STARTED:
            # update params
            pass
        
        # if Trial_Cue is stopping this frame...
        if Trial_Cue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Trial_Cue.tStartRefresh + 12-frameTolerance:
                # keep track of stop time/frame for later
                Trial_Cue.tStop = t  # not accounting for scr refresh
                Trial_Cue.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Trial_Cue.stopped')
                # update status
                Trial_Cue.status = FINISHED
                Trial_Cue.setAutoDraw(False)
        
        # *Trial_RatingText* updates
        
        # if Trial_RatingText is starting this frame...
        if Trial_RatingText.status == NOT_STARTED and tThisFlip >= 15-frameTolerance:
            # keep track of start time/frame for later
            Trial_RatingText.frameNStart = frameN  # exact frame index
            Trial_RatingText.tStart = t  # local t and not account for scr refresh
            Trial_RatingText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_RatingText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_RatingText.started')
            # update status
            Trial_RatingText.status = STARTED
            Trial_RatingText.setAutoDraw(True)
        
        # if Trial_RatingText is active this frame...
        if Trial_RatingText.status == STARTED:
            # update params
            pass
        
        # *Trial_RatingResponse* updates
        
        # if Trial_RatingResponse is starting this frame...
        if Trial_RatingResponse.status == NOT_STARTED and tThisFlip >= 15-frameTolerance:
            # keep track of start time/frame for later
            Trial_RatingResponse.frameNStart = frameN  # exact frame index
            Trial_RatingResponse.tStart = t  # local t and not account for scr refresh
            Trial_RatingResponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_RatingResponse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_RatingResponse.started')
            # update status
            Trial_RatingResponse.status = STARTED
            Trial_RatingResponse.setAutoDraw(True)
        
        # if Trial_RatingResponse is active this frame...
        if Trial_RatingResponse.status == STARTED:
            # update params
            pass
        # *Trial_ResponseDone* updates
        
        # if Trial_ResponseDone is starting this frame...
        if Trial_ResponseDone.status == NOT_STARTED and Trial_RatingResponse.getRating() != None:
            # keep track of start time/frame for later
            Trial_ResponseDone.frameNStart = frameN  # exact frame index
            Trial_ResponseDone.tStart = t  # local t and not account for scr refresh
            Trial_ResponseDone.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_ResponseDone, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_ResponseDone.started')
            # update status
            Trial_ResponseDone.status = STARTED
            Trial_ResponseDone.setAutoDraw(True)
        
        # if Trial_ResponseDone is active this frame...
        if Trial_ResponseDone.status == STARTED:
            # update params
            pass
            # check whether Trial_ResponseDone has been pressed
            if Trial_ResponseDone.isClicked:
                if not Trial_ResponseDone.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    Trial_ResponseDone.timesOn.append(Trial_ResponseDone.buttonClock.getTime())
                    Trial_ResponseDone.timesOff.append(Trial_ResponseDone.buttonClock.getTime())
                elif len(Trial_ResponseDone.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    Trial_ResponseDone.timesOff[-1] = Trial_ResponseDone.buttonClock.getTime()
                if not Trial_ResponseDone.wasClicked:
                    # end routine when Trial_ResponseDone is clicked
                    continueRoutine = False
                if not Trial_ResponseDone.wasClicked:
                    # run callback code when Trial_ResponseDone is clicked
                    pass
        # take note of whether Trial_ResponseDone was clicked, so that next frame we know if clicks are new
        Trial_ResponseDone.wasClicked = Trial_ResponseDone.isClicked and Trial_ResponseDone.status == STARTED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Trial" ---
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    NSB2.addData('Trial_RatingResponse.response', Trial_RatingResponse.getRating())
    NSB2.addData('Trial_RatingResponse.rt', Trial_RatingResponse.getRT())
    NSB2.addData('Trial_ResponseDone.numClicks', Trial_ResponseDone.numClicks)
    if Trial_ResponseDone.numClicks:
       NSB2.addData('Trial_ResponseDone.timesOn', Trial_ResponseDone.timesOn)
       NSB2.addData('Trial_ResponseDone.timesOff', Trial_ResponseDone.timesOff)
    else:
       NSB2.addData('Trial_ResponseDone.timesOn', "")
       NSB2.addData('Trial_ResponseDone.timesOff', "")
    # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'NSB2'


# --- Prepare to start Routine "GR" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
GRComponents = [GetReady_Text, GetRead_Cross]
for thisComponent in GRComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "GR" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *GetReady_Text* updates
    
    # if GetReady_Text is starting this frame...
    if GetReady_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GetReady_Text.frameNStart = frameN  # exact frame index
        GetReady_Text.tStart = t  # local t and not account for scr refresh
        GetReady_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GetReady_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'GetReady_Text.started')
        # update status
        GetReady_Text.status = STARTED
        GetReady_Text.setAutoDraw(True)
    
    # if GetReady_Text is active this frame...
    if GetReady_Text.status == STARTED:
        # update params
        GetReady_Text.setText('', log=False)
    
    # if GetReady_Text is stopping this frame...
    if GetReady_Text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > GetReady_Text.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            GetReady_Text.tStop = t  # not accounting for scr refresh
            GetReady_Text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'GetReady_Text.stopped')
            # update status
            GetReady_Text.status = FINISHED
            GetReady_Text.setAutoDraw(False)
    
    # *GetRead_Cross* updates
    
    # if GetRead_Cross is starting this frame...
    if GetRead_Cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GetRead_Cross.frameNStart = frameN  # exact frame index
        GetRead_Cross.tStart = t  # local t and not account for scr refresh
        GetRead_Cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GetRead_Cross, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'GetRead_Cross.started')
        # update status
        GetRead_Cross.status = STARTED
        GetRead_Cross.setAutoDraw(True)
    
    # if GetRead_Cross is active this frame...
    if GetRead_Cross.status == STARTED:
        # update params
        pass
    
    # if GetRead_Cross is stopping this frame...
    if GetRead_Cross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > GetRead_Cross.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            GetRead_Cross.tStop = t  # not accounting for scr refresh
            GetRead_Cross.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'GetRead_Cross.stopped')
            # update status
            GetRead_Cross.status = FINISHED
            GetRead_Cross.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GRComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "GR" ---
for thisComponent in GRComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# set up handler to look after randomisation of conditions etc
Neu2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PsychopyIntegrationSheets/Neutral2.xlsx'),
    seed=None, name='Neu2')
thisExp.addLoop(Neu2)  # add the loop to the experiment
thisNeu2 = Neu2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNeu2.rgb)
if thisNeu2 != None:
    for paramName in thisNeu2:
        exec('{} = thisNeu2[paramName]'.format(paramName))

for thisNeu2 in Neu2:
    currentLoop = Neu2
    # abbreviate parameter names if possible (e.g. rgb = thisNeu2.rgb)
    if thisNeu2 != None:
        for paramName in thisNeu2:
            exec('{} = thisNeu2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "SS" ---
    continueRoutine = True
    # update component parameters for each repeat
    StorySentence_Text.setText(StorySentences)
    # keep track of which components have finished
    SSComponents = [StorySentence_Text]
    for thisComponent in SSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "SS" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *StorySentence_Text* updates
        
        # if StorySentence_Text is starting this frame...
        if StorySentence_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StorySentence_Text.frameNStart = frameN  # exact frame index
            StorySentence_Text.tStart = t  # local t and not account for scr refresh
            StorySentence_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StorySentence_Text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'StorySentence_Text.started')
            # update status
            StorySentence_Text.status = STARTED
            StorySentence_Text.setAutoDraw(True)
        
        # if StorySentence_Text is active this frame...
        if StorySentence_Text.status == STARTED:
            # update params
            pass
        
        # if StorySentence_Text is stopping this frame...
        if StorySentence_Text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StorySentence_Text.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                StorySentence_Text.tStop = t  # not accounting for scr refresh
                StorySentence_Text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'StorySentence_Text.stopped')
                # update status
                StorySentence_Text.status = FINISHED
                StorySentence_Text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "SS" ---
    for thisComponent in SSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Neu2'


# set up handler to look after randomisation of conditions etc
NeuSta2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PsychopyIntegrationSheets/NeutralStatements2.xlsx'),
    seed=None, name='NeuSta2')
thisExp.addLoop(NeuSta2)  # add the loop to the experiment
thisNeuSta2 = NeuSta2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNeuSta2.rgb)
if thisNeuSta2 != None:
    for paramName in thisNeuSta2:
        exec('{} = thisNeuSta2[paramName]'.format(paramName))

for thisNeuSta2 in NeuSta2:
    currentLoop = NeuSta2
    # abbreviate parameter names if possible (e.g. rgb = thisNeuSta2.rgb)
    if thisNeuSta2 != None:
        for paramName in thisNeuSta2:
            exec('{} = thisNeuSta2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "NS" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    NSComponents = [NeutralStatement_Text]
    for thisComponent in NSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "NS" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 12.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NeutralStatement_Text* updates
        
        # if NeutralStatement_Text is starting this frame...
        if NeutralStatement_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NeutralStatement_Text.frameNStart = frameN  # exact frame index
            NeutralStatement_Text.tStart = t  # local t and not account for scr refresh
            NeutralStatement_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NeutralStatement_Text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NeutralStatement_Text.started')
            # update status
            NeutralStatement_Text.status = STARTED
            NeutralStatement_Text.setAutoDraw(True)
        
        # if NeutralStatement_Text is active this frame...
        if NeutralStatement_Text.status == STARTED:
            # update params
            pass
        
        # if NeutralStatement_Text is stopping this frame...
        if NeutralStatement_Text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > NeutralStatement_Text.tStartRefresh + 12-frameTolerance:
                # keep track of stop time/frame for later
                NeutralStatement_Text.tStop = t  # not accounting for scr refresh
                NeutralStatement_Text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'NeutralStatement_Text.stopped')
                # update status
                NeutralStatement_Text.status = FINISHED
                NeutralStatement_Text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "NS" ---
    for thisComponent in NSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-12.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'NeuSta2'


# --- Prepare to start Routine "Rat" ---
continueRoutine = True
# update component parameters for each repeat
Rating_Response.reset()
# reset Rating_Done to account for continued clicks & clear times on/off
Rating_Done.reset()
# keep track of which components have finished
RatComponents = [Rating_Text, Rating_Response, Rating_Done]
for thisComponent in RatComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Rat" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Rating_Text* updates
    
    # if Rating_Text is starting this frame...
    if Rating_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rating_Text.frameNStart = frameN  # exact frame index
        Rating_Text.tStart = t  # local t and not account for scr refresh
        Rating_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Text.started')
        # update status
        Rating_Text.status = STARTED
        Rating_Text.setAutoDraw(True)
    
    # if Rating_Text is active this frame...
    if Rating_Text.status == STARTED:
        # update params
        pass
    
    # *Rating_Response* updates
    
    # if Rating_Response is starting this frame...
    if Rating_Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rating_Response.frameNStart = frameN  # exact frame index
        Rating_Response.tStart = t  # local t and not account for scr refresh
        Rating_Response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Response, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Response.started')
        # update status
        Rating_Response.status = STARTED
        Rating_Response.setAutoDraw(True)
    
    # if Rating_Response is active this frame...
    if Rating_Response.status == STARTED:
        # update params
        pass
    # *Rating_Done* updates
    
    # if Rating_Done is starting this frame...
    if Rating_Done.status == NOT_STARTED and Rating_Response.getRating() != None:
        # keep track of start time/frame for later
        Rating_Done.frameNStart = frameN  # exact frame index
        Rating_Done.tStart = t  # local t and not account for scr refresh
        Rating_Done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Done, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Done.started')
        # update status
        Rating_Done.status = STARTED
        Rating_Done.setAutoDraw(True)
    
    # if Rating_Done is active this frame...
    if Rating_Done.status == STARTED:
        # update params
        pass
        # check whether Rating_Done has been pressed
        if Rating_Done.isClicked:
            if not Rating_Done.wasClicked:
                # if this is a new click, store time of first click and clicked until
                Rating_Done.timesOn.append(Rating_Done.buttonClock.getTime())
                Rating_Done.timesOff.append(Rating_Done.buttonClock.getTime())
            elif len(Rating_Done.timesOff):
                # if click is continuing from last frame, update time of clicked until
                Rating_Done.timesOff[-1] = Rating_Done.buttonClock.getTime()
            if not Rating_Done.wasClicked:
                # end routine when Rating_Done is clicked
                continueRoutine = False
            if not Rating_Done.wasClicked:
                # run callback code when Rating_Done is clicked
                pass
    # take note of whether Rating_Done was clicked, so that next frame we know if clicks are new
    Rating_Done.wasClicked = Rating_Done.isClicked and Rating_Done.status == STARTED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RatComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Rat" ---
for thisComponent in RatComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Rating_Response.response', Rating_Response.getRating())
thisExp.addData('Rating_Response.rt', Rating_Response.getRT())
thisExp.addData('Rating_Done.numClicks', Rating_Done.numClicks)
if Rating_Done.numClicks:
   thisExp.addData('Rating_Done.timesOn', Rating_Done.timesOn)
   thisExp.addData('Rating_Done.timesOff', Rating_Done.timesOff)
else:
   thisExp.addData('Rating_Done.timesOn', "")
   thisExp.addData('Rating_Done.timesOff', "")
# the Routine "Rat" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "RegRat" ---
continueRoutine = True
# update component parameters for each repeat
RegulationRating_Response.reset()
# reset RegulationRating_Done to account for continued clicks & clear times on/off
RegulationRating_Done.reset()
# keep track of which components have finished
RegRatComponents = [RegulationRating_Text, RegulationRating_Response, RegulationRating_Done]
for thisComponent in RegRatComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "RegRat" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *RegulationRating_Text* updates
    
    # if RegulationRating_Text is starting this frame...
    if RegulationRating_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RegulationRating_Text.frameNStart = frameN  # exact frame index
        RegulationRating_Text.tStart = t  # local t and not account for scr refresh
        RegulationRating_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RegulationRating_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RegulationRating_Text.started')
        # update status
        RegulationRating_Text.status = STARTED
        RegulationRating_Text.setAutoDraw(True)
    
    # if RegulationRating_Text is active this frame...
    if RegulationRating_Text.status == STARTED:
        # update params
        pass
    
    # *RegulationRating_Response* updates
    
    # if RegulationRating_Response is starting this frame...
    if RegulationRating_Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RegulationRating_Response.frameNStart = frameN  # exact frame index
        RegulationRating_Response.tStart = t  # local t and not account for scr refresh
        RegulationRating_Response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RegulationRating_Response, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RegulationRating_Response.started')
        # update status
        RegulationRating_Response.status = STARTED
        RegulationRating_Response.setAutoDraw(True)
    
    # if RegulationRating_Response is active this frame...
    if RegulationRating_Response.status == STARTED:
        # update params
        pass
    # *RegulationRating_Done* updates
    
    # if RegulationRating_Done is starting this frame...
    if RegulationRating_Done.status == NOT_STARTED and RegulationRating_Response.getRating() != None:
        # keep track of start time/frame for later
        RegulationRating_Done.frameNStart = frameN  # exact frame index
        RegulationRating_Done.tStart = t  # local t and not account for scr refresh
        RegulationRating_Done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RegulationRating_Done, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RegulationRating_Done.started')
        # update status
        RegulationRating_Done.status = STARTED
        RegulationRating_Done.setAutoDraw(True)
    
    # if RegulationRating_Done is active this frame...
    if RegulationRating_Done.status == STARTED:
        # update params
        pass
        # check whether RegulationRating_Done has been pressed
        if RegulationRating_Done.isClicked:
            if not RegulationRating_Done.wasClicked:
                # if this is a new click, store time of first click and clicked until
                RegulationRating_Done.timesOn.append(RegulationRating_Done.buttonClock.getTime())
                RegulationRating_Done.timesOff.append(RegulationRating_Done.buttonClock.getTime())
            elif len(RegulationRating_Done.timesOff):
                # if click is continuing from last frame, update time of clicked until
                RegulationRating_Done.timesOff[-1] = RegulationRating_Done.buttonClock.getTime()
            if not RegulationRating_Done.wasClicked:
                # end routine when RegulationRating_Done is clicked
                continueRoutine = False
            if not RegulationRating_Done.wasClicked:
                # run callback code when RegulationRating_Done is clicked
                pass
    # take note of whether RegulationRating_Done was clicked, so that next frame we know if clicks are new
    RegulationRating_Done.wasClicked = RegulationRating_Done.isClicked and RegulationRating_Done.status == STARTED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RegRatComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "RegRat" ---
for thisComponent in RegRatComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('RegulationRating_Response.response', RegulationRating_Response.getRating())
thisExp.addData('RegulationRating_Response.rt', RegulationRating_Response.getRT())
thisExp.addData('RegulationRating_Done.numClicks', RegulationRating_Done.numClicks)
if RegulationRating_Done.numClicks:
   thisExp.addData('RegulationRating_Done.timesOn', RegulationRating_Done.timesOn)
   thisExp.addData('RegulationRating_Done.timesOff', RegulationRating_Done.timesOff)
else:
   thisExp.addData('RegulationRating_Done.timesOn', "")
   thisExp.addData('RegulationRating_Done.timesOff', "")
# the Routine "RegRat" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "BC" ---
continueRoutine = True
# update component parameters for each repeat
# reset BContinue_Button to account for continued clicks & clear times on/off
BContinue_Button.reset()
# keep track of which components have finished
BCComponents = [BContinue_Button, BContinue_Text]
for thisComponent in BCComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "BC" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *BContinue_Button* updates
    
    # if BContinue_Button is starting this frame...
    if BContinue_Button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        BContinue_Button.frameNStart = frameN  # exact frame index
        BContinue_Button.tStart = t  # local t and not account for scr refresh
        BContinue_Button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BContinue_Button, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'BContinue_Button.started')
        # update status
        BContinue_Button.status = STARTED
        BContinue_Button.setAutoDraw(True)
    
    # if BContinue_Button is active this frame...
    if BContinue_Button.status == STARTED:
        # update params
        pass
        # check whether BContinue_Button has been pressed
        if BContinue_Button.isClicked:
            if not BContinue_Button.wasClicked:
                # if this is a new click, store time of first click and clicked until
                BContinue_Button.timesOn.append(BContinue_Button.buttonClock.getTime())
                BContinue_Button.timesOff.append(BContinue_Button.buttonClock.getTime())
            elif len(BContinue_Button.timesOff):
                # if click is continuing from last frame, update time of clicked until
                BContinue_Button.timesOff[-1] = BContinue_Button.buttonClock.getTime()
            if not BContinue_Button.wasClicked:
                # end routine when BContinue_Button is clicked
                continueRoutine = False
            if not BContinue_Button.wasClicked:
                # run callback code when BContinue_Button is clicked
                pass
    # take note of whether BContinue_Button was clicked, so that next frame we know if clicks are new
    BContinue_Button.wasClicked = BContinue_Button.isClicked and BContinue_Button.status == STARTED
    
    # *BContinue_Text* updates
    
    # if BContinue_Text is starting this frame...
    if BContinue_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BContinue_Text.frameNStart = frameN  # exact frame index
        BContinue_Text.tStart = t  # local t and not account for scr refresh
        BContinue_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BContinue_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'BContinue_Text.started')
        # update status
        BContinue_Text.status = STARTED
        BContinue_Text.setAutoDraw(True)
    
    # if BContinue_Text is active this frame...
    if BContinue_Text.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BCComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "BC" ---
for thisComponent in BCComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('BContinue_Button.numClicks', BContinue_Button.numClicks)
if BContinue_Button.numClicks:
   thisExp.addData('BContinue_Button.timesOn', BContinue_Button.timesOn)
   thisExp.addData('BContinue_Button.timesOff', BContinue_Button.timesOff)
else:
   thisExp.addData('BContinue_Button.timesOn', "")
   thisExp.addData('BContinue_Button.timesOff', "")
# the Routine "BC" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Cond" ---
continueRoutine = True
# update component parameters for each repeat
ConditionTextBox.reset()
# reset ConditionDone to account for continued clicks & clear times on/off
ConditionDone.reset()
# keep track of which components have finished
CondComponents = [ConditionTextBox, ConditionDone]
for thisComponent in CondComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Cond" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ConditionTextBox* updates
    
    # if ConditionTextBox is starting this frame...
    if ConditionTextBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ConditionTextBox.frameNStart = frameN  # exact frame index
        ConditionTextBox.tStart = t  # local t and not account for scr refresh
        ConditionTextBox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ConditionTextBox, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ConditionTextBox.started')
        # update status
        ConditionTextBox.status = STARTED
        ConditionTextBox.setAutoDraw(True)
    
    # if ConditionTextBox is active this frame...
    if ConditionTextBox.status == STARTED:
        # update params
        pass
    # *ConditionDone* updates
    
    # if ConditionDone is starting this frame...
    if ConditionDone.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        ConditionDone.frameNStart = frameN  # exact frame index
        ConditionDone.tStart = t  # local t and not account for scr refresh
        ConditionDone.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ConditionDone, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ConditionDone.started')
        # update status
        ConditionDone.status = STARTED
        ConditionDone.setAutoDraw(True)
    
    # if ConditionDone is active this frame...
    if ConditionDone.status == STARTED:
        # update params
        pass
        # check whether ConditionDone has been pressed
        if ConditionDone.isClicked:
            if not ConditionDone.wasClicked:
                # if this is a new click, store time of first click and clicked until
                ConditionDone.timesOn.append(ConditionDone.buttonClock.getTime())
                ConditionDone.timesOff.append(ConditionDone.buttonClock.getTime())
            elif len(ConditionDone.timesOff):
                # if click is continuing from last frame, update time of clicked until
                ConditionDone.timesOff[-1] = ConditionDone.buttonClock.getTime()
            if not ConditionDone.wasClicked:
                # end routine when ConditionDone is clicked
                continueRoutine = False
            if not ConditionDone.wasClicked:
                # run callback code when ConditionDone is clicked
                pass
    # take note of whether ConditionDone was clicked, so that next frame we know if clicks are new
    ConditionDone.wasClicked = ConditionDone.isClicked and ConditionDone.status == STARTED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CondComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Cond" ---
for thisComponent in CondComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ConditionTextBox.text',ConditionTextBox.text)
thisExp.addData('ConditionDone.numClicks', ConditionDone.numClicks)
if ConditionDone.numClicks:
   thisExp.addData('ConditionDone.timesOn', ConditionDone.timesOn)
   thisExp.addData('ConditionDone.timesOff', ConditionDone.timesOff)
else:
   thisExp.addData('ConditionDone.timesOn', "")
   thisExp.addData('ConditionDone.timesOff', "")
# the Routine "Cond" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "GR" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
GRComponents = [GetReady_Text, GetRead_Cross]
for thisComponent in GRComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "GR" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *GetReady_Text* updates
    
    # if GetReady_Text is starting this frame...
    if GetReady_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GetReady_Text.frameNStart = frameN  # exact frame index
        GetReady_Text.tStart = t  # local t and not account for scr refresh
        GetReady_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GetReady_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'GetReady_Text.started')
        # update status
        GetReady_Text.status = STARTED
        GetReady_Text.setAutoDraw(True)
    
    # if GetReady_Text is active this frame...
    if GetReady_Text.status == STARTED:
        # update params
        GetReady_Text.setText('', log=False)
    
    # if GetReady_Text is stopping this frame...
    if GetReady_Text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > GetReady_Text.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            GetReady_Text.tStop = t  # not accounting for scr refresh
            GetReady_Text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'GetReady_Text.stopped')
            # update status
            GetReady_Text.status = FINISHED
            GetReady_Text.setAutoDraw(False)
    
    # *GetRead_Cross* updates
    
    # if GetRead_Cross is starting this frame...
    if GetRead_Cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GetRead_Cross.frameNStart = frameN  # exact frame index
        GetRead_Cross.tStart = t  # local t and not account for scr refresh
        GetRead_Cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GetRead_Cross, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'GetRead_Cross.started')
        # update status
        GetRead_Cross.status = STARTED
        GetRead_Cross.setAutoDraw(True)
    
    # if GetRead_Cross is active this frame...
    if GetRead_Cross.status == STARTED:
        # update params
        pass
    
    # if GetRead_Cross is stopping this frame...
    if GetRead_Cross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > GetRead_Cross.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            GetRead_Cross.tStop = t  # not accounting for scr refresh
            GetRead_Cross.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'GetRead_Cross.stopped')
            # update status
            GetRead_Cross.status = FINISHED
            GetRead_Cross.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GRComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "GR" ---
for thisComponent in GRComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# set up handler to look after randomisation of conditions etc
Neg3 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PsychopyIntegrationSheets/Negative3.xlsx'),
    seed=None, name='Neg3')
thisExp.addLoop(Neg3)  # add the loop to the experiment
thisNeg3 = Neg3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNeg3.rgb)
if thisNeg3 != None:
    for paramName in thisNeg3:
        exec('{} = thisNeg3[paramName]'.format(paramName))

for thisNeg3 in Neg3:
    currentLoop = Neg3
    # abbreviate parameter names if possible (e.g. rgb = thisNeg3.rgb)
    if thisNeg3 != None:
        for paramName in thisNeg3:
            exec('{} = thisNeg3[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "SS" ---
    continueRoutine = True
    # update component parameters for each repeat
    StorySentence_Text.setText(StorySentences)
    # keep track of which components have finished
    SSComponents = [StorySentence_Text]
    for thisComponent in SSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "SS" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *StorySentence_Text* updates
        
        # if StorySentence_Text is starting this frame...
        if StorySentence_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StorySentence_Text.frameNStart = frameN  # exact frame index
            StorySentence_Text.tStart = t  # local t and not account for scr refresh
            StorySentence_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StorySentence_Text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'StorySentence_Text.started')
            # update status
            StorySentence_Text.status = STARTED
            StorySentence_Text.setAutoDraw(True)
        
        # if StorySentence_Text is active this frame...
        if StorySentence_Text.status == STARTED:
            # update params
            pass
        
        # if StorySentence_Text is stopping this frame...
        if StorySentence_Text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StorySentence_Text.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                StorySentence_Text.tStop = t  # not accounting for scr refresh
                StorySentence_Text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'StorySentence_Text.stopped')
                # update status
                StorySentence_Text.status = FINISHED
                StorySentence_Text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "SS" ---
    for thisComponent in SSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Neg3'


# --- Prepare to start Routine "Rat" ---
continueRoutine = True
# update component parameters for each repeat
Rating_Response.reset()
# reset Rating_Done to account for continued clicks & clear times on/off
Rating_Done.reset()
# keep track of which components have finished
RatComponents = [Rating_Text, Rating_Response, Rating_Done]
for thisComponent in RatComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Rat" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Rating_Text* updates
    
    # if Rating_Text is starting this frame...
    if Rating_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rating_Text.frameNStart = frameN  # exact frame index
        Rating_Text.tStart = t  # local t and not account for scr refresh
        Rating_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Text.started')
        # update status
        Rating_Text.status = STARTED
        Rating_Text.setAutoDraw(True)
    
    # if Rating_Text is active this frame...
    if Rating_Text.status == STARTED:
        # update params
        pass
    
    # *Rating_Response* updates
    
    # if Rating_Response is starting this frame...
    if Rating_Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rating_Response.frameNStart = frameN  # exact frame index
        Rating_Response.tStart = t  # local t and not account for scr refresh
        Rating_Response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Response, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Response.started')
        # update status
        Rating_Response.status = STARTED
        Rating_Response.setAutoDraw(True)
    
    # if Rating_Response is active this frame...
    if Rating_Response.status == STARTED:
        # update params
        pass
    # *Rating_Done* updates
    
    # if Rating_Done is starting this frame...
    if Rating_Done.status == NOT_STARTED and Rating_Response.getRating() != None:
        # keep track of start time/frame for later
        Rating_Done.frameNStart = frameN  # exact frame index
        Rating_Done.tStart = t  # local t and not account for scr refresh
        Rating_Done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Done, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Done.started')
        # update status
        Rating_Done.status = STARTED
        Rating_Done.setAutoDraw(True)
    
    # if Rating_Done is active this frame...
    if Rating_Done.status == STARTED:
        # update params
        pass
        # check whether Rating_Done has been pressed
        if Rating_Done.isClicked:
            if not Rating_Done.wasClicked:
                # if this is a new click, store time of first click and clicked until
                Rating_Done.timesOn.append(Rating_Done.buttonClock.getTime())
                Rating_Done.timesOff.append(Rating_Done.buttonClock.getTime())
            elif len(Rating_Done.timesOff):
                # if click is continuing from last frame, update time of clicked until
                Rating_Done.timesOff[-1] = Rating_Done.buttonClock.getTime()
            if not Rating_Done.wasClicked:
                # end routine when Rating_Done is clicked
                continueRoutine = False
            if not Rating_Done.wasClicked:
                # run callback code when Rating_Done is clicked
                pass
    # take note of whether Rating_Done was clicked, so that next frame we know if clicks are new
    Rating_Done.wasClicked = Rating_Done.isClicked and Rating_Done.status == STARTED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RatComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Rat" ---
for thisComponent in RatComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Rating_Response.response', Rating_Response.getRating())
thisExp.addData('Rating_Response.rt', Rating_Response.getRT())
thisExp.addData('Rating_Done.numClicks', Rating_Done.numClicks)
if Rating_Done.numClicks:
   thisExp.addData('Rating_Done.timesOn', Rating_Done.timesOn)
   thisExp.addData('Rating_Done.timesOff', Rating_Done.timesOff)
else:
   thisExp.addData('Rating_Done.timesOn', "")
   thisExp.addData('Rating_Done.timesOff', "")
# the Routine "Rat" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
NSB3 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PsychopyIntegrationSheets/NSB3.xlsx'),
    seed=None, name='NSB3')
thisExp.addLoop(NSB3)  # add the loop to the experiment
thisNSB3 = NSB3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNSB3.rgb)
if thisNSB3 != None:
    for paramName in thisNSB3:
        exec('{} = thisNSB3[paramName]'.format(paramName))

for thisNSB3 in NSB3:
    currentLoop = NSB3
    # abbreviate parameter names if possible (e.g. rgb = thisNSB3.rgb)
    if thisNSB3 != None:
        for paramName in thisNSB3:
            exec('{} = thisNSB3[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    Trial_RatingResponse.reset()
    # reset Trial_ResponseDone to account for continued clicks & clear times on/off
    Trial_ResponseDone.reset()
    # keep track of which components have finished
    TrialComponents = [Trial_NSB, Trial_Cue, Trial_RatingText, Trial_RatingResponse, Trial_ResponseDone]
    for thisComponent in TrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Trial" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Trial_NSB* updates
        
        # if Trial_NSB is starting this frame...
        if Trial_NSB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Trial_NSB.frameNStart = frameN  # exact frame index
            Trial_NSB.tStart = t  # local t and not account for scr refresh
            Trial_NSB.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_NSB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_NSB.started')
            # update status
            Trial_NSB.status = STARTED
            Trial_NSB.setAutoDraw(True)
        
        # if Trial_NSB is active this frame...
        if Trial_NSB.status == STARTED:
            # update params
            pass
        
        # if Trial_NSB is stopping this frame...
        if Trial_NSB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Trial_NSB.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                Trial_NSB.tStop = t  # not accounting for scr refresh
                Trial_NSB.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Trial_NSB.stopped')
                # update status
                Trial_NSB.status = FINISHED
                Trial_NSB.setAutoDraw(False)
        
        # *Trial_Cue* updates
        
        # if Trial_Cue is starting this frame...
        if Trial_Cue.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            Trial_Cue.frameNStart = frameN  # exact frame index
            Trial_Cue.tStart = t  # local t and not account for scr refresh
            Trial_Cue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_Cue, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_Cue.started')
            # update status
            Trial_Cue.status = STARTED
            Trial_Cue.setAutoDraw(True)
        
        # if Trial_Cue is active this frame...
        if Trial_Cue.status == STARTED:
            # update params
            pass
        
        # if Trial_Cue is stopping this frame...
        if Trial_Cue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Trial_Cue.tStartRefresh + 12-frameTolerance:
                # keep track of stop time/frame for later
                Trial_Cue.tStop = t  # not accounting for scr refresh
                Trial_Cue.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Trial_Cue.stopped')
                # update status
                Trial_Cue.status = FINISHED
                Trial_Cue.setAutoDraw(False)
        
        # *Trial_RatingText* updates
        
        # if Trial_RatingText is starting this frame...
        if Trial_RatingText.status == NOT_STARTED and tThisFlip >= 15-frameTolerance:
            # keep track of start time/frame for later
            Trial_RatingText.frameNStart = frameN  # exact frame index
            Trial_RatingText.tStart = t  # local t and not account for scr refresh
            Trial_RatingText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_RatingText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_RatingText.started')
            # update status
            Trial_RatingText.status = STARTED
            Trial_RatingText.setAutoDraw(True)
        
        # if Trial_RatingText is active this frame...
        if Trial_RatingText.status == STARTED:
            # update params
            pass
        
        # *Trial_RatingResponse* updates
        
        # if Trial_RatingResponse is starting this frame...
        if Trial_RatingResponse.status == NOT_STARTED and tThisFlip >= 15-frameTolerance:
            # keep track of start time/frame for later
            Trial_RatingResponse.frameNStart = frameN  # exact frame index
            Trial_RatingResponse.tStart = t  # local t and not account for scr refresh
            Trial_RatingResponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_RatingResponse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_RatingResponse.started')
            # update status
            Trial_RatingResponse.status = STARTED
            Trial_RatingResponse.setAutoDraw(True)
        
        # if Trial_RatingResponse is active this frame...
        if Trial_RatingResponse.status == STARTED:
            # update params
            pass
        # *Trial_ResponseDone* updates
        
        # if Trial_ResponseDone is starting this frame...
        if Trial_ResponseDone.status == NOT_STARTED and Trial_RatingResponse.getRating() != None:
            # keep track of start time/frame for later
            Trial_ResponseDone.frameNStart = frameN  # exact frame index
            Trial_ResponseDone.tStart = t  # local t and not account for scr refresh
            Trial_ResponseDone.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_ResponseDone, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_ResponseDone.started')
            # update status
            Trial_ResponseDone.status = STARTED
            Trial_ResponseDone.setAutoDraw(True)
        
        # if Trial_ResponseDone is active this frame...
        if Trial_ResponseDone.status == STARTED:
            # update params
            pass
            # check whether Trial_ResponseDone has been pressed
            if Trial_ResponseDone.isClicked:
                if not Trial_ResponseDone.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    Trial_ResponseDone.timesOn.append(Trial_ResponseDone.buttonClock.getTime())
                    Trial_ResponseDone.timesOff.append(Trial_ResponseDone.buttonClock.getTime())
                elif len(Trial_ResponseDone.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    Trial_ResponseDone.timesOff[-1] = Trial_ResponseDone.buttonClock.getTime()
                if not Trial_ResponseDone.wasClicked:
                    # end routine when Trial_ResponseDone is clicked
                    continueRoutine = False
                if not Trial_ResponseDone.wasClicked:
                    # run callback code when Trial_ResponseDone is clicked
                    pass
        # take note of whether Trial_ResponseDone was clicked, so that next frame we know if clicks are new
        Trial_ResponseDone.wasClicked = Trial_ResponseDone.isClicked and Trial_ResponseDone.status == STARTED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Trial" ---
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    NSB3.addData('Trial_RatingResponse.response', Trial_RatingResponse.getRating())
    NSB3.addData('Trial_RatingResponse.rt', Trial_RatingResponse.getRT())
    NSB3.addData('Trial_ResponseDone.numClicks', Trial_ResponseDone.numClicks)
    if Trial_ResponseDone.numClicks:
       NSB3.addData('Trial_ResponseDone.timesOn', Trial_ResponseDone.timesOn)
       NSB3.addData('Trial_ResponseDone.timesOff', Trial_ResponseDone.timesOff)
    else:
       NSB3.addData('Trial_ResponseDone.timesOn', "")
       NSB3.addData('Trial_ResponseDone.timesOff', "")
    # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'NSB3'


# --- Prepare to start Routine "GR" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
GRComponents = [GetReady_Text, GetRead_Cross]
for thisComponent in GRComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "GR" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *GetReady_Text* updates
    
    # if GetReady_Text is starting this frame...
    if GetReady_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GetReady_Text.frameNStart = frameN  # exact frame index
        GetReady_Text.tStart = t  # local t and not account for scr refresh
        GetReady_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GetReady_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'GetReady_Text.started')
        # update status
        GetReady_Text.status = STARTED
        GetReady_Text.setAutoDraw(True)
    
    # if GetReady_Text is active this frame...
    if GetReady_Text.status == STARTED:
        # update params
        GetReady_Text.setText('', log=False)
    
    # if GetReady_Text is stopping this frame...
    if GetReady_Text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > GetReady_Text.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            GetReady_Text.tStop = t  # not accounting for scr refresh
            GetReady_Text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'GetReady_Text.stopped')
            # update status
            GetReady_Text.status = FINISHED
            GetReady_Text.setAutoDraw(False)
    
    # *GetRead_Cross* updates
    
    # if GetRead_Cross is starting this frame...
    if GetRead_Cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GetRead_Cross.frameNStart = frameN  # exact frame index
        GetRead_Cross.tStart = t  # local t and not account for scr refresh
        GetRead_Cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GetRead_Cross, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'GetRead_Cross.started')
        # update status
        GetRead_Cross.status = STARTED
        GetRead_Cross.setAutoDraw(True)
    
    # if GetRead_Cross is active this frame...
    if GetRead_Cross.status == STARTED:
        # update params
        pass
    
    # if GetRead_Cross is stopping this frame...
    if GetRead_Cross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > GetRead_Cross.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            GetRead_Cross.tStop = t  # not accounting for scr refresh
            GetRead_Cross.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'GetRead_Cross.stopped')
            # update status
            GetRead_Cross.status = FINISHED
            GetRead_Cross.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GRComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "GR" ---
for thisComponent in GRComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# set up handler to look after randomisation of conditions etc
Neu3 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PsychopyIntegrationSheets/Neutral3.xlsx'),
    seed=None, name='Neu3')
thisExp.addLoop(Neu3)  # add the loop to the experiment
thisNeu3 = Neu3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNeu3.rgb)
if thisNeu3 != None:
    for paramName in thisNeu3:
        exec('{} = thisNeu3[paramName]'.format(paramName))

for thisNeu3 in Neu3:
    currentLoop = Neu3
    # abbreviate parameter names if possible (e.g. rgb = thisNeu3.rgb)
    if thisNeu3 != None:
        for paramName in thisNeu3:
            exec('{} = thisNeu3[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "SS" ---
    continueRoutine = True
    # update component parameters for each repeat
    StorySentence_Text.setText(StorySentences)
    # keep track of which components have finished
    SSComponents = [StorySentence_Text]
    for thisComponent in SSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "SS" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *StorySentence_Text* updates
        
        # if StorySentence_Text is starting this frame...
        if StorySentence_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StorySentence_Text.frameNStart = frameN  # exact frame index
            StorySentence_Text.tStart = t  # local t and not account for scr refresh
            StorySentence_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StorySentence_Text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'StorySentence_Text.started')
            # update status
            StorySentence_Text.status = STARTED
            StorySentence_Text.setAutoDraw(True)
        
        # if StorySentence_Text is active this frame...
        if StorySentence_Text.status == STARTED:
            # update params
            pass
        
        # if StorySentence_Text is stopping this frame...
        if StorySentence_Text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StorySentence_Text.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                StorySentence_Text.tStop = t  # not accounting for scr refresh
                StorySentence_Text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'StorySentence_Text.stopped')
                # update status
                StorySentence_Text.status = FINISHED
                StorySentence_Text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "SS" ---
    for thisComponent in SSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Neu3'


# set up handler to look after randomisation of conditions etc
NeuSta3 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PsychopyIntegrationSheets/NeutralStatements3.xlsx'),
    seed=None, name='NeuSta3')
thisExp.addLoop(NeuSta3)  # add the loop to the experiment
thisNeuSta3 = NeuSta3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNeuSta3.rgb)
if thisNeuSta3 != None:
    for paramName in thisNeuSta3:
        exec('{} = thisNeuSta3[paramName]'.format(paramName))

for thisNeuSta3 in NeuSta3:
    currentLoop = NeuSta3
    # abbreviate parameter names if possible (e.g. rgb = thisNeuSta3.rgb)
    if thisNeuSta3 != None:
        for paramName in thisNeuSta3:
            exec('{} = thisNeuSta3[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "NS" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    NSComponents = [NeutralStatement_Text]
    for thisComponent in NSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "NS" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 12.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NeutralStatement_Text* updates
        
        # if NeutralStatement_Text is starting this frame...
        if NeutralStatement_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NeutralStatement_Text.frameNStart = frameN  # exact frame index
            NeutralStatement_Text.tStart = t  # local t and not account for scr refresh
            NeutralStatement_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NeutralStatement_Text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NeutralStatement_Text.started')
            # update status
            NeutralStatement_Text.status = STARTED
            NeutralStatement_Text.setAutoDraw(True)
        
        # if NeutralStatement_Text is active this frame...
        if NeutralStatement_Text.status == STARTED:
            # update params
            pass
        
        # if NeutralStatement_Text is stopping this frame...
        if NeutralStatement_Text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > NeutralStatement_Text.tStartRefresh + 12-frameTolerance:
                # keep track of stop time/frame for later
                NeutralStatement_Text.tStop = t  # not accounting for scr refresh
                NeutralStatement_Text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'NeutralStatement_Text.stopped')
                # update status
                NeutralStatement_Text.status = FINISHED
                NeutralStatement_Text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "NS" ---
    for thisComponent in NSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-12.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'NeuSta3'


# --- Prepare to start Routine "Rat" ---
continueRoutine = True
# update component parameters for each repeat
Rating_Response.reset()
# reset Rating_Done to account for continued clicks & clear times on/off
Rating_Done.reset()
# keep track of which components have finished
RatComponents = [Rating_Text, Rating_Response, Rating_Done]
for thisComponent in RatComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Rat" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Rating_Text* updates
    
    # if Rating_Text is starting this frame...
    if Rating_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rating_Text.frameNStart = frameN  # exact frame index
        Rating_Text.tStart = t  # local t and not account for scr refresh
        Rating_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Text.started')
        # update status
        Rating_Text.status = STARTED
        Rating_Text.setAutoDraw(True)
    
    # if Rating_Text is active this frame...
    if Rating_Text.status == STARTED:
        # update params
        pass
    
    # *Rating_Response* updates
    
    # if Rating_Response is starting this frame...
    if Rating_Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rating_Response.frameNStart = frameN  # exact frame index
        Rating_Response.tStart = t  # local t and not account for scr refresh
        Rating_Response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Response, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Response.started')
        # update status
        Rating_Response.status = STARTED
        Rating_Response.setAutoDraw(True)
    
    # if Rating_Response is active this frame...
    if Rating_Response.status == STARTED:
        # update params
        pass
    # *Rating_Done* updates
    
    # if Rating_Done is starting this frame...
    if Rating_Done.status == NOT_STARTED and Rating_Response.getRating() != None:
        # keep track of start time/frame for later
        Rating_Done.frameNStart = frameN  # exact frame index
        Rating_Done.tStart = t  # local t and not account for scr refresh
        Rating_Done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Done, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Done.started')
        # update status
        Rating_Done.status = STARTED
        Rating_Done.setAutoDraw(True)
    
    # if Rating_Done is active this frame...
    if Rating_Done.status == STARTED:
        # update params
        pass
        # check whether Rating_Done has been pressed
        if Rating_Done.isClicked:
            if not Rating_Done.wasClicked:
                # if this is a new click, store time of first click and clicked until
                Rating_Done.timesOn.append(Rating_Done.buttonClock.getTime())
                Rating_Done.timesOff.append(Rating_Done.buttonClock.getTime())
            elif len(Rating_Done.timesOff):
                # if click is continuing from last frame, update time of clicked until
                Rating_Done.timesOff[-1] = Rating_Done.buttonClock.getTime()
            if not Rating_Done.wasClicked:
                # end routine when Rating_Done is clicked
                continueRoutine = False
            if not Rating_Done.wasClicked:
                # run callback code when Rating_Done is clicked
                pass
    # take note of whether Rating_Done was clicked, so that next frame we know if clicks are new
    Rating_Done.wasClicked = Rating_Done.isClicked and Rating_Done.status == STARTED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RatComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Rat" ---
for thisComponent in RatComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Rating_Response.response', Rating_Response.getRating())
thisExp.addData('Rating_Response.rt', Rating_Response.getRT())
thisExp.addData('Rating_Done.numClicks', Rating_Done.numClicks)
if Rating_Done.numClicks:
   thisExp.addData('Rating_Done.timesOn', Rating_Done.timesOn)
   thisExp.addData('Rating_Done.timesOff', Rating_Done.timesOff)
else:
   thisExp.addData('Rating_Done.timesOn', "")
   thisExp.addData('Rating_Done.timesOff', "")
# the Routine "Rat" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "RegRat" ---
continueRoutine = True
# update component parameters for each repeat
RegulationRating_Response.reset()
# reset RegulationRating_Done to account for continued clicks & clear times on/off
RegulationRating_Done.reset()
# keep track of which components have finished
RegRatComponents = [RegulationRating_Text, RegulationRating_Response, RegulationRating_Done]
for thisComponent in RegRatComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "RegRat" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *RegulationRating_Text* updates
    
    # if RegulationRating_Text is starting this frame...
    if RegulationRating_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RegulationRating_Text.frameNStart = frameN  # exact frame index
        RegulationRating_Text.tStart = t  # local t and not account for scr refresh
        RegulationRating_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RegulationRating_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RegulationRating_Text.started')
        # update status
        RegulationRating_Text.status = STARTED
        RegulationRating_Text.setAutoDraw(True)
    
    # if RegulationRating_Text is active this frame...
    if RegulationRating_Text.status == STARTED:
        # update params
        pass
    
    # *RegulationRating_Response* updates
    
    # if RegulationRating_Response is starting this frame...
    if RegulationRating_Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RegulationRating_Response.frameNStart = frameN  # exact frame index
        RegulationRating_Response.tStart = t  # local t and not account for scr refresh
        RegulationRating_Response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RegulationRating_Response, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RegulationRating_Response.started')
        # update status
        RegulationRating_Response.status = STARTED
        RegulationRating_Response.setAutoDraw(True)
    
    # if RegulationRating_Response is active this frame...
    if RegulationRating_Response.status == STARTED:
        # update params
        pass
    # *RegulationRating_Done* updates
    
    # if RegulationRating_Done is starting this frame...
    if RegulationRating_Done.status == NOT_STARTED and RegulationRating_Response.getRating() != None:
        # keep track of start time/frame for later
        RegulationRating_Done.frameNStart = frameN  # exact frame index
        RegulationRating_Done.tStart = t  # local t and not account for scr refresh
        RegulationRating_Done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RegulationRating_Done, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RegulationRating_Done.started')
        # update status
        RegulationRating_Done.status = STARTED
        RegulationRating_Done.setAutoDraw(True)
    
    # if RegulationRating_Done is active this frame...
    if RegulationRating_Done.status == STARTED:
        # update params
        pass
        # check whether RegulationRating_Done has been pressed
        if RegulationRating_Done.isClicked:
            if not RegulationRating_Done.wasClicked:
                # if this is a new click, store time of first click and clicked until
                RegulationRating_Done.timesOn.append(RegulationRating_Done.buttonClock.getTime())
                RegulationRating_Done.timesOff.append(RegulationRating_Done.buttonClock.getTime())
            elif len(RegulationRating_Done.timesOff):
                # if click is continuing from last frame, update time of clicked until
                RegulationRating_Done.timesOff[-1] = RegulationRating_Done.buttonClock.getTime()
            if not RegulationRating_Done.wasClicked:
                # end routine when RegulationRating_Done is clicked
                continueRoutine = False
            if not RegulationRating_Done.wasClicked:
                # run callback code when RegulationRating_Done is clicked
                pass
    # take note of whether RegulationRating_Done was clicked, so that next frame we know if clicks are new
    RegulationRating_Done.wasClicked = RegulationRating_Done.isClicked and RegulationRating_Done.status == STARTED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RegRatComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "RegRat" ---
for thisComponent in RegRatComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('RegulationRating_Response.response', RegulationRating_Response.getRating())
thisExp.addData('RegulationRating_Response.rt', RegulationRating_Response.getRT())
thisExp.addData('RegulationRating_Done.numClicks', RegulationRating_Done.numClicks)
if RegulationRating_Done.numClicks:
   thisExp.addData('RegulationRating_Done.timesOn', RegulationRating_Done.timesOn)
   thisExp.addData('RegulationRating_Done.timesOff', RegulationRating_Done.timesOff)
else:
   thisExp.addData('RegulationRating_Done.timesOn', "")
   thisExp.addData('RegulationRating_Done.timesOff', "")
# the Routine "RegRat" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "BC" ---
continueRoutine = True
# update component parameters for each repeat
# reset BContinue_Button to account for continued clicks & clear times on/off
BContinue_Button.reset()
# keep track of which components have finished
BCComponents = [BContinue_Button, BContinue_Text]
for thisComponent in BCComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "BC" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *BContinue_Button* updates
    
    # if BContinue_Button is starting this frame...
    if BContinue_Button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        BContinue_Button.frameNStart = frameN  # exact frame index
        BContinue_Button.tStart = t  # local t and not account for scr refresh
        BContinue_Button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BContinue_Button, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'BContinue_Button.started')
        # update status
        BContinue_Button.status = STARTED
        BContinue_Button.setAutoDraw(True)
    
    # if BContinue_Button is active this frame...
    if BContinue_Button.status == STARTED:
        # update params
        pass
        # check whether BContinue_Button has been pressed
        if BContinue_Button.isClicked:
            if not BContinue_Button.wasClicked:
                # if this is a new click, store time of first click and clicked until
                BContinue_Button.timesOn.append(BContinue_Button.buttonClock.getTime())
                BContinue_Button.timesOff.append(BContinue_Button.buttonClock.getTime())
            elif len(BContinue_Button.timesOff):
                # if click is continuing from last frame, update time of clicked until
                BContinue_Button.timesOff[-1] = BContinue_Button.buttonClock.getTime()
            if not BContinue_Button.wasClicked:
                # end routine when BContinue_Button is clicked
                continueRoutine = False
            if not BContinue_Button.wasClicked:
                # run callback code when BContinue_Button is clicked
                pass
    # take note of whether BContinue_Button was clicked, so that next frame we know if clicks are new
    BContinue_Button.wasClicked = BContinue_Button.isClicked and BContinue_Button.status == STARTED
    
    # *BContinue_Text* updates
    
    # if BContinue_Text is starting this frame...
    if BContinue_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BContinue_Text.frameNStart = frameN  # exact frame index
        BContinue_Text.tStart = t  # local t and not account for scr refresh
        BContinue_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BContinue_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'BContinue_Text.started')
        # update status
        BContinue_Text.status = STARTED
        BContinue_Text.setAutoDraw(True)
    
    # if BContinue_Text is active this frame...
    if BContinue_Text.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BCComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "BC" ---
for thisComponent in BCComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('BContinue_Button.numClicks', BContinue_Button.numClicks)
if BContinue_Button.numClicks:
   thisExp.addData('BContinue_Button.timesOn', BContinue_Button.timesOn)
   thisExp.addData('BContinue_Button.timesOff', BContinue_Button.timesOff)
else:
   thisExp.addData('BContinue_Button.timesOn', "")
   thisExp.addData('BContinue_Button.timesOff', "")
# the Routine "BC" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Cond" ---
continueRoutine = True
# update component parameters for each repeat
ConditionTextBox.reset()
# reset ConditionDone to account for continued clicks & clear times on/off
ConditionDone.reset()
# keep track of which components have finished
CondComponents = [ConditionTextBox, ConditionDone]
for thisComponent in CondComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Cond" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ConditionTextBox* updates
    
    # if ConditionTextBox is starting this frame...
    if ConditionTextBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ConditionTextBox.frameNStart = frameN  # exact frame index
        ConditionTextBox.tStart = t  # local t and not account for scr refresh
        ConditionTextBox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ConditionTextBox, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ConditionTextBox.started')
        # update status
        ConditionTextBox.status = STARTED
        ConditionTextBox.setAutoDraw(True)
    
    # if ConditionTextBox is active this frame...
    if ConditionTextBox.status == STARTED:
        # update params
        pass
    # *ConditionDone* updates
    
    # if ConditionDone is starting this frame...
    if ConditionDone.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        ConditionDone.frameNStart = frameN  # exact frame index
        ConditionDone.tStart = t  # local t and not account for scr refresh
        ConditionDone.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ConditionDone, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ConditionDone.started')
        # update status
        ConditionDone.status = STARTED
        ConditionDone.setAutoDraw(True)
    
    # if ConditionDone is active this frame...
    if ConditionDone.status == STARTED:
        # update params
        pass
        # check whether ConditionDone has been pressed
        if ConditionDone.isClicked:
            if not ConditionDone.wasClicked:
                # if this is a new click, store time of first click and clicked until
                ConditionDone.timesOn.append(ConditionDone.buttonClock.getTime())
                ConditionDone.timesOff.append(ConditionDone.buttonClock.getTime())
            elif len(ConditionDone.timesOff):
                # if click is continuing from last frame, update time of clicked until
                ConditionDone.timesOff[-1] = ConditionDone.buttonClock.getTime()
            if not ConditionDone.wasClicked:
                # end routine when ConditionDone is clicked
                continueRoutine = False
            if not ConditionDone.wasClicked:
                # run callback code when ConditionDone is clicked
                pass
    # take note of whether ConditionDone was clicked, so that next frame we know if clicks are new
    ConditionDone.wasClicked = ConditionDone.isClicked and ConditionDone.status == STARTED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CondComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Cond" ---
for thisComponent in CondComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ConditionTextBox.text',ConditionTextBox.text)
thisExp.addData('ConditionDone.numClicks', ConditionDone.numClicks)
if ConditionDone.numClicks:
   thisExp.addData('ConditionDone.timesOn', ConditionDone.timesOn)
   thisExp.addData('ConditionDone.timesOff', ConditionDone.timesOff)
else:
   thisExp.addData('ConditionDone.timesOn', "")
   thisExp.addData('ConditionDone.timesOff', "")
# the Routine "Cond" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "GR" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
GRComponents = [GetReady_Text, GetRead_Cross]
for thisComponent in GRComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "GR" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *GetReady_Text* updates
    
    # if GetReady_Text is starting this frame...
    if GetReady_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GetReady_Text.frameNStart = frameN  # exact frame index
        GetReady_Text.tStart = t  # local t and not account for scr refresh
        GetReady_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GetReady_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'GetReady_Text.started')
        # update status
        GetReady_Text.status = STARTED
        GetReady_Text.setAutoDraw(True)
    
    # if GetReady_Text is active this frame...
    if GetReady_Text.status == STARTED:
        # update params
        GetReady_Text.setText('', log=False)
    
    # if GetReady_Text is stopping this frame...
    if GetReady_Text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > GetReady_Text.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            GetReady_Text.tStop = t  # not accounting for scr refresh
            GetReady_Text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'GetReady_Text.stopped')
            # update status
            GetReady_Text.status = FINISHED
            GetReady_Text.setAutoDraw(False)
    
    # *GetRead_Cross* updates
    
    # if GetRead_Cross is starting this frame...
    if GetRead_Cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GetRead_Cross.frameNStart = frameN  # exact frame index
        GetRead_Cross.tStart = t  # local t and not account for scr refresh
        GetRead_Cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GetRead_Cross, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'GetRead_Cross.started')
        # update status
        GetRead_Cross.status = STARTED
        GetRead_Cross.setAutoDraw(True)
    
    # if GetRead_Cross is active this frame...
    if GetRead_Cross.status == STARTED:
        # update params
        pass
    
    # if GetRead_Cross is stopping this frame...
    if GetRead_Cross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > GetRead_Cross.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            GetRead_Cross.tStop = t  # not accounting for scr refresh
            GetRead_Cross.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'GetRead_Cross.stopped')
            # update status
            GetRead_Cross.status = FINISHED
            GetRead_Cross.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GRComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "GR" ---
for thisComponent in GRComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# set up handler to look after randomisation of conditions etc
Neg4 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PsychopyIntegrationSheets/Negative4.xlsx'),
    seed=None, name='Neg4')
thisExp.addLoop(Neg4)  # add the loop to the experiment
thisNeg4 = Neg4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNeg4.rgb)
if thisNeg4 != None:
    for paramName in thisNeg4:
        exec('{} = thisNeg4[paramName]'.format(paramName))

for thisNeg4 in Neg4:
    currentLoop = Neg4
    # abbreviate parameter names if possible (e.g. rgb = thisNeg4.rgb)
    if thisNeg4 != None:
        for paramName in thisNeg4:
            exec('{} = thisNeg4[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "SS" ---
    continueRoutine = True
    # update component parameters for each repeat
    StorySentence_Text.setText(StorySentences)
    # keep track of which components have finished
    SSComponents = [StorySentence_Text]
    for thisComponent in SSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "SS" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *StorySentence_Text* updates
        
        # if StorySentence_Text is starting this frame...
        if StorySentence_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StorySentence_Text.frameNStart = frameN  # exact frame index
            StorySentence_Text.tStart = t  # local t and not account for scr refresh
            StorySentence_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StorySentence_Text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'StorySentence_Text.started')
            # update status
            StorySentence_Text.status = STARTED
            StorySentence_Text.setAutoDraw(True)
        
        # if StorySentence_Text is active this frame...
        if StorySentence_Text.status == STARTED:
            # update params
            pass
        
        # if StorySentence_Text is stopping this frame...
        if StorySentence_Text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StorySentence_Text.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                StorySentence_Text.tStop = t  # not accounting for scr refresh
                StorySentence_Text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'StorySentence_Text.stopped')
                # update status
                StorySentence_Text.status = FINISHED
                StorySentence_Text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "SS" ---
    for thisComponent in SSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Neg4'


# --- Prepare to start Routine "Rat" ---
continueRoutine = True
# update component parameters for each repeat
Rating_Response.reset()
# reset Rating_Done to account for continued clicks & clear times on/off
Rating_Done.reset()
# keep track of which components have finished
RatComponents = [Rating_Text, Rating_Response, Rating_Done]
for thisComponent in RatComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Rat" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Rating_Text* updates
    
    # if Rating_Text is starting this frame...
    if Rating_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rating_Text.frameNStart = frameN  # exact frame index
        Rating_Text.tStart = t  # local t and not account for scr refresh
        Rating_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Text.started')
        # update status
        Rating_Text.status = STARTED
        Rating_Text.setAutoDraw(True)
    
    # if Rating_Text is active this frame...
    if Rating_Text.status == STARTED:
        # update params
        pass
    
    # *Rating_Response* updates
    
    # if Rating_Response is starting this frame...
    if Rating_Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rating_Response.frameNStart = frameN  # exact frame index
        Rating_Response.tStart = t  # local t and not account for scr refresh
        Rating_Response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Response, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Response.started')
        # update status
        Rating_Response.status = STARTED
        Rating_Response.setAutoDraw(True)
    
    # if Rating_Response is active this frame...
    if Rating_Response.status == STARTED:
        # update params
        pass
    # *Rating_Done* updates
    
    # if Rating_Done is starting this frame...
    if Rating_Done.status == NOT_STARTED and Rating_Response.getRating() != None:
        # keep track of start time/frame for later
        Rating_Done.frameNStart = frameN  # exact frame index
        Rating_Done.tStart = t  # local t and not account for scr refresh
        Rating_Done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Done, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Done.started')
        # update status
        Rating_Done.status = STARTED
        Rating_Done.setAutoDraw(True)
    
    # if Rating_Done is active this frame...
    if Rating_Done.status == STARTED:
        # update params
        pass
        # check whether Rating_Done has been pressed
        if Rating_Done.isClicked:
            if not Rating_Done.wasClicked:
                # if this is a new click, store time of first click and clicked until
                Rating_Done.timesOn.append(Rating_Done.buttonClock.getTime())
                Rating_Done.timesOff.append(Rating_Done.buttonClock.getTime())
            elif len(Rating_Done.timesOff):
                # if click is continuing from last frame, update time of clicked until
                Rating_Done.timesOff[-1] = Rating_Done.buttonClock.getTime()
            if not Rating_Done.wasClicked:
                # end routine when Rating_Done is clicked
                continueRoutine = False
            if not Rating_Done.wasClicked:
                # run callback code when Rating_Done is clicked
                pass
    # take note of whether Rating_Done was clicked, so that next frame we know if clicks are new
    Rating_Done.wasClicked = Rating_Done.isClicked and Rating_Done.status == STARTED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RatComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Rat" ---
for thisComponent in RatComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Rating_Response.response', Rating_Response.getRating())
thisExp.addData('Rating_Response.rt', Rating_Response.getRT())
thisExp.addData('Rating_Done.numClicks', Rating_Done.numClicks)
if Rating_Done.numClicks:
   thisExp.addData('Rating_Done.timesOn', Rating_Done.timesOn)
   thisExp.addData('Rating_Done.timesOff', Rating_Done.timesOff)
else:
   thisExp.addData('Rating_Done.timesOn', "")
   thisExp.addData('Rating_Done.timesOff', "")
# the Routine "Rat" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
NSB4 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PsychopyIntegrationSheets/NSB4.xlsx'),
    seed=None, name='NSB4')
thisExp.addLoop(NSB4)  # add the loop to the experiment
thisNSB4 = NSB4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNSB4.rgb)
if thisNSB4 != None:
    for paramName in thisNSB4:
        exec('{} = thisNSB4[paramName]'.format(paramName))

for thisNSB4 in NSB4:
    currentLoop = NSB4
    # abbreviate parameter names if possible (e.g. rgb = thisNSB4.rgb)
    if thisNSB4 != None:
        for paramName in thisNSB4:
            exec('{} = thisNSB4[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    Trial_RatingResponse.reset()
    # reset Trial_ResponseDone to account for continued clicks & clear times on/off
    Trial_ResponseDone.reset()
    # keep track of which components have finished
    TrialComponents = [Trial_NSB, Trial_Cue, Trial_RatingText, Trial_RatingResponse, Trial_ResponseDone]
    for thisComponent in TrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Trial" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Trial_NSB* updates
        
        # if Trial_NSB is starting this frame...
        if Trial_NSB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Trial_NSB.frameNStart = frameN  # exact frame index
            Trial_NSB.tStart = t  # local t and not account for scr refresh
            Trial_NSB.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_NSB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_NSB.started')
            # update status
            Trial_NSB.status = STARTED
            Trial_NSB.setAutoDraw(True)
        
        # if Trial_NSB is active this frame...
        if Trial_NSB.status == STARTED:
            # update params
            pass
        
        # if Trial_NSB is stopping this frame...
        if Trial_NSB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Trial_NSB.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                Trial_NSB.tStop = t  # not accounting for scr refresh
                Trial_NSB.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Trial_NSB.stopped')
                # update status
                Trial_NSB.status = FINISHED
                Trial_NSB.setAutoDraw(False)
        
        # *Trial_Cue* updates
        
        # if Trial_Cue is starting this frame...
        if Trial_Cue.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            Trial_Cue.frameNStart = frameN  # exact frame index
            Trial_Cue.tStart = t  # local t and not account for scr refresh
            Trial_Cue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_Cue, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_Cue.started')
            # update status
            Trial_Cue.status = STARTED
            Trial_Cue.setAutoDraw(True)
        
        # if Trial_Cue is active this frame...
        if Trial_Cue.status == STARTED:
            # update params
            pass
        
        # if Trial_Cue is stopping this frame...
        if Trial_Cue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Trial_Cue.tStartRefresh + 12-frameTolerance:
                # keep track of stop time/frame for later
                Trial_Cue.tStop = t  # not accounting for scr refresh
                Trial_Cue.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Trial_Cue.stopped')
                # update status
                Trial_Cue.status = FINISHED
                Trial_Cue.setAutoDraw(False)
        
        # *Trial_RatingText* updates
        
        # if Trial_RatingText is starting this frame...
        if Trial_RatingText.status == NOT_STARTED and tThisFlip >= 15-frameTolerance:
            # keep track of start time/frame for later
            Trial_RatingText.frameNStart = frameN  # exact frame index
            Trial_RatingText.tStart = t  # local t and not account for scr refresh
            Trial_RatingText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_RatingText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_RatingText.started')
            # update status
            Trial_RatingText.status = STARTED
            Trial_RatingText.setAutoDraw(True)
        
        # if Trial_RatingText is active this frame...
        if Trial_RatingText.status == STARTED:
            # update params
            pass
        
        # *Trial_RatingResponse* updates
        
        # if Trial_RatingResponse is starting this frame...
        if Trial_RatingResponse.status == NOT_STARTED and tThisFlip >= 15-frameTolerance:
            # keep track of start time/frame for later
            Trial_RatingResponse.frameNStart = frameN  # exact frame index
            Trial_RatingResponse.tStart = t  # local t and not account for scr refresh
            Trial_RatingResponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_RatingResponse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_RatingResponse.started')
            # update status
            Trial_RatingResponse.status = STARTED
            Trial_RatingResponse.setAutoDraw(True)
        
        # if Trial_RatingResponse is active this frame...
        if Trial_RatingResponse.status == STARTED:
            # update params
            pass
        # *Trial_ResponseDone* updates
        
        # if Trial_ResponseDone is starting this frame...
        if Trial_ResponseDone.status == NOT_STARTED and Trial_RatingResponse.getRating() != None:
            # keep track of start time/frame for later
            Trial_ResponseDone.frameNStart = frameN  # exact frame index
            Trial_ResponseDone.tStart = t  # local t and not account for scr refresh
            Trial_ResponseDone.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_ResponseDone, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_ResponseDone.started')
            # update status
            Trial_ResponseDone.status = STARTED
            Trial_ResponseDone.setAutoDraw(True)
        
        # if Trial_ResponseDone is active this frame...
        if Trial_ResponseDone.status == STARTED:
            # update params
            pass
            # check whether Trial_ResponseDone has been pressed
            if Trial_ResponseDone.isClicked:
                if not Trial_ResponseDone.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    Trial_ResponseDone.timesOn.append(Trial_ResponseDone.buttonClock.getTime())
                    Trial_ResponseDone.timesOff.append(Trial_ResponseDone.buttonClock.getTime())
                elif len(Trial_ResponseDone.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    Trial_ResponseDone.timesOff[-1] = Trial_ResponseDone.buttonClock.getTime()
                if not Trial_ResponseDone.wasClicked:
                    # end routine when Trial_ResponseDone is clicked
                    continueRoutine = False
                if not Trial_ResponseDone.wasClicked:
                    # run callback code when Trial_ResponseDone is clicked
                    pass
        # take note of whether Trial_ResponseDone was clicked, so that next frame we know if clicks are new
        Trial_ResponseDone.wasClicked = Trial_ResponseDone.isClicked and Trial_ResponseDone.status == STARTED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Trial" ---
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    NSB4.addData('Trial_RatingResponse.response', Trial_RatingResponse.getRating())
    NSB4.addData('Trial_RatingResponse.rt', Trial_RatingResponse.getRT())
    NSB4.addData('Trial_ResponseDone.numClicks', Trial_ResponseDone.numClicks)
    if Trial_ResponseDone.numClicks:
       NSB4.addData('Trial_ResponseDone.timesOn', Trial_ResponseDone.timesOn)
       NSB4.addData('Trial_ResponseDone.timesOff', Trial_ResponseDone.timesOff)
    else:
       NSB4.addData('Trial_ResponseDone.timesOn', "")
       NSB4.addData('Trial_ResponseDone.timesOff', "")
    # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'NSB4'


# --- Prepare to start Routine "GR" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
GRComponents = [GetReady_Text, GetRead_Cross]
for thisComponent in GRComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "GR" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *GetReady_Text* updates
    
    # if GetReady_Text is starting this frame...
    if GetReady_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GetReady_Text.frameNStart = frameN  # exact frame index
        GetReady_Text.tStart = t  # local t and not account for scr refresh
        GetReady_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GetReady_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'GetReady_Text.started')
        # update status
        GetReady_Text.status = STARTED
        GetReady_Text.setAutoDraw(True)
    
    # if GetReady_Text is active this frame...
    if GetReady_Text.status == STARTED:
        # update params
        GetReady_Text.setText('', log=False)
    
    # if GetReady_Text is stopping this frame...
    if GetReady_Text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > GetReady_Text.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            GetReady_Text.tStop = t  # not accounting for scr refresh
            GetReady_Text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'GetReady_Text.stopped')
            # update status
            GetReady_Text.status = FINISHED
            GetReady_Text.setAutoDraw(False)
    
    # *GetRead_Cross* updates
    
    # if GetRead_Cross is starting this frame...
    if GetRead_Cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GetRead_Cross.frameNStart = frameN  # exact frame index
        GetRead_Cross.tStart = t  # local t and not account for scr refresh
        GetRead_Cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GetRead_Cross, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'GetRead_Cross.started')
        # update status
        GetRead_Cross.status = STARTED
        GetRead_Cross.setAutoDraw(True)
    
    # if GetRead_Cross is active this frame...
    if GetRead_Cross.status == STARTED:
        # update params
        pass
    
    # if GetRead_Cross is stopping this frame...
    if GetRead_Cross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > GetRead_Cross.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            GetRead_Cross.tStop = t  # not accounting for scr refresh
            GetRead_Cross.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'GetRead_Cross.stopped')
            # update status
            GetRead_Cross.status = FINISHED
            GetRead_Cross.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GRComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "GR" ---
for thisComponent in GRComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# set up handler to look after randomisation of conditions etc
Neu4 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PsychopyIntegrationSheets/Neutral4.xlsx'),
    seed=None, name='Neu4')
thisExp.addLoop(Neu4)  # add the loop to the experiment
thisNeu4 = Neu4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNeu4.rgb)
if thisNeu4 != None:
    for paramName in thisNeu4:
        exec('{} = thisNeu4[paramName]'.format(paramName))

for thisNeu4 in Neu4:
    currentLoop = Neu4
    # abbreviate parameter names if possible (e.g. rgb = thisNeu4.rgb)
    if thisNeu4 != None:
        for paramName in thisNeu4:
            exec('{} = thisNeu4[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "SS" ---
    continueRoutine = True
    # update component parameters for each repeat
    StorySentence_Text.setText(StorySentences)
    # keep track of which components have finished
    SSComponents = [StorySentence_Text]
    for thisComponent in SSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "SS" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *StorySentence_Text* updates
        
        # if StorySentence_Text is starting this frame...
        if StorySentence_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StorySentence_Text.frameNStart = frameN  # exact frame index
            StorySentence_Text.tStart = t  # local t and not account for scr refresh
            StorySentence_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StorySentence_Text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'StorySentence_Text.started')
            # update status
            StorySentence_Text.status = STARTED
            StorySentence_Text.setAutoDraw(True)
        
        # if StorySentence_Text is active this frame...
        if StorySentence_Text.status == STARTED:
            # update params
            pass
        
        # if StorySentence_Text is stopping this frame...
        if StorySentence_Text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StorySentence_Text.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                StorySentence_Text.tStop = t  # not accounting for scr refresh
                StorySentence_Text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'StorySentence_Text.stopped')
                # update status
                StorySentence_Text.status = FINISHED
                StorySentence_Text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "SS" ---
    for thisComponent in SSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Neu4'


# set up handler to look after randomisation of conditions etc
NeuSta4 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PsychopyIntegrationSheets/NeutralStatements4.xlsx'),
    seed=None, name='NeuSta4')
thisExp.addLoop(NeuSta4)  # add the loop to the experiment
thisNeuSta4 = NeuSta4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNeuSta4.rgb)
if thisNeuSta4 != None:
    for paramName in thisNeuSta4:
        exec('{} = thisNeuSta4[paramName]'.format(paramName))

for thisNeuSta4 in NeuSta4:
    currentLoop = NeuSta4
    # abbreviate parameter names if possible (e.g. rgb = thisNeuSta4.rgb)
    if thisNeuSta4 != None:
        for paramName in thisNeuSta4:
            exec('{} = thisNeuSta4[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "NS" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    NSComponents = [NeutralStatement_Text]
    for thisComponent in NSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "NS" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 12.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NeutralStatement_Text* updates
        
        # if NeutralStatement_Text is starting this frame...
        if NeutralStatement_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NeutralStatement_Text.frameNStart = frameN  # exact frame index
            NeutralStatement_Text.tStart = t  # local t and not account for scr refresh
            NeutralStatement_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NeutralStatement_Text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NeutralStatement_Text.started')
            # update status
            NeutralStatement_Text.status = STARTED
            NeutralStatement_Text.setAutoDraw(True)
        
        # if NeutralStatement_Text is active this frame...
        if NeutralStatement_Text.status == STARTED:
            # update params
            pass
        
        # if NeutralStatement_Text is stopping this frame...
        if NeutralStatement_Text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > NeutralStatement_Text.tStartRefresh + 12-frameTolerance:
                # keep track of stop time/frame for later
                NeutralStatement_Text.tStop = t  # not accounting for scr refresh
                NeutralStatement_Text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'NeutralStatement_Text.stopped')
                # update status
                NeutralStatement_Text.status = FINISHED
                NeutralStatement_Text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "NS" ---
    for thisComponent in NSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-12.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'NeuSta4'


# --- Prepare to start Routine "Rat" ---
continueRoutine = True
# update component parameters for each repeat
Rating_Response.reset()
# reset Rating_Done to account for continued clicks & clear times on/off
Rating_Done.reset()
# keep track of which components have finished
RatComponents = [Rating_Text, Rating_Response, Rating_Done]
for thisComponent in RatComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Rat" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Rating_Text* updates
    
    # if Rating_Text is starting this frame...
    if Rating_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rating_Text.frameNStart = frameN  # exact frame index
        Rating_Text.tStart = t  # local t and not account for scr refresh
        Rating_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Text.started')
        # update status
        Rating_Text.status = STARTED
        Rating_Text.setAutoDraw(True)
    
    # if Rating_Text is active this frame...
    if Rating_Text.status == STARTED:
        # update params
        pass
    
    # *Rating_Response* updates
    
    # if Rating_Response is starting this frame...
    if Rating_Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rating_Response.frameNStart = frameN  # exact frame index
        Rating_Response.tStart = t  # local t and not account for scr refresh
        Rating_Response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Response, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Response.started')
        # update status
        Rating_Response.status = STARTED
        Rating_Response.setAutoDraw(True)
    
    # if Rating_Response is active this frame...
    if Rating_Response.status == STARTED:
        # update params
        pass
    # *Rating_Done* updates
    
    # if Rating_Done is starting this frame...
    if Rating_Done.status == NOT_STARTED and Rating_Response.getRating() != None:
        # keep track of start time/frame for later
        Rating_Done.frameNStart = frameN  # exact frame index
        Rating_Done.tStart = t  # local t and not account for scr refresh
        Rating_Done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Done, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Done.started')
        # update status
        Rating_Done.status = STARTED
        Rating_Done.setAutoDraw(True)
    
    # if Rating_Done is active this frame...
    if Rating_Done.status == STARTED:
        # update params
        pass
        # check whether Rating_Done has been pressed
        if Rating_Done.isClicked:
            if not Rating_Done.wasClicked:
                # if this is a new click, store time of first click and clicked until
                Rating_Done.timesOn.append(Rating_Done.buttonClock.getTime())
                Rating_Done.timesOff.append(Rating_Done.buttonClock.getTime())
            elif len(Rating_Done.timesOff):
                # if click is continuing from last frame, update time of clicked until
                Rating_Done.timesOff[-1] = Rating_Done.buttonClock.getTime()
            if not Rating_Done.wasClicked:
                # end routine when Rating_Done is clicked
                continueRoutine = False
            if not Rating_Done.wasClicked:
                # run callback code when Rating_Done is clicked
                pass
    # take note of whether Rating_Done was clicked, so that next frame we know if clicks are new
    Rating_Done.wasClicked = Rating_Done.isClicked and Rating_Done.status == STARTED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RatComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Rat" ---
for thisComponent in RatComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Rating_Response.response', Rating_Response.getRating())
thisExp.addData('Rating_Response.rt', Rating_Response.getRT())
thisExp.addData('Rating_Done.numClicks', Rating_Done.numClicks)
if Rating_Done.numClicks:
   thisExp.addData('Rating_Done.timesOn', Rating_Done.timesOn)
   thisExp.addData('Rating_Done.timesOff', Rating_Done.timesOff)
else:
   thisExp.addData('Rating_Done.timesOn', "")
   thisExp.addData('Rating_Done.timesOff', "")
# the Routine "Rat" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "RegRat" ---
continueRoutine = True
# update component parameters for each repeat
RegulationRating_Response.reset()
# reset RegulationRating_Done to account for continued clicks & clear times on/off
RegulationRating_Done.reset()
# keep track of which components have finished
RegRatComponents = [RegulationRating_Text, RegulationRating_Response, RegulationRating_Done]
for thisComponent in RegRatComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "RegRat" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *RegulationRating_Text* updates
    
    # if RegulationRating_Text is starting this frame...
    if RegulationRating_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RegulationRating_Text.frameNStart = frameN  # exact frame index
        RegulationRating_Text.tStart = t  # local t and not account for scr refresh
        RegulationRating_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RegulationRating_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RegulationRating_Text.started')
        # update status
        RegulationRating_Text.status = STARTED
        RegulationRating_Text.setAutoDraw(True)
    
    # if RegulationRating_Text is active this frame...
    if RegulationRating_Text.status == STARTED:
        # update params
        pass
    
    # *RegulationRating_Response* updates
    
    # if RegulationRating_Response is starting this frame...
    if RegulationRating_Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RegulationRating_Response.frameNStart = frameN  # exact frame index
        RegulationRating_Response.tStart = t  # local t and not account for scr refresh
        RegulationRating_Response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RegulationRating_Response, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RegulationRating_Response.started')
        # update status
        RegulationRating_Response.status = STARTED
        RegulationRating_Response.setAutoDraw(True)
    
    # if RegulationRating_Response is active this frame...
    if RegulationRating_Response.status == STARTED:
        # update params
        pass
    # *RegulationRating_Done* updates
    
    # if RegulationRating_Done is starting this frame...
    if RegulationRating_Done.status == NOT_STARTED and RegulationRating_Response.getRating() != None:
        # keep track of start time/frame for later
        RegulationRating_Done.frameNStart = frameN  # exact frame index
        RegulationRating_Done.tStart = t  # local t and not account for scr refresh
        RegulationRating_Done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RegulationRating_Done, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RegulationRating_Done.started')
        # update status
        RegulationRating_Done.status = STARTED
        RegulationRating_Done.setAutoDraw(True)
    
    # if RegulationRating_Done is active this frame...
    if RegulationRating_Done.status == STARTED:
        # update params
        pass
        # check whether RegulationRating_Done has been pressed
        if RegulationRating_Done.isClicked:
            if not RegulationRating_Done.wasClicked:
                # if this is a new click, store time of first click and clicked until
                RegulationRating_Done.timesOn.append(RegulationRating_Done.buttonClock.getTime())
                RegulationRating_Done.timesOff.append(RegulationRating_Done.buttonClock.getTime())
            elif len(RegulationRating_Done.timesOff):
                # if click is continuing from last frame, update time of clicked until
                RegulationRating_Done.timesOff[-1] = RegulationRating_Done.buttonClock.getTime()
            if not RegulationRating_Done.wasClicked:
                # end routine when RegulationRating_Done is clicked
                continueRoutine = False
            if not RegulationRating_Done.wasClicked:
                # run callback code when RegulationRating_Done is clicked
                pass
    # take note of whether RegulationRating_Done was clicked, so that next frame we know if clicks are new
    RegulationRating_Done.wasClicked = RegulationRating_Done.isClicked and RegulationRating_Done.status == STARTED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RegRatComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "RegRat" ---
for thisComponent in RegRatComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('RegulationRating_Response.response', RegulationRating_Response.getRating())
thisExp.addData('RegulationRating_Response.rt', RegulationRating_Response.getRT())
thisExp.addData('RegulationRating_Done.numClicks', RegulationRating_Done.numClicks)
if RegulationRating_Done.numClicks:
   thisExp.addData('RegulationRating_Done.timesOn', RegulationRating_Done.timesOn)
   thisExp.addData('RegulationRating_Done.timesOff', RegulationRating_Done.timesOff)
else:
   thisExp.addData('RegulationRating_Done.timesOn', "")
   thisExp.addData('RegulationRating_Done.timesOff', "")
# the Routine "RegRat" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "BC" ---
continueRoutine = True
# update component parameters for each repeat
# reset BContinue_Button to account for continued clicks & clear times on/off
BContinue_Button.reset()
# keep track of which components have finished
BCComponents = [BContinue_Button, BContinue_Text]
for thisComponent in BCComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "BC" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *BContinue_Button* updates
    
    # if BContinue_Button is starting this frame...
    if BContinue_Button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        BContinue_Button.frameNStart = frameN  # exact frame index
        BContinue_Button.tStart = t  # local t and not account for scr refresh
        BContinue_Button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BContinue_Button, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'BContinue_Button.started')
        # update status
        BContinue_Button.status = STARTED
        BContinue_Button.setAutoDraw(True)
    
    # if BContinue_Button is active this frame...
    if BContinue_Button.status == STARTED:
        # update params
        pass
        # check whether BContinue_Button has been pressed
        if BContinue_Button.isClicked:
            if not BContinue_Button.wasClicked:
                # if this is a new click, store time of first click and clicked until
                BContinue_Button.timesOn.append(BContinue_Button.buttonClock.getTime())
                BContinue_Button.timesOff.append(BContinue_Button.buttonClock.getTime())
            elif len(BContinue_Button.timesOff):
                # if click is continuing from last frame, update time of clicked until
                BContinue_Button.timesOff[-1] = BContinue_Button.buttonClock.getTime()
            if not BContinue_Button.wasClicked:
                # end routine when BContinue_Button is clicked
                continueRoutine = False
            if not BContinue_Button.wasClicked:
                # run callback code when BContinue_Button is clicked
                pass
    # take note of whether BContinue_Button was clicked, so that next frame we know if clicks are new
    BContinue_Button.wasClicked = BContinue_Button.isClicked and BContinue_Button.status == STARTED
    
    # *BContinue_Text* updates
    
    # if BContinue_Text is starting this frame...
    if BContinue_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BContinue_Text.frameNStart = frameN  # exact frame index
        BContinue_Text.tStart = t  # local t and not account for scr refresh
        BContinue_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BContinue_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'BContinue_Text.started')
        # update status
        BContinue_Text.status = STARTED
        BContinue_Text.setAutoDraw(True)
    
    # if BContinue_Text is active this frame...
    if BContinue_Text.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BCComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "BC" ---
for thisComponent in BCComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('BContinue_Button.numClicks', BContinue_Button.numClicks)
if BContinue_Button.numClicks:
   thisExp.addData('BContinue_Button.timesOn', BContinue_Button.timesOn)
   thisExp.addData('BContinue_Button.timesOff', BContinue_Button.timesOff)
else:
   thisExp.addData('BContinue_Button.timesOn', "")
   thisExp.addData('BContinue_Button.timesOff', "")
# the Routine "BC" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Cond" ---
continueRoutine = True
# update component parameters for each repeat
ConditionTextBox.reset()
# reset ConditionDone to account for continued clicks & clear times on/off
ConditionDone.reset()
# keep track of which components have finished
CondComponents = [ConditionTextBox, ConditionDone]
for thisComponent in CondComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Cond" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ConditionTextBox* updates
    
    # if ConditionTextBox is starting this frame...
    if ConditionTextBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ConditionTextBox.frameNStart = frameN  # exact frame index
        ConditionTextBox.tStart = t  # local t and not account for scr refresh
        ConditionTextBox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ConditionTextBox, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ConditionTextBox.started')
        # update status
        ConditionTextBox.status = STARTED
        ConditionTextBox.setAutoDraw(True)
    
    # if ConditionTextBox is active this frame...
    if ConditionTextBox.status == STARTED:
        # update params
        pass
    # *ConditionDone* updates
    
    # if ConditionDone is starting this frame...
    if ConditionDone.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        ConditionDone.frameNStart = frameN  # exact frame index
        ConditionDone.tStart = t  # local t and not account for scr refresh
        ConditionDone.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ConditionDone, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ConditionDone.started')
        # update status
        ConditionDone.status = STARTED
        ConditionDone.setAutoDraw(True)
    
    # if ConditionDone is active this frame...
    if ConditionDone.status == STARTED:
        # update params
        pass
        # check whether ConditionDone has been pressed
        if ConditionDone.isClicked:
            if not ConditionDone.wasClicked:
                # if this is a new click, store time of first click and clicked until
                ConditionDone.timesOn.append(ConditionDone.buttonClock.getTime())
                ConditionDone.timesOff.append(ConditionDone.buttonClock.getTime())
            elif len(ConditionDone.timesOff):
                # if click is continuing from last frame, update time of clicked until
                ConditionDone.timesOff[-1] = ConditionDone.buttonClock.getTime()
            if not ConditionDone.wasClicked:
                # end routine when ConditionDone is clicked
                continueRoutine = False
            if not ConditionDone.wasClicked:
                # run callback code when ConditionDone is clicked
                pass
    # take note of whether ConditionDone was clicked, so that next frame we know if clicks are new
    ConditionDone.wasClicked = ConditionDone.isClicked and ConditionDone.status == STARTED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CondComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Cond" ---
for thisComponent in CondComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ConditionTextBox.text',ConditionTextBox.text)
thisExp.addData('ConditionDone.numClicks', ConditionDone.numClicks)
if ConditionDone.numClicks:
   thisExp.addData('ConditionDone.timesOn', ConditionDone.timesOn)
   thisExp.addData('ConditionDone.timesOff', ConditionDone.timesOff)
else:
   thisExp.addData('ConditionDone.timesOn', "")
   thisExp.addData('ConditionDone.timesOff', "")
# the Routine "Cond" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "GR" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
GRComponents = [GetReady_Text, GetRead_Cross]
for thisComponent in GRComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "GR" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *GetReady_Text* updates
    
    # if GetReady_Text is starting this frame...
    if GetReady_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GetReady_Text.frameNStart = frameN  # exact frame index
        GetReady_Text.tStart = t  # local t and not account for scr refresh
        GetReady_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GetReady_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'GetReady_Text.started')
        # update status
        GetReady_Text.status = STARTED
        GetReady_Text.setAutoDraw(True)
    
    # if GetReady_Text is active this frame...
    if GetReady_Text.status == STARTED:
        # update params
        GetReady_Text.setText('', log=False)
    
    # if GetReady_Text is stopping this frame...
    if GetReady_Text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > GetReady_Text.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            GetReady_Text.tStop = t  # not accounting for scr refresh
            GetReady_Text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'GetReady_Text.stopped')
            # update status
            GetReady_Text.status = FINISHED
            GetReady_Text.setAutoDraw(False)
    
    # *GetRead_Cross* updates
    
    # if GetRead_Cross is starting this frame...
    if GetRead_Cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GetRead_Cross.frameNStart = frameN  # exact frame index
        GetRead_Cross.tStart = t  # local t and not account for scr refresh
        GetRead_Cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GetRead_Cross, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'GetRead_Cross.started')
        # update status
        GetRead_Cross.status = STARTED
        GetRead_Cross.setAutoDraw(True)
    
    # if GetRead_Cross is active this frame...
    if GetRead_Cross.status == STARTED:
        # update params
        pass
    
    # if GetRead_Cross is stopping this frame...
    if GetRead_Cross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > GetRead_Cross.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            GetRead_Cross.tStop = t  # not accounting for scr refresh
            GetRead_Cross.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'GetRead_Cross.stopped')
            # update status
            GetRead_Cross.status = FINISHED
            GetRead_Cross.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GRComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "GR" ---
for thisComponent in GRComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# set up handler to look after randomisation of conditions etc
Neg5 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PsychopyIntegrationSheets/Negative5.xlsx'),
    seed=None, name='Neg5')
thisExp.addLoop(Neg5)  # add the loop to the experiment
thisNeg5 = Neg5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNeg5.rgb)
if thisNeg5 != None:
    for paramName in thisNeg5:
        exec('{} = thisNeg5[paramName]'.format(paramName))

for thisNeg5 in Neg5:
    currentLoop = Neg5
    # abbreviate parameter names if possible (e.g. rgb = thisNeg5.rgb)
    if thisNeg5 != None:
        for paramName in thisNeg5:
            exec('{} = thisNeg5[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "SS" ---
    continueRoutine = True
    # update component parameters for each repeat
    StorySentence_Text.setText(StorySentences)
    # keep track of which components have finished
    SSComponents = [StorySentence_Text]
    for thisComponent in SSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "SS" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *StorySentence_Text* updates
        
        # if StorySentence_Text is starting this frame...
        if StorySentence_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StorySentence_Text.frameNStart = frameN  # exact frame index
            StorySentence_Text.tStart = t  # local t and not account for scr refresh
            StorySentence_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StorySentence_Text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'StorySentence_Text.started')
            # update status
            StorySentence_Text.status = STARTED
            StorySentence_Text.setAutoDraw(True)
        
        # if StorySentence_Text is active this frame...
        if StorySentence_Text.status == STARTED:
            # update params
            pass
        
        # if StorySentence_Text is stopping this frame...
        if StorySentence_Text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StorySentence_Text.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                StorySentence_Text.tStop = t  # not accounting for scr refresh
                StorySentence_Text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'StorySentence_Text.stopped')
                # update status
                StorySentence_Text.status = FINISHED
                StorySentence_Text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "SS" ---
    for thisComponent in SSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Neg5'


# --- Prepare to start Routine "Rat" ---
continueRoutine = True
# update component parameters for each repeat
Rating_Response.reset()
# reset Rating_Done to account for continued clicks & clear times on/off
Rating_Done.reset()
# keep track of which components have finished
RatComponents = [Rating_Text, Rating_Response, Rating_Done]
for thisComponent in RatComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Rat" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Rating_Text* updates
    
    # if Rating_Text is starting this frame...
    if Rating_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rating_Text.frameNStart = frameN  # exact frame index
        Rating_Text.tStart = t  # local t and not account for scr refresh
        Rating_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Text.started')
        # update status
        Rating_Text.status = STARTED
        Rating_Text.setAutoDraw(True)
    
    # if Rating_Text is active this frame...
    if Rating_Text.status == STARTED:
        # update params
        pass
    
    # *Rating_Response* updates
    
    # if Rating_Response is starting this frame...
    if Rating_Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rating_Response.frameNStart = frameN  # exact frame index
        Rating_Response.tStart = t  # local t and not account for scr refresh
        Rating_Response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Response, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Response.started')
        # update status
        Rating_Response.status = STARTED
        Rating_Response.setAutoDraw(True)
    
    # if Rating_Response is active this frame...
    if Rating_Response.status == STARTED:
        # update params
        pass
    # *Rating_Done* updates
    
    # if Rating_Done is starting this frame...
    if Rating_Done.status == NOT_STARTED and Rating_Response.getRating() != None:
        # keep track of start time/frame for later
        Rating_Done.frameNStart = frameN  # exact frame index
        Rating_Done.tStart = t  # local t and not account for scr refresh
        Rating_Done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Done, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Done.started')
        # update status
        Rating_Done.status = STARTED
        Rating_Done.setAutoDraw(True)
    
    # if Rating_Done is active this frame...
    if Rating_Done.status == STARTED:
        # update params
        pass
        # check whether Rating_Done has been pressed
        if Rating_Done.isClicked:
            if not Rating_Done.wasClicked:
                # if this is a new click, store time of first click and clicked until
                Rating_Done.timesOn.append(Rating_Done.buttonClock.getTime())
                Rating_Done.timesOff.append(Rating_Done.buttonClock.getTime())
            elif len(Rating_Done.timesOff):
                # if click is continuing from last frame, update time of clicked until
                Rating_Done.timesOff[-1] = Rating_Done.buttonClock.getTime()
            if not Rating_Done.wasClicked:
                # end routine when Rating_Done is clicked
                continueRoutine = False
            if not Rating_Done.wasClicked:
                # run callback code when Rating_Done is clicked
                pass
    # take note of whether Rating_Done was clicked, so that next frame we know if clicks are new
    Rating_Done.wasClicked = Rating_Done.isClicked and Rating_Done.status == STARTED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RatComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Rat" ---
for thisComponent in RatComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Rating_Response.response', Rating_Response.getRating())
thisExp.addData('Rating_Response.rt', Rating_Response.getRT())
thisExp.addData('Rating_Done.numClicks', Rating_Done.numClicks)
if Rating_Done.numClicks:
   thisExp.addData('Rating_Done.timesOn', Rating_Done.timesOn)
   thisExp.addData('Rating_Done.timesOff', Rating_Done.timesOff)
else:
   thisExp.addData('Rating_Done.timesOn', "")
   thisExp.addData('Rating_Done.timesOff', "")
# the Routine "Rat" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
NSB5 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PsychopyIntegrationSheets/NSB5.xlsx'),
    seed=None, name='NSB5')
thisExp.addLoop(NSB5)  # add the loop to the experiment
thisNSB5 = NSB5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNSB5.rgb)
if thisNSB5 != None:
    for paramName in thisNSB5:
        exec('{} = thisNSB5[paramName]'.format(paramName))

for thisNSB5 in NSB5:
    currentLoop = NSB5
    # abbreviate parameter names if possible (e.g. rgb = thisNSB5.rgb)
    if thisNSB5 != None:
        for paramName in thisNSB5:
            exec('{} = thisNSB5[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    Trial_RatingResponse.reset()
    # reset Trial_ResponseDone to account for continued clicks & clear times on/off
    Trial_ResponseDone.reset()
    # keep track of which components have finished
    TrialComponents = [Trial_NSB, Trial_Cue, Trial_RatingText, Trial_RatingResponse, Trial_ResponseDone]
    for thisComponent in TrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Trial" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Trial_NSB* updates
        
        # if Trial_NSB is starting this frame...
        if Trial_NSB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Trial_NSB.frameNStart = frameN  # exact frame index
            Trial_NSB.tStart = t  # local t and not account for scr refresh
            Trial_NSB.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_NSB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_NSB.started')
            # update status
            Trial_NSB.status = STARTED
            Trial_NSB.setAutoDraw(True)
        
        # if Trial_NSB is active this frame...
        if Trial_NSB.status == STARTED:
            # update params
            pass
        
        # if Trial_NSB is stopping this frame...
        if Trial_NSB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Trial_NSB.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                Trial_NSB.tStop = t  # not accounting for scr refresh
                Trial_NSB.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Trial_NSB.stopped')
                # update status
                Trial_NSB.status = FINISHED
                Trial_NSB.setAutoDraw(False)
        
        # *Trial_Cue* updates
        
        # if Trial_Cue is starting this frame...
        if Trial_Cue.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            Trial_Cue.frameNStart = frameN  # exact frame index
            Trial_Cue.tStart = t  # local t and not account for scr refresh
            Trial_Cue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_Cue, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_Cue.started')
            # update status
            Trial_Cue.status = STARTED
            Trial_Cue.setAutoDraw(True)
        
        # if Trial_Cue is active this frame...
        if Trial_Cue.status == STARTED:
            # update params
            pass
        
        # if Trial_Cue is stopping this frame...
        if Trial_Cue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Trial_Cue.tStartRefresh + 12-frameTolerance:
                # keep track of stop time/frame for later
                Trial_Cue.tStop = t  # not accounting for scr refresh
                Trial_Cue.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Trial_Cue.stopped')
                # update status
                Trial_Cue.status = FINISHED
                Trial_Cue.setAutoDraw(False)
        
        # *Trial_RatingText* updates
        
        # if Trial_RatingText is starting this frame...
        if Trial_RatingText.status == NOT_STARTED and tThisFlip >= 15-frameTolerance:
            # keep track of start time/frame for later
            Trial_RatingText.frameNStart = frameN  # exact frame index
            Trial_RatingText.tStart = t  # local t and not account for scr refresh
            Trial_RatingText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_RatingText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_RatingText.started')
            # update status
            Trial_RatingText.status = STARTED
            Trial_RatingText.setAutoDraw(True)
        
        # if Trial_RatingText is active this frame...
        if Trial_RatingText.status == STARTED:
            # update params
            pass
        
        # *Trial_RatingResponse* updates
        
        # if Trial_RatingResponse is starting this frame...
        if Trial_RatingResponse.status == NOT_STARTED and tThisFlip >= 15-frameTolerance:
            # keep track of start time/frame for later
            Trial_RatingResponse.frameNStart = frameN  # exact frame index
            Trial_RatingResponse.tStart = t  # local t and not account for scr refresh
            Trial_RatingResponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_RatingResponse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_RatingResponse.started')
            # update status
            Trial_RatingResponse.status = STARTED
            Trial_RatingResponse.setAutoDraw(True)
        
        # if Trial_RatingResponse is active this frame...
        if Trial_RatingResponse.status == STARTED:
            # update params
            pass
        # *Trial_ResponseDone* updates
        
        # if Trial_ResponseDone is starting this frame...
        if Trial_ResponseDone.status == NOT_STARTED and Trial_RatingResponse.getRating() != None:
            # keep track of start time/frame for later
            Trial_ResponseDone.frameNStart = frameN  # exact frame index
            Trial_ResponseDone.tStart = t  # local t and not account for scr refresh
            Trial_ResponseDone.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_ResponseDone, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_ResponseDone.started')
            # update status
            Trial_ResponseDone.status = STARTED
            Trial_ResponseDone.setAutoDraw(True)
        
        # if Trial_ResponseDone is active this frame...
        if Trial_ResponseDone.status == STARTED:
            # update params
            pass
            # check whether Trial_ResponseDone has been pressed
            if Trial_ResponseDone.isClicked:
                if not Trial_ResponseDone.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    Trial_ResponseDone.timesOn.append(Trial_ResponseDone.buttonClock.getTime())
                    Trial_ResponseDone.timesOff.append(Trial_ResponseDone.buttonClock.getTime())
                elif len(Trial_ResponseDone.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    Trial_ResponseDone.timesOff[-1] = Trial_ResponseDone.buttonClock.getTime()
                if not Trial_ResponseDone.wasClicked:
                    # end routine when Trial_ResponseDone is clicked
                    continueRoutine = False
                if not Trial_ResponseDone.wasClicked:
                    # run callback code when Trial_ResponseDone is clicked
                    pass
        # take note of whether Trial_ResponseDone was clicked, so that next frame we know if clicks are new
        Trial_ResponseDone.wasClicked = Trial_ResponseDone.isClicked and Trial_ResponseDone.status == STARTED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Trial" ---
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    NSB5.addData('Trial_RatingResponse.response', Trial_RatingResponse.getRating())
    NSB5.addData('Trial_RatingResponse.rt', Trial_RatingResponse.getRT())
    NSB5.addData('Trial_ResponseDone.numClicks', Trial_ResponseDone.numClicks)
    if Trial_ResponseDone.numClicks:
       NSB5.addData('Trial_ResponseDone.timesOn', Trial_ResponseDone.timesOn)
       NSB5.addData('Trial_ResponseDone.timesOff', Trial_ResponseDone.timesOff)
    else:
       NSB5.addData('Trial_ResponseDone.timesOn', "")
       NSB5.addData('Trial_ResponseDone.timesOff', "")
    # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'NSB5'


# --- Prepare to start Routine "GR" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
GRComponents = [GetReady_Text, GetRead_Cross]
for thisComponent in GRComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "GR" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *GetReady_Text* updates
    
    # if GetReady_Text is starting this frame...
    if GetReady_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GetReady_Text.frameNStart = frameN  # exact frame index
        GetReady_Text.tStart = t  # local t and not account for scr refresh
        GetReady_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GetReady_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'GetReady_Text.started')
        # update status
        GetReady_Text.status = STARTED
        GetReady_Text.setAutoDraw(True)
    
    # if GetReady_Text is active this frame...
    if GetReady_Text.status == STARTED:
        # update params
        GetReady_Text.setText('', log=False)
    
    # if GetReady_Text is stopping this frame...
    if GetReady_Text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > GetReady_Text.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            GetReady_Text.tStop = t  # not accounting for scr refresh
            GetReady_Text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'GetReady_Text.stopped')
            # update status
            GetReady_Text.status = FINISHED
            GetReady_Text.setAutoDraw(False)
    
    # *GetRead_Cross* updates
    
    # if GetRead_Cross is starting this frame...
    if GetRead_Cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GetRead_Cross.frameNStart = frameN  # exact frame index
        GetRead_Cross.tStart = t  # local t and not account for scr refresh
        GetRead_Cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GetRead_Cross, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'GetRead_Cross.started')
        # update status
        GetRead_Cross.status = STARTED
        GetRead_Cross.setAutoDraw(True)
    
    # if GetRead_Cross is active this frame...
    if GetRead_Cross.status == STARTED:
        # update params
        pass
    
    # if GetRead_Cross is stopping this frame...
    if GetRead_Cross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > GetRead_Cross.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            GetRead_Cross.tStop = t  # not accounting for scr refresh
            GetRead_Cross.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'GetRead_Cross.stopped')
            # update status
            GetRead_Cross.status = FINISHED
            GetRead_Cross.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GRComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "GR" ---
for thisComponent in GRComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# set up handler to look after randomisation of conditions etc
Neu5 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PsychopyIntegrationSheets/Neutral5.xlsx'),
    seed=None, name='Neu5')
thisExp.addLoop(Neu5)  # add the loop to the experiment
thisNeu5 = Neu5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNeu5.rgb)
if thisNeu5 != None:
    for paramName in thisNeu5:
        exec('{} = thisNeu5[paramName]'.format(paramName))

for thisNeu5 in Neu5:
    currentLoop = Neu5
    # abbreviate parameter names if possible (e.g. rgb = thisNeu5.rgb)
    if thisNeu5 != None:
        for paramName in thisNeu5:
            exec('{} = thisNeu5[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "SS" ---
    continueRoutine = True
    # update component parameters for each repeat
    StorySentence_Text.setText(StorySentences)
    # keep track of which components have finished
    SSComponents = [StorySentence_Text]
    for thisComponent in SSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "SS" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *StorySentence_Text* updates
        
        # if StorySentence_Text is starting this frame...
        if StorySentence_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StorySentence_Text.frameNStart = frameN  # exact frame index
            StorySentence_Text.tStart = t  # local t and not account for scr refresh
            StorySentence_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StorySentence_Text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'StorySentence_Text.started')
            # update status
            StorySentence_Text.status = STARTED
            StorySentence_Text.setAutoDraw(True)
        
        # if StorySentence_Text is active this frame...
        if StorySentence_Text.status == STARTED:
            # update params
            pass
        
        # if StorySentence_Text is stopping this frame...
        if StorySentence_Text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StorySentence_Text.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                StorySentence_Text.tStop = t  # not accounting for scr refresh
                StorySentence_Text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'StorySentence_Text.stopped')
                # update status
                StorySentence_Text.status = FINISHED
                StorySentence_Text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "SS" ---
    for thisComponent in SSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Neu5'


# set up handler to look after randomisation of conditions etc
NeuSta5 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PsychopyIntegrationSheets/NeutralStatements5.xlsx'),
    seed=None, name='NeuSta5')
thisExp.addLoop(NeuSta5)  # add the loop to the experiment
thisNeuSta5 = NeuSta5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNeuSta5.rgb)
if thisNeuSta5 != None:
    for paramName in thisNeuSta5:
        exec('{} = thisNeuSta5[paramName]'.format(paramName))

for thisNeuSta5 in NeuSta5:
    currentLoop = NeuSta5
    # abbreviate parameter names if possible (e.g. rgb = thisNeuSta5.rgb)
    if thisNeuSta5 != None:
        for paramName in thisNeuSta5:
            exec('{} = thisNeuSta5[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "NS" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    NSComponents = [NeutralStatement_Text]
    for thisComponent in NSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "NS" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 12.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NeutralStatement_Text* updates
        
        # if NeutralStatement_Text is starting this frame...
        if NeutralStatement_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NeutralStatement_Text.frameNStart = frameN  # exact frame index
            NeutralStatement_Text.tStart = t  # local t and not account for scr refresh
            NeutralStatement_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NeutralStatement_Text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NeutralStatement_Text.started')
            # update status
            NeutralStatement_Text.status = STARTED
            NeutralStatement_Text.setAutoDraw(True)
        
        # if NeutralStatement_Text is active this frame...
        if NeutralStatement_Text.status == STARTED:
            # update params
            pass
        
        # if NeutralStatement_Text is stopping this frame...
        if NeutralStatement_Text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > NeutralStatement_Text.tStartRefresh + 12-frameTolerance:
                # keep track of stop time/frame for later
                NeutralStatement_Text.tStop = t  # not accounting for scr refresh
                NeutralStatement_Text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'NeutralStatement_Text.stopped')
                # update status
                NeutralStatement_Text.status = FINISHED
                NeutralStatement_Text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "NS" ---
    for thisComponent in NSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-12.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'NeuSta5'


# --- Prepare to start Routine "Rat" ---
continueRoutine = True
# update component parameters for each repeat
Rating_Response.reset()
# reset Rating_Done to account for continued clicks & clear times on/off
Rating_Done.reset()
# keep track of which components have finished
RatComponents = [Rating_Text, Rating_Response, Rating_Done]
for thisComponent in RatComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Rat" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Rating_Text* updates
    
    # if Rating_Text is starting this frame...
    if Rating_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rating_Text.frameNStart = frameN  # exact frame index
        Rating_Text.tStart = t  # local t and not account for scr refresh
        Rating_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Text.started')
        # update status
        Rating_Text.status = STARTED
        Rating_Text.setAutoDraw(True)
    
    # if Rating_Text is active this frame...
    if Rating_Text.status == STARTED:
        # update params
        pass
    
    # *Rating_Response* updates
    
    # if Rating_Response is starting this frame...
    if Rating_Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rating_Response.frameNStart = frameN  # exact frame index
        Rating_Response.tStart = t  # local t and not account for scr refresh
        Rating_Response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Response, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Response.started')
        # update status
        Rating_Response.status = STARTED
        Rating_Response.setAutoDraw(True)
    
    # if Rating_Response is active this frame...
    if Rating_Response.status == STARTED:
        # update params
        pass
    # *Rating_Done* updates
    
    # if Rating_Done is starting this frame...
    if Rating_Done.status == NOT_STARTED and Rating_Response.getRating() != None:
        # keep track of start time/frame for later
        Rating_Done.frameNStart = frameN  # exact frame index
        Rating_Done.tStart = t  # local t and not account for scr refresh
        Rating_Done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Done, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Done.started')
        # update status
        Rating_Done.status = STARTED
        Rating_Done.setAutoDraw(True)
    
    # if Rating_Done is active this frame...
    if Rating_Done.status == STARTED:
        # update params
        pass
        # check whether Rating_Done has been pressed
        if Rating_Done.isClicked:
            if not Rating_Done.wasClicked:
                # if this is a new click, store time of first click and clicked until
                Rating_Done.timesOn.append(Rating_Done.buttonClock.getTime())
                Rating_Done.timesOff.append(Rating_Done.buttonClock.getTime())
            elif len(Rating_Done.timesOff):
                # if click is continuing from last frame, update time of clicked until
                Rating_Done.timesOff[-1] = Rating_Done.buttonClock.getTime()
            if not Rating_Done.wasClicked:
                # end routine when Rating_Done is clicked
                continueRoutine = False
            if not Rating_Done.wasClicked:
                # run callback code when Rating_Done is clicked
                pass
    # take note of whether Rating_Done was clicked, so that next frame we know if clicks are new
    Rating_Done.wasClicked = Rating_Done.isClicked and Rating_Done.status == STARTED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RatComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Rat" ---
for thisComponent in RatComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Rating_Response.response', Rating_Response.getRating())
thisExp.addData('Rating_Response.rt', Rating_Response.getRT())
thisExp.addData('Rating_Done.numClicks', Rating_Done.numClicks)
if Rating_Done.numClicks:
   thisExp.addData('Rating_Done.timesOn', Rating_Done.timesOn)
   thisExp.addData('Rating_Done.timesOff', Rating_Done.timesOff)
else:
   thisExp.addData('Rating_Done.timesOn', "")
   thisExp.addData('Rating_Done.timesOff', "")
# the Routine "Rat" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "RegRat" ---
continueRoutine = True
# update component parameters for each repeat
RegulationRating_Response.reset()
# reset RegulationRating_Done to account for continued clicks & clear times on/off
RegulationRating_Done.reset()
# keep track of which components have finished
RegRatComponents = [RegulationRating_Text, RegulationRating_Response, RegulationRating_Done]
for thisComponent in RegRatComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "RegRat" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *RegulationRating_Text* updates
    
    # if RegulationRating_Text is starting this frame...
    if RegulationRating_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RegulationRating_Text.frameNStart = frameN  # exact frame index
        RegulationRating_Text.tStart = t  # local t and not account for scr refresh
        RegulationRating_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RegulationRating_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RegulationRating_Text.started')
        # update status
        RegulationRating_Text.status = STARTED
        RegulationRating_Text.setAutoDraw(True)
    
    # if RegulationRating_Text is active this frame...
    if RegulationRating_Text.status == STARTED:
        # update params
        pass
    
    # *RegulationRating_Response* updates
    
    # if RegulationRating_Response is starting this frame...
    if RegulationRating_Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RegulationRating_Response.frameNStart = frameN  # exact frame index
        RegulationRating_Response.tStart = t  # local t and not account for scr refresh
        RegulationRating_Response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RegulationRating_Response, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RegulationRating_Response.started')
        # update status
        RegulationRating_Response.status = STARTED
        RegulationRating_Response.setAutoDraw(True)
    
    # if RegulationRating_Response is active this frame...
    if RegulationRating_Response.status == STARTED:
        # update params
        pass
    # *RegulationRating_Done* updates
    
    # if RegulationRating_Done is starting this frame...
    if RegulationRating_Done.status == NOT_STARTED and RegulationRating_Response.getRating() != None:
        # keep track of start time/frame for later
        RegulationRating_Done.frameNStart = frameN  # exact frame index
        RegulationRating_Done.tStart = t  # local t and not account for scr refresh
        RegulationRating_Done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RegulationRating_Done, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RegulationRating_Done.started')
        # update status
        RegulationRating_Done.status = STARTED
        RegulationRating_Done.setAutoDraw(True)
    
    # if RegulationRating_Done is active this frame...
    if RegulationRating_Done.status == STARTED:
        # update params
        pass
        # check whether RegulationRating_Done has been pressed
        if RegulationRating_Done.isClicked:
            if not RegulationRating_Done.wasClicked:
                # if this is a new click, store time of first click and clicked until
                RegulationRating_Done.timesOn.append(RegulationRating_Done.buttonClock.getTime())
                RegulationRating_Done.timesOff.append(RegulationRating_Done.buttonClock.getTime())
            elif len(RegulationRating_Done.timesOff):
                # if click is continuing from last frame, update time of clicked until
                RegulationRating_Done.timesOff[-1] = RegulationRating_Done.buttonClock.getTime()
            if not RegulationRating_Done.wasClicked:
                # end routine when RegulationRating_Done is clicked
                continueRoutine = False
            if not RegulationRating_Done.wasClicked:
                # run callback code when RegulationRating_Done is clicked
                pass
    # take note of whether RegulationRating_Done was clicked, so that next frame we know if clicks are new
    RegulationRating_Done.wasClicked = RegulationRating_Done.isClicked and RegulationRating_Done.status == STARTED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RegRatComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "RegRat" ---
for thisComponent in RegRatComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('RegulationRating_Response.response', RegulationRating_Response.getRating())
thisExp.addData('RegulationRating_Response.rt', RegulationRating_Response.getRT())
thisExp.addData('RegulationRating_Done.numClicks', RegulationRating_Done.numClicks)
if RegulationRating_Done.numClicks:
   thisExp.addData('RegulationRating_Done.timesOn', RegulationRating_Done.timesOn)
   thisExp.addData('RegulationRating_Done.timesOff', RegulationRating_Done.timesOff)
else:
   thisExp.addData('RegulationRating_Done.timesOn', "")
   thisExp.addData('RegulationRating_Done.timesOff', "")
# the Routine "RegRat" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "BC" ---
continueRoutine = True
# update component parameters for each repeat
# reset BContinue_Button to account for continued clicks & clear times on/off
BContinue_Button.reset()
# keep track of which components have finished
BCComponents = [BContinue_Button, BContinue_Text]
for thisComponent in BCComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "BC" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *BContinue_Button* updates
    
    # if BContinue_Button is starting this frame...
    if BContinue_Button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        BContinue_Button.frameNStart = frameN  # exact frame index
        BContinue_Button.tStart = t  # local t and not account for scr refresh
        BContinue_Button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BContinue_Button, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'BContinue_Button.started')
        # update status
        BContinue_Button.status = STARTED
        BContinue_Button.setAutoDraw(True)
    
    # if BContinue_Button is active this frame...
    if BContinue_Button.status == STARTED:
        # update params
        pass
        # check whether BContinue_Button has been pressed
        if BContinue_Button.isClicked:
            if not BContinue_Button.wasClicked:
                # if this is a new click, store time of first click and clicked until
                BContinue_Button.timesOn.append(BContinue_Button.buttonClock.getTime())
                BContinue_Button.timesOff.append(BContinue_Button.buttonClock.getTime())
            elif len(BContinue_Button.timesOff):
                # if click is continuing from last frame, update time of clicked until
                BContinue_Button.timesOff[-1] = BContinue_Button.buttonClock.getTime()
            if not BContinue_Button.wasClicked:
                # end routine when BContinue_Button is clicked
                continueRoutine = False
            if not BContinue_Button.wasClicked:
                # run callback code when BContinue_Button is clicked
                pass
    # take note of whether BContinue_Button was clicked, so that next frame we know if clicks are new
    BContinue_Button.wasClicked = BContinue_Button.isClicked and BContinue_Button.status == STARTED
    
    # *BContinue_Text* updates
    
    # if BContinue_Text is starting this frame...
    if BContinue_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BContinue_Text.frameNStart = frameN  # exact frame index
        BContinue_Text.tStart = t  # local t and not account for scr refresh
        BContinue_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BContinue_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'BContinue_Text.started')
        # update status
        BContinue_Text.status = STARTED
        BContinue_Text.setAutoDraw(True)
    
    # if BContinue_Text is active this frame...
    if BContinue_Text.status == STARTED:
        # update params
        pass
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BCComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "BC" ---
for thisComponent in BCComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('BContinue_Button.numClicks', BContinue_Button.numClicks)
if BContinue_Button.numClicks:
   thisExp.addData('BContinue_Button.timesOn', BContinue_Button.timesOn)
   thisExp.addData('BContinue_Button.timesOff', BContinue_Button.timesOff)
else:
   thisExp.addData('BContinue_Button.timesOn', "")
   thisExp.addData('BContinue_Button.timesOff', "")
# the Routine "BC" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Cond" ---
continueRoutine = True
# update component parameters for each repeat
ConditionTextBox.reset()
# reset ConditionDone to account for continued clicks & clear times on/off
ConditionDone.reset()
# keep track of which components have finished
CondComponents = [ConditionTextBox, ConditionDone]
for thisComponent in CondComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Cond" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ConditionTextBox* updates
    
    # if ConditionTextBox is starting this frame...
    if ConditionTextBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ConditionTextBox.frameNStart = frameN  # exact frame index
        ConditionTextBox.tStart = t  # local t and not account for scr refresh
        ConditionTextBox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ConditionTextBox, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ConditionTextBox.started')
        # update status
        ConditionTextBox.status = STARTED
        ConditionTextBox.setAutoDraw(True)
    
    # if ConditionTextBox is active this frame...
    if ConditionTextBox.status == STARTED:
        # update params
        pass
    # *ConditionDone* updates
    
    # if ConditionDone is starting this frame...
    if ConditionDone.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        ConditionDone.frameNStart = frameN  # exact frame index
        ConditionDone.tStart = t  # local t and not account for scr refresh
        ConditionDone.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ConditionDone, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'ConditionDone.started')
        # update status
        ConditionDone.status = STARTED
        ConditionDone.setAutoDraw(True)
    
    # if ConditionDone is active this frame...
    if ConditionDone.status == STARTED:
        # update params
        pass
        # check whether ConditionDone has been pressed
        if ConditionDone.isClicked:
            if not ConditionDone.wasClicked:
                # if this is a new click, store time of first click and clicked until
                ConditionDone.timesOn.append(ConditionDone.buttonClock.getTime())
                ConditionDone.timesOff.append(ConditionDone.buttonClock.getTime())
            elif len(ConditionDone.timesOff):
                # if click is continuing from last frame, update time of clicked until
                ConditionDone.timesOff[-1] = ConditionDone.buttonClock.getTime()
            if not ConditionDone.wasClicked:
                # end routine when ConditionDone is clicked
                continueRoutine = False
            if not ConditionDone.wasClicked:
                # run callback code when ConditionDone is clicked
                pass
    # take note of whether ConditionDone was clicked, so that next frame we know if clicks are new
    ConditionDone.wasClicked = ConditionDone.isClicked and ConditionDone.status == STARTED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CondComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Cond" ---
for thisComponent in CondComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ConditionTextBox.text',ConditionTextBox.text)
thisExp.addData('ConditionDone.numClicks', ConditionDone.numClicks)
if ConditionDone.numClicks:
   thisExp.addData('ConditionDone.timesOn', ConditionDone.timesOn)
   thisExp.addData('ConditionDone.timesOff', ConditionDone.timesOff)
else:
   thisExp.addData('ConditionDone.timesOn', "")
   thisExp.addData('ConditionDone.timesOff', "")
# the Routine "Cond" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "GR" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
GRComponents = [GetReady_Text, GetRead_Cross]
for thisComponent in GRComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "GR" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *GetReady_Text* updates
    
    # if GetReady_Text is starting this frame...
    if GetReady_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GetReady_Text.frameNStart = frameN  # exact frame index
        GetReady_Text.tStart = t  # local t and not account for scr refresh
        GetReady_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GetReady_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'GetReady_Text.started')
        # update status
        GetReady_Text.status = STARTED
        GetReady_Text.setAutoDraw(True)
    
    # if GetReady_Text is active this frame...
    if GetReady_Text.status == STARTED:
        # update params
        GetReady_Text.setText('', log=False)
    
    # if GetReady_Text is stopping this frame...
    if GetReady_Text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > GetReady_Text.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            GetReady_Text.tStop = t  # not accounting for scr refresh
            GetReady_Text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'GetReady_Text.stopped')
            # update status
            GetReady_Text.status = FINISHED
            GetReady_Text.setAutoDraw(False)
    
    # *GetRead_Cross* updates
    
    # if GetRead_Cross is starting this frame...
    if GetRead_Cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GetRead_Cross.frameNStart = frameN  # exact frame index
        GetRead_Cross.tStart = t  # local t and not account for scr refresh
        GetRead_Cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GetRead_Cross, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'GetRead_Cross.started')
        # update status
        GetRead_Cross.status = STARTED
        GetRead_Cross.setAutoDraw(True)
    
    # if GetRead_Cross is active this frame...
    if GetRead_Cross.status == STARTED:
        # update params
        pass
    
    # if GetRead_Cross is stopping this frame...
    if GetRead_Cross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > GetRead_Cross.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            GetRead_Cross.tStop = t  # not accounting for scr refresh
            GetRead_Cross.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'GetRead_Cross.stopped')
            # update status
            GetRead_Cross.status = FINISHED
            GetRead_Cross.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GRComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "GR" ---
for thisComponent in GRComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# set up handler to look after randomisation of conditions etc
Neg6 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PsychopyIntegrationSheets/Negative6.xlsx'),
    seed=None, name='Neg6')
thisExp.addLoop(Neg6)  # add the loop to the experiment
thisNeg6 = Neg6.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNeg6.rgb)
if thisNeg6 != None:
    for paramName in thisNeg6:
        exec('{} = thisNeg6[paramName]'.format(paramName))

for thisNeg6 in Neg6:
    currentLoop = Neg6
    # abbreviate parameter names if possible (e.g. rgb = thisNeg6.rgb)
    if thisNeg6 != None:
        for paramName in thisNeg6:
            exec('{} = thisNeg6[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "SS" ---
    continueRoutine = True
    # update component parameters for each repeat
    StorySentence_Text.setText(StorySentences)
    # keep track of which components have finished
    SSComponents = [StorySentence_Text]
    for thisComponent in SSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "SS" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *StorySentence_Text* updates
        
        # if StorySentence_Text is starting this frame...
        if StorySentence_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StorySentence_Text.frameNStart = frameN  # exact frame index
            StorySentence_Text.tStart = t  # local t and not account for scr refresh
            StorySentence_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StorySentence_Text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'StorySentence_Text.started')
            # update status
            StorySentence_Text.status = STARTED
            StorySentence_Text.setAutoDraw(True)
        
        # if StorySentence_Text is active this frame...
        if StorySentence_Text.status == STARTED:
            # update params
            pass
        
        # if StorySentence_Text is stopping this frame...
        if StorySentence_Text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StorySentence_Text.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                StorySentence_Text.tStop = t  # not accounting for scr refresh
                StorySentence_Text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'StorySentence_Text.stopped')
                # update status
                StorySentence_Text.status = FINISHED
                StorySentence_Text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "SS" ---
    for thisComponent in SSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Neg6'


# --- Prepare to start Routine "Rat" ---
continueRoutine = True
# update component parameters for each repeat
Rating_Response.reset()
# reset Rating_Done to account for continued clicks & clear times on/off
Rating_Done.reset()
# keep track of which components have finished
RatComponents = [Rating_Text, Rating_Response, Rating_Done]
for thisComponent in RatComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Rat" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Rating_Text* updates
    
    # if Rating_Text is starting this frame...
    if Rating_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rating_Text.frameNStart = frameN  # exact frame index
        Rating_Text.tStart = t  # local t and not account for scr refresh
        Rating_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Text.started')
        # update status
        Rating_Text.status = STARTED
        Rating_Text.setAutoDraw(True)
    
    # if Rating_Text is active this frame...
    if Rating_Text.status == STARTED:
        # update params
        pass
    
    # *Rating_Response* updates
    
    # if Rating_Response is starting this frame...
    if Rating_Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rating_Response.frameNStart = frameN  # exact frame index
        Rating_Response.tStart = t  # local t and not account for scr refresh
        Rating_Response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Response, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Response.started')
        # update status
        Rating_Response.status = STARTED
        Rating_Response.setAutoDraw(True)
    
    # if Rating_Response is active this frame...
    if Rating_Response.status == STARTED:
        # update params
        pass
    # *Rating_Done* updates
    
    # if Rating_Done is starting this frame...
    if Rating_Done.status == NOT_STARTED and Rating_Response.getRating() != None:
        # keep track of start time/frame for later
        Rating_Done.frameNStart = frameN  # exact frame index
        Rating_Done.tStart = t  # local t and not account for scr refresh
        Rating_Done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Done, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Done.started')
        # update status
        Rating_Done.status = STARTED
        Rating_Done.setAutoDraw(True)
    
    # if Rating_Done is active this frame...
    if Rating_Done.status == STARTED:
        # update params
        pass
        # check whether Rating_Done has been pressed
        if Rating_Done.isClicked:
            if not Rating_Done.wasClicked:
                # if this is a new click, store time of first click and clicked until
                Rating_Done.timesOn.append(Rating_Done.buttonClock.getTime())
                Rating_Done.timesOff.append(Rating_Done.buttonClock.getTime())
            elif len(Rating_Done.timesOff):
                # if click is continuing from last frame, update time of clicked until
                Rating_Done.timesOff[-1] = Rating_Done.buttonClock.getTime()
            if not Rating_Done.wasClicked:
                # end routine when Rating_Done is clicked
                continueRoutine = False
            if not Rating_Done.wasClicked:
                # run callback code when Rating_Done is clicked
                pass
    # take note of whether Rating_Done was clicked, so that next frame we know if clicks are new
    Rating_Done.wasClicked = Rating_Done.isClicked and Rating_Done.status == STARTED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RatComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Rat" ---
for thisComponent in RatComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Rating_Response.response', Rating_Response.getRating())
thisExp.addData('Rating_Response.rt', Rating_Response.getRT())
thisExp.addData('Rating_Done.numClicks', Rating_Done.numClicks)
if Rating_Done.numClicks:
   thisExp.addData('Rating_Done.timesOn', Rating_Done.timesOn)
   thisExp.addData('Rating_Done.timesOff', Rating_Done.timesOff)
else:
   thisExp.addData('Rating_Done.timesOn', "")
   thisExp.addData('Rating_Done.timesOff', "")
# the Routine "Rat" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
NSB6 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PsychopyIntegrationSheets/NSB6.xlsx'),
    seed=None, name='NSB6')
thisExp.addLoop(NSB6)  # add the loop to the experiment
thisNSB6 = NSB6.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNSB6.rgb)
if thisNSB6 != None:
    for paramName in thisNSB6:
        exec('{} = thisNSB6[paramName]'.format(paramName))

for thisNSB6 in NSB6:
    currentLoop = NSB6
    # abbreviate parameter names if possible (e.g. rgb = thisNSB6.rgb)
    if thisNSB6 != None:
        for paramName in thisNSB6:
            exec('{} = thisNSB6[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    Trial_RatingResponse.reset()
    # reset Trial_ResponseDone to account for continued clicks & clear times on/off
    Trial_ResponseDone.reset()
    # keep track of which components have finished
    TrialComponents = [Trial_NSB, Trial_Cue, Trial_RatingText, Trial_RatingResponse, Trial_ResponseDone]
    for thisComponent in TrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Trial" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Trial_NSB* updates
        
        # if Trial_NSB is starting this frame...
        if Trial_NSB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Trial_NSB.frameNStart = frameN  # exact frame index
            Trial_NSB.tStart = t  # local t and not account for scr refresh
            Trial_NSB.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_NSB, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_NSB.started')
            # update status
            Trial_NSB.status = STARTED
            Trial_NSB.setAutoDraw(True)
        
        # if Trial_NSB is active this frame...
        if Trial_NSB.status == STARTED:
            # update params
            pass
        
        # if Trial_NSB is stopping this frame...
        if Trial_NSB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Trial_NSB.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                Trial_NSB.tStop = t  # not accounting for scr refresh
                Trial_NSB.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Trial_NSB.stopped')
                # update status
                Trial_NSB.status = FINISHED
                Trial_NSB.setAutoDraw(False)
        
        # *Trial_Cue* updates
        
        # if Trial_Cue is starting this frame...
        if Trial_Cue.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            Trial_Cue.frameNStart = frameN  # exact frame index
            Trial_Cue.tStart = t  # local t and not account for scr refresh
            Trial_Cue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_Cue, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_Cue.started')
            # update status
            Trial_Cue.status = STARTED
            Trial_Cue.setAutoDraw(True)
        
        # if Trial_Cue is active this frame...
        if Trial_Cue.status == STARTED:
            # update params
            pass
        
        # if Trial_Cue is stopping this frame...
        if Trial_Cue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Trial_Cue.tStartRefresh + 12-frameTolerance:
                # keep track of stop time/frame for later
                Trial_Cue.tStop = t  # not accounting for scr refresh
                Trial_Cue.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Trial_Cue.stopped')
                # update status
                Trial_Cue.status = FINISHED
                Trial_Cue.setAutoDraw(False)
        
        # *Trial_RatingText* updates
        
        # if Trial_RatingText is starting this frame...
        if Trial_RatingText.status == NOT_STARTED and tThisFlip >= 15-frameTolerance:
            # keep track of start time/frame for later
            Trial_RatingText.frameNStart = frameN  # exact frame index
            Trial_RatingText.tStart = t  # local t and not account for scr refresh
            Trial_RatingText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_RatingText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_RatingText.started')
            # update status
            Trial_RatingText.status = STARTED
            Trial_RatingText.setAutoDraw(True)
        
        # if Trial_RatingText is active this frame...
        if Trial_RatingText.status == STARTED:
            # update params
            pass
        
        # *Trial_RatingResponse* updates
        
        # if Trial_RatingResponse is starting this frame...
        if Trial_RatingResponse.status == NOT_STARTED and tThisFlip >= 15-frameTolerance:
            # keep track of start time/frame for later
            Trial_RatingResponse.frameNStart = frameN  # exact frame index
            Trial_RatingResponse.tStart = t  # local t and not account for scr refresh
            Trial_RatingResponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_RatingResponse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_RatingResponse.started')
            # update status
            Trial_RatingResponse.status = STARTED
            Trial_RatingResponse.setAutoDraw(True)
        
        # if Trial_RatingResponse is active this frame...
        if Trial_RatingResponse.status == STARTED:
            # update params
            pass
        # *Trial_ResponseDone* updates
        
        # if Trial_ResponseDone is starting this frame...
        if Trial_ResponseDone.status == NOT_STARTED and Trial_RatingResponse.getRating() != None:
            # keep track of start time/frame for later
            Trial_ResponseDone.frameNStart = frameN  # exact frame index
            Trial_ResponseDone.tStart = t  # local t and not account for scr refresh
            Trial_ResponseDone.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial_ResponseDone, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Trial_ResponseDone.started')
            # update status
            Trial_ResponseDone.status = STARTED
            Trial_ResponseDone.setAutoDraw(True)
        
        # if Trial_ResponseDone is active this frame...
        if Trial_ResponseDone.status == STARTED:
            # update params
            pass
            # check whether Trial_ResponseDone has been pressed
            if Trial_ResponseDone.isClicked:
                if not Trial_ResponseDone.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    Trial_ResponseDone.timesOn.append(Trial_ResponseDone.buttonClock.getTime())
                    Trial_ResponseDone.timesOff.append(Trial_ResponseDone.buttonClock.getTime())
                elif len(Trial_ResponseDone.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    Trial_ResponseDone.timesOff[-1] = Trial_ResponseDone.buttonClock.getTime()
                if not Trial_ResponseDone.wasClicked:
                    # end routine when Trial_ResponseDone is clicked
                    continueRoutine = False
                if not Trial_ResponseDone.wasClicked:
                    # run callback code when Trial_ResponseDone is clicked
                    pass
        # take note of whether Trial_ResponseDone was clicked, so that next frame we know if clicks are new
        Trial_ResponseDone.wasClicked = Trial_ResponseDone.isClicked and Trial_ResponseDone.status == STARTED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Trial" ---
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    NSB6.addData('Trial_RatingResponse.response', Trial_RatingResponse.getRating())
    NSB6.addData('Trial_RatingResponse.rt', Trial_RatingResponse.getRT())
    NSB6.addData('Trial_ResponseDone.numClicks', Trial_ResponseDone.numClicks)
    if Trial_ResponseDone.numClicks:
       NSB6.addData('Trial_ResponseDone.timesOn', Trial_ResponseDone.timesOn)
       NSB6.addData('Trial_ResponseDone.timesOff', Trial_ResponseDone.timesOff)
    else:
       NSB6.addData('Trial_ResponseDone.timesOn', "")
       NSB6.addData('Trial_ResponseDone.timesOff', "")
    # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'NSB6'


# --- Prepare to start Routine "GR" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
GRComponents = [GetReady_Text, GetRead_Cross]
for thisComponent in GRComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "GR" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *GetReady_Text* updates
    
    # if GetReady_Text is starting this frame...
    if GetReady_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GetReady_Text.frameNStart = frameN  # exact frame index
        GetReady_Text.tStart = t  # local t and not account for scr refresh
        GetReady_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GetReady_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'GetReady_Text.started')
        # update status
        GetReady_Text.status = STARTED
        GetReady_Text.setAutoDraw(True)
    
    # if GetReady_Text is active this frame...
    if GetReady_Text.status == STARTED:
        # update params
        GetReady_Text.setText('', log=False)
    
    # if GetReady_Text is stopping this frame...
    if GetReady_Text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > GetReady_Text.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            GetReady_Text.tStop = t  # not accounting for scr refresh
            GetReady_Text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'GetReady_Text.stopped')
            # update status
            GetReady_Text.status = FINISHED
            GetReady_Text.setAutoDraw(False)
    
    # *GetRead_Cross* updates
    
    # if GetRead_Cross is starting this frame...
    if GetRead_Cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        GetRead_Cross.frameNStart = frameN  # exact frame index
        GetRead_Cross.tStart = t  # local t and not account for scr refresh
        GetRead_Cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(GetRead_Cross, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'GetRead_Cross.started')
        # update status
        GetRead_Cross.status = STARTED
        GetRead_Cross.setAutoDraw(True)
    
    # if GetRead_Cross is active this frame...
    if GetRead_Cross.status == STARTED:
        # update params
        pass
    
    # if GetRead_Cross is stopping this frame...
    if GetRead_Cross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > GetRead_Cross.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            GetRead_Cross.tStop = t  # not accounting for scr refresh
            GetRead_Cross.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'GetRead_Cross.stopped')
            # update status
            GetRead_Cross.status = FINISHED
            GetRead_Cross.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GRComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "GR" ---
for thisComponent in GRComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# set up handler to look after randomisation of conditions etc
Neu6 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PsychopyIntegrationSheets/Neutral6.xlsx'),
    seed=None, name='Neu6')
thisExp.addLoop(Neu6)  # add the loop to the experiment
thisNeu6 = Neu6.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNeu6.rgb)
if thisNeu6 != None:
    for paramName in thisNeu6:
        exec('{} = thisNeu6[paramName]'.format(paramName))

for thisNeu6 in Neu6:
    currentLoop = Neu6
    # abbreviate parameter names if possible (e.g. rgb = thisNeu6.rgb)
    if thisNeu6 != None:
        for paramName in thisNeu6:
            exec('{} = thisNeu6[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "SS" ---
    continueRoutine = True
    # update component parameters for each repeat
    StorySentence_Text.setText(StorySentences)
    # keep track of which components have finished
    SSComponents = [StorySentence_Text]
    for thisComponent in SSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "SS" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *StorySentence_Text* updates
        
        # if StorySentence_Text is starting this frame...
        if StorySentence_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StorySentence_Text.frameNStart = frameN  # exact frame index
            StorySentence_Text.tStart = t  # local t and not account for scr refresh
            StorySentence_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StorySentence_Text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'StorySentence_Text.started')
            # update status
            StorySentence_Text.status = STARTED
            StorySentence_Text.setAutoDraw(True)
        
        # if StorySentence_Text is active this frame...
        if StorySentence_Text.status == STARTED:
            # update params
            pass
        
        # if StorySentence_Text is stopping this frame...
        if StorySentence_Text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StorySentence_Text.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                StorySentence_Text.tStop = t  # not accounting for scr refresh
                StorySentence_Text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'StorySentence_Text.stopped')
                # update status
                StorySentence_Text.status = FINISHED
                StorySentence_Text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "SS" ---
    for thisComponent in SSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Neu6'


# set up handler to look after randomisation of conditions etc
NeuSta6 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('PsychopyIntegrationSheets/NeutralStatements6.xlsx'),
    seed=None, name='NeuSta6')
thisExp.addLoop(NeuSta6)  # add the loop to the experiment
thisNeuSta6 = NeuSta6.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNeuSta6.rgb)
if thisNeuSta6 != None:
    for paramName in thisNeuSta6:
        exec('{} = thisNeuSta6[paramName]'.format(paramName))

for thisNeuSta6 in NeuSta6:
    currentLoop = NeuSta6
    # abbreviate parameter names if possible (e.g. rgb = thisNeuSta6.rgb)
    if thisNeuSta6 != None:
        for paramName in thisNeuSta6:
            exec('{} = thisNeuSta6[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "NS" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    NSComponents = [NeutralStatement_Text]
    for thisComponent in NSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "NS" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 12.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NeutralStatement_Text* updates
        
        # if NeutralStatement_Text is starting this frame...
        if NeutralStatement_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NeutralStatement_Text.frameNStart = frameN  # exact frame index
            NeutralStatement_Text.tStart = t  # local t and not account for scr refresh
            NeutralStatement_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NeutralStatement_Text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NeutralStatement_Text.started')
            # update status
            NeutralStatement_Text.status = STARTED
            NeutralStatement_Text.setAutoDraw(True)
        
        # if NeutralStatement_Text is active this frame...
        if NeutralStatement_Text.status == STARTED:
            # update params
            pass
        
        # if NeutralStatement_Text is stopping this frame...
        if NeutralStatement_Text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > NeutralStatement_Text.tStartRefresh + 12-frameTolerance:
                # keep track of stop time/frame for later
                NeutralStatement_Text.tStop = t  # not accounting for scr refresh
                NeutralStatement_Text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'NeutralStatement_Text.stopped')
                # update status
                NeutralStatement_Text.status = FINISHED
                NeutralStatement_Text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "NS" ---
    for thisComponent in NSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-12.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'NeuSta6'


# --- Prepare to start Routine "Rat" ---
continueRoutine = True
# update component parameters for each repeat
Rating_Response.reset()
# reset Rating_Done to account for continued clicks & clear times on/off
Rating_Done.reset()
# keep track of which components have finished
RatComponents = [Rating_Text, Rating_Response, Rating_Done]
for thisComponent in RatComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Rat" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Rating_Text* updates
    
    # if Rating_Text is starting this frame...
    if Rating_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rating_Text.frameNStart = frameN  # exact frame index
        Rating_Text.tStart = t  # local t and not account for scr refresh
        Rating_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Text.started')
        # update status
        Rating_Text.status = STARTED
        Rating_Text.setAutoDraw(True)
    
    # if Rating_Text is active this frame...
    if Rating_Text.status == STARTED:
        # update params
        pass
    
    # *Rating_Response* updates
    
    # if Rating_Response is starting this frame...
    if Rating_Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Rating_Response.frameNStart = frameN  # exact frame index
        Rating_Response.tStart = t  # local t and not account for scr refresh
        Rating_Response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Response, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Response.started')
        # update status
        Rating_Response.status = STARTED
        Rating_Response.setAutoDraw(True)
    
    # if Rating_Response is active this frame...
    if Rating_Response.status == STARTED:
        # update params
        pass
    # *Rating_Done* updates
    
    # if Rating_Done is starting this frame...
    if Rating_Done.status == NOT_STARTED and Rating_Response.getRating() != None:
        # keep track of start time/frame for later
        Rating_Done.frameNStart = frameN  # exact frame index
        Rating_Done.tStart = t  # local t and not account for scr refresh
        Rating_Done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rating_Done, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'Rating_Done.started')
        # update status
        Rating_Done.status = STARTED
        Rating_Done.setAutoDraw(True)
    
    # if Rating_Done is active this frame...
    if Rating_Done.status == STARTED:
        # update params
        pass
        # check whether Rating_Done has been pressed
        if Rating_Done.isClicked:
            if not Rating_Done.wasClicked:
                # if this is a new click, store time of first click and clicked until
                Rating_Done.timesOn.append(Rating_Done.buttonClock.getTime())
                Rating_Done.timesOff.append(Rating_Done.buttonClock.getTime())
            elif len(Rating_Done.timesOff):
                # if click is continuing from last frame, update time of clicked until
                Rating_Done.timesOff[-1] = Rating_Done.buttonClock.getTime()
            if not Rating_Done.wasClicked:
                # end routine when Rating_Done is clicked
                continueRoutine = False
            if not Rating_Done.wasClicked:
                # run callback code when Rating_Done is clicked
                pass
    # take note of whether Rating_Done was clicked, so that next frame we know if clicks are new
    Rating_Done.wasClicked = Rating_Done.isClicked and Rating_Done.status == STARTED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RatComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Rat" ---
for thisComponent in RatComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Rating_Response.response', Rating_Response.getRating())
thisExp.addData('Rating_Response.rt', Rating_Response.getRT())
thisExp.addData('Rating_Done.numClicks', Rating_Done.numClicks)
if Rating_Done.numClicks:
   thisExp.addData('Rating_Done.timesOn', Rating_Done.timesOn)
   thisExp.addData('Rating_Done.timesOff', Rating_Done.timesOff)
else:
   thisExp.addData('Rating_Done.timesOn', "")
   thisExp.addData('Rating_Done.timesOff', "")
# the Routine "Rat" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "RegRat" ---
continueRoutine = True
# update component parameters for each repeat
RegulationRating_Response.reset()
# reset RegulationRating_Done to account for continued clicks & clear times on/off
RegulationRating_Done.reset()
# keep track of which components have finished
RegRatComponents = [RegulationRating_Text, RegulationRating_Response, RegulationRating_Done]
for thisComponent in RegRatComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "RegRat" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *RegulationRating_Text* updates
    
    # if RegulationRating_Text is starting this frame...
    if RegulationRating_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RegulationRating_Text.frameNStart = frameN  # exact frame index
        RegulationRating_Text.tStart = t  # local t and not account for scr refresh
        RegulationRating_Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RegulationRating_Text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RegulationRating_Text.started')
        # update status
        RegulationRating_Text.status = STARTED
        RegulationRating_Text.setAutoDraw(True)
    
    # if RegulationRating_Text is active this frame...
    if RegulationRating_Text.status == STARTED:
        # update params
        pass
    
    # *RegulationRating_Response* updates
    
    # if RegulationRating_Response is starting this frame...
    if RegulationRating_Response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        RegulationRating_Response.frameNStart = frameN  # exact frame index
        RegulationRating_Response.tStart = t  # local t and not account for scr refresh
        RegulationRating_Response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RegulationRating_Response, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RegulationRating_Response.started')
        # update status
        RegulationRating_Response.status = STARTED
        RegulationRating_Response.setAutoDraw(True)
    
    # if RegulationRating_Response is active this frame...
    if RegulationRating_Response.status == STARTED:
        # update params
        pass
    # *RegulationRating_Done* updates
    
    # if RegulationRating_Done is starting this frame...
    if RegulationRating_Done.status == NOT_STARTED and RegulationRating_Response.getRating() != None:
        # keep track of start time/frame for later
        RegulationRating_Done.frameNStart = frameN  # exact frame index
        RegulationRating_Done.tStart = t  # local t and not account for scr refresh
        RegulationRating_Done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(RegulationRating_Done, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'RegulationRating_Done.started')
        # update status
        RegulationRating_Done.status = STARTED
        RegulationRating_Done.setAutoDraw(True)
    
    # if RegulationRating_Done is active this frame...
    if RegulationRating_Done.status == STARTED:
        # update params
        pass
        # check whether RegulationRating_Done has been pressed
        if RegulationRating_Done.isClicked:
            if not RegulationRating_Done.wasClicked:
                # if this is a new click, store time of first click and clicked until
                RegulationRating_Done.timesOn.append(RegulationRating_Done.buttonClock.getTime())
                RegulationRating_Done.timesOff.append(RegulationRating_Done.buttonClock.getTime())
            elif len(RegulationRating_Done.timesOff):
                # if click is continuing from last frame, update time of clicked until
                RegulationRating_Done.timesOff[-1] = RegulationRating_Done.buttonClock.getTime()
            if not RegulationRating_Done.wasClicked:
                # end routine when RegulationRating_Done is clicked
                continueRoutine = False
            if not RegulationRating_Done.wasClicked:
                # run callback code when RegulationRating_Done is clicked
                pass
    # take note of whether RegulationRating_Done was clicked, so that next frame we know if clicks are new
    RegulationRating_Done.wasClicked = RegulationRating_Done.isClicked and RegulationRating_Done.status == STARTED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RegRatComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "RegRat" ---
for thisComponent in RegRatComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('RegulationRating_Response.response', RegulationRating_Response.getRating())
thisExp.addData('RegulationRating_Response.rt', RegulationRating_Response.getRT())
thisExp.addData('RegulationRating_Done.numClicks', RegulationRating_Done.numClicks)
if RegulationRating_Done.numClicks:
   thisExp.addData('RegulationRating_Done.timesOn', RegulationRating_Done.timesOn)
   thisExp.addData('RegulationRating_Done.timesOff', RegulationRating_Done.timesOff)
else:
   thisExp.addData('RegulationRating_Done.timesOn', "")
   thisExp.addData('RegulationRating_Done.timesOff', "")
# the Routine "RegRat" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "End" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = [text]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "End" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 10.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    
    # if text is starting this frame...
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        # update status
        text.status = STARTED
        text.setAutoDraw(True)
    
    # if text is active this frame...
    if text.status == STARTED:
        # update params
        pass
    
    # if text is stopping this frame...
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.stopped')
            # update status
            text.status = FINISHED
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "End" ---
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-10.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
