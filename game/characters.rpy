# Character Definitions
# Define semua karakter dengan styling

# Alexis Reid - Love Interest #1
define alexis = Character(
    "Alexis",
    color="#FF6B9D",
    outlines=[(2, "#000000", 0, 0)],
    callback=renpy.music.set_volume(0.7, channel="music")
)

# Jordan Vale - Love Interest #2  
define jordan = Character(
    "Jordan",
    color="#6B9DFF",
    outlines=[(2, "#000000", 0, 0)]
)

# Casey Morgan - Love Interest #3
define casey = Character(
    "Casey",
    color="#9DFF6B",
    outlines=[(2, "#000000", 0, 0)]
)

# Narrator
define narrator = Character(
    None,
    color="#FFFFFF",
    outlines=[(2, "#000000", 0, 0)]
)

# Player Character
define player = Character(
    "You",
    color="#FFD700",
    outlines=[(2, "#000000", 0, 0)]
)
