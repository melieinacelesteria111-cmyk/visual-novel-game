# Main Story Script - Visual Novel Dating Simulator
# "City Lights & Silent Truths" - Proof of Concept Demo

label start:
    scene black
    with fade
    
    # Show title
    show text "CITY LIGHTS & SILENT TRUTHS" at truecenter
    with dissolve
    pause(2)
    hide text
    with dissolve
    
    # Intro sequence
    scene bg_office
    with fade
    
    narrator "Your new apartment overlooks the city skyline. Tomorrow, you start at Luminous Advertising—the most prestigious agency in the metropolitan."
    narrator "You've dreamed of this moment for years. But as you stare at the glittering lights below, you feel a strange sense of unease."
    narrator "Something tells you that this job will change your life in ways you can't imagine."
    
    pause(1)
    
    narrator "Three months later..."
    narrator "You've settled into the rhythm of the agency. The work is demanding, the competition fierce."
    narrator "But there are three people who have captured your attention."
    
    # Show first character appearance
    scene bg_office
    show alexis_normal at right
    with dissolve
    
    narrator "First, there's Alexis Reid—your boss. Charismatic, brilliant, and impossibly beautiful."
    narrator "Alexis seems to have an effect on everyone in the office. They command respect without effort."
    narrator "But lately, you've noticed something else: a vulnerability hiding beneath the confidence."
    
    pause(1)
    
    hide alexis_normal
    with dissolve
    
    narrator "Then there's Jordan Vale, a freelance artist who collaborates with the agency on creative projects."
    narrator "Jordan's rebellious spirit and raw honesty are refreshing in this world of carefully crafted personas."
    narrator "There's something magnetic about someone who refuses to play the game."
    
    pause(1)
    
    narrator "Finally, there's Casey Morgan—the company's VP of Operations."
    narrator "Calm, collected, mysterious. Casey rarely shows emotion, but when they do, it feels significant."
    narrator "You find yourself wondering what stories are hidden behind those eyes."
    
    pause(1.5)
    
    # First choice
    narrator "Today, you're called to Alexis's office. Your heart quickens as you walk down the corridor."
    
    scene bg_office
    show alexis_normal at center
    with dissolve
    
    alexis "Hey, come in. I've been looking at your recent work on the Henderson campaign."
    
    menu:
        "(Nervous but professional) Thanks for reviewing it, Alexis. I'd love your feedback." "choice_professional":
            $ modify_affection("alexis", 5)
            $ modify_trust("alexis", 10)
            narrator "[Affection +5 | Trust +10]"
            
        "(Confident) I think it's some of my best work. What do you think?" "choice_confident":
            $ modify_affection("alexis", 10)
            $ modify_trust("alexis", 5)
            narrator "[Affection +10 | Trust +5]"
            
        "(Casual) Yeah, I put a lot of effort into it. Hoping it hits the mark." "choice_casual":
            $ modify_affection("alexis", 3)
            $ modify_trust("alexis", 7)
            narrator "[Affection +3 | Trust +7]"
    
    show alexis_happy at center
    with dissolve
    
    alexis "I was impressed. Really impressed. There's something fresh about your perspective."
    alexis "I want to put you on the Westbrook project. It's high-profile, high-stakes."
    
    player "That's... I'm honored. Thank you."
    
    alexis "Don't thank me yet. It's going to be demanding. Nights, weekends, sometimes all-nighters."
    alexis "I need to know you're ready for that commitment."
    
    menu:
        "I'm absolutely ready. Whatever it takes." "choice_commitment_high":
            $ modify_affection("alexis", 12)
            $ player_self_respect -= 5
            narrator "[Affection +12 | Self-Respect -5]"
            
        "I'm interested, but I need to maintain work-life balance. Can we discuss terms?" "choice_commitment_balanced":
            $ modify_affection("alexis", 8)
            $ modify_trust("alexis", 15)
            $ player_self_respect += 5
            narrator "[Affection +8 | Trust +15 | Self-Respect +5]"
            
        "I want it, but I need to think about what I'm signing up for." "choice_commitment_cautious":
            $ modify_affection("alexis", 2)
            $ modify_trust("alexis", 12)
            narrator "[Affection +2 | Trust +12]"
    
    show alexis_normal at center
    with dissolve
    
    alexis "Alright. I respect that you're thinking it through."
    alexis "Just... don't think too long, okay? Opportunities like this don't wait around."
    
    pause(1)
    
    # Scene transition
    scene bg_cafe
    with fade
    
    narrator "Later that week, you meet Jordan at a small cafe near the office."
    narrator "Jordan's working on sketches for an upcoming campaign while you nurse a coffee."
    
    show jordan_normal at center
    with dissolve
    
    jordan "So, word is Alexis picked you for the Westbrook project. That's huge."
    
    player "Yeah, I'm still processing it."
    
    jordan "Be careful, though. Alexis is talented, but they have a way of consuming people."
    jordan "I've seen people burn out trying to keep up with their standards."
    
    menu:
        "(Appreciative) Thanks for the warning. I'll be careful." "choice_jordan_thanks":
            $ modify_affection("jordan", 8)
            $ modify_trust("jordan", 12)
            narrator "[Jordan - Affection +8 | Trust +12]"
            
        "(Defensive) I can handle myself. Alexis believes in me." "choice_jordan_defensive":
            $ modify_affection("jordan", -3)
            $ modify_trust("jordan", 2)
            narrator "[Jordan - Affection -3 | Trust +2]"
            
        "(Curious) Have you and Alexis had issues before?" "choice_jordan_curious":
            $ modify_affection("jordan", 12)
            $ modify_trust("jordan", 10)
            narrator "[Jordan - Affection +12 | Trust +10]"
    
    show jordan_happy at center
    with dissolve
    
    jordan "I just don't want to see you get hurt. People matter, you know?"
    jordan "In this industry, it's easy to forget that."
    
    pause(1)
    
    # Display current stats
    show screen relationship_stats
    pause(2)
    hide screen relationship_stats
    with dissolve
    
    # Ending of demo
    scene black
    with fade
    
    narrator "As you leave the cafe, your phone buzzes."
    narrator "A text from Alexis: 'Drinks tomorrow? Need to discuss strategy for Westbrook. Also... want to get to know you better.'"
    narrator "Your heart skips a beat. This is the moment everything could change."
    narrator "But which path will you choose?"
    
    # Show end of demo
    show text "=== END OF DEMO ==="
    with dissolve
    pause(2)
    
    show text "Thanks for playing! Stats have been saved." at truecenter
    with dissolve
    pause(2)
    
    # Return to menu or exit
    scene black
    with fade
    
    return

# Choice labels (for clarity)
label choice_professional:
    jump after_choice_1

label choice_confident:
    jump after_choice_1
    
label choice_casual:
    jump after_choice_1

label after_choice_1:
    pass

label choice_commitment_high:
    jump after_choice_2

label choice_commitment_balanced:
    jump after_choice_2

label choice_commitment_cautious:
    jump after_choice_2

label after_choice_2:
    pass

label choice_jordan_thanks:
    jump after_choice_3

label choice_jordan_defensive:
    jump after_choice_3

label choice_jordan_curious:
    jump after_choice_3

label after_choice_3:
    pass
