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
