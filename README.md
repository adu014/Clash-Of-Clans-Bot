```markdown
# Discord Automation and Monitoring Bot

This repository contains a powerful Discord bot designed to automate repetitive tasks, monitor on-screen data, and execute user-defined commands. The bot integrates screen capturing, optical character recognition (OCR), and keyboard/mouse automation for versatile use cases.

---

## Features

### 🚀 Core Functionalities

#### 🔄 Automation Control
- **`!run`**: Starts a pre-defined automation routine that simulates mouse and keyboard actions and captures screen data.
- **`!stop`**: Stops the ongoing automation process gracefully.

#### 📊 Monitoring and OCR
- Extract numeric data (e.g., gold and elixir values) from specific screen regions using Tesseract OCR.

#### 🖥️ Remote Control Commands
- **`!check`**: Capture and share screenshots of gold and elixir regions.
- **`!screenshot`**: Capture and share a full-screen screenshot.
- **`!lock`**: Lock the workstation remotely.
- **`!type <text>`**: Type the specified text into the active window.
- **`!hotkey <key1> <key2> ...`**: Simulate pressing a sequence of hotkeys.
- **`!press <key1> <key2> ...`**: Simulate pressing individual keys in sequence.

---

## Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/username/discord-automation-bot.git
cd discord-automation-bot
```

### 2️⃣ Install Dependencies
```bash
pip install discord pyautogui pytesseract pillow
```

### 3️⃣ Configure Tesseract OCR
- Download and install Tesseract from [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).
- Update the `pytesseract.pytesseract.tesseract_cmd` path in the script to your Tesseract installation directory.

### 4️⃣ Configure the Bot
- Replace `TOKEN` with your bot's token.
- Replace `CHANNEL_ID` with the ID of your Discord channel.

### 5️⃣ Run the Bot
```bash
python bot.py
```

---

## Commands

### ⚙️ Automation
- **`!run`**: Start the automation process.
- **`!stop`**: Stop the ongoing automation process.

### 📸 Screenshots
- **`!check`**: Share the latest screenshots of gold and elixir regions.
- **`!screenshot`**: Capture and share a full-screen screenshot.

### 🔒 Remote Control
- **`!lock`**: Lock the workstation.
- **`!type <text>`**: Type the specified text in the active window.
- **`!hotkey <key1> <key2> ...`**: Simulate pressing a sequence of hotkeys.
- **`!press <key1> <key2> ...`**: Simulate pressing individual keys in sequence.

---

## Usage Notes
- Ensure your screen resolution matches the defined regions for OCR and automation.
- Modify `gold_region` and `elixir_region` variables to suit your setup.
- Use responsibly; some actions (e.g., `Alt+F4`) may interfere with active tasks.

---

## Dependencies
- **Python 3.x**
- **[Discord.py](https://discordpy.readthedocs.io)**: For bot integration.
- **[PyAutoGUI](https://pyautogui.readthedocs.io)**: For mouse and keyboard automation.
- **[Tesseract OCR](https://github.com/tesseract-ocr/tesseract)**: For text recognition.
- **[Pillow](https://pillow.readthedocs.io)**: For image processing.

---

## Future Enhancements
- Add dynamic region detection to support varying screen resolutions.
- Implement role-based access control for bot commands.
- Add logging for automation actions and screenshot history.

---

## Disclaimer
This bot is intended for educational purposes and personal use only. Use it responsibly to avoid unintended consequences.
```

