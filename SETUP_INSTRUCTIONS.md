# 🎮 Setup Instructions - Visual Novel Game

## ⚡ Quick Start (5 minutes)

### Step 1: Install Ren'Py
1. Go to https://www.renpy.org/
2. Download Ren'Py 8.1.3 or latest version
3. Extract to your preferred location (e.g., `C:\renpy` or `/Applications/renpy`)

### Step 2: Get the Game Files

**Option A: Clone from GitHub (Recommended)**
```bash
cd your-renpy-projects-folder
git clone https://github.com/melieinacelesteria111-cmyk/visual-novel-game.git
cd visual-novel-game
```

**Option B: Download as ZIP**
1. Visit: https://github.com/melieinacelesteria111-cmyk/visual-novel-game
2. Click "Code" → "Download ZIP"
3. Extract to your Ren'Py projects folder

### Step 3: Place in Ren'Py Projects

**Windows:**
```
C:\renpy\projects\visual-novel-game
```

**macOS:**
```
/Applications/renpy/projects/visual-novel-game
```

**Linux:**
```
~/renpy/projects/visual-novel-game
```

### Step 4: Launch the Game
1. Open Ren'Py Launcher
2. Click "Refresh" if you don't see the project
3. Select "visual-novel-game" from the list
4. Click "Launch Project"

✅ **Game should now run!**

---

## 🎨 Creating Assets (Optional)

### Character Sprites
1. Create or commission character art (recommended size: 600x800px PNG)
2. Save as `game/images/charactername_emotion.png`
   - Example: `alexis_normal.png`, `alexis_happy.png`, `alexis_sad.png`
3. Ren'Py will automatically detect the images

### Backgrounds
1. Create or download background images (recommended: 1280x720px PNG)
2. Save to `game/images/bg_locationname.png`
   - Example: `bg_office.png`, `bg_cafe.png`, `bg_apartment.png`

### Background Music & Sound Effects
1. Prepare audio files (MP3 for music, WAV for SFX)
2. Place in `game/audio/`
3. Reference in script:
   ```python
   play music "audio/bgm_main.mp3"
   play sound "audio/sfx_click.wav"
   ```

---

## 📝 File Structure After Setup

```
visual-novel-game/
├── game/
│   ├── script.rpy                 # Main story
│   ├── characters.rpy             # Character definitions
│   ├── affection_system.rpy       # Relationship system
│   ├── screens.rpy                # UI screens
│   ├── images.rpy                 # Image definitions
│   ├── options.rpy                # Game settings
│   ├── gui/
│   │   └── theme.rpy              # Theme customization
│   ├── images/
│   │   ├── bg_office.png
│   │   ├── bg_cafe.png
│   │   ├── alexis_normal.png
│   │   ├── alexis_happy.png
│   │   └── ... (add more as needed)
│   └── audio/
│       ├── bgm_main.mp3           # Add your music
│       └── sfx_click.wav          # Add sound effects
├── README.md                      # Project documentation
└── SETUP_INSTRUCTIONS.md          # This file
```

---

## 🐛 Troubleshooting

### "Project not found in launcher"
**Solution:** 
- Make sure the folder is in the correct projects directory
- Click "Refresh" in Ren'Py launcher
- Restart Ren'Py launcher

### "Missing images error"
**Solution:**
- Check that image files are in `game/images/` folder
- Make sure filenames match exactly (case-sensitive on Linux/Mac)
- Use PNG format for images

### "Black screen when launching"
**Solution:**
- This is normal if placeholder images aren't created
- Create placeholder images or download free art
- Check Ren'Py console for error messages

### "Game runs but no audio"
**Solution:**
- Create audio files and place in `game/audio/`
- Or comment out audio lines in script.rpy temporarily:
  ```python
  # play music "audio/bgm_main.mp3"
  ```

---

## 📚 Next Steps

### 1. Test the Demo
- Play through the current content (takes ~10 minutes)
- Check that choices affect relationship stats
- Save and load to test save system

### 2. Customize the Game
- Edit character names in `characters.rpy`
- Modify dialogue in `script.rpy`
- Change colors and fonts in `options.rpy`

### 3. Add Your Assets
- Create/commission character artwork
- Design backgrounds
- Record/compose music and sound effects

### 4. Expand the Story
- Write more dialogue and branching paths
- Add new scenes and acts
- Implement multiple endings

---

## 🎓 Learning Resources

### Ren'Py Documentation
- Official docs: https://www.renpy.org/doc/html/
- Tutorial: https://www.renpy.org/doc/html/quickstart.html

### Visual Novel Writing
- Story structure guide: [Link to resource]
- Character development: [Link to resource]
- Dialogue writing tips: [Link to resource]

### Art & Audio Resources
- Free sprite art: OpenGameArt.org
- Free music: Incompetech.com
- Free backgrounds: Pixabay, Unsplash

---

## 💡 Development Tips

### Editing Scripts
1. Open `.rpy` files with any text editor (Notepad++, VS Code, Sublime Text)
2. Ren'Py will auto-reload changes when you reload the game
3. Use `Shift+R` in-game to reload script changes quickly

### Testing Choices
1. Use Ren'Py's developer tools: Press `Shift+O` in-game
2. Skip to specific labels with: `renpy.jump('label_name')`
3. Check console for error messages: `Shift+E`

### Performance
- Cache images with: `image bg_office = Composite(...)`
- Use `with dissolve` or `with fade` for smooth transitions
- Keep sprite files under 1MB each

---

## 📞 Support

**Issues or Questions?**
- GitHub Issues: https://github.com/melieinacelesteria111-cmyk/visual-novel-game/issues
- Ren'Py Forums: https://forums.renpy.org/
- Reddit: r/renpy

---

## 🎉 You're All Set!

You now have a working Visual Novel game framework. Start exploring, customize, and create your own story!

**Happy game development!** 🚀✨
