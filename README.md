![Shell Script](https://img.shields.io/badge/RocknRoll-blue.svg) 
![Shell Script](https://img.shields.io/badge/linux--edu-red.svg)

# 📻 RocknRoll-Radio

A terminal-based radio & music player for **Linux** and **Termux**.  
ASCII art radio + menu interface. Streams online radio from [radiocast.co](https://radiocast.co) or plays your local music.

```
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

```

---

## 🚀 Installation

### Linux
```bash
sudo apt install mpv python3 -y
git clone https://github.com/linux-edu/RocknRoll-Radio.git
cd RocknRoll-Radio
pip install -r requirements.txt
python3 radio.py
```

### Termux
```bash
pkg install mpv python -y
git clone https://github.com/linux-edu/RocknRoll-Radio.git
cd RocknRoll-Radio
pip install -r requirements.txt
python radio.py
```

---

## 🎵 Local Music

RocknRoll-Radio can also play your own music files.
It will automatically search these locations:

~/Music/ → default on Linux

~/storage/music/ → default on Termux

music/ → included in this repo for beginners

👉 If you’re unsure, just copy your .mp3 or .wav files into the music/ folder inside this project.

```
RocknRoll-Radio/
 ├── radio.py
 ├── requirements.txt
 └── music/
      └── your_songs_here.mp3
```
---

## 📄 License
This project is licensed under the [MIT License](LICENSE).  
Copyright (c) 2025 **linux-edu**

---

## 🙌 Contribute
Pull requests are welcome!  
Fork and customize it for your own radio presets, or help improve the TUI.

---

## 💖 Sponsor Us
If you find our work useful, consider supporting it.  

Your sponsorship helps us:
- Maintain and improve open-source tools like `RocknRoll-Radio`
- Create more scripts for Termux and Linux users
- Dedicate time to education and community projects

Even small contributions go a long way — thank you for helping us keep open-source accessible to everyone. 🙏

[![Sponsor](https://img.shields.io/badge/sponsor-%E2%9D%A4-lightgrey?logo=github)](https://github.com/sponsors/linux-edu)
