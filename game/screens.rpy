## Screens are customizable. Since a PC Python VM is envoked to
## create them, you can use any Python construct allowed in
## normal Python source code.

default quick_menu = True

################################################################################
## Main and Game Menus
################################################################################

screen main_menu():
    tag menu
    
    add "#1a1a2e"
    
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 30
        
        text "CITY LIGHTS & SILENT TRUTHS" xalign 0.5 size 60 color "#FF6B9D"
        text "A Visual Novel Dating Simulator" xalign 0.5 size 20 color "#FFFFFF"
        
        vbox:
            xalign 0.5
            spacing 15
            
            textbutton "New Game" action Start() style "main_menu_button"
            textbutton "Continue" action ShowMenu("save") style "main_menu_button"
            textbutton "Load Game" action ShowMenu("load") style "main_menu_button"
            textbutton "Settings" action ShowMenu("preferences") style "main_menu_button"
            textbutton "About" action ShowMenu("about") style "main_menu_button"
            textbutton "Quit" action Quit() style "main_menu_button"

style main_menu_button:
    xysize (250, 50)
    background "#FF6B9D"
    hover_background "#FF8DB3"
    text_align 0.5
    text_color "#FFFFFF"
    hover_color "#FFFFFF"
    left_padding 10
    right_padding 10
    top_padding 8
    bottom_padding 8
    font "fonts/dejavu_sans_bold.ttf"
    size 18

screen game_menu(title):
    tag menu
    
    add "#1a1a2e"
    
    frame:
        xysize (600, 400)
        xalign 0.5
        yalign 0.5
        background "#2d2d44"
        
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            
            text title xalign 0.5 size 30 color "#FF6B9D"
            
            textbutton "Return" action Return() xalign 0.5 style "menu_button"

style menu_button:
    xysize (200, 40)
    background "#FF6B9D"
    hover_background "#FF8DB3"
    text_align 0.5
    text_color "#FFFFFF"

screen preferences():
    tag menu
    
    add "#1a1a2e"
    
    vbox:
        xalign 0.5
        yalign 0.1
        spacing 20
        
        text "SETTINGS" xalign 0.5 size 40 color "#FF6B9D"
        
        hbox:
            xalign 0.5
            spacing 20
            
            vbox:
                text "Master Volume:" color "#FFFFFF"
                bar value AudioVolume("master") xsize 200
            
            vbox:
                text "Music Volume:" color "#FFFFFF"
                bar value AudioVolume("music") xsize 200
            
            vbox:
                text "SFX Volume:" color "#FFFFFF"
                bar value AudioVolume("sfx") xsize 200
        
        textbutton "Back" action Return() xalign 0.5

screen about():
    tag menu
    
    add "#1a1a2e"
    
    frame:
        xysize (700, 500)
        xalign 0.5
        yalign 0.5
        background "#2d2d44"
        
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 15
            
            text "ABOUT" xalign 0.5 size 30 color "#FF6B9D"
            
            text "City Lights & Silent Truths" xalign 0.5 color "#FFFFFF" size 18
            text "Version 0.1.0 - Proof of Concept Demo" xalign 0.5 color "#AAAAAA" size 14
            
            text "" 
            
            text "A mature visual novel dating simulator with psychological depth." xalign 0.5 color "#FFFFFF"
            text "Experience complex relationships, moral dilemmas, and multiple branching paths." xalign 0.5 color "#FFFFFF"
            
            text ""
            
            text "Engine: Ren'Py" xalign 0.5 color "#AAAAAA"
            text "Developer: melieinacelesteria111-cmyk" xalign 0.5 color "#AAAAAA"
            text "Repository: github.com/melieinacelesteria111-cmyk/visual-novel-game" xalign 0.5 color "#AAAAAA" size 12
            
            text ""
            
            textbutton "Back" action Return() xalign 0.5

screen say(who, what):
    layers "master"
    
    window:
        xysize (900, 200)
        xalign 0.5
        yalign 0.9
        background Solid("#1a1a2e", xysize=(900, 200))
        
        vbox:
            xalign 0.0
            yalign 0.0
            spacing 10
            
            if who:
                text who style "say_label" color "#FF6B9D"
            
            text what style "say_text" color "#FFFFFF"

style say_label:
    size 24
    bold True

style say_text:
    size 18
    xalign 0.0
    text_align 0.0
    min_width 850

screen input(prompt):
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        
        text prompt xalign 0.5 color "#FFFFFF"
        input style "input_text" length 20

style input_text:
    xalign 0.5
    background "#2d2d44"
    color "#FFFFFF"
    selected_background "#FF6B9D"
    selected_color "#FFFFFF"
    xysize (300, 40)

screen choice(items):
    layer "master"
    
    window:
        xysize (900, None)
        xalign 0.5
        yalign 0.9
        background "#1a1a2e"
        
        vbox:
            xalign 0.5
            yalign 0.0
            spacing 15
            
            for i, (caption, action) in enumerate(items):
                button:
                    xysize (800, 60)
                    xalign 0.5
                    background "#2d2d44"
                    hover_background "#FF6B9D"
                    action action
                    
                    text caption xalign 0.5 yalign 0.5 color "#FFFFFF"

screen quick_menu():
    zorder 100
    
    hbox:
        xalign 1.0
        yalign 1.0
        spacing 6
        textbutton _"Q.Save") action QuickSave() style "quick_button"
        textbutton _("Q.Load") action QuickLoad() style "quick_button"
        textbutton _("Skip") action Skip() alternate_action SetVariable("skip_fast", not skip_fast) style "quick_button"
        textbutton _("A.Hide") action _Null() style "quick_button"
        textbutton _("S.Menu") action ShowMenu('save') style "quick_button"
        textbutton _("L.Menu") action ShowMenu('load') style "quick_button"
        textbutton _("Prefs") action ShowMenu('preferences') style "quick_button"

style quick_button:
    background "#FF6B9D"
    hover_background "#FF8DB3"
    text_color "#FFFFFF"
    padding (5, 5)
    xysize (75, 30)
