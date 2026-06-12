# GUI Theme Customization for Visual Novel

define gui.bar_size = 25
define gui.scrollbar_size = 15
define gui.choice_button_width = 800
define gui.choice_button_height = None
define gui.choice_spacing = 0
define gui.checkbox_selected_background = Transform("images/checkbox_selected_background.png", xysize=(24, 24))
define gui.checkbox_selected_foreground = Transform("images/checkbox_selected_foreground.png", xysize=(24, 24))
define gui.checkbox_unselected_background = Transform("images/checkbox_unselected_background.png", xysize=(24, 24))
define gui.checkbox_unselected_foreground = Transform("images/checkbox_unselected_foreground.png", xysize=(24, 24))

define gui.radiobutton_selected_background = Transform("images/radio_selected_background.png", xysize=(24, 24))
define gui.radiobutton_selected_foreground = Transform("images/radio_selected_foreground.png", xysize=(24, 24))
define gui.radiobutton_unselected_background = Transform("images/radio_unselected_background.png", xysize=(24, 24))
define gui.radiobutton_unselected_foreground = Transform("images/radio_unselected_foreground.png", xysize=(24, 24))

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5
    text_align 0.5

style label_button is button:
    background None
    padding gui.button_borders("button")

style label_button_text is button_text:
    color gui.accent_color
    hover_color gui.hover_color

style choice_button is button:
    background "#2d2d44"
    hover_background "#FF6B9D"
    selected_background "#FF6B9D"
    selected_hover_background "#FF8DB3"
    padding gui.button_borders("choice_button")

style choice_button_text is button_text:
    color gui.text_color
    hover_color "#FFFFFF"
    selected_color "#FFFFFF"
    selected_hover_color "#FFFFFF"
