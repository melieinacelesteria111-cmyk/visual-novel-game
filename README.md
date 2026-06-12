# City Lights & Silent Truths
## A Visual Novel / Dating Simulator Game

### 📖 Project Description

A mature visual novel dating simulator with psychological depth, featuring complex relationships, moral dilemmas, and multiple branching paths based on player choices.

**Genre:** Visual Novel / Dating Simulator  
**Target Audience:** 18+  
**Engine:** Ren'Py  
**Status:** Proof of Concept Demo (In Development)

---

### 🎮 Game Features

#### Core Mechanics
- **Affection System**: Track emotional connection with each love interest
- **Trust System**: Measure how much characters trust the player's integrity
- **Multiple Endings**: Choices lead to vastly different story outcomes
- **Relationship Stats**: Real-time tracking of relationship metrics
- **Branching Narrative**: Over 50+ unique dialogue paths in demo

#### Three Love Interests
1. **Alexis Reid** - Ambitious executive with hidden vulnerabilities
2. **Jordan Vale** - Rebellious artist with trust issues
3. **Casey Morgan** - Mysterious and emotionally guarded

---

### 🚀 Quick Start

#### Prerequisites
- [Ren'Py](https://www.renpy.org/) 8.1.3 or higher
- Python 3.8+

#### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/melieinacelesteria111-cmyk/visual-novel-game.git
   cd visual-novel-game
   ```

2. **Copy to Ren'Py projects folder:**
   - Windows: `C:\renpy\projects\`
   - macOS: `/Applications/renpy/projects/`
   - Linux: `~/renpy/projects/`

3. **Launch the game:**
   - Open Ren'Py Launcher
   - Select "visual-novel-game" from projects list
   - Click "Launch Project"

---

### 📁 Project Structure

```
game/
├── script.rpy              # Main story and dialogue
├── characters.rpy          # Character definitions
├── affection_system.rpy    # Relationship mechanics
├── images.rpy              # Image definitions
├── options.rpy             # Game configuration
├── images/
│   ├── bg_office.png       # Background images
│   ├── bg_cafe.png
│   ├── alexis_normal.png   # Character sprites
│   ├── alexis_happy.png
│   └── ... (more sprites)
├── audio/
│   ├── bgm_main.mp3        # Background music
│   └── sfx_click.wav       # Sound effects
└── gui/
    └── theme.rpy           # UI customization
```

---

### 🎨 Creating Assets

#### Placeholder Images
For now, the game uses 800x600px placeholder images. To add your own:

1. Create character sprites (recommended: 600x800px PNG)
2. Create backgrounds (recommended: 1280x720px PNG)
3. Place in `game/images/` folder
4. Update references in `images.rpy`

#### Audio
1. Add background music (MP3 format) to `game/audio/`
2. Add sound effects (WAV format) to `game/audio/`
3. Reference in script with: `play music "audio/filename.mp3"`

---

### 💾 Game Saves & Stats

Player progress is automatically saved:
- Affection points with each character
- Trust metrics
- Dialogue choices
- Self-respect values
- Game progress

Saves are stored in Ren'Py's default save folder.

---

### 📊 Affection System Explained

#### Affection Points (-100 to +100)
- **-100 to -50:** HOSTILE - Character avoids player
- **-50 to 0:** UNCOMFORTABLE - Distance and coldness
- **0 to +30:** ACQUAINTANCE - Friendly but not intimate
- **+30 to +60:** CLOSE FRIEND - Chemistry developing
- **+60 to +80:** ROMANTIC INTEREST - Exclusive romantic scenes unlock
- **+80 to +100:** DEEP LOVE - Maximum intimacy and special endings

#### Trust Points (0 to 100)
- Measures integrity and reliability in player's eyes
- Critical for "Good Endings"
- Built through honest choices and keeping promises
- Lost through deception and broken commitments

---

### 🎯 Dialogue Choice System

Each choice shows:
- **Dialogue Text** - What the player will say
- **Tone Indicator** - Emoji showing tone (❤️ romantic, 💪 assertive, etc.)
- **Hidden Consequences** - Unknown until revealed

**Example:**
```
Alexis: "I want you on the Westbrook project. Can you commit?"

☐ ❤️ "I'm absolutely ready. Whatever it takes."
    └─ +12 Affection | -5 Self-Respect
    
☐ 💪 "I'm interested, but need work-life balance."
    └─ +8 Affection | +15 Trust | +5 Self-Respect
    
☐ 🤐 "I need to think about this."
    └─ +2 Affection | +12 Trust
```

---

### 🔄 Game Flow

```
PROLOGUE: Introduction & Meeting Characters
    ↓
ACT 1: Initial Bonding (Weeks 1-4)
    └─ Meet all three love interests
    └─ First dialogue choices
    └─ Initial affection building
    ↓
ACT 2: Deepening Connections (Weeks 5-8)
    └��� Exclusive romantic scenes unlock
    └─ Personal quests for each character
    └─ First major conflict
    ↓
ACT 3: Crisis & Climax (Weeks 9-12)
    └─ Major decision point
    └─ Secrets revealed
    └─ Relationship stabilizes or crumbles
    ↓
EPILOGUE: Resolution
    └─ Multiple ending variants based on choices
    └─ Relationship status epilogue
    └─ New Game+ unlocked
```

---

### 📝 Story Premise Options

The game starts with **CONCEPT A: "City Lights & Silent Truths"**

A professional moves to the city and falls into a love triangle with:
- An ambitious boss (Alexis)
- A rebellious artist (Jordan)
- A mysterious executive (Casey)

The central conflict: Uncovering corporate corruption while navigating romantic relationships that demand conflicting loyalties.

---

### 🎬 Current Demo Content

**Playtime:** ~10-15 minutes

**Included Scenes:**
1. Prologue - Introduction to the city and three characters
2. Office Scene - Meeting Alexis and first major choice
3. Cafe Scene - Encountering Jordan
4. Stats Display - Relationship metrics reveal

**Branching Paths:** 12+ unique dialogue variations

---

### 📋 Planned Features (Post-Demo)

- [ ] Complete Act 1 (8 full scenes)
- [ ] Complete Act 2 (8 full scenes with intimate moments)
- [ ] Complete Act 3 (climax and major choices)
- [ ] Full art assets (character sprites & backgrounds)
- [ ] Voice acting options
- [ ] Original soundtrack
- [ ] 5+ distinct endings per character route
- [ ] New Game+ with secret content
- [ ] Save/Load screen UI
- [ ] Achievement system
- [ ] CG gallery

---

### 🛠️ Development Roadmap

**Phase 1 (Current):** Proof of Concept Demo ✅
- Basic story framework
- Affection system
- Choice mechanics
- Character introductions

**Phase 2:** Core Story (Est. 2-3 months)
- Complete all 3 acts
- Full dialogue writing
- All character routes
- Multiple endings implementation

**Phase 3:** Asset Creation (Est. 1-2 months)
- Character art & animation
- Background art
- Original music & sound design

**Phase 4:** Polish & Release (Est. 1 month)
- Bug fixes
- Playtesting
- UI/UX refinement
- Final optimization

---

### 💬 Dialogue Statistics

**Demo Version:**
- Total lines written: 2,000+
- Unique dialogue paths: 12+
- Character-specific dialogue: 300+ lines per character

**Full Game (Projected):**
- Total lines: 50,000+
- Unique paths: 500+
- Per character: 5,000+ lines

---

### 🐛 Known Issues & TODO

- [ ] Placeholder images need to be replaced with actual artwork
- [ ] Audio files not yet created
- [ ] Full Act 2 & 3 dialogue incomplete
- [ ] Secret ending conditions not yet implemented
- [ ] Achievement system pending
- [ ] Mobile optimization needed

---

### 📢 Contributing

This is a solo development project, but feedback and suggestions are welcome!

**How to contribute:**
1. Test the demo and report bugs
2. Suggest dialogue improvements
3. Propose story ideas or character routes
4. Share artistic assets or voice acting

---

### 📧 Contact & Support

**Developer:** melieinacelesteria111-cmyk  
**Repository:** https://github.com/melieinacelesteria111-cmyk/visual-novel-game

For bug reports or feature requests, open an issue on GitHub.

---

### 📜 License

This project is proprietary. All rights reserved.

**Note:** Ren'Py is open-source and free to use for commercial and non-commercial games.

---

### 🙏 Credits

- **Engine:** Ren'Py (https://www.renpy.org/)
- **Concept & Writing:** melieinacelesteria111-cmyk
- **Special Thanks:** Visual novel community and Ren'Py documentation

---

### 🎮 How to Play

1. Launch the game
2. Read the story and character introductions
3. Make dialogue choices that reflect your personality
4. Watch your relationship metrics change in real-time
5. Explore different paths in subsequent playthroughs
6. Aim for all 5+ different endings per character route

**Pro Tips:**
- Pay attention to tone indicators (❤️, 💪, 🤐, etc.)
- Different characters respond to different personality types
- Honesty and consistency build trust
- Some choices have hidden long-term consequences
- Save frequently to explore different paths

---

**Last Updated:** June 12, 2026  
**Version:** 0.1.0 (Proof of Concept)

Enjoy the game! 🎮✨
