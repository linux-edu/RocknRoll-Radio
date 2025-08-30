#!/usr/bin/env python3
import os
import subprocess
import sys

# ───────────────────────────────
# ASCII Radio Splash
# ───────────────────────────────
def show_radio_art():
    art = r"""
                                   \
                                    \
                                     \
                                      \
                                       \
                                        \
                                         \
   _________________________________________
  /              RocknRoll                  \
 /___________________________________________\
|             author: linux-edu               |
|  ____________              ______           |
| |------------|            /      \          |
| |------------|           |        |         |
| |------------|            \______/          |
|  ____________                               |
|                                             |
|   VOL   |   TUNER   |   FM   |   AM         |
|_____________________________________________|
 \___________________________________________/
"""
    print(art)
# ───────────────────────────────
# Radio Stations (real working ones)
# ───────────────────────────────
stations = {
    "[Cape Town] SABC 5 FM (C.T)": "https://23543.live.streamtheworld.com/5FMAAC.aac",
    "[Cape Town] Good Hope FM (JHB)": "https://28513.live.streamtheworld.com/GOODHOPEFMAAC.aac"
}

# ───────────────────────────────
# Helpers
# ───────────────────────────────
def play_stream(url):
    """
    Play a radio stream with mpv and allow for a clean exit.
    mpv is a command-line media player.
    """
    try:
        print("\n▶️ Press 'q' inside mpv to quit the stream.")
        # check=False allows the process to return a non-zero exit code (when 'q' is pressed)
        # without raising an exception.
        subprocess.run(["mpv", url], check=False)
    except FileNotFoundError:
        print("❌ mpv not found. Please install it to play streams.")
    except KeyboardInterrupt:
        print("\n⏹️ Stream stopped by user.")


def play_local_music():
    """Play local music files from common directories."""
    search_dirs = [
        os.path.join(os.getcwd(), "music"),         # project folder
        os.path.expanduser("~/Music"),              # Linux default
        os.path.expanduser("~/storage/music"),      # Termux default
    ]

    music_dir = None
    for d in search_dirs:
        if os.path.exists(d):
            files = [f for f in os.listdir(d) if f.lower().endswith((".mp3", ".wav", ".ogg"))]
            if files:
                music_dir = d
                break

    if not music_dir:
        print("❌ No music files found in ./music, ~/Music or ~/storage/music.")
        return

    print(f"\n🎵 Local Music Library (from {music_dir}):")
    for i, f in enumerate(files, 1):
        print(f"  {i}. {f}")

    choice = input("\nSelect a track number (or press Enter to cancel): ")
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(files):
        print("❌ Invalid choice or canceled.")
        return

    track = os.path.join(music_dir, files[int(choice) - 1])
    print(f"▶️ Playing {files[int(choice) - 1]}...\n")
    try:
        subprocess.run(["mpv", track], check=False)
    except FileNotFoundError:
        print("❌ mpv not found. Please install it to play local music.")
    except KeyboardInterrupt:
        print("\n⏹️ Playback stopped by user.")


def request_station():
    """Prints instructions for requesting a new station via WhatsApp."""
    print("\n--- Request a New Station ---")
    print("To add a new station...")
    print("Like & Follow on..")
    print("Facebook: https://www.facebook.com/profile.php?id=61577819146441")
    print("Then join our WhatsApp channel and submit your request.")
    print("WhatsApp: https://whatsapp.com/channel/0029VbBkaQyG3R3maDo9S52b")
    print("\n✅ You will be taken back to the main menu now.")


# ───────────────────────────────
# Main Menu
# ───────────────────────────────
def main_menu():
    """Displays the main menu and handles user choices."""
    while True:
        print("\n=== Main Menu ===")
        print("1. 📻 World Radio")
        print("2. 🎵 Play Local Music")
        print("3. ➕ Request New Station")
        print("4. ❌ Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":
            print("\n📻 Available Stations:")
            for i, name in enumerate(stations.keys(), 1):
                print(f"  {i}. {name}")

            sel = input("\nChoose a station: ")
            if sel.isdigit() and 1 <= int(sel) <= len(stations):
                station_name = list(stations.keys())[int(sel) - 1]
                print(f"\nConnecting to {station_name}...")
                print(f"\n▶️ Tuning into {station_name}...\n")
                play_stream(stations[station_name])
            else:
                print("❌ Invalid station choice.")

        elif choice == "2":
            play_local_music()

        elif choice == "3":
            request_station()

        elif choice == "4":
            print("\n👋 Thanks for using RocknRoll-Radio!")
            sys.exit(0)

        else:
            print("❌ Invalid option, try again.")

# ───────────────────────────────
# Entry Point
# ───────────────────────────────
if __name__ == "__main__":
    os.system("clear")
    show_radio_art()
    main_menu()
