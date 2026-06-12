## This file contains some of the options that can customize your Ren'Py
## game. When you run the Ren'Py demo, it little version of this file is
## put into a new game/ directory. When you create new game directory, this
## file is also put there.
##
## Because this filestarts with two percent signs, it is ignored by the game
## since no label or variable definitions occur before the first percent sign.
##
##############################################################################

## Window title
define config.window_title = _("City Lights & Silent Truths - Visual Novel") 

## Folder of the game's archive files. None is the normal, ephemeral
## delete-me.txt in the game folder. When not None, game folder files are
## used when available.
define config.archive_directories = [ ]

## Enable multiprocessing on Windows.
define config.multiprocessing = True

## Sounds that are used when Ren'Py boots.
define config.main_menu_music = "audio/bgm_main.mp3"

## Fonts
define gui.default_font = "fonts/dejavu_sans.ttf"
define gui.name_font = "fonts/dejavu_sans_bold.ttf"
define gui.interface_font = "fonts/dejavu_sans.ttf"
define gui.text_font = "fonts/dejavu_sans.ttf"

## Positioning and Spacing
define gui.text_xalign = 0.5

## Colors
define gui.accent_color = '#FF6B9D'
define gui.insensitive_color = '#8888888f'
define gui.disabled_color = '#8888888f'
define gui.idle_color = '#888888'
define gui.hover_color = '#cccccc'
define gui.selected_color = '#ffffff'
define gui.insensitive_foreground_color = '#8888888f'
define gui.muted_color = '#512222'
define gui.muted_foreground_color = '#8b5a5a'

## Dark Ren'Py Theme
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'

## Transitions
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = fadeout
define config.after_warp_transition = None
define config.audio_when_minimized = None
define config.layered_shifts = False

## UI Sizing
define gui.theme_invert_colors = False
define gui.text_size = 22
define gui.name_text_size = 24
define gui.notify_text_size = 16

## Use SDL2
define config.gl2 = True
define config.angle = "auto"

## Game version
define config.version = "0.1.0 - Proof of Concept Demo"
