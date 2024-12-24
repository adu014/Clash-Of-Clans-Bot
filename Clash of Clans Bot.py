import discord
from discord.ext import commands
import asyncio
import pyautogui
import time
import threading
import pytesseract
from PIL import ImageGrab
import ctypes

TOKEN = '######################################################'
CHANNEL_ID = 1305998723062562841 
pyautogui.FAILSAFE = False 
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

automation_running = False
automation_thread = None

gold_region = (1670, 37, 1820, 70)
elixir_region = (1670, 120, 1820, 153)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

gold_image_path = "latest_gold_screenshot.png"
elixir_image_path = "latest_elixir_screenshot.png"
screenshot_path = "full_screenshot.png"
pyautogui.hotkey("alt", "tab")
def capture_and_read(region):
    screenshot = ImageGrab.grab(bbox=region)
    gray_image = screenshot.convert("L")
    text = pytesseract.image_to_string(gray_image, config="--psm 7 digits")
    numbers = ''.join(filter(str.isdigit, text))
    return int(numbers) if numbers.isdigit() else None

def capture_gold_elixir_screenshots():
    gold_screenshot = ImageGrab.grab(bbox=gold_region)
    elixir_screenshot = ImageGrab.grab(bbox=elixir_region)
    gold_screenshot.save(gold_image_path)
    elixir_screenshot.save(elixir_image_path)

def capture_full_screen_screenshot():
    full_screenshot = ImageGrab.grab(bbox=(0, 0, 1919, 1079))
    full_screenshot.save(screenshot_path)

def perform_automation():
    global automation_running
    screen_width, screen_height = pyautogui.size()

    def move(x, y, delay=0, click=True):
        time.sleep(delay)
        pyautogui.moveTo(x, y)
        if click:
            pyautogui.click()
    
    while automation_running:
        capture_gold_elixir_screenshots()

        move(1225, 85)
        move(1400, 925)
        move(1600, 90)
        move(150, 1000)
        move(1400, 700)
        time.sleep(4)

        move(450, 950, delay=0.5)
        move(screen_width // 2, 50)
        move(0, screen_height // 2)
        move((screen_width // 2) - 400, screen_height - 225)
        move((screen_width // 2) + 400, screen_height - 225)
        move(screen_width - 100, screen_height // 2)
        move(screen_width // 2, 50)
        pyautogui.hotkey("alt", "f4")
        pyautogui.press("winleft")
        pyautogui.press("c")
        pyautogui.press("enter")
        time.sleep(8)

async def send_warning(message):
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(message)

async def send_latest_screenshots(ctx):
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await ctx.send("Here are the latest screenshots of gold and elixir storage:")
        await ctx.send(file=discord.File(gold_image_path))
        await ctx.send(file=discord.File(elixir_image_path))

async def send_full_screenshot(ctx):
    capture_full_screen_screenshot()
    await ctx.send("Here is the full screenshot of your screen:")
    await ctx.send(file=discord.File(screenshot_path))

@bot.command()
async def run(ctx):
    global automation_running, automation_thread
    if not automation_running:
        automation_running = True
        automation_thread = threading.Thread(target=perform_automation)
        automation_thread.start()
        await ctx.send("Automation started.")
    else:
        await ctx.send("Automation is already running.")

@bot.command()
async def stop(ctx):
    global automation_running, automation_thread
    if automation_running:
        automation_running = False
        if automation_thread is not None:
            automation_thread.join()
            automation_thread = None
        await ctx.send("Automation stopped.")
    else:
        await ctx.send("No automation is currently running.")

@bot.command()
async def check(ctx):
    await send_latest_screenshots(ctx)

@bot.command()
async def screenshot(ctx):
    await send_full_screenshot(ctx)
    
@bot.command()
async def lock(ctx):
    ctypes.windll.user32.LockWorkStation()
    await ctx.send("Computer is now locked.")

@bot.command(name="type")
async def type_text(ctx, *, text: str):
    pyautogui.write(text)
    await ctx.send (f"Typed the following text: `{text}`")

@bot.command(name="hotkey")
async def press_hotkey(ctx, *keys):
    if keys:
        pyautogui.hotkey(*keys)
        await ctx.send(f"Pressed hotkey sequence: {' + '.join(keys)}")
    else:
        await ctx.send("Please provide at least one key for the hotkey command.")
 
@bot.command(name="press")
async def press_keys(ctx, *keys):
    if keys:
        for key in keys:
            pyautogui.press(key)
        await ctx.send(f"Pressed keys in sequence: {' '.join(keys)}")
    else:
        await ctx.send("Please provide at least one key for the press command.")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("Bot is online and ready!\n         `**`Available Commands:**\n"
        "`!run` - **Starts the automation process** to perform a series of screen captures and actions.\n"
        "`!stop` - **Stops the ongoing automation** process if it’s running.\n"
        "`!check` - **Captures and sends** the latest screenshots of gold and elixir storage.\n"
        "`!screenshot` - **Captures and sends** a full-screen screenshot of your screen.\n"
        "`!lock` - **Locks your computer** screen immediately.\n"
        "`!type <text>` - **Types the specified text** on the active window.\n"
        "`!hotkey <key1> <key2>...` - **Simulates pressing a sequence of hotkeys** (e.g., `!hotkey ctrl s` for save).\n"
        "`!press <key1> <key2>...` - **Presses each specified key** in sequence (e.g., `!press enter esc`).\n\n")
    else:
        print("Channel not found.")

bot.run(TOKEN)