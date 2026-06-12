# Affection & Relationship System
# Core mechanics untuk tracking hubungan dengan setiap karakter

default alexis_affection = 0
default alexis_trust = 0
default alexis_conflict = 0

default jordan_affection = 0
default jordan_trust = 0
default jordan_conflict = 0

default casey_affection = 0
default casey_trust = 0
default casey_conflict = 0

default player_self_respect = 50

# Affection Level Names
define AFFECTION_LEVELS = {
    -100: "HOSTILE",
    -50: "UNCOMFORTABLE",
    0: "NEUTRAL",
    30: "ACQUAINTANCE",
    60: "CLOSE FRIEND",
    80: "ROMANTIC INTEREST",
    100: "DEEP LOVE"
}

init python:
    def get_affection_level(affection):
        """Return affection level name based on points"""
        if affection < -50:
            return "HOSTILE"
        elif affection < 0:
            return "UNCOMFORTABLE"
        elif affection < 30:
            return "NEUTRAL"
        elif affection < 60:
            return "ACQUAINTANCE"
        elif affection < 80:
            return "CLOSE FRIEND"
        elif affection < 100:
            return "ROMANTIC INTEREST"
        else:
            return "DEEP LOVE"
    
    def modify_affection(character, amount):
        """Modify affection points for a character"""
        if character == "alexis":
            renpy.store.alexis_affection = max(-100, min(100, renpy.store.alexis_affection + amount))
            return renpy.store.alexis_affection
        elif character == "jordan":
            renpy.store.jordan_affection = max(-100, min(100, renpy.store.jordan_affection + amount))
            return renpy.store.jordan_affection
        elif character == "casey":
            renpy.store.casey_affection = max(-100, min(100, renpy.store.casey_affection + amount))
            return renpy.store.casey_affection
    
    def modify_trust(character, amount):
        """Modify trust points for a character"""
        if character == "alexis":
            renpy.store.alexis_trust = max(0, min(100, renpy.store.alexis_trust + amount))
            return renpy.store.alexis_trust
        elif character == "jordan":
            renpy.store.jordan_trust = max(0, min(100, renpy.store.jordan_trust + amount))
            return renpy.store.jordan_trust
        elif character == "casey":
            renpy.store.casey_trust = max(0, min(100, renpy.store.casey_trust + amount))
            return renpy.store.casey_trust
    
    def get_stats_display(character):
        """Get formatted stats for displaying character relationship"""
        if character == "alexis":
            aff = renpy.store.alexis_affection
            trust = renpy.store.alexis_trust
            name = "Alexis"
        elif character == "jordan":
            aff = renpy.store.jordan_affection
            trust = renpy.store.jordan_trust
            name = "Jordan"
        elif character == "casey":
            aff = renpy.store.casey_affection
            trust = renpy.store.casey_trust
            name = "Casey"
        
        level = get_affection_level(aff)
        return f"{name}\n[Affection: {aff}/100] [{level}]\n[Trust: {trust}/100]"

# Screen untuk display stats
screen relationship_stats():
    zorder 100
    vbox:
        xpos 20
        ypos 20
        spacing 10
        
        text "=== RELATIONSHIP STATS ===" color "#FFD700" size 20
        text get_stats_display("alexis") color "#FF6B9D" size 16
        text "" # spacing
        text get_stats_display("jordan") color "#6B9DFF" size 16
        text "" # spacing
        text get_stats_display("casey") color "#9DFF6B" size 16
        text "" # spacing
        text f"Self-Respect: {player_self_respect}/100" color "#FFFFFF" size 16
