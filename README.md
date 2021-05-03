<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Vaughan-Esports/MovieTime">
    <img src="https://image.brandonly.me/ve white.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">MovieTime</h3>

  <p align="center">
    Discord bot to automatically edit 16:9 clips into TikTok friendly 9:16 videos with blur.
    <br />
    <br />
    <a href="https://vaughanesports.org/discord">View Demo</a>
    ·
    <a href="https://github.com/Vaughan-Esports/MovieTime/issues">Report Bug</a>
    ·
    <a href="https://github.com/Vaughan-Esports/MovieTime/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## About The Project

Bugging our editors everytime we needed to edit videos into a TikTok friendly 
format became too much of a hassle. So, we made a bot to do it automatically!

### Built With

* [Discord.py](https://github.com/Rapptz/discord.py)
* [MoviePy](https://github.com/Zulko/moviepy)

<!-- GETTING STARTED -->

## Getting Started

Follow the steps below if you'd like to host your own instance our the bot.

### Prerequisites

- Python 3.8 or higher (May work on 3.6 and 3.7 but untested)
- Discord Developer Account

### Installation

1. Get your Discord bot API Key (
   Instructions [here](https://discordpy.readthedocs.io/en/latest/discord.html))
2. Clone the repo
   ```sh
   git clone https://github.com/Vaughan-Esports/MovieTime.git
   ```
3. Install Python packages
   ```sh
   pip install -r requirements.txt
   ```
4. Create a file called `.env` amd put your API key in like so:
   ```dotenv
   BOT_TOKEN=YOUR_TOKEN
   ```
   
**NOTE:** If you'd like to host it on a Rasberry Pi, you must manually install
[FFMPEG](https://snapcraft.io/install/ffmpeg/raspbian#install)

<!-- USAGE EXAMPLES -->

## Usage

It has one command: `edit!tiktok`
- You submit a `.mp4` file to be rendered
- After rendering, it will ping you with an Imgur link to the uploaded file


<!-- ROADMAP -->

## Roadmap

- Nothing at the moment

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->

## Contact

Brandon Ly - [@brndnly](https://twitter.com/brndnly) - [brandon@brandonly.me](mailto:brandon@brandonly.me)

Vincent Tran - [@vincentrann](https://github.com/vincentrann)

Project
Link: [https://github.com/Vaughan-Esports/MovieTime](https://github.com/Vaughan-Esports/MovieTime)
