#!/usr/bin/env python3
import os
import json
import subprocess
from rich.console import Console

console = Console()

ASCII_RADIO = r"""
      _________.-.
 ___ /  _____ /  |______
|   |  |  _  |   _  _  |
|___|__| |_| |__| || |_|   __
|  _  _   ___   _  __  |  |o |
| | |/ \ / _ \ | |/  \ |  |  |
| |_| () | (_)| |_| () |  |  |
|____\__/ \___/ \__\__/ |  |__|
|  VOL  |  TUNER  |  FM |  |||
|_______|_________|_____|  |||

       author: linux-edu
"""

STATIONS_FILE = "stations.json"

def load_stations():
    if not os.path.exists(STATIONS_FILE):
        console.print("[red]stations.json not found![/red]")
        return {}
    with open(STATIONS_FILE, "r") as f:
        return json.load(f)

def play_stream(url):
    subprocess.call(["mpv", url])

def play_local_music():
    music_dir = os.path.expanduser("~/Music")
    if not os.path.isdir(music_dir):
        console.print("[red]No ~/Music folder found.[/red]")
        input("Press Enter...")
        return
    files = [f for f in os.listdir(music_dir) if f.endswith((".mp3", ".ogg", ".wav", ".flac"))]
    if not files:
        console.print("[red]No music files found in ~/Music.[/red]")
        input("Press Enter...")
        return
    console.print("\n[bold]Local Music:[/bold]\n")
    for i, f in enumerate(files, 1):
        console.print(f"[{i}] {f}")
    choice = input("\nPick a file: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(files):
        file_path = os.path.join(music_dir, files[int(choice)-1])
        console.print(f"▶ Playing {file_path}...")
        subprocess.call(["mpv", file_path])

def main():
    stations = load_stations()
    if not stations:
        return
    while True:
        os.system("clear")
        console.print(ASCII_RADIO)
        console.print("\n[bold]Choose a station:[/bold]\n")
        for k, v in stations.items():
            console.print(f"[{k}] {v[0]}")
        console.print("[L] Local Music")
        console.print("[Q] Quit\n")
        choice = input("Select option: ").strip().lower()
        if choice == "q":
            break
        elif choice == "l":
            play_local_music()
        elif choice in stations:
            console.print(f"▶ Playing {stations[choice][0]}...")
            play_stream(stations[choice][1])
        else:
            console.print("[red]Invalid choice![/red]")
            input("Press Enter...")

if __name__ == "__main__":
    main()
