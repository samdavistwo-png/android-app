# MacroDroid Automation Script for SE 2.2.6 Key Testing

**Device:** OPPO K13 5G (1080 x 2400 pixels)
**Device ID:** 105363
**Total Keys:** 832
**Estimated Time:** 2-4 hours (automatic)

---

## 📱 STEP 1: Install MacroDroid

1. **Download MacroDroid:**
   - Open Google Play Store
   - Search for "MacroDroid"
   - Install **MacroDroid - Device Automation** (by ArloSoft)
   - Free version works fine (5 macros limit)

2. **Grant Permissions:**
   - Open MacroDroid
   - Grant all requested permissions:
     - Accessibility Service (REQUIRED for UI automation)
     - Display over other apps
     - Notification access
     - Usage stats access

---

## 📋 STEP 2: Prepare the Key List File

1. **Download the keys file to your phone:**
   - Go to: https://github.com/samdavistwo-png/android-app
   - Open: `mixed_case_keys.json`
   - Download to your phone's `/Download` folder

2. **Or create a simple text file:**
   - Create file: `/sdcard/Download/keys.txt`
   - Each line = one key
   - Total 832 lines

---

## 🤖 STEP 3: Create the MacroDroid Macro

### **Macro Configuration:**

**Name:** SE Key Tester Auto

**Trigger:**
- Manual trigger (you'll start it manually)

**Actions Sequence:**

```
1. SET VARIABLE
   - Variable name: keyIndex
   - Value: 0

2. SET VARIABLE
   - Variable name: keysFound
   - Value: 0

3. LOOP (832 times)

   3.1 READ FILE LINE
       - File: /sdcard/Download/keys.txt
       - Line number: {lv=keyIndex}
       - Store in variable: currentKey

   3.2 LAUNCH APP
       - Package: com.snake (SE 2.2.6 app)
       - Wait for app to load: 2 seconds

   3.3 WAIT
       - 2 seconds

   3.4 UI INTERACTION - Tap (Entry Key Button)
       - X coordinate: 540
       - Y coordinate: 943
       - Duration: Normal tap

   3.5 WAIT
       - 2 seconds

   3.6 UI INTERACTION - Tap (Key Input Field)
       - X coordinate: 540
       - Y coordinate: 541
       - Duration: Normal tap

   3.7 WAIT
       - 1 second

   3.8 TYPE TEXT
       - Text: {lv=currentKey}
       - Use clipboard: No
       - Type slowly: Yes (150ms between chars)

   3.9 WAIT
       - 1 second

   3.10 UI INTERACTION - Tap (Activate Button)
        - X coordinate: 834
        - Y coordinate: 657
        - Duration: Normal tap

   3.11 WAIT
        - 3 seconds (wait for response)

   3.12 TAKE SCREENSHOT
        - Save to: /sdcard/Pictures/KeyTests/
        - Filename: key_{lv=keyIndex}_{lv=currentKey}.png

   3.13 CHECK IF SUCCESS (OCR or Toast detection)
        - IF screen contains "activated successfully"
        - OR screen contains "Matagumpay"
        - THEN:
            - INCREMENT variable: keysFound
            - PLAY SOUND (alert you)
            - STOP MACRO (found working key!)

   3.14 FORCE CLOSE APP
        - Package: com.snake

   3.15 INCREMENT VARIABLE
        - Variable: keyIndex
        - By: 1

   3.16 WAIT
        - 2 seconds

   3.17 LOOP BACK to step 3.1

4. SHOW NOTIFICATION
   - Title: "Testing Complete"
   - Text: "Tested {lv=keyIndex} keys. Found {lv=keysFound} working keys."
   - Sound: Alert
```

---

## 🎯 SIMPLIFIED VERSION (If Above is Too Complex)

### **Simple 3-Step Macro:**

**This version tests ONE key at a time (you trigger it 832 times):**

```
TRIGGER: Widget tap or shake gesture

ACTIONS:
1. Launch App: com.snake
2. Wait: 2 sec
3. Tap: (540, 943) - Entry Key button
4. Wait: 2 sec
5. Tap: (540, 541) - Key field
6. Wait: 1 sec
7. Type: [PASTE YOUR KEY HERE]
8. Wait: 1 sec
9. Tap: (834, 657) - Activate button
10. Wait: 3 sec
11. Screenshot: /sdcard/test.png
12. Force close app
```

**You would:**
- Edit macro for each key
- Tap widget 832 times
- Check screenshots manually

---

## ⚙️ DETAILED SETUP INSTRUCTIONS

### **A. Enable Accessibility Service:**

1. Open MacroDroid
2. Go to Settings → Accessibility
3. Enable "MacroDroid Accessibility Service"
4. Grant permission in Android Settings

### **B. Create the Macro:**

1. Open MacroDroid
2. Tap **"+"** (Add Macro)
3. Name it: "SE Key Auto Test"
4. Add **Trigger:**
   - Category: MacroDroid Specific
   - Select: Manual
5. Add **Actions** (follow sequence above)
6. Add **Constraints:** None needed
7. Save macro

### **C. Test with One Key First:**

Before running all 832 keys, test with just ONE key:

1. Modify loop to: 1 iteration
2. Hardcode a test key (e.g., "123456")
3. Run macro
4. Watch it:
   - Open app ✓
   - Tap Entry Key ✓
   - Type key ✓
   - Tap Activate ✓
   - Take screenshot ✓
   - Close app ✓

If successful, change loop to 832 and run full test!

---

## 📊 EXACT TAP COORDINATES (From Your Screenshots)

| Element | X | Y | Purpose |
|---------|---|---|---------|
| **Entry Key Button** | 540 | 943 | Opens key entry screen |
| **Key Input Field** | 540 | 541 | Click to focus for typing |
| **Activate Button** | 834 | 657 | Submit the key |
| **Copy Device ID** | 916 | 156 | (optional) |
| **Back Button** | 98 | 77 | Go back |
| **Close Button** | 296 | 657 | Cancel/clear |

**Screen Resolution:** 1080 x 2400 pixels

---

## 🔧 ALTERNATIVE: Simple Semi-Auto Helper

If full automation is too complex, use this **hybrid approach:**

### **MacroDroid Helper Macro:**

**Trigger:** Volume Down button (3 quick presses)

**Actions:**
1. Read clipboard (you copy key manually)
2. Launch SE app
3. Wait 2s
4. Tap Entry Key (540, 943)
5. Wait 2s
6. Tap Key field (540, 541)
7. Wait 1s
8. Paste clipboard
9. Wait 1s
10. Tap Activate (834, 657)
11. Wait 3s
12. Screenshot
13. Close app

**You would:**
- Open `ALL_832_KEYS_FULL_LIST.txt`
- Copy key #001
- Press Volume Down 3 times
- Macro runs automatically
- Check screenshot
- Copy key #002
- Repeat...

**Much faster than fully manual! (~1 hour total)**

---

## 📁 FILE STRUCTURE

Create these folders on your phone:

```
/sdcard/Download/
  └── keys.txt (832 keys, one per line)

/sdcard/Pictures/KeyTests/
  └── (screenshots will be saved here)
```

---

## 🎬 STEP-BY-STEP EXECUTION

### **Before Starting:**

1. ✅ MacroDroid installed & permissions granted
2. ✅ SE 2.2.6 app installed
3. ✅ Device fully charged (or plugged in)
4. ✅ Keep screen on (Developer options → Stay awake)
5. ✅ Disable auto-lock (Settings → Display → Sleep: Never)
6. ✅ Close all other apps
7. ✅ Put phone in "Do Not Disturb" mode

### **Running the Automation:**

1. Open MacroDroid
2. Find macro: "SE Key Auto Test"
3. Tap the play button (▶)
4. **Leave phone alone for 2-4 hours**
5. Macro will run automatically

### **Monitoring Progress:**

- MacroDroid shows current action
- Screenshots saved to `/sdcard/Pictures/KeyTests/`
- Check last screenshot to see progress
- If working key found → macro stops + notification

### **After Completion:**

1. Check notification for results
2. Browse screenshots folder
3. Look for "activated successfully" in screenshots
4. Working keys will have green success message
5. Failed keys will have red error message

---

## 🆘 TROUBLESHOOTING

### **Macro Not Running:**
- Check Accessibility Service is enabled
- Grant all permissions to MacroDroid
- Restart MacroDroid

### **Taps Missing Elements:**
- Screen coordinates might be slightly off
- Adjust X/Y values ±10-20 pixels
- Test each tap individually

### **Keys Not Typing:**
- Enable "Type slowly" option
- Increase delay between characters
- Make sure keyboard is English

### **App Crashes:**
- Add longer wait times (3-5 seconds)
- Add "Clear Cache" action before launch
- Restart phone before long run

### **Screen Turns Off:**
- Enable "Keep screen on" in Developer Options
- Use MacroDroid action: "Keep Screen On"
- Plug in charger (some phones stay on when charging)

---

## 💡 PRO TIPS

1. **Battery:** Plug in phone before starting
2. **Testing:** Test with 5 keys first before full run
3. **Backup:** Save screenshots to cloud (Google Drive)
4. **Monitoring:** Set up notification every 100 keys
5. **Recovery:** Save progress (which key you're on) to file

---

## 📊 EXPECTED RESULTS

**Timeline:**
- Per key: ~10 seconds
- 832 keys: ~138 minutes (2.3 hours)
- With delays: ~3-4 hours total

**Output:**
- 832 screenshots in `/sdcard/Pictures/KeyTests/`
- Notification when complete
- Working keys = screenshots showing "activated successfully"

---

## 🎯 RECOMMENDED APPROACH

**Start with this:**

1. **Install MacroDroid** (15 min)
2. **Create simple semi-auto helper** (15 min)
3. **Test with 10 keys manually** (5 min)
4. **If it works well, upgrade to full automation** (30 min)
5. **Let it run overnight** (automatic)

**Total setup time:** ~1 hour
**Total testing time:** 3-4 hours (unattended)

---

## ✅ FINAL CHECKLIST

Before starting automation:

- [ ] MacroDroid installed
- [ ] Accessibility enabled
- [ ] SE 2.2.6 app installed
- [ ] keys.txt file prepared
- [ ] Macro created and tested
- [ ] Phone charged/plugged in
- [ ] Screen set to never sleep
- [ ] Do Not Disturb enabled
- [ ] Ready to let phone run for 3-4 hours

---

**Questions? Issues? Let me know and I'll help troubleshoot!**

**Last Updated:** June 11, 2026
**Device:** OPPO K13 5G
**Screen:** 1080 x 2400 pixels
**Total Keys:** 832
